# GLOSARIO-ES · hormozi-skills-es

Aparato terminológico canónico para la traducción al **español neutro LatAm**.
Se incrusta *verbatim inline* en los prompts de los 10 traductores. **Ninguna entrada es opcional.**

- **Corpus medido:** 26 archivos `.md` (20 en `skills/`, 6 en `agents/`) + `README.md` + `CLAUDE.md` = **28 archivos**, ~29.000 palabras.
- **Frecuencia:** `N/M` = *N* ocurrencias totales en *M* archivos distintos. Medida con `grep -ohiP … | wc -l` y `grep -liP … | wc -l`. **No estimada.**
- **¿KEEP inglés?** `SÍ` = se deja en inglés tal cual · `NO` = se traduce · `PARCIAL` = híbrido (una parte queda en inglés).
- Los ítems marcados **`[REVISAR]`** llevan mi mejor propuesta pero necesitan visto bueno del usuario.

---

## 0. CADENA CANÓNICA OBLIGATORIA

Esta línea aparece **byte a byte idéntica** en tres archivos que pertenecen a buckets con dueños distintos:
`agents/sub-value.md:35`, `agents/sub-sales.md:45` (ambas envueltas en `**…**`) y `skills/hormozi-pitch/SKILL.md:99` (sin negritas).

```
EN: Value = (Dream Outcome × Perceived Likelihood) / (Time Delay × Effort & Sacrifice)
ES: Valor = (Resultado Soñado × Probabilidad Percibida) / (Demora × Esfuerzo y Sacrificio)
```

Reglas duras sobre esta cadena:

1. El signo de multiplicación es **`×` (U+00D7)**, verificado en el fuente (`c3 97` en UTF-8). **Nunca** la letra `x`.
2. El `&` del inglés se convierte en **`y`** dentro de la fórmula.
3. Los cuatro nombres de variable van en **Title Case** *solo dentro de esta fórmula* (son nombres de variable). Como encabezado o etiqueta suelta se escriben en minúscula: `Resultado soñado`, `Probabilidad percibida`, `Demora`, `Esfuerzo y sacrificio`.
4. Se conservan los paréntesis, la barra `/` y los espacios exactamente como están.
5. Se conserva el envoltorio `**…**` donde el original lo tenga, y se omite donde no lo tenga.

**Variante en `README.md:176`** (prosa, no fórmula): `Dream outcome × likelihood × time delay × effort equation` → `ecuación resultado soñado × probabilidad × demora × esfuerzo`.

### Otras cadenas de fórmula que deben ser idénticas en todos los archivos

| EN | ES | Archivos |
|---|---|---|
| `WHO + RESULT + SPEED/EASE + OBJECTION REMOVAL` | `QUIÉN + RESULTADO + VELOCIDAD/FACILIDAD + ELIMINACIÓN DE OBJECIÓN` | hormozi-hooks, hormozi-hooks/ref, idea-to-product, sub-offer, sub-sales |
| `WHO + RESULT + TIME + WITHOUT X` | `QUIÉN + RESULTADO + TIEMPO + SIN X` | hormozi-hooks, sub-sales |
| `WHO + RESULT + SPEED/EASE + PROOF` | `QUIÉN + RESULTADO + VELOCIDAD/FACILIDAD + PRUEBA` | hormozi-hooks/ref |
| `Hook → Retain → Reward` | `Hook → Retener → Recompensar` | hormozi-hooks/ref |
| `Time Delay ↓ → Value ↑` | `Demora ↓ → Valor ↑` | value-accelerator |
| `Effort & Sacrifice ↓ → Value ↑` | `Esfuerzo y sacrificio ↓ → Valor ↑` | effort-reduction |
| `Same offer → better perception → higher conversions` | `La misma oferta → mejor percepción → más conversiones` | value-perception, sub-value |
| `Same offer → different angle → different demand` | `La misma oferta → distinto ángulo → distinta demanda` | offer-angles |
| `Idea → Offer → Pitch` | `Idea → Oferta → Pitch` | idea-to-product |
| `Idea → Market → Offer → Pitch → Content → Sales` | `Idea → Mercado → Oferta → Pitch → Contenido → Ventas` | idea-to-product |
| `Purchase → Start → Progress → Result` | `Compra → Inicio → Progreso → Resultado` | effort-reduction |
| `Step → Friction → Delay caused` | `Paso → Fricción → Demora causada` | value-accelerator |
| `Step → Friction → Why it feels hard` | `Paso → Fricción → Por qué se siente difícil` | effort-reduction |
| `Objection → Hidden belief` | `Objeción → Creencia oculta` | objection-destroyer |
| `Old belief → New belief` | `Creencia vieja → Creencia nueva` | objection-destroyer, sub-pricing |
| `Belief shift → Proof` | `Cambio de creencia → Prueba` | objection-destroyer, sub-pricing |
| `Objection → Reframe → Proof` | `Objeción → Reencuadre → Prueba` | objection-destroyer |
| `Objection → Bonus idea` | `Objeción → Idea de bono` | bonus-stack |
| `Obstacle → Solution → Delivery method` | `Obstáculo → Solución → Método de entrega` | hormozi-offer |
| `Objection → Response` | `Objeción → Respuesta` | hormozi-pitch, idea-to-product, landing-page-copy |
| `Question → Answer` | `Pregunta → Respuesta` | landing-page-copy |
| `Hour 0 → what they see / Hour 1 → what they do / Day 1 → what they achieve` | `Hora 0 → qué ven / Hora 1 → qué hacen / Día 1 → qué logran` | value-accelerator, sub-value |
| `service → productized service → product → ecosystem` | `servicio → servicio productizado → producto → ecosistema` | business-model |
| `DIY → DWY → DFY` | `DIY → DWY → DFY` (sin cambios) | dfy-dwy-diy, sub-pricing |
| `low-ticket → mid-ticket → premium` | `low-ticket → mid-ticket → premium` (sin cambios) | dfy-dwy-diy |

