# Informe de consolidación — Ola 1 (traducción ES)

**Repo:** `/home/justincast/Documents/projects/hormozi-skills-es`
**Rama:** `feat/traduccion-es` · **BASE de paridad:** `e5e5b42`
**Informes recibidos:** 10 de 10 (C1–C5 claude, X1–X5 codex)
**Fecha de consolidación:** 2026-08-07

---

## 1. Resumen ejecutivo

| Control | Resultado |
|---|---|
| Cobertura | **33/33 archivos, cada uno exactamente una vez.** Sin huérfanos, sin duplicados. |
| Paridad estructural (líneas, fences, separadores, tabs, filas de tabla) | **0 banderas rojas reales.** 1 desviación declarada y legítima (`.codex-plugin/plugin.json`, stub → completo). |
| Cadena canónica de Valor | **Idéntica en los 10 informes y byte a byte en los 3 archivos en disco.** |
| Residuo de inglés sin traducir | **0.** Las 19 coincidencias son términos KEEP o líneas prescritas por el núcleo. |
| Identificadores funcionales (`name:` de frontmatter, nombres de artefacto) | **100 % preservados.** |
| `verify_i18n.py --base e5e5b42` | `blockers=2 majors=21` → **triaje: los 23 son falsos positivos.** Ver §5. |
| Divergencias de glosario que exigen decisión | **4** (ver §7). |

**Veredicto:** la ola 1 está estructuralmente limpia y lista para revisión de contenido. No hay ningún archivo que haya que retraducir. Lo que queda son 4 decisiones de unificación léxica y 2 correcciones puntuales de una línea cada una.

---

## 2. Cobertura por bucket

| Bucket | Track | Archivos | Estados | Paridad |
|---|---|---:|---|---|
| C1 | claude | 5 | 5 traducido | OK |
| C2 | claude | 3 | 3 traducido | OK |
| C3 | claude | 2 | 2 traducido | OK |
| C4 | claude | 2 | 2 traducido | OK |
| C5 | claude | 2 | 2 traducido | OK |
| X1 | codex | 3 | 3 traducido | OK |
| X2 | codex | 4 | 4 traducido | OK |
| X3 | codex | 3 | 3 traducido | OK |
| X4 | codex | 3 | 3 traducido | OK |
| X5 | codex | 6 | 4 traducido, 2 creado | OK (1 desviación declarada) |
| **Total** | | **33** | **31 traducido, 2 creado** | |

### Detalle de cobertura

| Categoría | Esperado | Cubierto | Estado |
|---|---:|---:|---|
| `skills/**/*.md` (18 `SKILL.md` + 2 `references/`) | 20 | 20 | Completo |
| `agents/*.md` | 6 | 6 | Completo |
| `README.md` | 1 | 1 | C5→X5 |
| `CLAUDE.md` | 1 | 1 | C1 |
| Manifiestos (4) | 4 | 4 | C1 (claude ×2), X5 (codex ×2) |
| `AGENTS.md` | creado | creado | X5 |
| `.codex-plugin/marketplace.json` | creado | creado | X5 |

**Huérfanos:** ninguno. **Duplicados:** ninguno. **Fantasmas (reportados pero inexistentes):** ninguno.

Se confirma que los dos archivos exigidos como **creado** lo están:

```
?? .codex-plugin/marketplace.json      16 líneas
?? AGENTS.md                           67 líneas
```

> Nota: `26 archivos de contenido` = 18 `SKILL.md` + 2 `references/*.md` + 6 `agents/*.md`. La cifra "18 skills y 6 agentes" que aparece en `README.md` y en `marketplace.json` es por tanto **correcta**, no un error heredado.

---

## 3. Banderas rojas de paridad estructural

Verificación hecha **en disco**, no sobre lo declarado: para cada archivo se comparó el árbol de trabajo contra `git show e5e5b42:<ruta>`.

### 3.1 Resultado

