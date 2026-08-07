#!/usr/bin/env python3
"""Puerta mecánica de la traducción al español de hormozi-skills-es.

Compara cada archivo del árbol de trabajo contra su versión en el commit BASE
(el commit de saneamiento, previo a cualquier traducción) y reporta toda
divergencia estructural. Todo lo que hay aquí es determinista: un LLM lo haría
peor, más lento y más caro.

Uso:
    python3 .i18n/verify_i18n.py --base e5e5b42          # informe legible
    python3 .i18n/verify_i18n.py --base e5e5b42 --json   # JSON para los verificadores

Código de salida: 0 si no hay blockers ni majors, 1 en caso contrario.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Archivos que la traducción crea y que por tanto no existen en BASE.
ARCHIVOS_NUEVOS = [".codex-plugin/marketplace.json", "AGENTS.md"]

# Archivos que deliberadamente NO se traducen.
EXCLUIDOS = {"LICENSE", ".gitignore", "input/your-files-go-here.txt", "output/.gitkeep"}

MANIFIESTOS = [
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".codex-plugin/plugin.json",
    ".codex-plugin/marketplace.json",
]

SEPARADOR = "⸻"      # ⸻ TWO-EM DASH
FLECHA = "→"         # →
MULTIPLICA = "×"     # ×

# Fences cuyo contenido debe quedar byte a byte idéntico al original.
FENCES_LITERALES = {"json", "bash", "gitignore", "sh", "shell"}

# Palabras función inglesas: si sobreviven fuera de un fence literal, la línea
# probablemente quedó sin traducir.
RESIDUO_EN = re.compile(
    r"\b(the|and|with|your|you|for|this|that|should|when|must|from|will|into|"
    r"which|their|there|about|before|after|what|where|does|doesn|they|them|"
    r"have|has|been|being|make|makes|why|how|who|are|is|of|to|in|on)\b",
    re.IGNORECASE,
)

# Líneas que nunca se evalúan por residuo inglés.
EXENTO_RESIDUO = re.compile(
    r"^\s*(\||```|#{1,6}\s*$|-{3,}\s*$|https?://|!\[|\[!)|"
    r"\{\{|\$\{|shields\.io|github\.com"
)


# --------------------------------------------------------------------------- #
# utilidades

def git_show(base, ruta):
    """Contenido de `ruta` en el commit `base`, o None si allí no existía."""
    try:
        return subprocess.run(
            ["git", "-C", REPO, "show", f"{base}:{ruta}"],
            capture_output=True, check=True,
        ).stdout.decode("utf-8")
    except subprocess.CalledProcessError:
        return None


def git_ls(base):
    out = subprocess.run(
        ["git", "-C", REPO, "ls-tree", "-r", "--name-only", base],
        capture_output=True, check=True,
    ).stdout.decode("utf-8")
    return [l for l in out.splitlines() if l]


def leer(ruta):
    p = os.path.join(REPO, ruta)
    if not os.path.exists(p):
        return None
    with open(p, "rb") as f:
        crudo = f.read()
    return crudo.decode("utf-8"), crudo


def fences(texto):
    """Devuelve (etiquetas, bloques) de los fences de nivel superior."""
    etiquetas, bloques = [], []
    dentro, etiqueta, buf = False, None, []
    for linea in texto.split("\n"):
        if linea.startswith("```"):
            if not dentro:
                dentro, etiqueta, buf = True, linea[3:].strip(), []
            else:
                etiquetas.append(etiqueta)
                bloques.append((etiqueta, "\n".join(buf)))
                dentro, etiqueta, buf = False, None, []
        elif dentro:
            buf.append(linea)
    if dentro:  # fence sin cerrar
        etiquetas.append(etiqueta + " [SIN CERRAR]")
        bloques.append((etiqueta, "\n".join(buf)))
    return etiquetas, bloques


def rangos_fence_literal(texto):
    """Índices de línea que caen dentro de un fence json/bash/gitignore."""
    dentro, etiqueta, prohibidas = False, None, set()
    for i, linea in enumerate(texto.split("\n")):
        if linea.startswith("```"):
            if not dentro:
                dentro, etiqueta = True, linea[3:].strip().lower()
            else:
                dentro, etiqueta = False, None
            prohibidas.add(i)
        elif dentro and etiqueta in FENCES_LITERALES:
            prohibidas.add(i)
    return prohibidas


def frontmatter(texto):
    if not texto.startswith("---\n"):
        return {}
    fin = texto.find("\n---\n", 4)
    if fin == -1:
        return {}
    campos = {}
    for linea in texto[4:fin].split("\n"):
        if ":" in linea and not linea.startswith(" "):
            k, _, v = linea.partition(":")
            campos[k.strip()] = v.strip()
    return campos


def niveles_encabezado(texto):
    return [len(m.group(1)) for m in re.finditer(r"^(#{1,6})\s", texto, re.M)]


def es_emoji(ch):
    return unicodedata.category(ch) == "So"


def metricas(texto):
    lineas = texto.split("\n")
    etiquetas, _ = fences(texto)
    return {
        "lineas": len(lineas),
        "blancos": [i for i, l in enumerate(lineas) if l.strip() == ""],
        "fences": texto.count("\n```") + (1 if texto.startswith("```") else 0),
        "etiquetas_fence": etiquetas,
        "separadores": texto.count(SEPARADOR),
        "tabs": sum(1 for l in lineas if l.startswith("\t")),
        "filas_tabla": sum(1 for l in lineas if l.lstrip().startswith("|")),
        "pipes_por_fila": [l.count("|") for l in lineas if l.lstrip().startswith("|")],
        "encabezados": niveles_encabezado(texto),
        "flechas": texto.count(FLECHA),
        "multiplica": texto.count(MULTIPLICA),
        "emoji": sum(1 for ch in texto if es_emoji(ch)),
        "urls": len(re.findall(r"https?://\S+", texto)),
    }


# --------------------------------------------------------------------------- #
# carga del aparato canónico

def cargar_no_traducir():
    p = os.path.join(REPO, ".i18n", "NO-TRADUCIR.txt")
    if not os.path.exists(p):
        return [], []
    estrictos, presencia = [], []
    with open(p, encoding="utf-8") as f:
        for linea in f:
            t = linea.strip()
            if not t or t.startswith("#"):
                continue
            # Paridad estricta de recuento solo para identificadores de alta
            # señal: artefactos MAYUSCULAS.md, slugs con guion, y rutas.
            if re.fullmatch(r"[A-Z][A-Z0-9_]*\.md", t) \
               or re.fullmatch(r"[a-z][a-z0-9]*(-[a-z0-9]+)+", t) \
               or "/" in t:
                estrictos.append(t)
            else:
                presencia.append(t)
    return estrictos, presencia


def cargar_glosario():
    """(traducibles, keeps).

    traducibles: términos KEEP=NO — su forma inglesa debe haber desaparecido.
    keeps:       términos KEEP=SÍ/PARCIAL — su forma inglesa DEBE sobrevivir, y por
                 tanto hay que enmascararla antes de buscar residuo inglés.
    """
    p = os.path.join(REPO, ".i18n", "GLOSARIO-ES.md")
    if not os.path.exists(p):
        return [], []
    traducibles, keeps = [], []
    with open(p, encoding="utf-8") as f:
        for linea in f:
            if not linea.startswith("|"):
                continue
            celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
            if len(celdas) < 3:
                continue
            en, es, keep = celdas[0].strip("`*"), celdas[1].strip("`*"), celdas[2].upper()
            if not en or en.lower() in ("en", "---"):
                continue
            if "SÍ" in keep or "SI" in keep or "PARCIAL" in keep:
                # Puede venir como "DFY / DWY / DIY": cada alternativa se enmascara.
                for parte in re.split(r"\s*/\s*", en):
                    if len(parte) >= 3:
                        keeps.append(parte)
                if es and es != en:
                    keeps.append(es)
            elif keep == "NO":
                # Solo términos léxicos limpios de una o dos palabras.
                if re.fullmatch(r"[A-Za-z][A-Za-z ']{2,30}", en) and len(en) >= 4:
                    traducibles.append((en, es))
    return traducibles, keeps


def construir_mascara():
    """Tokens que deben desaparecer del texto antes de buscar residuo inglés.

    Sin esto, 'offer' matchea dentro de OFFER.md / sub-offer / hormozi-offer, y
    los términos KEEP del glosario (hook, pitch, Done For You...) se reportan
    como si fueran inglés sin traducir.
    """
    estrictos, presencia = cargar_no_traducir()
    _, keeps = cargar_glosario()
    tokens = set(estrictos) | set(presencia) | set(keeps)
    # Los más largos primero: 'OFFER_ANGLES.md' debe consumirse antes que 'OFFER.md'.
    orden = sorted((t for t in tokens if len(t) >= 3), key=len, reverse=True)
    if not orden:
        return None, set()
    patron = re.compile("|".join(re.escape(t) for t in orden), re.IGNORECASE)
    return patron, {t.lower() for t in orden}


def enmascarar(texto, patron):
    """Sustituye cada token por espacios, preservando offsets y saltos de linea."""
    if patron is None:
        return texto
    return patron.sub(lambda m: " " * len(m.group(0)), texto)


# --------------------------------------------------------------------------- #
# comprobaciones

class Informe:
    def __init__(self):
        self.hallazgos = []

    def add(self, sev, archivo, check, detalle):
        self.hallazgos.append(
            {"severidad": sev, "archivo": archivo, "check": check, "detalle": detalle}
        )

    blocker = lambda self, *a: self.add("blocker", *a)
    major = lambda self, *a: self.add("major", *a)
    minor = lambda self, *a: self.add("minor", *a)


def comparar_markdown(inf, ruta, antes, ahora, mascara=None):
    ma, mb = metricas(antes), metricas(ahora)

    if ma["lineas"] != mb["lineas"]:
        inf.blocker(ruta, "paridad-lineas",
                    f"{ma['lineas']} -> {mb['lineas']} lineas")
    elif ma["blancos"] != mb["blancos"]:
        faltan = sorted(set(ma["blancos"]) ^ set(mb["blancos"]))[:12]
        inf.blocker(ruta, "indices-lineas-blanco",
                    f"lineas en blanco movidas en indices {faltan}")

    if ma["fences"] != mb["fences"]:
        inf.blocker(ruta, "paridad-fences",
                    f"{ma['fences']} -> {mb['fences']} fences")
    elif ma["etiquetas_fence"] != mb["etiquetas_fence"]:
        inf.blocker(ruta, "etiquetas-fence",
                    f"{ma['etiquetas_fence']} -> {mb['etiquetas_fence']}")

    if ma["separadores"] != mb["separadores"]:
        inf.blocker(ruta, "separadores",
                    f"{ma['separadores']} -> {mb['separadores']} separadores U+2E3B")

    if ma["tabs"] != mb["tabs"]:
        inf.blocker(ruta, "vinetas-tab",
                    f"{ma['tabs']} -> {mb['tabs']} lineas que empiezan por TAB")

    if ma["filas_tabla"] != mb["filas_tabla"]:
        inf.blocker(ruta, "filas-tabla",
                    f"{ma['filas_tabla']} -> {mb['filas_tabla']} filas de tabla")
    elif ma["pipes_por_fila"] != mb["pipes_por_fila"]:
        for i, (x, y) in enumerate(zip(ma["pipes_por_fila"], mb["pipes_por_fila"])):
            if x != y:
                inf.blocker(ruta, "celdas-tabla",
                            f"fila de tabla #{i + 1}: {x} -> {y} pipes")
                break

    if ma["encabezados"] != mb["encabezados"]:
        inf.blocker(ruta, "niveles-encabezado",
                    f"secuencia de #: {len(ma['encabezados'])} -> "
                    f"{len(mb['encabezados'])} encabezados")

    # Fences literales byte a byte.
    _, ba = fences(antes)
    _, bb = fences(ahora)
    def sin_comentarios(bloque):
        # ESTILO §3.2 permite traducir los comentarios '#' dentro de fences bash.
        return [l for l in bloque.split("\n") if not l.lstrip().startswith("#")]

    for i, ((ta, ca), (tb, cb)) in enumerate(zip(ba, bb)):
        et = (ta or "").lower()
        if et not in FENCES_LITERALES:
            continue
        if et in ("bash", "sh", "shell"):
            if sin_comentarios(ca) != sin_comentarios(cb):
                inf.blocker(ruta, "fence-bash-alterado",
                            f"fence #{i + 1} ({ta}): cambio codigo ejecutable, no solo "
                            "comentarios '#'")
        elif ca != cb:
            inf.blocker(ruta, "fence-literal-alterado",
                        f"fence #{i + 1} ({ta}) no es byte-identico al original")

    for clave, nombre, sev in (("flechas", "→", "major"),
                               ("multiplica", "×", "major"),
                               ("emoji", "emoji", "major"),
                               ("urls", "URLs", "major")):
        if ma[clave] != mb[clave]:
            getattr(inf, sev)(ruta, f"recuento-{clave}",
                              f"{nombre}: {ma[clave]} -> {mb[clave]}")

    # Frontmatter.
    fa, fb = frontmatter(antes), frontmatter(ahora)
    if fa:
        for campo in ("name", "tools", "model", "color"):
            if fa.get(campo) != fb.get(campo):
                inf.blocker(ruta, f"frontmatter-{campo}",
                            f"{campo}: {fa.get(campo)!r} -> {fb.get(campo)!r}")
        if "description" in fa:
            d = fb.get("description", "")
            if not d:
                inf.blocker(ruta, "description-vacia", "description ausente o vacia")
            elif d == fa["description"]:
                inf.blocker(ruta, "description-sin-traducir",
                            "description identica al original")

    # Puntuación española de apertura.
    prohibidas = rangos_fence_literal(ahora)
    for i, linea in enumerate(ahora.split("\n")):
        if i in prohibidas:
            continue
        s = linea.strip()
        if s.endswith("?") and "¿" not in s:
            inf.minor(ruta, "signo-apertura", f"linea {i + 1}: falta ¿ — {s[:70]}")
        if s.endswith("!") and "¡" not in s and not s.endswith("]!"):
            inf.minor(ruta, "signo-apertura", f"linea {i + 1}: falta ¡ — {s[:70]}")

    # Residuo inglés. Se enmascaran antes los identificadores protegidos y los
    # términos KEEP: sin eso, 'Done For You' o 'sub-offer' se reportan como ingles.
    residuos = 0
    for i, linea in enumerate(ahora.split("\n")):
        if i in prohibidas or EXENTO_RESIDUO.search(linea):
            continue
        hits = RESIDUO_EN.findall(enmascarar(linea, mascara))
        if len(hits) >= 3:
            residuos += 1
            if residuos <= 4:
                inf.major(ruta, "residuo-ingles",
                          f"linea {i + 1}: {sorted(set(h.lower() for h in hits))[:6]} "
                          f"— {linea.strip()[:80]}")
    if residuos > 4:
        inf.major(ruta, "residuo-ingles",
                  f"...y {residuos - 4} lineas mas con >=3 palabras funcion inglesas")


def comparar_identificadores(inf, ruta, antes, ahora, estrictos):
    for t in estrictos:
        if re.fullmatch(r"[A-Za-z][A-Za-z0-9_.-]*", t):
            pat = re.compile(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])")
            a, b = len(pat.findall(antes)), len(pat.findall(ahora))
        else:
            a, b = antes.count(t), ahora.count(t)
        if a != b:
            inf.blocker(ruta, "identificador-alterado",
                        f"'{t}': {a} -> {b} ocurrencias")


def comparar_json(inf, ruta, antes, ahora):
    try:
        db = json.loads(ahora)
    except Exception as e:
        inf.blocker(ruta, "json-invalido", str(e))
        return
    if antes is None:
        return db
    try:
        da = json.loads(antes)
    except Exception:
        return db

    def claves(o, pre=""):
        s = set()
        if isinstance(o, dict):
            for k, v in o.items():
                s.add(pre + k)
                s |= claves(v, pre + k + ".")
        elif isinstance(o, list):
            for v in o:
                s |= claves(v, pre + "[].")
        return s

    faltan = claves(da) - claves(db)
    if faltan:
        inf.blocker(ruta, "json-claves-perdidas", f"faltan {sorted(faltan)}")
    return db


def comprobar_manifiestos(inf):
    for ruta in MANIFIESTOS:
        r = leer(ruta)
        if r is None:
            inf.blocker(ruta, "manifiesto-ausente", "el archivo no existe")
            continue
        try:
            d = json.loads(r[0])
        except Exception as e:
            inf.blocker(ruta, "json-invalido", str(e))
            continue
        if d.get("name") != "hormozi-skills-es":
            inf.blocker(ruta, "nombre-plugin",
                        f"name = {d.get('name')!r}, se esperaba 'hormozi-skills-es'")

    r = leer(".codex-plugin/marketplace.json")
    if r:
        try:
            m = json.loads(r[0])
            p = (m.get("plugins") or [{}])[0]
            if p.get("source") != {"source": "local", "path": "./"}:
                inf.blocker(".codex-plugin/marketplace.json", "codex-source",
                            f"source = {p.get('source')!r}, la spec de create-plugin "
                            "exige {'source': 'local', 'path': './'}")
            if p.get("category") != "Productivity":
                inf.blocker(".codex-plugin/marketplace.json", "codex-category",
                            f"category = {p.get('category')!r}, se espera 'Productivity' "
                            "en Title Case")
            if not (m.get("interface") or {}).get("displayName"):
                inf.major(".codex-plugin/marketplace.json", "codex-displayname",
                          "falta interface.displayName")
        except Exception as e:
            inf.blocker(".codex-plugin/marketplace.json", "codex-estructura", str(e))

    r = leer(".codex-plugin/plugin.json")
    if r:
        try:
            d = json.loads(r[0])
            if d.get("skills") != "./skills/":
                inf.blocker(".codex-plugin/plugin.json", "codex-skills-path",
                            f"skills = {d.get('skills')!r}, se espera './skills/' "
                            "(Codex no auto-descubre)")
            for campo in ("version", "description", "license"):
                if not d.get(campo):
                    inf.major(".codex-plugin/plugin.json", "codex-campo-faltante",
                              f"falta '{campo}'")
        except Exception:
            pass


def comprobar_slugs(inf):
    dir_skills = os.path.join(REPO, "skills")
    for slug in sorted(os.listdir(dir_skills)):
        p = os.path.join(dir_skills, slug, "SKILL.md")
        if not os.path.exists(p):
            inf.blocker(f"skills/{slug}", "skill-sin-SKILL.md", "falta SKILL.md")
            continue
        with open(p, encoding="utf-8") as f:
            txt = f.read()
        if frontmatter(txt).get("name") != slug:
            inf.blocker(f"skills/{slug}/SKILL.md", "slug-roto",
                        f"name != '{slug}' (carpeta y slug deben coincidir)")

    for a in ("hormozi-orchestrator", "sub-market", "sub-offer",
              "sub-value", "sub-pricing", "sub-sales"):
        p = os.path.join(REPO, "agents", f"{a}.md")
        if not os.path.exists(p):
            inf.blocker(f"agents/{a}.md", "agente-ausente", "el archivo no existe")
            continue
        with open(p, encoding="utf-8") as f:
            if frontmatter(f.read()).get("name") != a:
                inf.blocker(f"agents/{a}.md", "slug-roto", f"name != '{a}'")


def comprobar_glosario(inf, corpus, mascara):
    """Términos marcados para traducir cuya forma inglesa sobrevive."""
    traducibles, _ = cargar_glosario()
    # Los valores de "keywords" de los manifiestos quedan en ingles a proposito.
    corpus_json_keywords = {
        r for r in corpus if r.endswith(".json")
    }
    for en, es in traducibles:
        pat = re.compile(r"(?<![\w-])" + re.escape(en) + r"(?![\w-])", re.IGNORECASE)
        donde = defaultdict(int)
        for ruta, txt in corpus.items():
            if ruta in corpus_json_keywords:
                continue
            prohibidas = rangos_fence_literal(txt)
            for i, linea in enumerate(txt.split("\n")):
                if i in prohibidas:
                    continue
                n = len(pat.findall(enmascarar(linea, mascara)))
                if n:
                    donde[ruta] += n
        total = sum(donde.values())
        if total:
            top = sorted(donde.items(), key=lambda kv: -kv[1])[:4]
            inf.major("(corpus)", "termino-ingles-superviviente",
                      f"'{en}' (deberia ser '{es}') aparece {total} veces en "
                      f"{len(donde)} archivos: {top}")


def comprobar_divergencia(inf, corpus):
    """Un mismo rótulo canónico traducido de dos formas distintas."""
    p = os.path.join(REPO, ".i18n", "ENCABEZADOS-CANONICOS.md")
    if not os.path.exists(p):
        return
    canon = {}
    with open(p, encoding="utf-8") as f:
        for linea in f:
            if not linea.startswith("|"):
                continue
            c = [x.strip().strip("`") for x in linea.strip().strip("|").split("|")]
            if len(c) >= 3 and c[0] and c[1] and not c[0].startswith("--"):
                canon[c[0]] = c[1]

    # Cabeceras de la propia tabla del documento canonico, no rotulos del corpus.
    CABECERAS = {"Plantilla", "Dueño A", "Dueño B", "Riesgo", "Encabezado EN",
                 "Encabezado ES", "Archivos", "EN", "ES", "Rotulo"}

    faltantes = defaultdict(list)
    for en, es in canon.items():
        if en in CABECERAS or es in CABECERAS:
            continue
        # Regla identidad: si el rotulo canonico ES es igual al EN (OFFER.md,
        # Upsell, Downsell...), encontrarlo en ingles es lo CORRECTO.
        if es.strip().lower() == en.strip().lower():
            continue
        if len(en) < 6 or not re.fullmatch(r"[A-Za-z0-9 &/'.,()-]{6,60}", en):
            continue
        pat_en = re.compile(r"(?<![\w-])" + re.escape(en) + r"(?![\w-])")
        for ruta, txt in corpus.items():
            if pat_en.search(txt):
                faltantes[en].append(ruta)
    for en, rutas in sorted(faltantes.items(), key=lambda kv: -len(kv[1]))[:25]:
        inf.major("(corpus)", "rotulo-canonico-sin-traducir",
                  f"'{en}' -> deberia ser '{canon[en]}', sigue en ingles en "
                  f"{len(rutas)} archivos: {rutas[:4]}")


# --------------------------------------------------------------------------- #

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="commit de saneamiento (BASE de paridad)")
    ap.add_argument("--json", action="store_true", dest="como_json")
    args = ap.parse_args()

    inf = Informe()
    estrictos, _ = cargar_no_traducir()
    mascara, _ = construir_mascara()

    rutas_base = [
        r for r in git_ls(args.base)
        if (r.endswith(".md") or r.endswith(".json"))
        and r not in EXCLUIDOS
        and not r.startswith(".i18n/")
    ]

    corpus = {}
    for ruta in sorted(rutas_base):
        antes = git_show(args.base, ruta)
        r = leer(ruta)
        if r is None:
            inf.blocker(ruta, "archivo-desaparecido",
                        "existia en BASE y ya no esta en el arbol de trabajo")
            continue
        ahora = r[0]
        corpus[ruta] = ahora

        if r[1].startswith(b"\xef\xbb\xbf"):
            inf.minor(ruta, "bom", "el archivo empieza con BOM UTF-8")
        # Paridad, no valor absoluto: 12 archivos ya venian sin salto final en BASE.
        if antes is not None and antes.endswith("\n") != ahora.endswith("\n"):
            inf.minor(ruta, "newline-final-cambiado",
                      f"salto de linea final: {antes.endswith(chr(10))} -> "
                      f"{ahora.endswith(chr(10))}")

        if ruta.endswith(".json"):
            comparar_json(inf, ruta, antes, ahora)
        else:
            comparar_markdown(inf, ruta, antes, ahora, mascara)
            comparar_identificadores(inf, ruta, antes, ahora, estrictos)

    for nuevo in ARCHIVOS_NUEVOS:
        r = leer(nuevo)
        if r is None:
            inf.blocker(nuevo, "archivo-nuevo-ausente",
                        "la traduccion debia crearlo y no existe")
        else:
            corpus.setdefault(nuevo, r[0])
            if nuevo.endswith(".json"):
                comparar_json(inf, nuevo, None, r[0])

    comprobar_slugs(inf)
    comprobar_manifiestos(inf)
    comprobar_glosario(inf, corpus, mascara)
    comprobar_divergencia(inf, corpus)

    cuenta = Counter(h["severidad"] for h in inf.hallazgos)
    salida = {
        "base": args.base,
        "archivos_comparados": len(corpus),
        "blockers": cuenta["blocker"],
        "majors": cuenta["major"],
        "minors": cuenta["minor"],
        "hallazgos": inf.hallazgos,
    }

    if args.como_json:
        print(json.dumps(salida, ensure_ascii=False, indent=2))
    else:
        orden = {"blocker": 0, "major": 1, "minor": 2}
        print(f"BASE {args.base} · {len(corpus)} archivos comparados")
        print(f"blockers={cuenta['blocker']}  majors={cuenta['major']}  "
              f"minors={cuenta['minor']}\n")
        por_archivo = defaultdict(list)
        for h in inf.hallazgos:
            por_archivo[h["archivo"]].append(h)
        for archivo in sorted(por_archivo):
            hs = sorted(por_archivo[archivo], key=lambda h: orden[h["severidad"]])
            print(f"── {archivo}")
            for h in hs:
                print(f"   [{h['severidad'].upper():7}] {h['check']}: {h['detalle']}")
            print()

    return 1 if cuenta["blocker"] or cuenta["major"] else 0


if __name__ == "__main__":
    sys.exit(main())