> La flecha es **`→` (U+2192)**, 212 ocurrencias en 27 archivos. Nunca se convierte a `->`.

### Acróstico MAGIC (`skills/hormozi-pitch/SKILL.md:210-216`, `agents/sub-sales.md:84-90`)

El acróstico **no funciona en español**. Regla única para los dos archivos: **se conserva la línea en inglés byte a byte y se agrega un glose en español precedido de ` — `.** Texto exacto a producir:

```
- **M**ake it about them — hazlo sobre el cliente
- **A**nnounce the avatar — nombra al avatar
- **G**ive a clear goal — da una meta clara
- **I**ndicate a time frame — indica un plazo
- **C**ontainer word (system / program / accelerator / blueprint / bootcamp) — palabra contenedora
```

En `hormozi-pitch` las líneas no llevan la negrita de la inicial ni el paréntesis final; se conserva la forma del fuente y se agrega el mismo glose.

---

## 1. Núcleo Hormozi

| EN | ES | ¿KEEP inglés? | Frecuencia | Nota |
|---|---|---|---|---|
| Grand Slam Offer | Grand Slam Offer | SÍ | 8/3 | Glosar **la primera vez de cada archivo** como `Grand Slam Offer (oferta irresistible)`; después, solo `Grand Slam Offer`. Nunca traducirlo suelto. |
| Value Equation | Ecuación de Valor | NO | 16/8 | Nombre propio de framework → mayúscula en ambas palabras. `Hormozi Value Equation` → `Ecuación de Valor de Hormozi`. |
| dream outcome | resultado soñado | NO | 27/10 | En la fórmula canónica: `Resultado Soñado`. Como encabezado/etiqueta: `Resultado soñado`. |
| perceived likelihood | probabilidad percibida | NO | 14/5 | Idem: `Probabilidad Percibida` solo dentro de la fórmula. |
| time delay | demora | NO | 18/7 | **NO "retraso"** (implica falla) ni "tiempo de espera". Fórmula: `Demora`. |
| effort & sacrifice | esfuerzo y sacrificio | NO | 15/7 | El `&` pasa a `y`. Fórmula: `Esfuerzo y Sacrificio`. |
| starving crowd | multitud hambrienta | NO | 6/4 | `Starving Crowd Engine` → `Motor de la Multitud Hambrienta`. |
| value stack | stack de valor | PARCIAL | 48/14 | `stack` se queda; "pila de valor" suena mal. Ver §7 para toda la familia *stack*. |
| value stacking | apilado de valor | PARCIAL | 4/2 | Actividad. Verbo `to stack value` → **apilar valor**. |
| bonus / bonuses | bono / bonos | NO | 101/16 | `bonus stack` → **stack de bonos**. `fast-action bonus` → **bono por acción rápida**. |
| offer | oferta | NO | 412/27 | Término más frecuente del corpus. Femenino: *la oferta*. |
| core offer | oferta principal | NO | 24/13 | **NO "oferta central"** ni "oferta core". Como nivel de escalera: `Core` → `Principal`. |
| entry offer | oferta de entrada | NO | 6/4 | |
| premium offer | oferta premium | PARCIAL | 5/4 | `premium` queda en inglés (31/11). |
| offer ladder | escalera de ofertas | NO | 7/4 | `OFFER_LADDER.md` no se toca. |
| guarantee | garantía | NO | 38/13 | |
| unconditional guarantee | garantía incondicional | NO | 5/5 | |
| conditional guarantee | garantía condicional | NO | 5/5 | |
| outcome-based guarantee | garantía basada en resultados | NO | 7/5 | |
| effort-based / support-based guarantee | garantía basada en esfuerzo / en soporte | NO | 6/4 | |
| anti-risk guarantee | garantía antirriesgo | NO | 1/1 | Una sola palabra, sin guion. |
| objection | objeción | NO | 189/16 | `objection handling` → **manejo de objeciones**. `objection-handling statements` → **frases para manejar objeciones**. |
| belief | creencia | NO | 44/11 | |
| belief shift | cambio de creencia | NO | 8/2 | `Belief Shift Engine` → `Motor de Cambio de Creencias`. |
| hidden belief | creencia oculta | NO | 3/2 | |
| scarcity | escasez | NO | 8/2 | `fake scarcity` → **escasez falsa**. |
| urgency | urgencia | NO | 30/15 | |
| funnel | embudo | NO | 6/5 | `funnel stage` → **etapa del embudo**. |
| obstacle | obstáculo | NO | ~40/8 | `Map obstacles` → `Mapea los obstáculos`. |
| transformation | transformación | NO | 25/14 | |
| proof | prueba / pruebas | NO | 59/15 | `social proof` → **prueba social**. `Proof Section` → `Sección de pruebas`. |
| trust | confianza | NO | 37/17 | `high-trust buy` → **compra de alta confianza**. |

