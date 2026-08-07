# DECISIONES.md · hormozi-skills-es → español

Registro trazable de las decisiones de proyecto. **Las decisiones marcadas LEY no se revisan durante la traducción.**

- **Repo:** `/home/justincast/Documents/projects/hormozi-skills-es`
- **Rama:** `feat/traduccion-es`
- **Base de paridad:** commit `e5e5b42` — *"fix: sanitize repo before Spanish translation"*
- **Corpus:** 26 archivos `.md` traducibles (20 en `skills/`, 6 en `agents/`) + `README.md` + `CLAUDE.md` + 3 manifiestos JSON. ~29.000 palabras.
- **Fecha del aparato canónico:** 2026-08-07
- **Rol que produjo este documento:** lexicógrafo. **No tradujo ningún archivo del corpus.** Solo escribió dentro de `.i18n/`.

---

## D1 · Alcance, rama y modelo de trabajo — `[PARCIALMENTE COMUNICADA]`

Lo confirmado:

- La traducción se hace sobre la rama `feat/traduccion-es`, partiendo del commit de paridad `e5e5b42`.
- El trabajo se reparte entre **10 traductores independientes que trabajan en paralelo y no se ven entre sí**.
- Cada traductor recibe el aparato canónico de `.i18n/` **incrustado verbatim inline en su prompt** — no como referencia a leer, sino como texto presente.
- El aparato canónico se produce **antes** de que empiece cualquier traducción. Ese es el motivo de existir de este directorio.
- Los 26 archivos se reparten en **buckets**; buckets distintos tienen dueños distintos y varias plantillas están duplicadas entre buckets (ver `ENCABEZADOS-CANONICOS.md`, tabla de duplicaciones).

`[PENDIENTE DE CONFIRMAR]` — el enunciado literal de D1 no llegó al lexicógrafo. Lo anterior se reconstruye del encargo. Si D1 fija además el reparto exacto archivo↔traductor o el criterio de merge, debe agregarse acá antes de arrancar.

---

## D2 · Variante y registro — **LEY**

**Español neutro LatAm. Sin voseo, sin "vosotros", sin localismos.**

Registro **híbrido**. Este es el matiz más importante del proyecto: los archivos tienen **dos audiencias**.

1. **Instrucciones AL asistente** (≈85 % del texto: `The assistant should…`, `Ask the user…`, `Identify:`)
   → **imperativo impersonal dirigido al asistente**: `El asistente debe…`, `Pregunta al usuario…`, `Identifica:`.
   **Nunca "usted".**

2. **Texto que el asistente DICE al usuario** (los bloques `>` de ejemplo, el prompt de instalación de `CLAUDE.md:9-13`, el bloque `DETECTED STAGE:` del orquestador)
   → **tuteo directo, sin hype**.

Desarrollo operativo con ejemplos reales del corpus: `ESTILO.md` §1.

---

## D3 · Qué queda en inglés y qué se traduce — **LEY**

### Quedan en INGLÉS

Anglicismos de marketing:
`hook` · `pitch` · `landing page` · `upsell` · `downsell` · `cross-sell` · `copy` / `copywriting` · `CTA` · `lead` · `lead magnet` · `avatar` · `DFY` / `DWY` / `DIY` · `high-ticket` / `low-ticket` / `mid-ticket` · `onboarding` · `framework` · `checklist` · `swipe file` · `churn` · `skill` / `skills`

Y **todos los nombres de artefacto generado**: `OFFER.md`, `PITCH.md`, `HOOKS.md`, `OFFER_AUDIT.md`, `VALUE_PERCEPTION.md`, `BONUS_STACK.md`, `PRICING.md`, `OBJECTIONS.md`, `PRODUCTIZATION.md`, `LANDING_PAGE.md`, `MARKET_RESEARCH.md`, `OFFER_ANGLES.md`, `OFFER_LADDER.md`, `REVENUE_FLOW.md`, `TIME_TO_VALUE.md`, `EFFORT_REDUCTION.md`, `DELIVERY_MECHANISM.md`, `BUSINESS_MODEL.md`, `CUSTOMER_PAIN.md`, `DEMAND_VALIDATION.md`, `MARKET_SELECTION.md`, `LEAN_OFFER_SYSTEM.md`, `SUMMARY.md` (23 nombres).

Inventario completo y consumible por script: `NO-TRADUCIR.txt`.

