### A · CADENAS CANÓNICAS Y ACRÓSTICO (byte a byte idénticas entre archivos)
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


### B · TÉRMINOS QUE QUEDAN EN INGLÉS (KEEP)
| Grand Slam Offer | Grand Slam Offer | SÍ | 8/3 | Glosar **la primera vez de cada archivo** como `Grand Slam Offer (oferta irresistible)`; después, solo `Grand Slam Offer`. Nunca traducirlo suelto. |
| value stack | stack de valor | PARCIAL | 48/14 | `stack` se queda; "pila de valor" suena mal. Ver §7 para toda la familia *stack*. |
| value stacking | apilado de valor | PARCIAL | 4/2 | Actividad. Verbo `to stack value` → **apilar valor**. |
| premium offer | oferta premium | PARCIAL | 5/4 | `premium` queda en inglés (31/11). |
| avatar | avatar | SÍ | 22/8 | *el avatar*. `one-sentence avatar` → **avatar en una frase**. |
| fake door test | test de puerta falsa (fake door) | PARCIAL | 2/1 | Glosar una vez; después `test de puerta falsa`. |
| freelancer | freelancer | SÍ | 4/4 | |
| solopreneur | solopreneur | SÍ | 1/1 | |
| coach | coach | SÍ | ~15/8 | *el coach / la coach*. |
| coaching | coaching | SÍ | 5/3 | |
| DFY / DWY / DIY | DFY / DWY / DIY | SÍ | 55/13 · 43/13 · 46/13 | Las expansiones `Done For You` / `Done With You` / `Do It Yourself` **también quedan en inglés**, sin glose: el cuerpo del skill ya las explica. |
| done-for-you (adj., minúscula) | done-for-you | SÍ | 15/7 | `Done-for-You Additions` → `Adiciones done-for-you`. `done-for-you element` → `elemento done-for-you`. |
| high-ticket / low-ticket / mid-ticket | high-ticket / low-ticket / mid-ticket | SÍ | 9/7 · 9/7 · 2/2 | Sin cursiva ni comillas. |
| retainer | retainer | SÍ | 1/1 | `[REVISAR]` — alternativa LatAm: "iguala". Frecuencia mínima (1 ocurrencia, `business-model`). |
| toolkit | toolkit | SÍ | 7/4 | **Discutible.** Es un formato de producto nombrado (`Program / Course / Toolkit`); traducirlo a "kit de herramientas" rompe el paralelismo de la lista. |
| dashboard | dashboard | SÍ | 6/5 | *el dashboard*. |
| workbook | workbook | SÍ | 2/2 | `[REVISAR]` — alternativa: "cuaderno de trabajo". |
| upsell / downsell | upsell / downsell | SÍ | 23/5 · 19/3 | *el upsell / los upsells*. `Upsell / Downsell Logic` → `Lógica de upsell / downsell`. |
| cross-sell | cross-sell | SÍ | 0/0 | No aparece en el corpus. Regla preventiva por si entra en una revisión. |
| lead | lead | SÍ | 7/6 | ⚠️ **Ojo:** el verbo inglés *to lead to* ("each level leads to the next") **no** es este término → `lleva al siguiente`. |
| lead magnet | lead magnet | SÍ | 0/0 | No aparece. Regla preventiva. |
| churn | churn | SÍ | 0/0 | No aparece. Regla preventiva. |
| fulfillment | fulfillment | SÍ | 1/1 | `[REVISAR]` — 1 ocurrencia (`complexity of fulfillment` → `complejidad del fulfillment`). Alternativa: "cumplimiento/entrega". |
| stacked value / total stacked value | valor apilado / valor total apilado | PARCIAL | 8/5 | Coherente con *stack de valor*. |
| charm pricing | charm pricing | SÍ | 2/2 | Glosar la 1.ª vez: `charm pricing (precios terminados en 7 o 9)`. **Discutible**; "precio de encanto" es un calco que nadie usa. |
| early-bird pricing | precio early bird | PARCIAL | 2/2 | |
| onboarding | onboarding | SÍ | 11/6 | *el onboarding*. |
| workflow | workflow | SÍ | 1/1 | 1 ocurrencia (`guided workflows` → `workflows guiados`). |
| checklist | checklist | SÍ | 11/7 | *el checklist / los checklists*. |
| swipe file | swipe file | SÍ | 6/6 | *el swipe file*. |
| script | script | SÍ | ~6/4 | |
| plug-and-play | plug-and-play | SÍ | 6/5 | |
| naming | naming | SÍ | 14/7 | `Naming Optimization` → `Optimización del naming`. **Discutible**; alternativa: "nomenclatura". |
| hook | hook | SÍ | 232/15 | *el hook / los hooks*. Segundo término más frecuente. Nunca "gancho". |
| pitch | pitch | SÍ | 73/10 | *el pitch*. |
| copy | copy | SÍ | 33/5 | *el copy*. `[copy]` como placeholder de plantilla **no se traduce**. |
| copywriting | copywriting | SÍ | 1/1 | |
| CTA | CTA | SÍ | 24/7 | *el CTA*. `CTA button` → **botón de CTA**. |
| landing page | landing page | SÍ | 33/11 | *la landing page*. `LANDING_PAGE.md` no se toca. |
| headline / subheadline | headline / subheadline | SÍ | 5/3 · 4/2 | **Discutible**; alternativas "titular/subtitular". Se mantiene el anglicismo por coherencia con *copy* y *hook*. |
| hero section | sección hero | PARCIAL | 4/3 | |
| above the fold | above the fold | SÍ | 2/2 | |
| callout | callout | SÍ | 11/5 | `Callout Hooks` → `Hooks de callout`. **Discutible**; alternativa "hooks de interpelación". |
| DM | DM | SÍ | 14/6 | *el DM / los DMs*. `DM-ready` → **listo para DM**. |
| FAQ | FAQ | SÍ | 12/5 | *las FAQ*. |
| engagement | engagement | SÍ | 2/2 | |
| hype | hype | SÍ | 3/3 | `avoid hype` → **evita el hype**; `no hype tone` → **sin tono de hype**. |
| bullet (de copy) | bullet | SÍ | 18/6 | `3 outcome-driven bullets` → `3 bullets orientados a resultado`. ⚠️ No confundir con `bullet point` de markdown → **viñeta**. |
| skill / skills (el artefacto) | skill / skills | SÍ | 203/23 | **Femenino: *la skill / las skills*.** `This skill works with:` → `Esta skill funciona con:`. |
| brief | brief | SÍ | 24/7 | *el brief*. `ORCHESTRATOR BRIEF:` → `BRIEF DEL ORQUESTADOR:`. `structured brief` → **brief estructurado**. **Discutible**; alternativa "informe estructurado". |
| framework | framework | SÍ | 42/13 | *el framework / los frameworks*. `Framework to Apply` → `Framework a aplicar`. |
| plugin | plugin | SÍ | 39/2 | |
| marketplace | marketplace | SÍ | 12/3 | |
| repo / repository | repo / repositorio | PARCIAL | ~15/3 | `repo root` → **raíz del repo**. |
| scaffold | scaffold / generar el andamiaje | PARCIAL | ~4/2 | `Scaffolds the complete file structure` → `Genera la estructura completa de archivos`. |
| namespaced | con namespace | PARCIAL | 2/1 | `Skills are namespaced` → `Las skills llevan namespace`. |
| tradeoff | tradeoff | SÍ | ~8/5 | *el tradeoff*. `[REVISAR]` — alternativa: "compensación". |