---

## 2. Mercado y cliente

| EN | ES | ¿KEEP inglés? | Frecuencia | Nota |
|---|---|---|---|---|
| niche | nicho | NO | 37/8 | |
| micro-niche | micronicho | NO | 7/2 | Sin guion, junto. |
| market | mercado | NO | ~90/20 | `Target Market` → `Mercado objetivo`. |
| segment | segmento | NO | 9/4 | |
| avatar | avatar | SÍ | 22/8 | *el avatar*. `one-sentence avatar` → **avatar en una frase**. |
| target customer | cliente objetivo | NO | 6/4 | |
| ideal customer | cliente ideal | NO | 3/2 | `Ideal Customer Avatar` → `Avatar del cliente ideal`. |
| target audience | audiencia objetivo | NO | ~10/8 | |
| buyers | compradores | NO | 32/14 | |
| browsers | curiosos | NO | 7/2 | **Discutible.** "Buyers vs Browsers" → **Compradores vs curiosos**. Alternativas descartadas: "mirones" (coloquial), "navegantes" (confunde con navegador). |
| pain | dolor | NO | ~150/20 | Nunca "pena" ni "sufrimiento". |
| pain point | punto de dolor | NO | 5/5 | |
| surface pain | dolor superficial | NO | 4/2 | |
| deeper pain | dolor profundo | NO | 4/2 | |
| hidden pain | dolor oculto | NO | 4/2 | |
| midnight thoughts | pensamientos de medianoche | NO | 5/2 | |
| pain intensity | intensidad del dolor | NO | 2/2 | |
| purchasing power | poder adquisitivo | NO | 4/3 | |
| reachability / reach | alcance | NO | 2/2 + col. `Reach` | Una sola palabra para ambos; la columna `Reach` de la tabla de nichos → `Alcance`. |
| demand | demanda | NO | 31/9 | `demand signals` → **señales de demanda**; `demand validation` → **validación de demanda**. |
| willingness to pay | disposición a pagar | NO | 9/5 | |
| validation | validación | NO | 14/3 | `validation test` → **test de validación**. |
| pre-sell test | test de preventa | NO | 3/2 | |
| fake door test | test de puerta falsa (fake door) | PARCIAL | 2/1 | Glosar una vez; después `test de puerta falsa`. |
| testimonial | testimonio | NO | 11/9 | |
| case study | caso de éxito | NO | 9/7 | Decisión del usuario. En este corpus siempre funciona como elemento de prueba, no como género académico. |
| founder | fundador / fundadora | NO | 4/3 | |
| freelancer | freelancer | SÍ | 4/4 | |
| solopreneur | solopreneur | SÍ | 1/1 | |
| coach | coach | SÍ | ~15/8 | *el coach / la coach*. |
| coaching | coaching | SÍ | 5/3 | |
| consulting | consultoría | NO | 9/5 | |
| agency | agencia | NO | 3/3 | |

---

## 3. Entrega y modelo de negocio