### SÍ se traducen

- El **`description:` del frontmatter** — dispara el matching de skills con prompts en español. Es la razón funcional de traducir el repo.
- **`Stage A–E` → `Etapa A–E`**.

### NUNCA se traduce

- El **`name:` del frontmatter**. Es el identificador del skill/agente en el runtime.

### Aplicaciones derivadas resueltas por el lexicógrafo

| Situación | Resolución | Dónde queda registrada |
|---|---|---|
| `skill` = artefacto vs. `skill` = habilidad humana | artefacto → `skill` (KEEP, femenino: *la skill*); habilidad humana → **habilidad** | `GLOSARIO-ES.md` §8 |
| Género de los anglicismos KEEP | *la skill*, *el hook*, *el pitch*, *el copy*, *el CTA*, *la landing page*, *el brief*, *el framework*, *el checklist*, *el upsell*, *los DMs*, *las FAQ* | `GLOSARIO-ES.md` §§3-8 |
| Expansiones `Done For You` / `Done With You` / `Do It Yourself` | quedan en inglés, sin glose (el cuerpo del skill ya las explica) | `GLOSARIO-ES.md` §3 |
| `Grand Slam Offer` | KEEP, glosado la **primera vez de cada archivo** como `Grand Slam Offer (oferta irresistible)` | `GLOSARIO-ES.md` §1 |
| Acróstico MAGIC | líneas en inglés byte a byte + glose en español tras ` — `; texto exacto fijado | `GLOSARIO-ES.md` §0 |

---

## D4 · `[NO COMUNICADA AL LEXICÓGRAFO]`

El enunciado de D4 no llegó con el encargo. **No se inventa.**
Debe completarse antes de arrancar la traducción si condiciona el trabajo de los 10 traductores.

Candidatos observables que probablemente cubra: criterio de bucketización de los 26 archivos, orden de traducción, o política de QA/merge.

---

## D5 · `[NO COMUNICADA AL LEXICÓGRAFO]`

El enunciado de D5 no llegó con el encargo. **No se inventa.**
Debe completarse antes de arrancar la traducción si condiciona el trabajo de los 10 traductores.

---

## D6 · `LICENSE` queda en inglés — **LEY**

El archivo `LICENSE` (MIT) **no se traduce**. Está registrado en `NO-TRADUCIR.txt`.

---

## Decisiones terminológicas tomadas por el lexicógrafo (no eran ley; se fijan acá)

Estas no venían decididas. Se resuelven de una sola forma para que 10 traductores no diverjan. Son **revisables por el usuario**, pero mientras no se cambien acá, son vinculantes.

| # | Término | Decisión | Razón |
|---|---|---|---|
| 1 | `skill` (artefacto) | **femenino: la skill / las skills** | "Habilidad" y "capacidad" son femeninas; el ecosistema en español dice "las skills". 203 ocurrencias en 23 archivos: una discordancia de género se nota en todo el repo. |
| 2 | `skill` (humana) ≠ `skill` (artefacto) | humana → **habilidad** | `skill level`, `skill deficits`, `your skills`, `users lack skill or time` no hablan del artefacto. Traducirlos como "skill" haría ilegible `business-model` y `dfy-dwy-diy`. |
| 3 | `asset` | **recurso** (excepto *turn problems into assets* → **activos**) | El sentido dominante es "entregable". `Quick Win Asset` → "Recurso de victoria rápida" lee natural; "Activo de victoria rápida" no. |
| 4 | `browsers` | **curiosos** | Se opone a *compradores*. "Mirones" es coloquial; "navegantes" colisiona con navegador web. |
| 5 | `contrarian` | **a contracorriente** | Español neutro y transparente. "Contrarian" sin traducir no está asentado en LatAm; "contrario" pierde el sentido de desafiar el consenso. |
| 6 | `callout` | **callout** (KEEP) | `Callout Hooks` → "Hooks de callout". Coherente con mantener `hook`; "hooks de interpelación" es correcto pero nadie lo dice. |
| 7 | `headline` / `subheadline` | **KEEP** | Coherente con `copy` y `hook`, que ya son ley. Traducir a "titular/subtitular" rompería la familia léxica de copywriting. |
| 8 | `brief` | **KEEP** (*el brief*) | Vocabulario estándar de agencia en LatAm. `ORCHESTRATOR BRIEF:` → `BRIEF DEL ORQUESTADOR:`. Alternativa descartada: "informe estructurado" (más largo y menos preciso). |
| 9 | `tier` | **nivel** | Colisiona con "nivel de involucramiento" y con los niveles de la escalera, pero la colisión es semánticamente coherente: son el mismo concepto en tres capas. Evita introducir un cuarto término. |
| 10 | Familia `stack` | `value stack` → **stack de valor**; verbo *to stack* → **apilar**; *stacking* → **apilado** | Decisión mixta deliberada. El sustantivo compuesto queda en híbrido (ley del usuario); el verbo y el sustantivo de actividad se traducen porque "stackear" es jerga y "hacer stacking" es feo. Resolución completa en `GLOSARIO-ES.md` §7. |
| 11 | `charm pricing` | **KEEP** + glose la 1.ª vez | "Precio de encanto" es un calco que no circula. |
| 12 | `toolkit` | **KEEP** | Es un formato de producto nombrado dentro de la lista `Program / Course / Toolkit`; traducir solo uno rompe el paralelismo. |
| 13 | `score` (sust./verbo) | **puntaje / puntuar** | "Puntaje" es marcadamente LatAm, que es la variante pedida. |
| 14 | `case study` | **caso de éxito** | Arranque del usuario, verificado: en este corpus siempre funciona como elemento de prueba de venta, no como género académico. |
| 15 | `time delay` | **demora** | Arranque del usuario, verificado. "Retraso" implica una falla; acá es un intervalo neutro dentro de una ecuación. |

