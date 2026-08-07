# Informe de verificación adversarial — ola 2

Rama `feat/traduccion-es` · base inglesa `e5e5b42` · traducción `9b0a52b`
Agregación de 5 lentes de verificación (V1 fidelidad, V2 glosario, V3 naturalidad, V4 identificadores, V5 contrato).

Cada hallazgo bruto fue **reabierto contra el archivo real** (`awk` sobre el árbol de trabajo + `git show e5e5b42:<ruta>`); no se aceptó ninguna cita de verificador sin comprobarla.

---

## 1. Resumen

| | Blocker | Major | Minor | Total |
|---|---|---|---|---|
| **Confirmados** | 1 | 29 | 49 | **79** |
| Descartados | — | — | — | 17 |

**Veredicto: rechazado.** 1 blocker (`AGENTS.md:67`, directorio fantasma `_archive/`) y 29 majors bloquean el merge.

Ningún arreglo propuesto altera la paridad estructural: **los 79 son reemplazos dentro de la misma línea**. No cambia el número de líneas, de fences, de separadores `⸻` (U+2E3B), de viñetas de tabulación dura (`TAB • TAB`) ni de celdas de tabla en ningún archivo.

### Origen por lente (tras deduplicar)

| Lente | Brutos | Confirmados | Descartados | Deduplicados en otra lente |
|---|---|---|---|---|
| V1 — fidelidad | 9 | 8 | 0 | 1 (AGENTS.md:67 → V5) |
| V2 — glosario | 13 | 11 | 0 | 2 (od:60 → V5, pitch:6 → V5) |
| V3 — naturalidad | 38 | 30 | 8 | 0 |
| V4 — identificadores | 3 | 1 | 0 | 2 (AGENTS.md:67 → V5, sub-sales:147 → V5) |
| V5 — contrato | 16 | 12 | 4 | 0 |
| Ampliación del agregador | — | 17 | — | — |

> **Ampliación del agregador**: V5 reportó la mayúscula tras dos puntos en encabezados como **un** hallazgo por archivo (`sub-offer:38`, `sub-market:31`). Al abrir los archivos aparecieron **17 encabezados** afectados (12 en `sub-offer`, 5 en `sub-market`). Se expandió a un hallazgo por línea para que el arreglo sea aplicable byte a byte.

### Severidades reclasificadas

| Archivo:línea | Lente | Bruto | Final | Razón |
|---|---|---|---|---|
| `AGENTS.md:67` | V1/V4 major, V5 blocker | major | **blocker** | Se conserva la severidad más alta (regla de deduplicación). |
| `skills/hormozi-pitch/SKILL.md:6` | V2 major, V5 minor | minor | **major** | Se conserva la más alta. |
| `agents/sub-offer.md:121`, `skills/offer-angles/SKILL.md:84`, `offer-key-points.md:19` | V3 | major | **minor** | «Hacer + OD + predicativo» **sí** es válido en español (`hacer la vida imposible`, `hazlo simple`). Es rigidez, no agramaticalidad. |
| `agents/sub-market.md:78` | V3 | major | **minor** | «tomar acción» es un calco, pero está ampliamente naturalizado en el registro de negocios LatAm. |
| `agents/hormozi-orchestrator.md:11` | V3 | major | **minor** | Apilamiento nominal pesado, pero gramatical y comprensible en una lectura. |
| `agents/hormozi-orchestrator.md:185` | V2 | minor | **major** | Viola un literal **prescrito** en `ENCABEZADOS-CANONICOS.md:752` y es el placeholder del BRIEF que `sub-pricing.md:26` declara como formato de entrada. |
| `skills/objection-destroyer/SKILL.md:73` | V2 | major | **minor** | El inglés de las dos listas **difiere** (`"This will take too much effort"` vs `"…require too much effort and I'll fail to follow through"`): no es la misma cadena, es una lista de ejemplo local. |

---

## 2. Descartados (17)

### 2.1 Falsos positivos ya triados (4)

| # | Item | Razón |
|---|---|---|
| 1 | `Done For You / Done With You / Do It Yourself` en `skills/dfy-dwy-diy/SKILL.md` | KEEP prescrito. |
| 2 | `Make it about them` y las demás líneas MAGIC en `hormozi-pitch` / `sub-sales` | Acróstico prescrito en inglés byte a byte. |
| 3 | `program` en `agents/sub-sales.md:90` | Palabra contenedora del acróstico, KEEP. |
| 4 | Valores del array `keywords` de los 4 manifiestos | En inglés a propósito. |