| EN | ES | ¿KEEP inglés? | Frecuencia | Nota |
|---|---|---|---|---|
| DFY / DWY / DIY | DFY / DWY / DIY | SÍ | 55/13 · 43/13 · 46/13 | Las expansiones `Done For You` / `Done With You` / `Do It Yourself` **también quedan en inglés**, sin glose: el cuerpo del skill ya las explica. |
| done-for-you (adj., minúscula) | done-for-you | SÍ | 15/7 | `Done-for-You Additions` → `Adiciones done-for-you`. `done-for-you element` → `elemento done-for-you`. |
| delivery mechanism | mecanismo de entrega | NO | 3/2 | |
| delivery model | modelo de entrega | NO | 19/7 | |
| delivery method | método de entrega | NO | 3/2 | |
| delivery format | formato de entrega | NO | ~6/5 | |
| delivery (etiqueta suelta `- Delivery:`) | Entrega | NO | — | |
| high-ticket / low-ticket / mid-ticket | high-ticket / low-ticket / mid-ticket | SÍ | 9/7 · 9/7 · 2/2 | Sin cursiva ni comillas. |
| business model | modelo de negocio | NO | ~12/4 | |
| productize / productized | productizar / productizado | NO | 30/6 | `productization` → **productización**. `Productized Service` → `Servicio productizado`. |
| membership | membresía | NO | 4/4 | |
| subscription | suscripción | NO | 4/1 | |
| recurring | recurrente | NO | 3/2 | |
| retainer | retainer | SÍ | 1/1 | `[REVISAR]` — alternativa LatAm: "iguala". Frecuencia mínima (1 ocurrencia, `business-model`). |
| cohort | cohorte | NO | 5/5 | *la cohorte*. |
| course | curso | NO | 22/9 | |
| program | programa | NO | 19/8 | |
| toolkit | toolkit | SÍ | 7/4 | **Discutible.** Es un formato de producto nombrado (`Program / Course / Toolkit`); traducirlo a "kit de herramientas" rompe el paralelismo de la lista. |
| module | módulo | NO | 6/3 | |
| dashboard | dashboard | SÍ | 6/5 | *el dashboard*. |
| workbook | workbook | SÍ | 2/2 | `[REVISAR]` — alternativa: "cuaderno de trabajo". |
| upsell / downsell | upsell / downsell | SÍ | 23/5 · 19/3 | *el upsell / los upsells*. `Upsell / Downsell Logic` → `Lógica de upsell / downsell`. |
| cross-sell | cross-sell | SÍ | 0/0 | No aparece en el corpus. Regla preventiva por si entra en una revisión. |
| lead | lead | SÍ | 7/6 | ⚠️ **Ojo:** el verbo inglés *to lead to* ("each level leads to the next") **no** es este término → `lleva al siguiente`. |
| lead magnet | lead magnet | SÍ | 0/0 | No aparece. Regla preventiva. |
| churn | churn | SÍ | 0/0 | No aparece. Regla preventiva. |
| scale / scaling | escalar / escalado | NO | 15/5 | `scaling goal` → **meta de escalado**. |
| scalable / scalability | escalable / escalabilidad | NO | 19/5 | |
| leverage (sust.) | apalancamiento | NO | 4/2 | `high-leverage moves` → **movimientos de mayor apalancamiento**. |
| revenue | ingresos | NO | 15/6 | `revenue per customer` → **ingresos por cliente**. |
| income | ingresos | NO | 9/2 | Mismo destino que *revenue*; el contexto los distingue (`income target` → **meta de ingresos**). |
| lifetime value | valor de vida del cliente | NO | 2/1 | |
| average order value | valor promedio de compra | NO | 1/1 | |
| fulfillment | fulfillment | SÍ | 1/1 | `[REVISAR]` — 1 ocurrencia (`complexity of fulfillment` → `complejidad del fulfillment`). Alternativa: "cumplimiento/entrega". |

---

## 4. Precio