### Marcadores `[REVISAR]` abiertos

| Término | Propuesta actual | Frecuencia | Duda |
|---|---|---|---|
| `retainer` | retainer (KEEP) | 1/1 | "Iguala" es LatAm pero suena contable, no de agencia. |
| `workbook` | workbook (KEEP) | 2/2 | "Cuaderno de trabajo" es correcto pero largo dentro de una lista de formatos cortos. |
| `fulfillment` | fulfillment (KEEP) | 1/1 | Acá significa "entrega del servicio", no logística. |
| `tradeoff` | tradeoff (KEEP) | ~8/5 | "Compensación" pierde el matiz de "elegir A implica perder B". |

---

## Entregables producidos

| Archivo | Contenido | Tamaño |
|---|---|---|
| `.i18n/GLOSARIO-ES.md` | Cadena canónica de la Ecuación de Valor + 25 cadenas/fórmulas más, acróstico MAGIC, **223 entradas** de glosario con frecuencia medida, resolución de la familia *stack*, 19 falsos amigos, matriz de registro | 12 secciones, 301 filas de tabla |
| `.i18n/ENCABEZADOS-CANONICOS.md` | **278** encabezados de plantilla (**87** en ≥2 archivos), 48 encabezados de estructura, 58 pseudoencabezados en texto plano, 189 etiquetas de viñeta, 47 cabeceras de columna, 39 bloques literales del orquestador = **659 rótulos**, 210 de ellos compartidos por ≥2 archivos | 6 tablas |
| `.i18n/NO-TRADUCIR.txt` | **189 tokens**, uno por línea, sin duplicados ni comentarios — consumible por script Python | plano |
| `.i18n/ESTILO.md` | Registro D2 con ejemplos reales y referencias `archivo:línea`, puntuación `¿ ¡`, 13 caracteres a conservar byte a byte, viñetas de tab duro, 22 prohibiciones anticalco, preferencias LatAm, checklist de 12 puntos | 7 secciones |
| `.i18n/DECISIONES.md` | este archivo | — |

## Verificaciones ejecutadas sobre el fuente

- Frecuencias: `grep -ohiP <patrón> <28 archivos> \| wc -l` y `grep -liP … \| wc -l`. Ninguna estimada a ojo.
- Cadena canónica: confirmada en 3 archivos, 1 ocurrencia cada uno, con `×` = `c3 97` (U+00D7) verificado en hexdump.
- Encabezados: extracción programática de `^#{1,4}` distinguiendo dentro/fuera de fences ` ```md `, con normalización de la numeración `N.`.
- Viñetas de tab: `grep -rlP '(\t•\t|\t\d+\.\t)'` → **19 archivos**, coincide con lo esperado.
- Separador `⸻` (U+2E3B): 187 ocurrencias en 19 archivos.
- Slugs de skill y agente: leídos del `name:` del frontmatter real, no de memoria.