### C · ENCABEZADOS/RÓTULOS COMPARTIDOS POR ≥2 ARCHIVOS (traducción única obligatoria)
| Plantilla | Dueño A | Dueño B | Riesgo |
| `OFFER_AUDIT.md` | `agents/sub-value.md` | `skills/audit-offer/SKILL.md` | alto |
| `VALUE_PERCEPTION.md` | `agents/sub-value.md` | `skills/value-perception/SKILL.md` | alto |
| `BONUS_STACK.md` | `agents/sub-value.md` | `skills/bonus-stack/SKILL.md` | alto |
| `PRICING.md` | `agents/sub-pricing.md` | `skills/pricing-strategy/SKILL.md` | alto |
| `OBJECTIONS.md` | `agents/sub-pricing.md` | `skills/objection-destroyer/SKILL.md` | alto |
| `PRODUCTIZATION.md` | `agents/sub-pricing.md` | `skills/productize/SKILL.md` | alto |
| `PITCH.md` | `agents/sub-sales.md` | `skills/hormozi-pitch/SKILL.md` | alto |
| `HOOKS.md` | `agents/sub-sales.md` | `skills/hormozi-hooks/SKILL.md` | alto |
| `LANDING_PAGE.md` | `agents/sub-sales.md` | `skills/landing-page-copy/SKILL.md` | alto |
| `OFFER.md` | `agents/sub-offer.md` | `skills/hormozi-offer/SKILL.md` | alto |
| `OFFER_ANGLES.md` | `agents/sub-offer.md` | `skills/offer-angles/SKILL.md` | alto |
| `MARKET_RESEARCH.md` | `agents/sub-market.md` | `skills/market-research/SKILL.md` | alto |
| `Friction Map` | `skills/effort-reduction` | `skills/value-accelerator` | medio |
| `Onboarding Flow` | `agents/sub-value.md` | `skills/value-accelerator` | medio |
| `Offer Ladder` | `agents/sub-pricing.md` | `skills/dfy-dwy-diy` | medio |
| `Recommended Model` | `skills/business-model` | `skills/dfy-dwy-diy` | medio |
| Sección | Rótulos | En ≥2 archivos |
| C · Pseudoencabezados en texto plano | 58 | 10 |
| D · Etiquetas de viñeta con dos puntos | 189 | 95 |
| E · Cabeceras de columna de tabla | 47 | 5 |
| F · Bloques literales del orquestador | 39 | — |
| **Total** | **659** | **210** |
| Core Offer | Oferta principal | hormozi-offer, hormozi-pitch, landing-page-copy, productize, sub-offer, sub-sales |
| Value Stack | Stack de valor | audit-offer, hormozi-offer, hormozi-pitch, landing-page-copy, sub-offer, sub-sales |
| Bonus Stack | Stack de bonos | bonus-stack, hormozi-offer, hormozi-pitch, sub-offer, sub-value |
| Guarantee | Garantía | hormozi-offer, hormozi-pitch, landing-page-copy, sub-offer, sub-sales |
| Offer Summary | Resumen de la oferta | audit-offer, hormozi-pitch, sub-sales, sub-value |
| Dream Outcome | Resultado soñado | audit-offer, hormozi-offer, sub-offer |
| Messaging | Mensajes | audit-offer, hormozi-offer, sub-offer |
| Objection Handling | Manejo de objeciones | hormozi-pitch, landing-page-copy, sub-sales |
| Pitch | Pitch | hormozi-pitch, idea-to-product, sub-sales |
| Positioning | Posicionamiento | hormozi-offer, idea-to-product, sub-offer |
| Angle 1: Outcome-Specific | Ángulo 1: resultado específico | offer-angles, sub-offer |
| Angle 2: Time-Based | Ángulo 2: tiempo | offer-angles, sub-offer |
| Angle 3: Pain-Based | Ángulo 3: dolor | offer-angles, sub-offer |
| Angle 4: Identity-Based | Ángulo 4: identidad | offer-angles, sub-offer |
| Angle 5: Effort-Based | Ángulo 5: esfuerzo | offer-angles, sub-offer |
| Angle 6: Speed-Based | Ángulo 6: velocidad | offer-angles, sub-offer |
| Base Offer | Oferta base | offer-angles, sub-offer |
| BONUS_STACK.md | BONUS_STACK.md | bonus-stack, sub-value |
| Business Snapshot | Panorama del negocio | hormozi-offer, sub-offer |
| Callout Hooks | Hooks de callout | hormozi-hooks, sub-sales |
| Contrarian Hooks | Hooks a contracorriente | hormozi-hooks, sub-sales |
| Core Message | Mensaje central | hormozi-hooks, sub-sales |
| Core Offer Summary | Resumen de la oferta principal | bonus-stack, sub-value |
| CTA Section | Sección de CTA | landing-page-copy, sub-sales |
| Current Perception Issues | Problemas de percepción actuales | sub-value, value-perception |
| Current Service | Servicio actual | productize, sub-pricing |
| Delivery Model | Modelo de entrega | productize, sub-offer |
| Delivery Model Impact | Impacto del modelo de entrega | pricing-strategy, sub-pricing |
| Effort Reduction Hooks | Hooks de reducción de esfuerzo | hormozi-hooks, sub-sales |
| FAQ | FAQ | landing-page-copy, sub-sales |
| Friction Map | Mapa de fricción | effort-reduction, value-accelerator |
| Generated Angles | Ángulos generados | offer-angles, sub-offer |
| Hero Section | Sección hero | landing-page-copy, sub-sales |
| Hook Variations | Variaciones de hooks | hormozi-hooks, sub-sales |
| HOOKS.md | HOOKS.md | hormozi-hooks, sub-sales |
| Ideal Customer Avatar | Avatar del cliente ideal | hormozi-offer, sub-offer |
| Key Objections | Objeciones clave | bonus-stack, sub-value |
| LANDING_PAGE.md | LANDING_PAGE.md | landing-page-copy, sub-sales |
| Launch Notes | Notas de lanzamiento | hormozi-offer, sub-offer |
| MARKET_RESEARCH.md | MARKET_RESEARCH.md | market-research, sub-market |
| Mechanism Hooks | Hooks de mecanismo | hormozi-hooks, sub-sales |
| Mechanism Section | Sección de mecanismo | landing-page-copy, sub-sales |
| Midnight Thoughts | Pensamientos de medianoche | market-research, sub-market |
| Naming Improvements | Mejoras de naming | sub-value, value-perception |
| OBJECTIONS.md | OBJECTIONS.md | objection-destroyer, sub-pricing |
| Obstacles | Obstáculos | hormozi-offer, sub-offer |
| Offer Ladder | Escalera de ofertas | dfy-dwy-diy, sub-pricing |
| Offer Name Options | Opciones de nombre para la oferta | hormozi-pitch, sub-sales |
| OFFER.md | OFFER.md | hormozi-offer, sub-offer |
| OFFER_ANGLES.md | OFFER_ANGLES.md | offer-angles, sub-offer |
| OFFER_AUDIT.md | OFFER_AUDIT.md | audit-offer, sub-value |
| Onboarding Flow | Flujo de onboarding | sub-value, value-accelerator |
| Outcome Hooks | Hooks de resultado | hormozi-hooks, sub-sales |
| Outcome Section | Sección de resultado | landing-page-copy, sub-sales |
| Overall Diagnosis | Diagnóstico general | audit-offer, sub-value |
| Packaging Upgrade | Mejora del empaquetado | sub-value, value-perception |
| Pain Hooks | Hooks de dolor | hormozi-hooks, sub-sales |
| PITCH.md | PITCH.md | hormozi-pitch, sub-sales |
| Price Justification Story | Historia que justifica el precio | pricing-strategy, sub-pricing |
| Pricing Experiments | Experimentos de precio | pricing-strategy, sub-pricing |
| Pricing Range | Rango de precios | pricing-strategy, sub-pricing |
| Pricing Tiers (if applicable) | Niveles de precio (si aplica) | pricing-strategy, sub-pricing |
| PRICING.md | PRICING.md | pricing-strategy, sub-pricing |
| Problem Section | Sección de problema | landing-page-copy, sub-sales |
| PRODUCTIZATION.md | PRODUCTIZATION.md | productize, sub-pricing |
| Productized System | Sistema productizado | productize, sub-pricing |
| Proof Section | Sección de pruebas | landing-page-copy, sub-sales |
| Psychological Pricing | Precios psicológicos | pricing-strategy, sub-pricing |
| Recommended Model | Modelo recomendado | business-model, dfy-dwy-diy |
| Recommended Use | Uso recomendado | offer-angles, sub-offer |
| Repeatable Components | Componentes repetibles | productize, sub-pricing |
| Scarcity & Urgency | Escasez y urgencia | hormozi-pitch, sub-sales |
| Selected Niche | Nicho seleccionado | market-research, sub-market |
| Solution Map | Mapa de soluciones | hormozi-offer, sub-offer |
| Solution Section | Sección de solución | landing-page-copy, sub-sales |
| Stack Strategy | Estrategia del stack | bonus-stack, sub-value |
| Target Market | Mercado objetivo | hormozi-offer, sub-offer |
| Time-Based Hooks | Hooks de tiempo | hormozi-hooks, sub-sales |
| Top 1 | Top 1 | hormozi-hooks, offer-angles |
| Top 2 | Top 2 | hormozi-hooks, offer-angles |
| Top 3 | Top 3 | hormozi-hooks, offer-angles |
| Transformation Hooks | Hooks de transformación | hormozi-hooks, sub-sales |
| Validation Tests | Tests de validación | market-research, sub-market |
| Value Analysis | Análisis de valor | pricing-strategy, sub-pricing |
| Value Equation Analysis | Análisis de la Ecuación de Valor | audit-offer, sub-value |
| Value Framing | Encuadre del valor | sub-value, value-perception |
| VALUE_PERCEPTION.md | VALUE_PERCEPTION.md | sub-value, value-perception |
| "[Objection 1]" | "[Objeción 1]" | sub-pricing |
| "How I" Hooks | Hooks de "Cómo yo" | sub-sales |
| “How I” Hooks | Hooks de “Cómo yo” | hormozi-hooks |
| Agent: Example | Agente: Ejemplo | create-plugin |
| Anchoring | Anclaje | sub-value |
| Anchoring Improvements | Mejoras de anclaje | value-perception |
| Angle 7: Niche-Specific | Ángulo 7: nicho específico | sub-offer |
| Angle 7: Status-Based | Ángulo 7: estatus | offer-angles |
| Angle 8: Anti-Angle | Ángulo 8: anti-ángulo | sub-offer |
| Angle 8: Mechanism-Based | Ángulo 8: mecanismo | offer-angles |
| Angle 9: Niche-Specific | Ángulo 9: nicho específico | offer-angles |
| Angle 10: Anti-Angle | Ángulo 10: anti-ángulo | offer-angles |
| Automation Opportunities | Oportunidades de automatización | effort-reduction |
| Belief Shifts | Cambios de creencia | objection-destroyer |
| Bonus 1 | Bono 1 | bonus-stack |
| Bonus 2 | Bono 2 | bonus-stack |
| Bonus 3 | Bono 3 | bonus-stack |
| Bonus 1: [Name] | Bono 1: [nombre] | sub-value |
| Bonus Descriptions | Descripciones de los bonos | sub-value |
| Bonuses | Bonos | landing-page-copy |
| Business Structure | Estructura del negocio | business-model |
| BUSINESS_MODEL.md | BUSINESS_MODEL.md | business-model |
| Buyer vs Browser | Comprador vs curioso | market-research |
| Contrast Enhancements | Mejoras de contraste | value-perception |
| Contrast Statements | Frases de contraste | sub-value |
| Core Problems | Problemas centrales | market-research |
| Current Effort Analysis | Análisis del esfuerzo actual | effort-reduction |
| Current Model Gaps | Brechas del modelo actual | dfy-dwy-diy |
| Current Stage | Etapa actual | business-model |
| Current Time-to-Value | Tiempo hasta el valor actual | value-accelerator |
| Customer Journey | Recorrido del cliente | productize |
| Customer Pain | Dolor del cliente | market-research |
| Customer Pain Map | Mapa del dolor del cliente | sub-market |
| Customer Profile | Perfil del cliente | dfy-dwy-diy |
| CUSTOMER_PAIN.md | CUSTOMER_PAIN.md | market-research |
| Decisions to Eliminate | Decisiones a eliminar | effort-reduction |
| Deeper Pain | Dolor profundo | sub-market |
| Delivery Model Comparison | Comparación de modelos de entrega | dfy-dwy-diy |
| DELIVERY_MECHANISM.md | DELIVERY_MECHANISM.md | dfy-dwy-diy |
| Demand Assessment | Evaluación de la demanda | sub-market |
| Demand Score | Puntaje de demanda | market-research |
| Demand Signals | Señales de demanda | market-research |
| Demand Validation | Validación de demanda | market-research |
| DEMAND_VALIDATION.md | DEMAND_VALIDATION.md | market-research |
| DFY | DFY | dfy-dwy-diy |
| DWY | DWY | dfy-dwy-diy |
| DIY | DIY | dfy-dwy-diy |
| Digital Product (DIY) | Producto digital (DIY) | business-model |
| Done-for-You Additions | Adiciones done-for-you | effort-reduction |
| Downsell 1 | Downsell 1 | productize |
| Downsell Options | Opciones de downsell | productize |
| Ease Improvements | Mejoras de facilidad | dfy-dwy-diy |
| Effort & Sacrifice | Esfuerzo y sacrificio | audit-offer |
| Effort Perception Improvements | Mejoras en la percepción del esfuerzo | effort-reduction |
| Effort Reduction Ideas | Ideas para reducir el esfuerzo | value-accelerator |
| Effort Reduction Map | Mapa de reducción de esfuerzo | sub-value |
| EFFORT_REDUCTION.md | EFFORT_REDUCTION.md | effort-reduction |
| Emotional Triggers | Disparadores emocionales | market-research |
| Entry Offer | Oferta de entrada | productize |
| Entry Point | Punto de entrada | productize |
| Expansion | Expansión | idea-to-product |
| Final Notes | Notas finales | bonus-stack |
| Final Perception Upgrade | Mejora final de la percepción | value-perception |
| Final Product Offer | Oferta de producto final | productize |
| First Win Asset | Recurso de la primera victoria | sub-value |
| First Win Definition | Definición de la primera victoria | value-accelerator |
| Flow Logic | Lógica del flujo | productize |
| Funnel Integration | Integración en el embudo | sub-pricing |
| Growth Path | Ruta de crecimiento | business-model |
| Guarantee Section | Sección de garantía | sub-sales |
| Hidden Beliefs | Creencias ocultas | objection-destroyer |
| Hidden Pain | Dolor oculto | sub-market |
| Hidden Value (now made explicit) | Valor oculto (ahora explícito) | sub-value |
| Hidden Value Highlights | Destacados de valor oculto | value-perception |
| High-Ticket | High-ticket | business-model |
| Low-Ticket | Low-ticket | business-model |
| Hooks | Hooks | idea-to-product |
| Hybrid | Híbrido | business-model |
| Hybrid Hooks (Best Performers) | Hooks híbridos (los que mejor funcionan) | sub-sales |
| Hybrid Hooks (Best) | Hooks híbridos (los mejores) | hormozi-hooks |
| Hybrid Options | Opciones híbridas | dfy-dwy-diy |
| Idea | Idea | market-research |
| Integration Points | Puntos de integración | objection-destroyer |
| Key Decisions Made | Decisiones clave tomadas | hormozi-orchestrator |
| Key Insight for Offer Building | Hallazgo clave para construir la oferta | sub-market |
| Ladder Flow | Flujo de la escalera | productize |
| LEAN_OFFER_SYSTEM.md | LEAN_OFFER_SYSTEM.md | idea-to-product |
| Long Version | Versión larga | hormozi-pitch |
| Long Version (full pitch) | Versión larga (pitch completo) | sub-sales |
| Market | Mercado | idea-to-product |
| Market Fit | Encaje con el mercado | audit-offer |
| MARKET_SELECTION.md | MARKET_SELECTION.md | market-research |
| Medium Version | Versión media | hormozi-pitch |
| Medium Version (landing page) | Versión media (landing page) | sub-sales |
| Micro-Niches | Micronichos | market-research |
| Micro-Niches Evaluated | Micronichos evaluados | sub-market |
| Model Evaluation | Evaluación de modelos | business-model |
| Next Actions | Próximas acciones | business-model |
| Next Session Entry Point | Punto de entrada para la próxima sesión | hormozi-orchestrator |
| Niche Scoring | Puntaje de nichos | market-research |
| Objection 1 | Objeción 1 | objection-destroyer |
| Objection 2 | Objeción 2 | objection-destroyer |
| Objection 3 | Objeción 3 | objection-destroyer |
| Objection Categories | Categorías de objeciones | objection-destroyer |
| Objection Handling Statements | Frases para manejar objeciones | objection-destroyer |
| Objection-Handling Statements | Frases para manejar objeciones | sub-pricing |
| Objection Map | Mapa de objeciones | sub-pricing |
| Objection → Bonus Mapping | Mapeo objeción → bono | bonus-stack |
| Objections | Objeciones | idea-to-product |
| Objections & Trust | Objeciones y confianza | audit-offer |
| Offer | Oferta | idea-to-product |
| Offer Improvements Needed | Mejoras necesarias en la oferta | objection-destroyer |
| Offer Improvements Triggered | Mejoras de la oferta detonadas | sub-pricing |
| Offer Structure | Estructura de la oferta | audit-offer |
| OFFER_LADDER.md | OFFER_LADDER.md | productize |
| One Hook to Start With Today | Un hook para empezar hoy | hormozi-orchestrator |
| Optional Fast Action Bonuses | Bonos opcionales por acción rápida | bonus-stack |
| Outcome Analysis | Análisis del resultado | dfy-dwy-diy |
| Pain Bullets | Bullets de dolor | market-research |
| Perceived Likelihood | Probabilidad percibida | audit-offer |
| Perceived Speed Improvements | Mejoras en la velocidad percibida | value-accelerator |
| Premium Offer | Oferta premium | productize |
| Price: | Precio: | landing-page-copy |
| Total Value: | Valor total: | landing-page-copy |
| Pricing | Precios | audit-offer |
| Product Format | Formato del producto | productize |
| Productized Service (DWY) | Servicio productizado (DWY) | business-model |
| Service (DFY) | Servicio (DFY) | business-model |
| Subscription | Suscripción | business-model |
| Profile | Perfil | business-model |
| Proof Mapping | Mapeo de pruebas | objection-destroyer |
| Quick Win Asset | Recurso de victoria rápida | value-accelerator |
| Quick Wins | Victorias rápidas | audit-offer |
| Quick Wins (implement immediately) | Victorias rápidas (implementar de inmediato) | sub-value |
| Raw Language | Lenguaje crudo | market-research |
| Recommended Pricing Strategy | Estrategia de precios recomendada | pricing-strategy |
| Recommended Strategy | Estrategia recomendada | sub-pricing |
| REVENUE_FLOW.md | REVENUE_FLOW.md | productize |
| Risk Check | Chequeo de riesgo | pricing-strategy |
| Risks | Riesgos | business-model |
| Sales Flow | Flujo de ventas | idea-to-product |
| Scaling Path | Ruta de escalado | sub-pricing |
| Secondary Model | Modelo secundario | business-model |
| Selected Market | Mercado seleccionado | market-research |
| Short Responses (DM-ready) | Respuestas cortas (listas para DM) | objection-destroyer |
| Short Version | Versión corta | hormozi-pitch |
| Short Version (1–2 lines) | Versión corta (1–2 líneas) | sub-sales |
| Simplicity Improvements | Mejoras de simplicidad | value-perception |
| Simplified Execution Flow | Flujo de ejecución simplificado | effort-reduction |
| Skill: Example | Skill: Ejemplo | create-plugin |
| Speed Improvements | Mejoras de velocidad | dfy-dwy-diy |
| Stack Value | Valor del stack | sub-value |
| Steps to Remove | Pasos a eliminar | effort-reduction |
| Steps to Simplify | Pasos a simplificar | effort-reduction |
| SUMMARY.md | SUMMARY.md | hormozi-orchestrator |
| Surface Objections | Objeciones superficiales | objection-destroyer |
| Surface Pain | Dolor superficial | sub-market |
| Templates to Add | Plantillas a agregar | effort-reduction |
| Test 1: Pre-Sell | Test 1: preventa | market-research |
| Test 2: Fake Door | Test 2: puerta falsa | market-research |
| Test 3: Content | Test 3: contenido | market-research |
| Tier 1 | Nivel 1 | pricing-strategy |
| Tier 2 | Nivel 2 | pricing-strategy |
| Tier 3 | Nivel 3 | pricing-strategy |
| Time Delay | Demora | audit-offer |
| Time Reduction Ideas | Ideas para reducir el tiempo | value-accelerator |
| TIME_TO_VALUE.md | TIME_TO_VALUE.md | value-accelerator |
| Top 3 Angles | Top 3 de ángulos | sub-offer |
| Top Angles | Mejores ángulos | offer-angles |
| Top Hooks | Mejores hooks | hormozi-hooks |
| Top 5 Hooks | Top 5 de hooks | sub-sales |
| Top 3 Priority Actions | Top 3 de acciones prioritarias | hormozi-orchestrator |
| Top 3 Priority Fixes | Top 3 de correcciones prioritarias | sub-value |
| Top Priority Fixes | Correcciones prioritarias | audit-offer |
| Top Objections to Address | Objeciones principales a atender | objection-destroyer |
| Total Bonus Value | Valor total de los bonos | bonus-stack |
| Updated Offer Structure | Estructura de la oferta actualizada | value-accelerator |
| Upsell / Downsell Logic | Lógica de upsell / downsell | sub-pricing |
| Upsell 1 | Upsell 1 | productize |
| Upsell 2 | Upsell 2 | productize |
| Upsell Options | Opciones de upsell | productize |
| Usage Suggestions | Sugerencias de uso | hormozi-hooks |
| Validation Criteria | Criterios de validación | market-research |
| Value Equation Assessment | Evaluación de la Ecuación de Valor | sub-sales |
| Value Equation Breakdown | Desglose de la Ecuación de Valor | hormozi-pitch |
| Value Increase Strategy | Estrategia de aumento de valor | productize |
| Value Perception Upgrades | Mejoras de la percepción de valor | dfy-dwy-diy |
| Value Stack (reordered) | Stack de valor (reordenado) | sub-value |
| Value Stack Optimization | Optimización del stack de valor | value-perception |
| What Was Built (File Index) | Lo que se construyó (índice de archivos) | hormozi-orchestrator |
| Your Offer in One Paragraph | Tu oferta en un párrafo | hormozi-orchestrator |
| Purpose | Propósito | 18 archivos (todos los `skills/*` menos las 2 referencias) |
| Inputs | Entradas | 16 skills |
| When to Use | Cuándo usarla | 16 skills |
| Assistant Behavior | Comportamiento del asistente | 15 skills |
| Core Outcome | Resultado principal | 15 skills |
| Output Format | Formato de salida | 14 skills |
| Output | Salida | sub-market, sub-offer, sub-pricing, sub-sales, sub-value |
| Report Back | Reporte al orquestador | sub-market, sub-offer, sub-pricing, sub-sales, sub-value |
| Your Role | Tu rol | sub-market, sub-offer, sub-pricing, sub-sales, sub-value |
| Input Format | Formato de entrada | sub-market, sub-offer, sub-pricing, sub-value |
| Core Principles (Hormozi Style) | Principios centrales (estilo Hormozi) | hormozi-hooks, landing-page-copy |
| Framework to Apply | Framework a aplicar | sub-market, sub-offer |
| Frameworks to Apply | Frameworks a aplicar | sub-value |
| Constraints | Restricciones | business-model, hormozi-pitch |
| Core Models | Modelos centrales | business-model |
| Key Models | Modelos clave | dfy-dwy-diy |
| Core Levers | Palancas centrales | value-perception |
| Core Flows | Flujos principales | idea-to-product |
| Core Formula | Fórmula central | hormozi-hooks |
| Audit Framework (Hormozi-Based) | Framework de auditoría (basado en Hormozi) | audit-offer |
| Offer-Building Framework | Framework de construcción de la oferta | hormozi-offer |
| Brainstorming Rules | Reglas de brainstorming | hormozi-offer |
| Clarifying Questions Library | Biblioteca de preguntas aclaratorias | hormozi-offer |
| Decision Heuristics | Heurísticas de decisión | hormozi-offer |
| Output File Format: `OFFER.md` | Formato del archivo de salida: `OFFER.md` | hormozi-offer |
| Landing Page Structure | Estructura de la landing page | landing-page-copy |
| Operating Rules | Reglas de operación | hormozi-orchestrator |
| Phase 1: Intake | Fase 1: Recepción | hormozi-orchestrator |
| Phase 2: Interview | Fase 2: Entrevista | hormozi-orchestrator |
| Phase 3: Funnel Stage Detection | Fase 3: Detección de la etapa del embudo | hormozi-orchestrator |
| Phase 4: Subagent Delegation | Fase 4: Delegación a subagentes | hormozi-orchestrator |
| Phase 5: Summary | Fase 5: Resumen | hormozi-orchestrator |
| Stage A — Idea Only | Etapa A — Solo idea | hormozi-orchestrator |
| Stage B — Offer Exists, Not Converting | Etapa B — La oferta existe pero no convierte | hormozi-orchestrator |
| Stage C — Needs Sales Assets Only | Etapa C — Solo faltan recursos de venta | hormozi-orchestrator |
| Stage D — Service Business, Wants to Scale | Etapa D — Negocio de servicios que quiere escalar | hormozi-orchestrator |
| Stage E — Custom / Mixed | Etapa E — Personalizada / mixta | hormozi-orchestrator |
| Structure of SUMMARY.md | Estructura de SUMMARY.md | hormozi-orchestrator |
| Sub-Agent: Market Research Specialist | Subagente: especialista en investigación de mercado | sub-market |
| Sub-Agent: Offer Builder Specialist | Subagente: especialista en construcción de ofertas | sub-offer |
| Sub-Agent: Value Layer Specialist | Subagente: especialista en la capa de valor | sub-value |
| Sub-Agent: Pricing & Objection Specialist | Subagente: especialista en precios y objeciones | sub-pricing |
| Sub-Agent: Sales Layer Specialist | Subagente: especialista en la capa de ventas | sub-sales |
| Hormozi Orchestrator — Master Offer Builder | Orquestador Hormozi — Constructor maestro de ofertas | hormozi-orchestrator |
| Skill: … (título H1 de cada skill) | Skill: … | los 18 skills |
| Step 1 … Step 10 | Paso 1 … Paso 10 | varios |
| Part 1 / Part 2 / Part 3 | Parte 1 / Parte 2 / Parte 3 | sub-offer, sub-pricing |
| PART 1 / PART 2 / PART 3 (mayúsculas) | PARTE 1 / PARTE 2 / PARTE 3 | market-research, productize, idea-to-product |
| Style Guidelines | Guía de estilo | 17 skills |
| Success Criteria | Criterios de éxito | 17 skills |
| Decision Rules | Reglas de decisión | 15 skills |
| Before | Antes | 10 skills |
| After | Después | 10 skills |
| Before vs After Example | Ejemplo de antes vs después | 9 skills |
| Assistant Behavior | Comportamiento del asistente | hormozi-hooks, market-research, productize |
| Output Format | Formato de salida | hormozi-hooks, market-research, productize |
| Purpose | Propósito | market-research, productize |
| Examples | Ejemplos | dfy-dwy-diy, value-accelerator |
| Conversation Flow | Flujo de conversación | hormozi-offer |
| Fallback Behavior | Comportamiento de respaldo | hormozi-offer |
| Scoring System (Optional) | Sistema de puntaje (opcional) | audit-offer |
| Hybrid Rules | Reglas para híbridos | dfy-dwy-diy |
| Combined Output | Salida combinada | market-research |
| Core Output | Salida principal | idea-to-product |
| Core Idea | Idea central | productize |
| Weak / Improved | Débil / Mejorado | dfy-dwy-diy |
| OUTPUT FORMAT | FORMATO DE SALIDA | idea-to-product |
| 50 KEY PRINCIPLES (INTEGRATED) | 50 PRINCIPIOS CLAVE (INTEGRADOS) | idea-to-product |
| OFFER SYSTEM — 50 KEY POINTS | SISTEMA DE OFERTA — 50 PUNTOS CLAVE | idea-to-product/references |
| Market & Positioning | Mercado y posicionamiento | idea-to-product, idea-to-product/references |
| Offer Fundamentals | Fundamentos de la oferta | idea-to-product, idea-to-product/references |
| Value Equation | Ecuación de Valor | idea-to-product, idea-to-product/references |
| Obstacles & Solutions | Obstáculos y soluciones | idea-to-product, idea-to-product/references |
| Offer Construction | Construcción de la oferta | idea-to-product, idea-to-product/references |
| Pricing | Precios | idea-to-product, idea-to-product/references |
| Bonuses | Bonos | idea-to-product, idea-to-product/references |
| Speed & Effort | Velocidad y esfuerzo | idea-to-product, idea-to-product/references |
| Delivery | Entrega | idea-to-product, idea-to-product/references |
| Psychology | Psicología | idea-to-product |
| Psychology & Perception | Psicología y percepción | idea-to-product/references |
| One-Line Mental Model | Modelo mental en una línea | idea-to-product/references |
| Simple Mental Model | Modelo mental simple | hormozi-hooks/references |
| Mental Shortcut | Atajo mental | hormozi-hooks/references |
| Common Hook Types | Tipos de hook comunes | hormozi-hooks/references |
| Hormozi Hook Frameworks | Frameworks de hooks de Hormozi | hormozi-hooks/references |
| Hidden Techniques He Uses | Técnicas ocultas que usa | hormozi-hooks/references |
| Hormozi Hook Style — TL;DR | Estilo de hooks de Hormozi — TL;DR | hormozi-hooks/references |
| Full Guide | Guía completa | hormozi-hooks/references |
| What makes a Hormozi hook (core idea) | Qué hace que un hook sea de Hormozi (idea central) | hormozi-hooks/references |
| Core Principles of Hormozi Hooks | Principios centrales de los hooks de Hormozi | hormozi-hooks/references |
| What makes his hooks convert (not just go viral) | Qué hace que sus hooks conviertan (no solo que se viralicen) | hormozi-hooks/references |
| Pattern Interrupt | Interrupción de patrón | hormozi-hooks/references |
| Compression | Compresión | hormozi-hooks/references |
| Objection pre-handling | Manejo anticipado de objeciones | hormozi-hooks/references |
| Curiosity gap (but controlled) | Brecha de curiosidad (pero controlada) | hormozi-hooks/references |
| “Give value immediately” bias | Sesgo de “dar valor de inmediato” | hormozi-hooks/references |
| Value Equation Hook | Hook de Ecuación de Valor | hormozi-hooks/references |
| Question Hook | Hook de pregunta | hormozi-hooks/references |
| Pain Amplification Hook | Hook de amplificación del dolor | hormozi-hooks/references |
| Speed Hook | Hook de velocidad | hormozi-hooks/references |
| Effort Reduction Hook | Hook de reducción de esfuerzo | hormozi-hooks/references |
| Mechanism Hook | Hook de mecanismo | hormozi-hooks/references |
| Story Hook | Hook de historia | hormozi-hooks/references |
| Callout Hook | Hook de callout | hormozi-hooks/references |
| Contrarian Hook | Hook a contracorriente | hormozi-hooks/references |
| “How I…” Proof Hook | Hook de prueba “Cómo yo…” | hormozi-hooks/references |
| Format | Formato | bonus-stack, hormozi-offer, hormozi-pitch, productize, sub-offer, sub-pricing, sub-sales, sub-value, value-accelerator |
| Name | Nombre | bonus-stack, landing-page-copy, pricing-strategy, productize, sub-pricing, sub-value, value-accelerator |
| Price | Precio | audit-offer, hormozi-pitch, idea-to-product, pricing-strategy, productize, sub-value |
| Who it’s for / Who it's for | Para quién es | audit-offer, bonus-stack, hormozi-offer, hormozi-pitch, idea-to-product, offer-angles, sub-offer, sub-sales, sub-value |
| Who it’s not for / Who it's NOT for | Para quién NO es | hormozi-offer, sub-offer |
| Delivery | Entrega | hormozi-offer, hormozi-pitch, idea-to-product, sub-offer, sub-sales |
| Option 1 / Option 2 / Option 3 | Opción 1 / Opción 2 / Opción 3 | dfy-dwy-diy, hormozi-offer, hormozi-pitch, sub-offer, sub-sales |
| Value | Valor | bonus-stack, hormozi-offer, hormozi-pitch, landing-page-copy, objection-destroyer |
| What it does | Qué hace | bonus-stack, idea-to-product, offer-angles, sub-value, value-accelerator |
| How it works | Cómo funciona | audit-offer, hormozi-pitch, sub-sales, sub-value |
| Outcome | Resultado | bonus-stack, idea-to-product, pricing-strategy, productize |
| Pain | Dolor | hormozi-hooks, idea-to-product, market-research, sub-sales |
| Reasoning | Razonamiento | dfy-dwy-diy, market-research, pricing-strategy, sub-pricing |
| Bonus | Bono | bonus-stack, hormozi-pitch, landing-page-copy |
| CTA | CTA | hormozi-offer, landing-page-copy, sub-offer |
| Description | Descripción | landing-page-copy, market-research, productize |
| Time to first win | Tiempo hasta la primera victoria | hormozi-offer, sub-offer, value-accelerator |
| Unique angle | Ángulo único | hormozi-offer, idea-to-product, sub-offer |
| What’s included / What's included | Qué incluye | hormozi-offer, hormozi-pitch, pricing-strategy, sub-offer, sub-sales |
| Why | Por qué | business-model, sub-market, sub-offer |
| Why it works | Por qué funciona | hormozi-hooks, offer-angles, sub-value |
| Willingness to pay | Disposición a pagar | dfy-dwy-diy, market-research, sub-market |
| Audience | Audiencia | hormozi-hooks, sub-sales |
| Best channel | Mejor canal | hormozi-offer, sub-offer |
| Bullets | Bullets | hormozi-offer, sub-offer |
| Pros / Cons | Pros / Contras | business-model, dfy-dwy-diy |
| Current positioning | Posicionamiento actual | offer-angles, sub-offer |
| Current situation | Situación actual | hormozi-offer, sub-offer |
| Current stage | Etapa actual | hormozi-offer, sub-offer |
| Hour 0 / Hour 1 / Day 1 | Hora 0 / Hora 1 / Día 1 | sub-value, value-accelerator |
| Desired outcome | Resultado deseado | hormozi-offer, sub-offer |
| Downsell | Downsell | idea-to-product, sub-pricing |
| Upsell | Upsell | idea-to-product, sub-pricing |
| Dream Outcome | Resultado soñado | hormozi-pitch, sub-sales |
| Perceived Likelihood | Probabilidad percibida | hormozi-pitch, sub-sales |
| Time Delay | Demora | hormozi-pitch, sub-sales |
| Effort & Sacrifice | Esfuerzo y sacrificio | hormozi-pitch, sub-sales |
| Ease | Facilidad | hormozi-hooks, sub-sales |
| Speed | Velocidad | hormozi-hooks, sub-sales |
| Result | Resultado | hormozi-hooks, sub-sales |
| Emotional outcome | Resultado emocional | hormozi-offer, sub-offer |
| Primary outcome | Resultado principal | hormozi-offer, sub-offer |
| Outcome statement | Frase de resultado | hormozi-offer, sub-offer |
| Status shift | Cambio de estatus | hormozi-offer, sub-offer |
| Failed attempts | Intentos fallidos | hormozi-offer, sub-offer |
| Pain points | Puntos de dolor | hormozi-offer, sub-offer |
| One-sentence avatar | Avatar en una frase | hormozi-offer, sub-offer |
| Hook 1 / Hook 2 / Hook 3 | Hook 1 / Hook 2 / Hook 3 | hormozi-hooks, idea-to-product |
| Hooks | Hooks | hormozi-offer, sub-offer |
| Key improvements made | Mejoras clave realizadas | hormozi-pitch, sub-sales |
| Main channel | Canal principal | hormozi-offer, sub-offer |
| Market | Mercado | hormozi-offer, sub-offer |
| Segment | Segmento | hormozi-offer, sub-offer |
| Why this segment | Por qué este segmento | hormozi-offer, sub-offer |
| Mechanism | Mecanismo | hormozi-pitch, sub-sales |
| Messaging changes | Cambios en los mensajes | effort-reduction, value-accelerator |
| Model | Modelo | sub-offer, sub-pricing |
| Primary model | Modelo principal | business-model, dfy-dwy-diy |
| Next actions | Próximas acciones | hormozi-offer, sub-offer |
| Objections to handle | Objeciones a manejar | hormozi-offer, sub-offer |
| Offer name | Nombre de la oferta | hormozi-offer, sub-offer |
| Positioning statement | Frase de posicionamiento | hormozi-offer, sub-offer |
| Pricing implications | Implicaciones de precio | pricing-strategy, sub-pricing |
| Purpose | Propósito | hormozi-offer, hormozi-pitch |
| Reason | Motivo | hormozi-pitch, sub-sales |
| Recommended | Recomendada | sub-offer, sub-sales |
| Recommended guarantee | Garantía recomendada | hormozi-offer, hormozi-pitch |
| Sales angle | Ángulo de venta | hormozi-offer, sub-offer |
| Score | Puntaje | audit-offer, dfy-dwy-diy |
| Stage 1 / Stage 2 / Stage 3 | Etapa 1 / Etapa 2 / Etapa 3 | business-model, sub-pricing |
| Steps | Pasos | productize, sub-pricing |
| Strengths / Weaknesses | Fortalezas / Debilidades | audit-offer, sub-value |
| Critical weaknesses | Debilidades críticas | sub-value |
| Templates | Plantillas | productize, value-accelerator |
| Time to result | Tiempo hasta el resultado | sub-value, value-accelerator |
| Total value | Valor total | hormozi-offer, hormozi-pitch, sub-sales |
| Urgency | Urgencia | dfy-dwy-diy, market-research |
| What is being sold | Qué se vende | hormozi-offer, sub-offer |
| What is offered | Qué se ofrece | productize, sub-pricing |
| What the business does | Qué hace el negocio | hormozi-offer, sub-offer |
| What it promises | Qué promete | audit-offer, sub-value |
| What objections are removed | Qué objeciones se eliminan | bonus-stack, sub-value |
| Who | Quién | sub-market, sub-offer |
| Why it matters | Por qué importa | pricing-strategy, value-accelerator |
| Why this order | Por qué este orden | bonus-stack, sub-value |
| Issues / Fixes | Problemas / Correcciones | audit-offer |
| Before (weak description) / After (improved framing) | Antes (descripción débil) / Después (encuadre mejorado) | value-perception |
| Buyers / Browsers | Compradores / Curiosos | market-research, sub-market |
| Buyer vs browser / Buyers vs Browsers | Comprador vs curioso / Compradores vs curiosos | market-research, sub-market |
| Surface pain / Deeper pain / Hidden pain | Dolor superficial / Dolor profundo / Dolor oculto | market-research |
| Midnight thoughts | Pensamientos de medianoche | market-research |
| Emotional triggers | Disparadores emocionales | market-research |
| Fear / Frustration / Desire | Miedo / Frustración / Deseo | market-research |
| Niche 1 / Niche 2 / Niche 3 | Nicho 1 / Nicho 2 / Nicho 3 | market-research |
| Pain / Money / Reach / Growth | Dolor / Dinero / Alcance / Crecimiento | market-research, sub-market |
| Competition / Competition signal | Competencia / Señal de competencia | market-research, sub-market |
| Overall demand | Demanda general | sub-market |
| Urgency score | Puntaje de urgencia | sub-market |
| Winning niche | Nicho ganador | sub-market |
| Low price / Mid price / High price | Precio bajo / Precio medio / Precio alto | pricing-strategy |
| Low-end / Mid-range / Premium | Gama baja / Gama media / Premium | sub-pricing |
| Strategy type | Tipo de estrategia | pricing-strategy |
| Techniques used | Técnicas usadas | pricing-strategy |
| Narrative | Narrativa | pricing-strategy |
| Potential issues / Adjustments | Problemas potenciales / Ajustes | pricing-strategy |
| Tests to run | Tests a correr | pricing-strategy |
| Skills / Assets / Constraints / Goals | Habilidades / Activos / Restricciones / Metas | business-model |
| Beginner / Intermediate / Advanced | Principiante / Intermedio / Avanzado | business-model, productize |
| Fit | Encaje | business-model |
| Role | Rol | business-model |
| Supporting model | Modelo de apoyo | business-model |
| Key risks / How to mitigate | Riesgos clave / Cómo mitigarlos | business-model |
| Step 1 / Step 2 / Step 3 | Paso 1 / Paso 2 / Paso 3 | business-model |
| Skill level | Nivel de habilidad | dfy-dwy-diy |
| Time availability | Tiempo disponible | dfy-dwy-diy |
| Skills required | Habilidades requeridas | dfy-dwy-diy |
| Speed required | Velocidad requerida | dfy-dwy-diy |
| Complexity | Complejidad | dfy-dwy-diy |
| Desired result | Resultado deseado | dfy-dwy-diy |
| What’s weak / What’s missing | Qué está débil / Qué falta | dfy-dwy-diy |
| Suggestions | Sugerencias | dfy-dwy-diy |
| Entry offer / Core offer / Premium offer | Oferta de entrada / Oferta principal / Oferta premium | dfy-dwy-diy |
| Total steps | Pasos totales | effort-reduction |
| Key effort points | Puntos clave de esfuerzo | effort-reduction |
| Where users struggle | Dónde se traba el usuario | effort-reduction |
| Step / Friction / Fix | Paso / Fricción / Corrección | effort-reduction, sub-value |
| Decision / Default replacement | Decisión / Reemplazo por defecto | effort-reduction |
| Template name / What it replaces / Where it’s used | Nombre de la plantilla / Qué reemplaza / Dónde se usa | effort-reduction |
| Task / Automation idea / Impact | Tarea / Idea de automatización / Impacto | effort-reduction |
| What is done for the user / Where it helps / Value added | Qué se hace por el usuario / Dónde ayuda / Valor agregado | effort-reduction |
| New step-by-step path | Nuevo camino paso a paso | effort-reduction |
| Structural changes | Cambios estructurales | effort-reduction |
| Promised result | Resultado prometido | value-accelerator |
| Time to full result | Tiempo hasta el resultado completo | value-accelerator |
| Key delays | Demoras clave | value-accelerator |
| What the first win is / Why it matters / When it happens | Qué es la primera victoria / Por qué importa / Cuándo ocurre | value-accelerator |
| What to remove / What to simplify / What to pre-build | Qué eliminar / Qué simplificar / Qué prearmar | value-accelerator |
| Automation / Templates / Shortcuts | Automatización / Plantillas / Atajos | value-accelerator |
| New flow / First result placement / Key upgrades | Nuevo flujo / Ubicación del primer resultado / Mejoras clave | value-accelerator |
| What feels weak / What is unclear | Qué se siente débil / Qué no queda claro | value-perception |
| Offer name options / Component names / Bonus names | Opciones de nombre para la oferta / Nombres de componentes / Nombres de bonos | value-perception |
| New structure / Grouped components / System naming | Nueva estructura / Componentes agrupados / Naming del sistema | value-perception |
| New order / Clear layers / Improved presentation | Nuevo orden / Capas claras / Presentación mejorada | value-perception |
| Comparisons / Value references | Comparaciones / Referencias de valor | value-perception |
| Before vs after / Problem vs solution | Antes vs después / Problema vs solución | value-perception |
| What was implicit → now explicit | Lo que era implícito → ahora explícito | value-perception |
| What was simplified / Why it helps | Qué se simplificó / Por qué ayuda | value-perception |
| Summary of improvements | Resumen de las mejoras | value-perception |
| Why the offer now feels more valuable | Por qué la oferta ahora se siente más valiosa | value-perception |
| What the offer does | Qué hace la oferta | bonus-stack |
| Condition (time/limit) | Condición (tiempo/límite) | bonus-stack |
| Sum of all bonuses | Suma de todos los bonos | bonus-stack |
| What was removed / Why this stack works | Qué se eliminó / Por qué funciona este stack | bonus-stack |
| Objection / Reframe / Proof | Objeción / Reencuadre / Prueba | objection-destroyer |
| Value / Trust / Effort / Time / Identity / Risk | Valor / Confianza / Esfuerzo / Tiempo / Identidad / Riesgo | objection-destroyer |
| Priority list | Lista de prioridades | objection-destroyer |
| Where to use each response | Dónde usar cada respuesta | objection-destroyer |
| What to fix in the offer | Qué corregir en la oferta | objection-destroyer |
| Quick replies | Respuestas rápidas | objection-destroyer |
| Angle | Ángulo | offer-angles |
| Variation 1 / Variation 2 / Variation 3 | Variación 1 / Variación 2 / Variación 3 | offer-angles |
| V1 / V2 | V1 / V2 | sub-offer |
| Best angle for ads / landing page / content / premium offer | Mejor ángulo para anuncios / landing page / contenido / oferta premium | offer-angles |
| Best for ads / landing page / organic content / high-ticket | Mejor para anuncios / landing page / contenido orgánico / high-ticket | sub-offer |
| Best hooks for ads / organic content / email / landing page | Mejores hooks para anuncios / contenido orgánico / email / landing page | hormozi-hooks |
| Headline / Subheadline / Copy | Headline / Subheadline / Copy | landing-page-copy |
| Testimonials / Case studies | Testimonios / Casos de éxito | landing-page-copy |
| Standalone value | Valor individual | hormozi-offer |
| Price hypothesis | Hipótesis de precio | hormozi-offer |
| Price justification | Justificación del precio | hormozi-pitch |
| Component | Componente | hormozi-offer |
| Bonus name | Nombre del bono | hormozi-offer |
| Avatar / Demand | Avatar / Demanda | idea-to-product |
| Short version / Full version | Versión corta / Versión completa | idea-to-product |
| How it sells | Cómo vende | idea-to-product |
| Ladder | Escalera | idea-to-product |
| First purchase | Primera compra | productize |
| Offer / Why it fits | Oferta / Por qué encaja | productize |
| When upsell appears / When downsell appears | Cuándo aparece el upsell / Cuándo aparece el downsell | productize |
| How customers move between offers | Cómo se mueven los clientes entre las ofertas | productize |
| How revenue per customer increases | Cómo aumentan los ingresos por cliente | productize |
| How it is delivered / How it’s delivered | Cómo se entrega | productize, sub-pricing |
| Where time is spent | En qué se va el tiempo | sub-pricing |
| Core outcome | Resultado principal | sub-pricing |
| Type | Tipo | sub-pricing |
| Ratio | Ratio | sub-value |
| Current / Improved | Actual / Mejorado | sub-value |
| Comparison | Comparación | sub-value |
| Upgraded structure / Current structure | Estructura mejorada / Estructura actual | sub-value |
| Component | Componente | sub-offer, sub-sales |
| Format | Formato | sub-pricing, sub-value |
| Objection | Objeción | sub-pricing, sub-sales |
| Price | Precio | sub-pricing, sub-sales |
| Value | Valor | sub-sales, sub-value |
| Dimension | Dimensión | sub-value |
| Score | Puntaje | sub-value |
| Key Issue | Problema clave | sub-value |
| Fix | Corrección | sub-value |
| Solves | Resuelve | sub-value |
| Bonus Name | Nombre del bono | sub-value |
| Step / Friction | Paso / Fricción | sub-value |
| Before / After | Antes / Después | sub-value |
| Current / Improved | Actual / Mejorado | sub-value |
| Obstacle / Solution / Delivery Method | Obstáculo / Solución / Método de entrega | sub-offer |
| Purpose | Propósito | sub-offer |
| Estimated Value | Valor estimado | sub-offer |
| Standalone Value | Valor individual | sub-offer |
| Total value: / Price hypothesis: | Valor total: / Hipótesis de precio: | sub-offer |
| Niche / Pain / Money / Reach / Growth / Total | Nicho / Dolor / Dinero / Alcance / Crecimiento / Total | sub-market |
| Hidden Belief | Creencia oculta | sub-pricing |
| Belief Shift | Cambio de creencia | sub-pricing |
| Proof | Prueba | sub-pricing |
| Handle Where | Dónde manejarla | sub-pricing |
| Hero / FAQ / DM / Sales call | Hero / FAQ / DM / Llamada de ventas | sub-pricing |
| Technique / Application | Técnica / Aplicación | sub-pricing |
| Price anchoring | Anclaje de precio | sub-pricing |
| Charm / round pricing | Charm pricing / precios redondos | sub-pricing |
| Tier contrast | Contraste entre niveles | sub-pricing |
| Tier / Name / What's Included | Nivel / Nombre / Qué incluye | sub-pricing |
| Level | Nivel | sub-pricing |
| Entry / Core / Premium | Entrada / Principal / Premium | sub-pricing |
| Outcome | Resultado | sub-pricing |
| Rank / Hook / Why It Works / Best For | Puesto / Hook / Por qué funciona / Mejor para | sub-sales |
| Description | Descripción | sub-sales |
| Response | Respuesta | sub-sales |
| Total value / Your price | Valor total / Tu precio | sub-sales |
| Decision / Choice / Reasoning | Decisión / Elección / Razonamiento | hormozi-orchestrator |
| Target customer / Core problem / Dream outcome | Cliente objetivo / Problema central / Resultado soñado | hormozi-orchestrator |
| Delivery model / Price point / Offer name / Guarantee | Modelo de entrega / Punto de precio / Nombre de la oferta / Garantía | hormozi-orchestrator |
| File / What It Contains / Use It When | Archivo / Qué contiene / Cuándo usarlo | hormozi-orchestrator |
| Signal / What You're Extracting | Señal / Qué estás extrayendo | hormozi-orchestrator |
| WHO / PAIN / OUTCOME / STAGE / DELIVERY / CONSTRAINTS / GOAL / PROOF | QUIÉN / DOLOR / RESULTADO / ETAPA / ENTREGA / RESTRICCIONES / META / PRUEBAS | hormozi-orchestrator |
| Model / Price Range Guidance | Modelo / Rango de precio sugerido | sub-pricing |
| Rule / Detail | Regla / Detalle | create-plugin |
| Skill / Purpose | Skill / Propósito | README.md |
| File / What's Inside | Archivo / Qué contiene | README.md |