| EN | ES | ¿KEEP inglés? | Frecuencia | Nota |
|---|---|---|---|---|
| pricing (sust.) | precios / estrategia de precios | NO | ~90/12 | `Pricing Strategy` → `Estrategia de precios`. `Psychological Pricing` → `Precios psicológicos`. |
| price | precio | NO | ~120/18 | |
| price anchoring / anchoring | anclaje de precio / anclaje | NO | 5/3 · 15/6 | `Value Anchoring Engine` → `Motor de Anclaje de Valor`. |
| tier | nivel | NO | 34/7 | `Tier 1/2/3` → `Nivel 1/2/3`. `pricing tiers` → **niveles de precio**. `tier contrast` → **contraste entre niveles**. |
| perceived value | valor percibido | NO | 42/15 | |
| standalone value | valor individual | NO | 4/2 | Valor del componente vendido por separado. |
| stacked value / total stacked value | valor apilado / valor total apilado | PARCIAL | 8/5 | Coherente con *stack de valor*. |
| cost of inaction | costo de no actuar | NO | 2/2 | **costo**, no "coste" (LatAm). |
| charm pricing | charm pricing | SÍ | 2/2 | Glosar la 1.ª vez: `charm pricing (precios terminados en 7 o 9)`. **Discutible**; "precio de encanto" es un calco que nadie usa. |
| round pricing | precios redondos | NO | 3/2 | |
| impulse buy | compra por impulso | NO | 2/2 | |
| considered buy | compra meditada | NO | 2/2 | |
| no-brainer | decisión obvia | NO | 1/1 | |
| payment plan | plan de pagos | NO | 3/2 | |
| early-bird pricing | precio early bird | PARCIAL | 2/2 | |
| money-back | devolución del dinero | NO | 3/3 | `30-day money back` → **devolución a los 30 días**. |
| refund | reembolso | NO | 3/2 | |
| A/B test | test A/B | NO | 2/2 | |
| conversion / conversions | conversión / conversiones | NO | 29/13 | |
| conversion rate | tasa de conversión | NO | 1/1 | |
| margin | margen | NO | ~6/3 | `Margin (High-Ticket)` → `Margen (high-ticket)`. |
| volume | volumen | NO | ~8/3 | |

---

## 5. Valor, esfuerzo y tiempo

| EN | ES | ¿KEEP inglés? | Frecuencia | Nota |
|---|---|---|---|---|
| friction | fricción | NO | 32/10 | `Friction Killer` → `Matafricciones`. `friction map` → **mapa de fricción**. |
| quick win | victoria rápida | NO | 16/6 | `Quick Win Asset` → `Recurso de victoria rápida`. |
| first win | primera victoria | NO | 17/7 | Misma raíz que *quick win*, deliberadamente. |
| time to value / time-to-value | tiempo hasta el valor | NO | 8/2 | `Time-to-Value Accelerator` → `Acelerador del tiempo hasta el valor`. `TIME_TO_VALUE.md` no se toca. |
| onboarding | onboarding | SÍ | 11/6 | *el onboarding*. |
| drop-off | abandono | NO | 6/3 | `drop-off is high` → `el abandono es alto`. |
| completion rate | tasa de finalización | NO | 3/3 | |
| retention | retención | NO | 4/3 | |
| cognitive load | carga cognitiva | NO | 2/2 | |
| automation | automatización | NO | 11/5 | |
| workflow | workflow | SÍ | 1/1 | 1 ocurrencia (`guided workflows` → `workflows guiados`). |
| template | plantilla | NO | 55/15 | Nunca "template". |
| checklist | checklist | SÍ | 11/7 | *el checklist / los checklists*. |
| swipe file | swipe file | SÍ | 6/6 | *el swipe file*. |
| script | script | SÍ | ~6/4 | |
| pre-built | prearmado | NO | 4/3 | |
| plug-and-play | plug-and-play | SÍ | 6/5 | |
| asset | recurso | NO | 30/13 | **Discutible.** Sentido dominante = entregable. Excepción única: `turn problems into assets` / `turns objections into assets` → **convierte los problemas/objeciones en activos** (sentido financiero figurado). |
| execution | ejecución | NO | 28/17 | |
| step-by-step | paso a paso | NO | 11/8 | |
| milestone | hito | NO | 1/1 | |
| effort | esfuerzo | NO | ~70/15 | |
| ease | facilidad | NO | ~30/10 | `perceived ease` → **facilidad percibida**. |
| speed | velocidad | NO | ~45/12 | `perceived speed` → **velocidad percibida**. |
| hidden value | valor oculto | NO | 5/2 | |
| contrast | contraste | NO | 19/9 | |
| framing | encuadre | NO | 15/8 | `Value Framing` → `Encuadre del valor`. |
| reframe | reencuadre / reencuadrar | NO | 8/3 | |
| naming | naming | SÍ | 14/7 | `Naming Optimization` → `Optimización del naming`. **Discutible**; alternativa: "nomenclatura". |
| packaging | empaquetado | NO | 11/5 | `Packaging Upgrade` → `Mejora del empaquetado`. |
| positioning | posicionamiento | NO | 34/11 | |
| angle | ángulo | NO | 82/8 | `Anti-Angle` → `Anti-ángulo`. |
| identity | identidad | NO | 8/4 | |
| status shift | cambio de estatus | NO | 5/3 | |
| mechanism | mecanismo | NO | 30/12 | |
| pattern interrupt | interrupción de patrón | NO | 2/2 | |

---

## 6. Contenido, copy y venta