### 2.2 La traducción es fiel: el defecto está en el fuente inglés (3)

Reparar aquí sería **añadir contenido que no está en el original**. Se documentan para elevarlos como incidencia upstream, fuera del alcance de esta ola.

| Archivo:línea | Reporte | Verificación |
|---|---|---|
| `README.md:109` | V5: la fila `value-accelerator \| Aumenta el valor percibido` describe otra skill. | **Cierto pero el inglés dice lo mismo**: `git show e5e5b42:README.md` línea 109 = `\| \`value-accelerator\` \| Increase perceived value \|`. `skills/value-accelerator/SKILL.md:6` se titula «Acelerador del tiempo hasta el valor» y produce `TIME_TO_VALUE.md` (línea 201). Es un bug del README inglés. |
| `AGENTS.md:56` | V5: «tabla de agentes del README.md» — el README tiene un árbol ASCII (líneas 119-126), no una tabla. | **Cierto**, pero `CLAUDE.md:76` traduce fielmente `Add it to the agents table in \`README.md\``. `AGENTS.md` es el gemelo deliberado de `CLAUDE.md`; divergir aquí rompería la paridad de los gemelos sin arreglar el fuente. |
| `agents/sub-sales.md:425` | V3: «hará el mayor trabajo» rompe el tiempo presente del bloque. | El inglés **también** está en futuro: `(the one that will do the most work)`. El argumento de tiempo verbal es falso. *(El matiz «el mayor trabajo» ≠ «the most work» sí se conserva como minor — ver X-bucket C5.)* |

### 2.3 El español replica exactamente la caja del inglés (2)

V3 los reportó como «minúscula suelta que rompe el paralelismo». Se abrió el fuente: el inglés tiene la misma minúscula.

| Archivo:línea | ES | EN (`e5e5b42`) |
|---|---|---|
| `skills/landing-page-copy/SKILL.md:396` | `simplifica cuando:` | `simplify when:` |
| `skills/landing-page-copy/SKILL.md:400` | `enfatiza el valor cuando:` | `emphasize value when:` |
| `skills/value-perception/SKILL.md:159` | `4. bonos` | `4. bonuses` |

*(Tres líneas, dos entradas de V3.)* Corregir la caja sería **divergir** del fuente, no acercarse a él.

### 2.4 Fiel al fuente y natural en español (2)

| Archivo:línea | ES | EN | Razón |
|---|---|---|---|
| `skills/hormozi-pitch/SKILL.md:68` | `> Estás ayudando a X a lograr el resultado Y…` | `> You're helping X get Y result…` | El inglés usa progresivo; el español progresivo es natural aquí y es un bloque `>` en tuteo. |
| `skills/hormozi-pitch/SKILL.md:167` | `- antirriesgo (sigues ayudando hasta el resultado)` | `- anti-risk (you keep helping until result)` | El inglés también usa 2.ª persona. El «paralelismo nominal» que V3 exige no existe en el fuente. |

### 2.5 Español idiomático: no hay defecto (4)

| Archivo:línea | Item | Razón |
|---|---|---|
| `skills/market-research/SKILL.md:385` | «vale la pena perseguir la idea» | «perseguir una idea» es colocación asentada en español. |
| `skills/idea-to-product/references/offer-key-points.md:74` | «Reemplaza el pensar con plantillas» | El infinitivo sustantivado (`el pensar`) es legítimo y aquí es más preciso que «el pensamiento». |
| `skills/dfy-dwy-diy/SKILL.md:322` | «un punto de precio medio» | `ENCABEZADOS-CANONICOS.md:703` fija `Price point → Punto de precio`. Usar el mismo término en prosa es **coherencia con el aparato**, no un calco suelto. |
| `skills/effort-reduction/SKILL.md:124` | «Reemplaza el trabajo en blanco con plantillas» | Preserva el eco léxico del fuente: `blank work` → línea 125 `Blank pages create friction` / «Las páginas en blanco generan fricción». Romper «en blanco» rompería el eco. |

### 2.6 Orden sujeto-verbo en criterios de éxito: ambos órdenes son idiomáticos (2)

V5 reportó 3 líneas de viñeta de tabulación dura por orden S-V vs V-S. Verificado: **el inglés difiere en cada archivo** (`conversions improve` vs `conversions increase` vs `perceived value increases`), ambos órdenes son español correcto, y ninguna regla de `ENCABEZADOS-CANONICOS.md` cubre contenido de viñeta (solo rótulos). No son claves de búsqueda ni contrato productor→consumidor.