**Ninguna bandera roja real.** Los 28 `.md` modificados conservan exactamente: número de líneas, fences ` ``` `, separadores `---`, líneas con tabulador y filas de tabla `|`.

Controles globales adicionales:

| Carácter intocable | BASE | Ahora | Estado |
|---|---:|---:|---|
| `→` (U+2192) | 212 | 212 | OK |
| `×` (U+00D7) | 10 | 10 | OK |
| `name:` de frontmatter | 28 | 28 idénticos | OK |
| Nombres de artefacto (`OFFER.md`, `PITCH.md`, …) | 26 distintos | 26 idénticos, mismas frecuencias | OK |

### 3.2 Única desviación de conteo — declarada y legítima

| Ruta | Métrica | Antes | Después | Dictamen |
|---|---|---:|---:|---|
| `.codex-plugin/plugin.json` | líneas | 3 | 12 | **No es regresión.** En BASE el archivo era el stub `{"name": "hormozi-skills-es"}`. X5 lo completó siguiendo la spec de `skills/create-plugin/SKILL.md:88-103`. El JSON valida. |

Los 4 manifiestos parsean como JSON válido.

---

## 4. Prueba de lectura del núcleo

### 4.1 Cadena canónica de Valor — **los 10 buckets coinciden**

Versión canónica en `.i18n/NUCLEO-INLINE.md` §0 (línea 9):

```
Valor = (Resultado Soñado × Probabilidad Percibida) / (Demora × Esfuerzo y Sacrificio)
```

Los 10 informes reportan esta cadena **carácter por carácter idéntica**. **Cero divergencias**, es decir: ningún traductor omitió leer el núcleo.

Verificación en disco de las 3 ocurrencias que §0 prescribe:

| Archivo | Línea esperada | Línea real | Envoltorio `**…**` | Estado |
|---|---:|---:|---|---|
| `agents/sub-value.md` | 35 | 35 | sí (correcto) | OK |
| `agents/sub-sales.md` | 45 | 45 | sí (correcto) | OK |
| `skills/hormozi-pitch/SKILL.md` | 99 | 99 | no (correcto) | OK |

Sin residuo inglés de la fórmula. La variante de prosa de `README.md` está presente (línea 175) con la única diferencia declarada por X5: mayúscula inicial `Ecuación` por abrir viñeta.

### 4.2 Rótulos canónicos

Los 30 rótulos citados por los 10 buckets como prueba de lectura son coherentes entre sí y con `NUCLEO-INLINE.md`. No se detectó ningún par contradictorio.

### 4.3 Acróstico MAGIC (punto de fricción entre C5 y X-track)

Regla del núcleo §A: conservar la línea inglesa byte a byte + glose español tras ` — `. **Ambos archivos cumplen.**

- `agents/sub-sales.md:86-90` — conserva negrita de inicial y paréntesis del fuente. Correcto.
- `skills/hormozi-pitch/SKILL.md:212-216` — sin negrita ni paréntesis, como su fuente. Correcto.

La duda de C5 sobre `Give a goal — da una meta clara` (el fuente dice `Give a goal`, el glose canónico dice `da una meta clara`) **se resuelve a favor de lo que C5 hizo**: el núcleo fija el glose, no lo deriva del fuente. Sin acción.

---

## 5. Verificador mecánico `verify_i18n.py` — triaje

Ejecución: `python3 .i18n/verify_i18n.py --base e5e5b42` → `blockers=2 majors=21 minors=0` (exit 1).

**Tras triaje manual, los 23 hallazgos son falsos positivos.** Detalle:

### 5.1 Los 2 BLOCKERS — falsos positivos por regla no implementada

| Archivo | Hallazgo | Diff real | Dictamen |
|---|---|---|---|
| `CLAUDE.md` | `fence-literal-alterado: fence #1 (bash)` | solo `# Project (default)` → `# Proyecto (por defecto)` y `# User (global)` → `# Usuario (global)` | **Falso positivo** |
| `README.md` | `fence-literal-alterado: fence #3 (bash)` | solo `# Clone the skill library` → `# Clona la biblioteca de skills` y `# Copy skills and agents…` → `# Copia skills y agents…` | **Falso positivo** |

Motivo: `ESTILO.md:155` (§3.2) dice literalmente:

> Bloques de código (` ```bash `, ` ```json `, ` ```text `): **el código no se traduce.** En ` ```json ` no se traduce ni una clave ni un valor. En ` ```bash ` se pueden traducir **solo los comentarios `#`**.

C1 y X5 tradujeron **únicamente comentarios `#`**; ningún comando fue alterado. El verificador no implementa la excepción de §3.2 para `bash`. **La traducción es correcta; el verificador tiene el bug.**

> **Acción sugerida (no ejecutada):** parchear `verify_i18n.py` para exceptuar las líneas que empiezan por `#` dentro de fences `bash`. No tocar `CLAUDE.md` ni `README.md`.

### 5.2 Los 21 MAJORS — tres causas, todas espurias

| Causa | Hallazgos afectados | Explicación |
|---|---|---|
| **Regla identidad ES==EN** | 13: `OFFER.md`, `PRICING.md`, `PITCH.md`, `OBJECTIONS.md`, `HOOKS.md`, `SUMMARY.md`, `PRODUCTIZATION.md`, `Bullets`, `Upsell`, `Downsell`, `Upsell 1`, `Upsell 2`, `Downsell 1` | El verificador dispara `rotulo-canonico-sin-traducir: 'X' -> deberia ser 'X'`. En `NUCLEO-INLINE.md` estas filas tienen ES **idéntico** a EN (líneas 188, 198, 202, 211, 216, 218, 395, 562, 569, 570). Es autocontradictorio por construcción. |
| **Fila de tabla mal parseada** | 1: `'Plantilla' -> deberia ser 'Dueño A'` | `NUCLEO-INLINE.md:131` es `\| Plantilla \| Dueño A \| Dueño B \| Riesgo \|`, la **cabecera** de la matriz de propiedad/riesgo, no un mapeo de términos. Bug del parser. |
| **Términos KEEP y líneas prescritas** | 7: `offer`, `funnel`, `positioning`, `program`, y los 3 `residuo-ingles` | `offer` (55×) solo aparece dentro de identificadores (`sub-offer`, `audit-offer`, `offer-angles`, `hormozi-offer`), nombres de artefacto y `Grand Slam Offer` (KEEP). `funnel`/`positioning` están en los arrays `keywords` de los manifiestos. `program` está en la línea MAGIC que el núcleo exige en inglés. Los `residuo-ingles` son `Done For You` / `done-for-you` / `Make it about them` — todos KEEP o prescritos. |

### 5.3 Barrido independiente de residuo inglés

Barrido propio sobre las 19 líneas con vocabulario inglés frecuente: **las 19 son legítimas** (`done-for-you`, `done-with-you`, `do-it-yourself`, `above the fold`, y las 2 líneas MAGIC). **Cero residuo real.**

---

## 6. Desviaciones de glosario agregadas por término

Agregación de las 22 desviaciones declaradas por los 10 buckets. La columna **Conflicto** marca los términos que aparecen en más de un bucket con renderings distintos.

| Término EN | Rendering(s) ES | Bucket(s) | Conflicto | Dictamen |
|---|---|---|:---:|---|
| **feedback** | `retroalimentación` (×3) · `feedback` (×1) | C2, X4 / C3 | **SÍ** | **Inconsistencia real.** Ver §7.1 |
| **em dash `—` → `:`** | conservado (×4 archivos) · convertido (×1) | C1, C4, C5 / C2 | **SÍ (aparente)** | C2 tenía prescripción explícita línea a línea en `ESTILO §1.1(b)`; su conversión es correcta. C1 sí ignoró una prescripción de `ESTILO §1.2`. Ver §7.2 |
| **`*-Killer`** | `Matafricciones` (compuesto) · `matador de objeciones` (perífrasis) | X4 / X5 | **SÍ** | Patrón inconsistente. Ver §7.3 |
| **description de plugin** | 3 redacciones distintas de una cadena que en EN era única | C1 / X5 | **SÍ** | Ver §7.4 |
| **charm pricing** | `**Charm pricing** (precios terminados en 7 o 9)` · `charm pricing (…; p. ej. 27, 97, 297)` | C4 / X3 | parcial | Ambos glosan la primera ocurrencia del archivo, como manda el glosario. La mayúscula difiere solo por posición (inicio de viñeta vs. media de lista). **Aceptable.** |
| **Belief shift → Proof** | `Cambio de creencia → Prueba` · `Cambio de creencia → Elemento de prueba` | X3 / C4 | no | **Justificado y verificado en fuente:** `objection-destroyer` dice `Proof`; `sub-pricing:143` dice `Proof element`. Divergencia correcta. |
| **Purchase → Start → Progress → Result** | Title Case · minúscula | X4 / C4 | no | **Justificado y verificado en fuente:** `effort-reduction:62` es línea suelta en Title Case; `sub-value:128` va en minúscula dentro de paréntesis en prosa. Correcto. |
| **Hybrid Hooks** | `los que mejor funcionan` · `los mejores` | X1, C5 / X1 | no | Refleja la distinción del fuente (`Best performers` vs `Best`) y respeta §C. Correcto, aunque conviven dentro de `hormozi-hooks`. |
| **Objection Destroyer** | `Destructor de objeciones` | C4, X3 | no | **Coincidencia verificada** entre `objection-destroyer:6` y `sub-pricing:14,:104`. Riesgo de C4 resuelto favorablemente. |
| **Objection Handling Statements** | `Frases para manejar objeciones` | C4, X3 | no | **Coincidencia byte a byte verificada** (`sub-pricing:260`, `objection-destroyer:219`). |
| **accountability** | `rendición de cuentas` | C2, C3 | no | Consistente. |
| **assets** | `Activos` | X2 | no | Correcto: §C:644 sobrescribe explícitamente el §5 del glosario (`asset → recurso`) para `business-model`. |
| **skills** (habilidad humana) | `habilidades` | X3 | no | Correcto por desambiguación §8. |
| **value equation** (minúscula en fuente) | `Ecuación de Valor` | X4 | no | Correcto: nombre propio de framework, §1. |
| **Weak Point Detector** | `detector de puntos débiles` | C3 | no | Correcto: `ESTILO §4` impone caja de oración en encabezados. |
| **Strategic Monetization Engine** | `Motor de Monetización Estratégica` | X2 | no | Correcto por analogía con los otros `Motor de …` ya fijados. |
| **pitch deck** | `pitch deck` (KEEP) | C1 | no | Extensión razonable de `pitch` KEEP. |
| **freelancing** | `freelancing` (KEEP) | X2 | no | Extensión razonable de `freelancer` KEEP. |
| **`[bullet]`** (placeholder) | `[bullet]` (KEEP) | C1 | no | Correcto: es placeholder de plantilla, no viñeta markdown. |
| **payment plans** | `planes de pagos` | X3 | no | Concordancia de plural. Correcto. |
| **Stress test the price** | `Pon el precio a prueba` | X3 | no | Correcto: evita el calco, mantiene el registro imperativo. |
| **insider knowledge / curiosity bait / struggle** | `información privilegiada` / `carnada de curiosidad` / `trabarse` | X1 | no | Fuera de glosario; elecciones coherentes y aplicadas de forma uniforme. |

---

## 7. Inconsistencias entre buckets que exigen decisión

### 7.1 `feedback` — **la única inconsistencia léxica real** (prioridad alta, trivial de arreglar)

| Ubicación | Rendering | Bucket |
|---|---|---|
| `skills/dfy-dwy-diy/SKILL.md:84` | `ciclos de retroalimentación` | C2 |
| `skills/dfy-dwy-diy/SKILL.md:229` | `agrega auditorías o retroalimentación` | C2 |
| `skills/effort-reduction/SKILL.md:166` | `retroalimentación personalizada` | X4 |
| `skills/audit-offer/SKILL.md:24` | **`el feedback`** | C3 |

El término no está en `GLOSARIO-ES.md` ni en la lista KEEP, así que la regla por defecto (traducir) aplica. **3 contra 1 a favor de `retroalimentación`.**

> **Decisión pedida:** ¿unificar `audit-offer:24` a `el feedback` → `la retroalimentación`? (1 línea) — o al revés, declarar `feedback` KEEP y cambiar las otras 3.

### 7.2 Em dash en `agents/hormozi-orchestrator.md:308` (prioridad media, 1 línea)

C1 conservó el em dash:

```
"Eso es demasiado amplio — déjame proponerte una versión más afilada"
```

pero `ESTILO.md §1.2` cita esa línea exacta **con coma**. C1 lo declaró y argumentó que `ESTILO §3`/`§7.2` protegen U+2014 byte a byte.

Contraste: C2 sí aplicó la conversión en `sub-offer.md:16` porque `ESTILO §1.1(b)` traía prescripción explícita para esa línea. **Las dos situaciones son idénticas en estructura**, y se resolvieron al revés.

> **Decisión pedida:** ¿prevalece la prescripción línea a línea de `ESTILO §1.2` (→ cambiar el `—` por `,`) o la protección genérica de U+2014 (→ dejar como está)? Afecta 1 línea. C4 y C5 también conservaron sus em dashes bajo el mismo criterio que C1, así que la respuesta fija el precedente para todo el corpus.

### 7.3 Familia `*-Killer` — patrón inconsistente (prioridad media, 1 línea)

| Fuente EN | ES actual | Forma | Bucket |
|---|---|---|---|
| `# Skill: Effort Reduction (Friction Killer)` | `# Skill: Reducción de esfuerzo (Matafricciones)` | compuesto, mayúscula | X4 |
| `# Skill: Bonus Stack Generator (Objection Killer)` | `# Skill: Generador de stack de bonos (matador de objeciones)` | perífrasis, minúscula | X5 |

`Matafricciones` está fijado en el glosario §5; `Objection Killer` no tiene entrada. X5 descartó `Mataobjeciones` por sonar forzado.

> **Decisión pedida:** ¿se acepta la asimetría (el glosario manda en uno, la naturalidad en el otro) o se unifica? Las dos salidas coherentes serían `(Mataobjeciones)` o bien degradar `Matafricciones` a `(matador de fricciones)`.

### 7.4 Las tres `description` de plugin ya no coinciden (prioridad alta, funcional)

En BASE, `.claude-plugin/plugin.json` y `.claude-plugin/marketplace.json → plugins[0]` tenían la **misma cadena byte a byte**. Ahora hay **tres redacciones**:

| Archivo | Redacción actual |
|---|---|
| `.claude-plugin/plugin.json` | `Framework de **la** Grand Slam Offer **(oferta irresistible)**. … optimización **de** valor, …` |
| `.claude-plugin/marketplace.json` | `Framework de **la** Grand Slam Offer. … optimización **de** valor, …` |
| `.codex-plugin/plugin.json` | `Framework de Grand Slam Offer. … optimización **del** valor, …` |

Dos causas acumuladas:
1. **C1**, aplicando "glosar la primera vez de cada archivo", puso el glose solo en `plugin.json` (en `marketplace.json` ya se había consumido en `metadata.description`). Declarado.
2. **X5**, que escribió el manifiesto de Codex sin ver el de Claude, eligió redacción propia (`de Grand Slam Offer`, `optimización del valor`). **No detectado por ningún bucket** — emerge solo en consolidación.

> **Decisión pedida:** ¿alinear las tres a una sola cadena? Recomendación: usar la de `.claude-plugin/plugin.json` (con glose) en los tres, o sin glose en los tres. Es un campo de escaparate visible al usuario final.

### 7.5 Registro de los H1 de skill (prioridad baja, cosmética)

Conviven tres registros en los 18 títulos:

- **Nominal** (16 archivos): `Skill: Investigación de mercado…`, `Skill: Generador de hooks…`
- **Infinitivo** (1): `skills/hormozi-offer/SKILL.md` → `Skill: Construir una Grand Slam Offer → OFFER.md`
- **Imperativo en minúscula** (1): `skills/hormozi-pitch/SKILL.md` → `Skill: construye un pitch al estilo Hormozi`

C3 levantó exactamente esta duda para los encabezados `Paso N`. La forma nominal es la mayoritaria por amplio margen.

> **Decisión pedida:** ¿normalizar los 2 outliers a forma nominal? Afecta 2 líneas.

---

## 8. Dudas abiertas que necesitan al usuario

Ordenadas por impacto. Las dudas de los informes que ya quedaron **resueltas por verificación** se listan al final para cerrarlas explícitamente.

### 8.1 Requieren decisión

| # | Tema | Archivos | Coste |
|---|---|---|---|
| 1 | Unificar `feedback` vs `retroalimentación` (§7.1) | `audit-offer/SKILL.md:24` | 1 línea |
| 2 | Unificar las 3 `description` de plugin (§7.4) | 3 manifiestos | 3 líneas |
| 3 | Em dash vs coma en `ESTILO §1.2` (§7.2) — **fija precedente para todo el corpus** | `hormozi-orchestrator.md:308` | 1 línea |
| 4 | Patrón `*-Killer` (§7.3) | `bonus-stack/SKILL.md:6` | 1 línea |
| 5 | Parchear `verify_i18n.py` para la excepción `bash #` de `ESTILO §3.2` (§5.1) — si no, la puerta mecánica seguirá en rojo permanente | `.i18n/verify_i18n.py` | ~5 líneas |
| 6 | ¿`keywords` de los manifiestos en inglés o español? Hoy están en inglés (`funnel`, `positioning`, `offer`…), lo que es defendible como tokens de búsqueda | 2 manifiestos | decisión |
| 7 | ¿`.codex-plugin/plugin.json` debe llevar el array `keywords` que sí tiene el de Claude? La spec de `create-plugin` no lo incluye (X5) | 1 manifiesto | decisión |
| 8 | `interface.displayName` de `.codex-plugin/marketplace.json` quedó como el slug `hormozi-skills-es`; ¿se quiere un nombre legible (`Hormozi Skills ES`)? (X5) | 1 manifiesto | 1 línea |
| 9 | Registro de los H1 de skill (§7.5) | 2 archivos | 2 líneas |
| 10 | `AGENTS.md` es prosa nueva sin fuente inglesa; requiere lectura de aprobación, no cotejo (X5) | `AGENTS.md` | revisión |
| 11 | `CLAUDE.md` en disco (82 líneas) no contiene la línea sobre `_archive/` que sí aparece en el contexto del sistema. C1 tradujo el archivo real sin añadirla. ¿Se debe añadir? | `CLAUDE.md` | decisión |
| 12 | Los 3 archivos de X4 y el de X1 terminan **sin salto de línea final**, igual que el fuente. Si se adopta un linter que lo exija, aplicar a los 28 a la vez | corpus | decisión |

### 8.2 Conflictos de regla resueltos por los traductores — **ratificación recomendada**

Los tres se resolvieron **a favor del núcleo** y, notablemente, **X1 y X2 llegaron a la misma resolución de forma independiente**, lo que refuerza el criterio:

| Caso | Qué se hizo | Ratificar |
|---|---|---|
| Fence ` ```text ` en `hormozi-hooks/SKILL.md:68-73` | Traducido, porque §A fija `QUIÉN + RESULTADO + VELOCIDAD/FACILIDAD + ELIMINACIÓN DE OBJECIÓN` y es la única ocurrencia (X1) | Sí |
| Fence ` ```text ` en `idea-to-product/SKILL.md:37-43` | Traducido, porque §A fija `Idea → Oferta → Pitch` e `Idea → Mercado → Oferta → Pitch → Contenido → Ventas` (X2) | Sí |
| Fences sin etiqueta (bloques BRIEF) en `sub-offer.md:22-32` y `sub-pricing.md:23-32` | Traducidos, porque §8 y §C fijan rótulos internos (`Etapa: [A / B / C / D / E]`) (C2, C4) | Sí |

> Si se ratifica, conviene añadir la excepción a `ESTILO §3.2` para que la regla quede escrita y no se reabra en la ola 2.

### 8.3 Dudas ya cerradas por verificación en disco (sin acción)

| Duda original | Bucket | Cierre |
|---|---|---|
| ¿`Destructor de objeciones` coincide entre `sub-pricing` y `objection-destroyer`? | C4 | **Sí**, verificado en `:6`, `:14`, `:104`. |
| ¿`Frases para manejar objeciones` coincide byte a byte entre buckets? | X3, C4 | **Sí**, verificado en `sub-pricing:260` y `objection-destroyer:219`. |
| ¿`Give a goal` debe llevar el glose `da una meta clara`? | C5 | **Sí**, el núcleo §A fija el glose con independencia del fuente. |
| ¿`Belief shift → Elemento de prueba` rompe el canon? | C4 | **No**, el fuente dice `Proof element`. Correcto. |
| ¿`compra → inicio → progreso → resultado` en minúscula rompe el canon? | C4 | **No**, el fuente va en minúscula en prosa. Correcto. |
| ¿Se preservaron los identificadores `name:` y los nombres de artefacto? | todos | **Sí**, 100 %. |
| ¿Anidamiento de viñetas de dos tabs en los archivos de X1? | X1 | **Confirmado inexistente**; el aviso del bucket era erróneo. |

---

## 9. Metodología de verificación

Todo lo de §3, §4 y §5 se comprobó **contra el disco**, no contra los informes:

```bash
git status --short
git diff --name-only e5e5b42
# por archivo: wc -l  vs  git show e5e5b42:<ruta> | wc -l
# por archivo: grep -c '^```' | grep -c '^---$' | grep -cP '\t' | grep -c '^|'
python3 .i18n/verify_i18n.py --base e5e5b42
```

Los conteos de separadores de este informe usan la definición `^---$` y por eso difieren de los declarados por algunos buckets (que excluían el frontmatter). Lo que se validó es la **invariancia antes/después** bajo una definición única, que se cumple en los 28 archivos.

---

*Consolidado a partir de los 10 informes de la ola 1. Ningún archivo traducido fue modificado durante esta consolidación.*