| EN | ES | ¿KEEP inglés? | Frecuencia | Nota |
|---|---|---|---|---|
| hook | hook | SÍ | 232/15 | *el hook / los hooks*. Segundo término más frecuente. Nunca "gancho". |
| pitch | pitch | SÍ | 73/10 | *el pitch*. |
| copy | copy | SÍ | 33/5 | *el copy*. `[copy]` como placeholder de plantilla **no se traduce**. |
| copywriting | copywriting | SÍ | 1/1 | |
| CTA | CTA | SÍ | 24/7 | *el CTA*. `CTA button` → **botón de CTA**. |
| landing page | landing page | SÍ | 33/11 | *la landing page*. `LANDING_PAGE.md` no se toca. |
| sales page | página de ventas | NO | 13/8 | Contraste deliberado con *landing page*, igual que en el original. |
| headline / subheadline | headline / subheadline | SÍ | 5/3 · 4/2 | **Discutible**; alternativas "titular/subtitular". Se mantiene el anglicismo por coherencia con *copy* y *hook*. |
| hero section | sección hero | PARCIAL | 4/3 | |
| above the fold | above the fold | SÍ | 2/2 | |
| callout | callout | SÍ | 11/5 | `Callout Hooks` → `Hooks de callout`. **Discutible**; alternativa "hooks de interpelación". |
| contrarian | a contracorriente | NO | 9/3 | `Contrarian Hooks` → `Hooks a contracorriente`. **Discutible**; "contrarian" también circula sin traducir. |
| pain amplification | amplificación del dolor | NO | 2/2 | |
| DM | DM | SÍ | 14/6 | *el DM / los DMs*. `DM-ready` → **listo para DM**. |
| FAQ | FAQ | SÍ | 12/5 | *las FAQ*. |
| ads | anuncios | NO | 23/7 | Incluye el copy de ejemplo (`without ads` → `sin anuncios`). |
| organic content | contenido orgánico | NO | 3/3 | |
| outreach | prospección | NO | 3/3 | `cold outreach` → **prospección en frío**. |
| engagement | engagement | SÍ | 2/2 | |
| scan / scan-friendly | escanear / fácil de escanear | NO | ~8/3 | Lectura visual rápida, no digitalización. |
| fluff | relleno | NO | 7/6 | `no fluff` → **sin relleno**. |
| hype | hype | SÍ | 3/3 | `avoid hype` → **evita el hype**; `no hype tone` → **sin tono de hype**. |
| bullet (de copy) | bullet | SÍ | 18/6 | `3 outcome-driven bullets` → `3 bullets orientados a resultado`. ⚠️ No confundir con `bullet point` de markdown → **viñeta**. |
| launch | lanzamiento | NO | ~12/6 | |

---

## 7. Familia *stack* — resolución única

`stack*` aparece 95 veces en 16 archivos. Regla cerrada para que los 10 traductores no diverjan:

| EN | ES | Nota |
|---|---|---|
| `value stack` (sust.) | **stack de valor** | |
| `bonus stack` (sust.) | **stack de bonos** | |
| `offer stack` (sust.) | **stack de ofertas** | |
| `stack` solo, referido al anterior | **el stack** | |
| `to stack (value / bonuses)` (verbo) | **apilar (valor / bonos)** | `Stack value clearly` → `Apila el valor con claridad`. |
| `stacking` (sust. de actividad) | **apilado** | `Value Stacking` → `Apilado de valor`; `no stacking` → `sin apilado`. |
| `stacked value` | **valor apilado** | |
| `Stack Strategy` (encabezado) | **Estrategia del stack** | |
| `Stack Value` (encabezado) | **Valor del stack** | |
| `BONUS_STACK.md` | *sin cambios* | Nombre de artefacto. |

---

## 8. Vocabulario del sistema de agentes