| Archivo:línea | ES actual |
|---|---|
| `skills/value-perception/SKILL.md:332` | `	•	mejoran las conversiones` |
| `skills/bonus-stack/SKILL.md:300` | `	•	aumentan las conversiones` |
| `skills/value-accelerator/SKILL.md:306` | `	•	sube el valor percibido` |

*(Tres líneas, dos entradas de V5 más una tercera contada aparte.)*

---

## 3. Evidencia del blocker

```
$ ls -a                        → sin _archive/
$ find . -name _archive        → (vacío)
$ git ls-files | grep archive  → (vacío)
$ git show e5e5b42:CLAUDE.md | tail -3
- Subagents receive a fully structured brief — they have no memory of the conversation.
- All output lands in `output/` relative to the repo root.
- Skills are user-facing; subagents are internal execution units. Do not mix the two roles.
                               ↑ el commit de saneamiento BORRÓ el bullet de _archive/
$ awk 'NR==67' AGENTS.md
- `_archive/` guarda versiones deprecadas: no las borres ni las edites.
```

`AGENTS.md` es archivo nuevo del commit de traducción y está en `ARCHIVOS_NUEVOS` de `verify_i18n.py:28`, por lo que **el verificador mecánico no lo compara** contra la base. La línea 67 revierte una corrección deliberada del baseline, contradice a `CLAUDE.md` (que termina en su línea 82 sin ella) y le da a Codex una regla sobre un directorio inexistente.

**Arreglo con paridad**: `AGENTS.md` no tiene contraparte inglesa, así que no hay paridad de líneas que respetar; aun así se repara **en la misma línea** sustituyendo la regla falsa por una verdadera sobre `input/`, que sí existe (`input/your-files-go-here.txt`) y está documentada en `README.md:151`. Se descarta el arreglo propuesto por V4/V5 (repetir el texto de la línea 66), que crearía un bullet duplicado.

---

## 4. Plan de reparación por bucket

Orden sugerido: **X5 → C1 → C2 → C5 → C4 → C3 → X3 → X1 → X2 → X4**. Todos los buckets son independientes entre sí salvo los pares marcados ⇄, que deben aplicarse en la misma pasada para no dejar el corpus a medio unificar.

### C1 — `hormozi-orchestrator` · `sub-market` · `CLAUDE.md` (17: 8 major, 9 minor)

**Major**
1. `hormozi-orchestrator.md:265` — «rankeados» es la única ocurrencia del anglicismo en el corpus y «30+» quedó sin traducir; `README.md:82` y `:95` dicen «ordenados» y «Más de 30» para el mismo inglés.
2. `hormozi-orchestrator.md:185` — `[DIY / DWY / DFY / híbrido]` incumple el literal prescrito en `ENCABEZADOS-CANONICOS.md:752`; las otras 3 ocurrencias (`sub-offer:203`, `sub-pricing:26`, `sub-pricing:214`) usan `Híbrido`. Es el placeholder del BRIEF que `sub-pricing:26` declara como formato de entrada.
3-7. `sub-market.md:31,41,50,69,85` — mayúscula tras dos puntos en los 5 encabezados `### Paso N:`; incumple la regla 3 de `ENCABEZADOS-CANONICOS.md` (sentence case) y diverge de su espejo `market-research` y de `sub-pricing`/`sub-sales`/`hormozi-offer`.
8. `sub-market.md:81` — «¿qué tan agudo sienten el dolor?»: adjetivo usado como adverbio de modo.

**Minor** — `orchestrator:107` (única concordancia femenina de un artefacto `.md` en todo el repo; cf. `:130` «OFFER.md actualizado»), `:244` («movimientos … a tomar»), `:11` (apilamiento nominal), `:69` («a través de él»), `:306` («llenador de formularios»); `sub-market:46` («encogiéndose»), `:78` («tomar acción financiera»); `CLAUDE.md:60` («pertenece dentro de») ⇄ `AGENTS.md:38`, `CLAUDE.md:81` («cae en … relativo») ⇄ `AGENTS.md:63`.

### C2 — `sub-offer` · `market-research` · `dfy-dwy-diy` (15: 13 major, 2 minor)

**Major**
1-12. `sub-offer.md:36,38,45,51,62,69,78,86,95,103,110,117` — los 10 `#### Paso N:` y los 2 `### Parte N:` capitalizan tras los dos puntos. El propio archivo se contradice: sus 8 encabezados `### Ángulo N:` (líneas 230-258) **sí** van en minúscula. Espejo `hormozi-offer:191-279` en minúscula.
13. `sub-offer.md:97` — «Incondicional (devolución a los 30 días)»: cambia la ventana de reembolso por una fecha de reembolso. ⇄ `sub-sales.md:67` (C5), aplicar juntos.

