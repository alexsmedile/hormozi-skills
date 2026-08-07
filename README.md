# hormozi-skills-es

**Convierte cualquier idea de negocio en una oferta completa y vendible — con los frameworks de Alex Hormozi.**

![License](https://img.shields.io/badge/license-MIT-blue)
![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-blueviolet)
![Platform](https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Codex%20%7C%20Cursor-lightgrey)
![Inspired by](https://img.shields.io/badge/inspired%20by-Alex%20Hormozi-orange)

---

> Una biblioteca de skills para agentes de código. Conéctala, describe tu negocio y obtén un sistema de oferta completo — investigación de mercado, estructura de la oferta, precios, pitch, hooks, landing page — escrito en archivos en una sola sesión.

---

## El problema

Construir una oferta convincente es difícil. La mayoría de los fundadores, coaches y consultores hace una de estas tres cosas:

- Escribe ofertas vagas que no convierten — *"Ayudo a la gente a hacer crecer su negocio"*
- Pone mal el precio — demasiado bajo para que lo tomen en serio, demasiado alto sin justificación
- Se salta por completo la capa de ventas — sin hooks, sin pitch, sin copy de landing page

**hormozi-skills-es** resuelve esto de punta a punta. Un orquestador, cinco subagentes especializados, 18 skills, 11 archivos de salida.

---

## Inicio rápido

### Claude Code

Agrega el marketplace y después instala el plugin:

```bash
/plugin marketplace add JustinCast/hormozi-skills-es
/plugin install hormozi-skills-es@hormozi-skills-es
```

Después invoca el agente `hormozi-orchestrator` o una skill específica.

### Codex

Instala directamente desde GitHub:

```bash
codex plugin install https://github.com/JustinCast/hormozi-skills-es
```

### Instalación manual

Si prefieres los archivos de skill en crudo en lugar del flujo del plugin:

```bash
# Clona la biblioteca de skills
git clone https://github.com/JustinCast/hormozi-skills-es
cd hormozi-skills-es

# Copia skills y agents a tu configuración de Claude
cp -r skills/ agents/ ~/.claude/
```

> [!TIP]
> Describe tu negocio en lenguaje simple — una idea en bruto, un volcado de ideas o una oferta que ya tengas. El orquestador te entrevista, detecta tu etapa y construye todo a partir de ahí.

---

## 📦 Lo que obtienes

11 archivos de salida escritos en `output/` en una sola sesión:

| Archivo | Qué contiene |
|------|--------------|
| `MARKET_RESEARCH.md` | Nicho validado, mapa del dolor, señales de demanda |
| `OFFER.md` | Grand Slam Offer (oferta irresistible) completa — avatar, obstáculos, mapa de soluciones, stack de valor |
| `OFFER_ANGLES.md` | 8 ángulos de posicionamiento, ordenados |
| `OFFER_AUDIT.md` | Puntaje por dimensión + correcciones prioritarias |
| `VALUE_PERCEPTION.md` | Naming, empaquetado y encuadre mejorados |
| `BONUS_STACK.md` | Estructura de bonos que elimina objeciones, con valor percibido |
| `PRICING.md` | Precio anclado al valor, niveles, historia que lo justifica |
| `OBJECTIONS.md` | Creencias ocultas, cambios de creencia, respuestas listas para DM |
| `PITCH.md` | Versiones corta / media / larga del pitch |
| `HOOKS.md` | Más de 30 hooks en 10 tipos, ordenados |
| `LANDING_PAGE.md` | Copy completo de la landing page, sección por sección |

---

## 🧠 Biblioteca de skills

Usa cualquier skill por separado — no hace falta el orquestador:

| Skill | Propósito |
|-------|---------|
| `hormozi-offer` | Construye una Grand Slam Offer desde cero → `OFFER.md` |
| `hormozi-pitch` | Pitch deck y narrativa de ventas |
| `hormozi-hooks` | Generación de hooks y headlines (más de 30 hooks) |
| `audit-offer` | Puntúa y reescribe una oferta débil que ya existe |
| `bonus-stack` | Construye un stack de bonos que elimina objeciones |
| `business-model` | Elige y estructura el modelo de negocio correcto |
| `create-plugin` | Herramientas — genera el andamiaje de este repo como plugin de Claude Code + Codex |
| `dfy-dwy-diy` | Encuadra la oferta en niveles DFY / DWY / DIY |
| `effort-reduction` | Reduce el esfuerzo percibido en la oferta |
| `idea-to-product` | Convierte una idea en bruto en una oferta productizada |
| `landing-page-copy` | Genera el copy de la landing page a partir de una oferta existente |
| `market-research` | Investiga el dolor del mercado y las señales de demanda |
| `objection-destroyer` | Mapea y neutraliza las objeciones comunes |
| `offer-angles` | Genera múltiples ángulos de posicionamiento |
| `pricing-strategy` | Anclaje de precio y empaquetado |
| `productize` | Productiza un negocio de servicios |
| `value-accelerator` | Aumenta el valor percibido |
| `value-perception` | Mejora cómo se comunica el valor |

> [!TIP]
> Sáltate el orquestador y llama a cualquier skill directamente: `/audit-offer`, `/pricing-strategy`, `/landing-page-copy` — cada una funciona por separado, sin contexto previo.

---

## 🔀 Sistema de agentes

```
hormozi-orchestrator
├── sub-market    → MARKET_RESEARCH.md
├── sub-offer     → OFFER.md + OFFER_ANGLES.md
├── sub-value     → OFFER_AUDIT.md + VALUE_PERCEPTION.md + BONUS_STACK.md
├── sub-pricing   → PRICING.md + OBJECTIONS.md
└── sub-sales     → PITCH.md + HOOKS.md + LANDING_PAGE.md
```

**Orden de dependencia:** mercado → oferta → (valor ∥ precios) → ventas

El orquestador detecta tu etapa del embudo (idea / oferta que no convierte / falta capa de ventas / escalado de servicios) y ejecuta solo los subagentes que necesitas.

---

## ⚙️ Cómo funciona

1. **Recepción** — dale al orquestador lo que sea: una idea en bruto, una oferta existente, un volcado de ideas o una página de ventas
2. **Entrevista** — preguntas puntuales de a una, cada una con una respuesta sugerida
3. **Detección de etapa** — clasifica tu situación (Etapa A–E) y muestra qué subagentes se van a ejecutar
4. **Delegación** — lanza los subagentes en orden de dependencia y les pasa briefs estructurados
5. **Resumen** — produce `output/SUMMARY.md`: tu oferta en un párrafo, decisiones clave, top 3 de acciones y el mejor hook para usar hoy

---

## Estructura del repo

```
hormozi-skills-es/
├── skills/     # 18 skills de agente independientes
├── agents/     # Orquestador + 5 subagentes
├── output/     # Documentos de oferta generados (empieza vacía)
└── input/      # Deja acá ofertas, notas o páginas de ventas existentes
```

---

## Para quién es

- Fundadores, coaches, consultores y freelancers que construyen ofertas
- Cualquiera que aplique la metodología de Hormozi y quiera ejecución con IA, no solo consejos de IA
- Agentes de código que corren pipelines de generación de ofertas

## Para quién NO es

- Copywriters genéricos que buscan plantillas para rellenar — esto piensa, no solo rellena
- Desarrolladores que necesitan una biblioteca de código — esto es a base de prompts, nativo de agentes
- Gente que quiere una respuesta de un solo tiro sin iterar — el orquestador te entrevista

---

## Frameworks

Construido sobre la metodología de ofertas de Alex Hormozi de *$100M Offers* y *$100M Leads*:

- Construcción de la Grand Slam Offer
- Ecuación resultado soñado × probabilidad × demora × esfuerzo
- Inversión obstáculo → solución
- Stack de valor e ingeniería de bonos
- Diseño de garantías (incondicional / condicional / basada en esfuerzo)
- Anclaje de precio y valor percibido
- Arquitectura de hooks (interrupción de patrón, identidad, resultado, curiosidad)

---

## Créditos

Inspirado en el trabajo de Alex Hormozi. Construido para agentes de código por [@alexsmedile](https://github.com/alexsmedile).