| EN | ES | ¿KEEP inglés? | Frecuencia | Nota |
|---|---|---|---|---|
| skill / skills (el artefacto) | skill / skills | SÍ | 203/23 | **Femenino: *la skill / las skills*.** `This skill works with:` → `Esta skill funciona con:`. |
| skill (habilidad humana) | habilidad | NO | — | ⚠️ **Desambiguación crítica.** Cuando *skill* significa la capacidad de una persona → **habilidad**: `skill level` → `nivel de habilidad`; `skill deficits` → `carencias de habilidad`; `your skills` → `tus habilidades`; `skill or expertise` → `habilidad o experiencia`; `Reduce skill requirements` → `Reduce los requisitos de habilidad`; `users lack skill or time` → `al usuario le falta habilidad o tiempo`. |
| agent | agente | NO | 48/9 | Los *slugs* (`sub-market`, `hormozi-orchestrator`…) nunca se traducen. |
| subagent / sub-agent | subagente | NO | 39/8 | Junto, sin guion. `Sub-Agent: Market Research Specialist` → `Subagente: especialista en investigación de mercado`. |
| orchestrator | orquestador | NO | 39/8 | `hormozi-orchestrator` como slug no se traduce. |
| brief | brief | SÍ | 24/7 | *el brief*. `ORCHESTRATOR BRIEF:` → `BRIEF DEL ORQUESTADOR:`. `structured brief` → **brief estructurado**. **Discutible**; alternativa "informe estructurado". |
| framework | framework | SÍ | 42/13 | *el framework / los frameworks*. `Framework to Apply` → `Framework a aplicar`. |
| Stage A–E | Etapa A–E | NO | 9/3 | Decisión del usuario. `Stage: [A / B / C / D / E]` → `Etapa: [A / B / C / D / E]`. |
| stage (etapa genérica) | etapa | NO | 36/8 | `Current stage` → `Etapa actual`; `Scaling Path Stage 1` → `Etapa 1`. |
| output / outputs | salida / salidas | NO | ~60/22 | La carpeta `output/` **no** se traduce. `Expected outputs` → `Salidas esperadas`. |
| input / inputs | entrada / entradas | NO | ~35/20 | La carpeta `input/` **no** se traduce. |
| plugin | plugin | SÍ | 39/2 | |
| marketplace | marketplace | SÍ | 12/3 | |
| repo / repository | repo / repositorio | PARCIAL | ~15/3 | `repo root` → **raíz del repo**. |
| scaffold | scaffold / generar el andamiaje | PARCIAL | ~4/2 | `Scaffolds the complete file structure` → `Genera la estructura completa de archivos`. |
| auto-discovered | autodetectado | NO | 2/1 | |
| namespaced | con namespace | PARCIAL | 2/1 | `Skills are namespaced` → `Las skills llevan namespace`. |

---

## 9. Diagnóstico y evaluación

| EN | ES | ¿KEEP inglés? | Frecuencia | Nota |
|---|---|---|---|---|
| audit (sust. / verbo) | auditoría / auditar | NO | 26/10 | `Offer Audit` → `Auditoría de la oferta`. `OFFER_AUDIT.md` no se toca. |
| score (sust.) | puntaje | NO | 28/8 | LatAm. `Overall Score` → `Puntaje total`. |
| score (verbo) | puntuar | NO | — | `Score each niche` → `Puntúa cada nicho`. |
| fix (sust. / verbo) | corrección / corregir | NO | 30/5 | `Top Priority Fixes` → `Correcciones prioritarias`. Columna `Fix` → `Corrección`. |
| weak point / weak spot | punto débil | NO | 7/3 | `Weak Point Detector` → `Detector de puntos débiles`. |
| weak signs | señales de debilidad | NO | ~10/2 | |
| diagnosis / diagnose | diagnóstico / diagnosticar | NO | 8/6 | |
| severity | severidad | NO | 1/1 | |
| gap | brecha | NO | 7/5 | `curiosity gap` → **brecha de curiosidad**; `skill gaps` → **brechas de habilidad**. |
| fit | encaje | NO | 20/8 | `Market Fit` → `Encaje con el mercado`; `Fit:` (etiqueta) → `Encaje:`. |
| broad | amplio | NO | 16/9 | `too broad` → **demasiado amplio**. |
| vague | vago | NO | ~30/14 | |
| generic | genérico | NO | ~25/12 | |
| compelling | convincente | NO | 6/5 | |
| desirable | deseable | NO | 6/6 | |
| actionable | accionable | NO | 5/3 | |
| tradeoff | tradeoff | SÍ | ~8/5 | *el tradeoff*. `[REVISAR]` — alternativa: "compensación". |
| constraint | restricción | NO | 23/10 | |
| assumption | supuesto | NO | 7/3 | `state the assumption` → `enuncia el supuesto`. |
| hesitate / hesitation | dudar / duda | NO | 8/6 | |
| overwhelmed | abrumado | NO | ~8/5 | |
| stuck | trabado | NO | ~8/5 | Neutro LatAm; evitar "atascado" (peninsular) y "atorado" (MX). |
| insight | hallazgo | NO | 2/2 | `Key Insight for Offer Building` → `Hallazgo clave para construir la oferta`; `actionable insights` → `hallazgos accionables`. |
| takeaway / highlight | punto clave / destacado | NO | ~3/2 | `50 sharp highlights` → `50 puntos clave y afilados`. |
| clarity > cleverness | claridad > astucia | NO | 2/2 | El `>` es "mayor que", no una cita markdown. Igual con `Buyers > audience size` → `Compradores > tamaño de audiencia`, `Perception > reality` → `Percepción > realidad`, `Specific > general` → `Específico > general`, `Fewer, stronger bonuses > many weak ones` → `Menos bonos y más fuertes > muchos débiles`, `Immediate clarity > cleverness` → `Claridad inmediata > astucia`. |