**Minor** — `sub-offer:121` («haz el resultado concreto»), `dfy-dwy-diy:128` («Después resume:» → «Luego resume:», 3 contra 2 en el corpus) ⇄ `pricing-strategy:64` (X3).

Sin hallazgos en `market-research/SKILL.md`.

### C3 — `hormozi-offer` · `audit-offer` (3: 1 major, 2 minor)

**Major**
1. `audit-offer.md:309` — la leyenda de puntaje 1-10 está duplicada byte a byte entre los dos dueños de `OFFER_AUDIT.md`; 3 de 4 filas coinciden y solo esta diverge (`necesita mejora` vs `necesita mejorar` en `sub-value.md:39`).

**Minor** — `audit-offer:6` (`GLOSARIO-ES.md:355` prescribe literalmente `Detector de puntos débiles` con D mayúscula; los otros 6 motores del corpus van capitalizados); `hormozi-offer:500` (pierde el numeral enfático «un solo» que sí conserva `orchestrator:319` en el bloque duplicado).

### C4 — `sub-value` · `sub-pricing` (3: 2 major, 1 minor)

**Major**
1. `sub-value.md:63` — «todos» como objetivo, contra «todo el mundo» en `orchestrator:46`, `audit-offer:143` y `hormozi-offer:344` (3 contra 1). Contraparte exacta de `audit-offer:143` en el par de riesgo alto que produce `OFFER_AUDIT.md`.
2. `sub-value.md:173` — «Podría fracasar» contra «Puede que fracase» en `bonus-stack:65` y `:83` (2 contra 1). Es clave del mapeo objeción→bono que ambos escriben en `BONUS_STACK.md`.

**Minor** — `sub-value:104` (colapsa `features → outcomes` y `content → results` en el mismo «→ resultados») ⇄ `value-perception:130` (X4), aplicar juntos.

Sin hallazgos en `sub-pricing.md`: es el lado que **gana** en las 3 divergencias de objeciones.

### C5 — `sub-sales` · `hormozi-pitch` (5: 2 major, 3 minor)

**Major**
1. `hormozi-pitch.md:6` — único H1 de los 19 en minúscula y en imperativo; su gemelo con verbo, `hormozi-offer:6`, usa infinitivo capitalizado.
2. `sub-sales.md:67` — «Devolución del dinero a los 30 días»: mismo cambio de sentido que `sub-offer:97` (C2), en el otro extremo del par productor→consumidor de `PITCH.md`.

**Minor** — `sub-sales:14` y `:147` («Constructor de landing page» singular vs el H1 del skill espejo `landing-page-copy:6` en plural; el par no está en los 659 rótulos, ningún control determinista lo cubre); `sub-sales:425` («el mayor trabajo» ≠ «the most work»).

### X1 — `hormozi-hooks` · `hormozi-style-hooks` · `landing-page-copy` (7: 1 major, 6 minor)

**Major**
1. `hormozi-style-hooks.md:74` — el fuente dice `he applies the same logic`; el español elide el sujeto y «aplica» se lee como imperativo al lector, cuando el párrafo describe en 3.ª persona cómo escribe Hormozi.

**Minor** — `hormozi-style-hooks:76` (única «ecuación de valor» en minúscula del corpus; `GLOSARIO-ES.md §1` y la excepción explícita de la regla 3 exigen `Ecuación de Valor`, y las líneas 68 y 210 del mismo archivo ya la capitalizan), `:172` («Gana la simplicidad» se lee como imperativo), `:295` («que te consigue»); `landing-page-copy:17` («fácil de creer» por `easy to trust`; la propia skill dice «Meta: aumentar la confianza» en `:162`), `:15` y `:437` («tomar acción»).

### X2 — `idea-to-product` · `offer-key-points` · `offer-angles` · `business-model` (3: 1 major, 2 minor)

**Major**
1. `idea-to-product/SKILL.md:274` — `Outcomes sell, not products` → «Venden los resultados…» invierte el sujeto: se lee «ellos venden los resultados». El principio equivalente de `offer-key-points:17` sí lo resuelve.

**Minor** — `offer-angles:84` y `offer-key-points:19` («haz el resultado + adjetivo») ⇄ `sub-offer:121` (C2).

Sin hallazgos en `business-model/SKILL.md`.

### X3 — `pricing-strategy` · `objection-destroyer` · `productize` (7: 1 major, 6 minor)

**Major**
1. `objection-destroyer.md:60` — «Esto no me va a funcionar» contra «Esto no va a funcionar para mí» en `sub-pricing:111`, `sub-value:171` y `bonus-stack:61` (3 contra 1). `sub-pricing` es el productor de `OBJECTIONS.md` y `objection-destroyer` su segundo dueño: si el usuario corre la skill suelta y luego el orquestador, la misma objeción aparece con dos textos en el mismo artefacto, y el mapeo objeción→bono de `BONUS_STACK.md` deja de cruzarse.

**Minor** — `objection-destroyer:73` («Sin tiempo» vs «No hay tiempo» en `sub-pricing:123`), `:67` y `:253` («Ve más profundo»), `:280` («vuelve pequeña la inversión»); `pricing-strategy:64` («Después resume:») ⇄ `dfy-dwy-diy:128` (C2); `productize:16` (doble «con» en la misma cláusula).

### X4 — `value-perception` · `value-accelerator` · `effort-reduction` (6: 0 major, 6 minor)

**Minor** — `value-perception:130` (líneas 129 y 130 terminan ambas en «→ resultados» en una lista vertical, donde el colapso parece error de edición) ⇄ `sub-value:104` (C4); `value-accelerator:9` («vivir un resultado»), `:71` («desde la compra →» sin «hasta»), `:304` («rápida de comprar»); `effort-reduction:190` («cantidad de pasos reducidos», concordancia ambigua), `:213` («no se necesita experiencia» vs «sin experiencia previa» en `hormozi-hooks:199` y `hormozi-style-hooks:129`).

### X5 — `README` · `create-plugin` · `bonus-stack` · `AGENTS.md` · `.codex-plugin` (13: 1 blocker, 0 major, 12 minor)

**Blocker**
1. `AGENTS.md:67` — `_archive/` inexistente (§3). **Reparar primero: es el único blocker del corpus.**

**Minor** — `AGENTS.md:60` («Reglas de diseño clave» vs `CLAUDE.md:78` «Reglas clave de diseño»), `:63` y `:38` ⇄ `CLAUDE.md:81` y `:60` (C1), `:64` («de cara al usuario», giro peninsular, vs `CLAUDE.md:82` «para el usuario»); `README:18` («tres cosas», cifra que no está en el fuente), `:51` («en crudo»), `:165` («a base de prompts»); `create-plugin:233` y `:236` (los 2 únicos comentarios `#` sin traducir del corpus; `ESTILO.md:155` permite traducirlos y `CLAUDE.md:20`, `README:54` y `:58` sí lo hicieron); `bonus-stack:39` («la audiencia objetivo» vs «audiencia objetivo» en `landing-page-copy:38`, `pricing-strategy:41`, `productize:36`), `:169` y `:286` («concéntrate en» vs «enfócate en» en 8 puntos del corpus, incluida la línea inglesa idéntica de `value-perception:318`).

Sin hallazgos en `.codex-plugin/plugin.json` ni `.codex-plugin/marketplace.json`.

---

## 5. Controles que pasaron (sin hallazgos)

Reproducidos y confirmados por el agregador:

- **Paridad estructural**: los 28 `.md` del corpus conservan el número de líneas de `e5e5b42`. Multiset de code spans, recuentos de fences y de rutas/placeholders idénticos.
- **Nombres de artefacto**: los 23 nombres `*.md` sin traducir, en `ALL_CAPS`, con recuento por archivo idéntico EN/ES.
- **Slugs e identificadores**: 18 slugs de `skills/` + 6 de `agents/` coinciden con su frontmatter `name`; `tools:`/`model:`/`color:` intactos; cero slugs traducidos.
- **`Stage` → `Etapa`**: cero supervivientes fuera de `.i18n/`; `Etapa A–E` consistente y separada de `Fase 1–5`.
- **Manifiestos**: claves JSON sin traducir en los 4; solo cambian los valores `description`, ya alineados a una sola cadena.
- **`verify_i18n.py --base e5e5b42`**: 33 archivos comparados, blockers = 0, majors = 3, y los 3 son falsos positivos ya triados.

El aparato mecánico está limpio. **Todo lo que queda es semántico o transversal, es decir, exactamente lo que un verificador determinista no puede ver** — y una parte relevante (los 13 hallazgos de `AGENTS.md`, incluido el blocker) es invisible para él por construcción, porque `AGENTS.md` está en `ARCHIVOS_NUEVOS`.