---

## 10. Falsos amigos y trampas detectadas en este corpus

| Aparece como | NO traducir como | Traducir como | Dónde |
|---|---|---|---|
| `support` (sustantivo: soporte del producto) | "soporte" ✅ correcto | **soporte** | `support layer` → `capa de soporte` |
| `support` (verbo: *claims without support*) | "soportar" ❌ | **respaldo / respaldar** | `big claims without support` → `promesas grandes sin respaldo` |
| `remove` | "remover" ❌ | **eliminar / quitar** | `remove objections`, `remove steps`, `remove friction` |
| `apply` (*apply the framework*) | "aplicar para" ❌ | **aplicar** (transitivo) | `Apply the framework to the brief` |
| `in order to` | "en orden de" ❌ | **para** | |
| `make sense` | "hacer sentido" ❌ | **tener sentido** | `the offer structure makes sense` |
| `actually` | "actualmente" ❌ | **realmente / de hecho** | `what the customer actually feels` |
| `eventually` | "eventualmente" ❌ | **con el tiempo / al final** | |
| `to lead to` | "lead" ❌ | **llevar a / conducir a** | `each level leads to the next` |
| `retain` (*Hook → Retain → Reward*) | "retener información" | **retener (a la audiencia)** | |
| `content` (adj. inexistente aquí) | — | siempre **contenido** (sust.) | |
| `argument` | "argumento" en sentido de discusión | **discusión** en `avoid defensive tone… focus on belief, not argument` → `no en la discusión` | objection-destroyer |
| `close` (*doesn't apply here*) | — | — | |
| `library` (*Clarifying Questions Library*, *skill library*) | "librería" ❌ | **biblioteca** | |
| `character` / `figure` | — | — | |
| `demand` (verbo) | — | siempre sustantivo en este corpus: **demanda** | |
| `sensible` | — | no aparece; regla preventiva: **sensato**, no "sensible" | |
| `discipline` | — | **disciplina** ✅ | |
| `commitment` | "comprometimiento" ❌ | **compromiso** | `low commitment → entry` |

---

## 11. Fórmulas de tratamiento (resumen operativo de D2)

| Contexto | Registro | Ejemplo del corpus | Traducción |
|---|---|---|---|
| Instrucción al asistente (≈85 % del texto) | **imperativo impersonal / 3.ª persona sobre "el asistente"** | `The assistant should produce a polished markdown file` | `El asistente debe producir un archivo markdown pulido` |
| Instrucción al asistente, imperativa | **imperativo (tú), dirigido al asistente** | `Ask the user these questions (all at once)` | `Hazle estas preguntas al usuario (todas juntas)` |
| Instrucción al asistente, lista | **imperativo** | `Identify:` / `Extract:` / `Check:` | `Identifica:` / `Extrae:` / `Revisa:` |
| Texto que el asistente **dice** al usuario (bloques `>`) | **tuteo directo, sin hype** | `> Here's what I'm hearing: you help…` | `> Esto es lo que entiendo: ayudas a…` |
| Prompt de instalación (`CLAUDE.md:9-13`) | **tuteo directo** | `Where should I install hormozi-skills-es?` | `¿Dónde instalo hormozi-skills-es?` |
| Bloque `DETECTED STAGE:` del orquestador | **tuteo directo** | `Confirm to proceed, or tell me what to change.` | `Confirma para continuar, o dime qué cambiar.` |
| Plantillas de artefacto (dentro de ` ```md `) | **sustantivos, sin verbo conjugado** | `## 7. Core Offer` | `## 7. Oferta principal` |

**Nunca "usted". Nunca voseo. Nunca "vosotros".**

---

## 12. Marcadores `[REVISAR]`

| Término | Propuesta | Motivo de la duda |
|---|---|---|
| `retainer` | retainer (KEEP) | 1 sola ocurrencia; "iguala" es LatAm pero suena contable, no de agencia. |
| `workbook` | workbook (KEEP) | 2 ocurrencias; "cuaderno de trabajo" es correcto pero largo dentro de una lista de formatos cortos. |
| `fulfillment` | fulfillment (KEEP) | 1 ocurrencia; en logística LatAm se deja, pero aquí significa "entrega del servicio". |
| `tradeoff` | tradeoff (KEEP) | 8 ocurrencias; "compensación" pierde el matiz de "elegir A implica perder B". |
