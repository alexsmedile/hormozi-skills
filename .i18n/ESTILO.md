# ESTILO.md · hormozi-skills-es

Reglas de registro, tipografía y anticalco. **Vinculante para los 10 traductores.**
Variante: **español neutro LatAm**. Sin voseo, sin "vosotros", sin localismos (ni MX, ni AR, ni ES).

---

## 1. Registro (D2) — el punto más delicado del proyecto

Estos archivos tienen **dos audiencias mezcladas dentro del mismo documento**. Antes de traducir una frase hay que decidir a cuál pertenece.

### 1.1 · Instrucciones AL asistente (≈85 % del texto)

**Imperativo impersonal dirigido al asistente. Nunca "usted". Nunca "el usuario debería".**

Tres formas admitidas:

**(a) "El asistente debe…" / "El asistente debería…"** — cuando el fuente usa `The assistant should/must`.

| Fuente | Traducción |
|---|---|
| `skills/hormozi-offer/SKILL.md:24` · `By the end, the assistant should produce a polished markdown file called `OFFER.md` with:` | `Al final, el asistente debe producir un archivo markdown pulido llamado `OFFER.md` con:` |
| `skills/hormozi-offer/SKILL.md:132` · `The assistant should say what looks strong and what looks weak.` | `El asistente debe decir qué se ve fuerte y qué se ve débil.` |
| `skills/hormozi-offer/SKILL.md:290` · `When brainstorming, the assistant must:` | `Al hacer brainstorming, el asistente debe:` |
| `skills/hormozi-offer/SKILL.md:481` · `The assistant should not:` | `El asistente no debe:` |
| `skills/hormozi-offer/SKILL.md:19` · `The skill should feel like a strategic partner, not a form filler.` | `La skill debe sentirse como un socio estratégico, no como un formulario.` |

**(b) Imperativo en tú, dirigido al asistente** — cuando el fuente usa un imperativo inglés.

| Fuente | Traducción |
|---|---|
| `skills/create-plugin/SKILL.md:16` · `Ask the user these questions (all at once):` | `Hazle estas preguntas al usuario (todas juntas):` |
| `skills/hormozi-offer/SKILL.md:70` · `Identify:` | `Identifica:` |
| `skills/audit-offer/SKILL.md:87` · `Check:` | `Revisa:` |
| `skills/hormozi-pitch/SKILL.md:58` · `Extract:` | `Extrae:` |
| `skills/hormozi-offer/SKILL.md:88` · `Do not ask everything at once if the input is very vague.` | `No preguntes todo de una si la entrada es muy vaga.` |
| `agents/sub-offer.md:16` · `read it first — use the winning niche…` | `léelo primero: usa el nicho ganador…` |
| `agents/hormozi-orchestrator.md:26` · `**Read any referenced files** using the Read tool before proceeding.` | `**Lee los archivos referenciados** con la herramienta Read antes de continuar.` |

**(c) Segunda persona sobre el rol del agente** — solo en los `agents/*.md`, donde el fuente ya dice `You are…`.

| Fuente | Traducción |
|---|---|
| `agents/sub-market.md:10` · `You are an internal execution specialist. You do NOT interview the user.` | `Eres un especialista de ejecución interno. NO entrevistas al usuario.` |
| `agents/hormozi-orchestrator.md:11` · `You are the master orchestrator for building Hormozi-inspired offers.` | `Eres el orquestador maestro para construir ofertas inspiradas en Hormozi.` |
| `agents/hormozi-orchestrator.md:13` · `Your job: take anything the user gives you…` | `Tu trabajo: tomar cualquier cosa que el usuario te dé…` |

> ⚠️ **Nunca mezclar.** Si un párrafo empieza con "El asistente debe…", no puede terminar con "…y pregúntale al usuario". Elegí una forma por párrafo y sostenela.

### 1.2 · Texto que el asistente DICE al usuario → **tuteo directo, sin hype**

Se reconoce por: bloques `>`, el prompt de instalación de `CLAUDE.md`, y los bloques de consola del orquestador.

| Fuente | Traducción |
|---|---|
| `agents/hormozi-orchestrator.md:31` · `> Here's what I'm hearing: you help [specific audience] with [specific problem]. You currently deliver this as [format]. What's still unclear is [gap 1] and [gap 2]. Let me ask a few focused questions to fill those in.` | `> Esto es lo que entiendo: ayudas a [audiencia específica] con [problema específico]. Hoy lo entregas como [formato]. Lo que todavía no queda claro es [hueco 1] y [hueco 2]. Te voy a hacer unas preguntas puntuales para cerrar eso.` |
| `skills/hormozi-offer/SKILL.md:80-81` · `> Here's what I understand so far: you help X get Y result through Z.` / `> What's still unclear is who the buyer is…` | `> Esto es lo que entiendo hasta ahora: ayudas a X a lograr Y a través de Z.` / `> Lo que todavía no queda claro es quién es el comprador…` |
| `skills/hormozi-offer/SKILL.md:135-136` · `> Strong: the audience is easy to target and already spends money.` / `> Weak: the outcome is still too broad.` | `> Fuerte: la audiencia es fácil de segmentar y ya gasta dinero.` / `> Débil: el resultado sigue siendo demasiado amplio.` |
| `skills/hormozi-offer/SKILL.md:182-183` · `> Based on what you shared, the best first offer is X.` | `> Por lo que compartiste, la mejor primera oferta es X.` |
| `skills/value-accelerator/SKILL.md:65-66` · `> Right now, the first real result happens after X.` / `> This feels slow because the user must first do Y and Z.` | `> Hoy, el primer resultado real llega después de X.` / `> Se siente lento porque el usuario primero tiene que hacer Y y Z.` |
| `skills/effort-reduction/SKILL.md:73-74` · `> Right now, the user must do X steps, make Y decisions, and figure out Z alone.` | `> Hoy, el usuario tiene que dar X pasos, tomar Y decisiones y resolver Z solo.` |
| `skills/audit-offer/SKILL.md:82` · `> This offer helps X achieve Y using Z.` | `> Esta oferta ayuda a X a lograr Y usando Z.` |
| `skills/pricing-strategy/SKILL.md:66` · `> This offer helps X achieve Y, which is worth Z in terms of time, money, or status.` | `> Esta oferta ayuda a X a lograr Y, que vale Z en tiempo, dinero o estatus.` |
| `skills/dfy-dwy-diy/SKILL.md:144` · `> This customer wants results fast and does not want to learn deeply.` | `> Este cliente quiere resultados rápido y no quiere aprender en profundidad.` |
| `agents/hormozi-orchestrator.md:308` · `Challenge weak ideas: "That's too broad — let me suggest a sharper version"` | `Cuestiona las ideas débiles: "Eso es demasiado amplio, déjame proponerte una versión más afilada"` |

**Prompt de instalación (`CLAUDE.md:9-13`) — tuteo, traducción fija:**

```
> "¿Dónde instalo hormozi-skills-es?
> - **Proyecto** (por defecto) — `.claude/` en la carpeta del proyecto actual. Solo disponible en este proyecto.
> - **Usuario** — `~/.claude/` en tu carpeta personal. Disponible en todos los proyectos.
>
> Presiona Enter para usar la opción por defecto (proyecto)."
```

**Bloque `DETECTED STAGE:` (`agents/hormozi-orchestrator.md:145-156`) — tuteo, traducción fija:**

```
ETAPA DETECTADA: [A / B / C / D / E — descripción breve]

SKILLS QUE SE EJECUTARÁN:
1. [subagente] → [archivos de salida]
2. [subagente] → [archivos de salida]
...

SALIDA ESTIMADA: [lista de archivos que se van a producir]

Confirma para continuar, o dime qué cambiar.
```

### 1.3 · Plantillas de artefacto (dentro de ` ```md `) → **sustantivos, sin verbo conjugado**

`## 7. Core Offer` → `## 7. Oferta principal`. Nunca `## 7. Define la oferta principal`.
Ver `ENCABEZADOS-CANONICOS.md` §A y §D.

---

## 2. Puntuación española obligatoria

- **`¿` y `¡` de apertura son obligatorios, siempre.** El corpus tiene 156 líneas con `?`; ninguna se traduce sin `¿`.
  - `Is the audience specific?` → `¿La audiencia es específica?`
  - `Who has paid you before?` → `¿Quién te ha pagado antes?`
  - `Can they afford solutions ($50–$5000+)?` → `¿Pueden pagar soluciones ($50–$5000+)?`
  - `Where should I install hormozi-skills-es?` → `¿Dónde instalo hormozi-skills-es?`
- Dentro de listas de preguntas cortas, el `¿` va **después** del guion de viñeta: `- ¿La audiencia es específica?`
- Cuando solo la última parte de la oración es interrogativa, el `¿` se abre ahí: `Si el resultado no es claro, ¿qué lo bloquea?`
- Comillas: se **conservan los glifos del fuente**. Si el fuente usa `“ ”`, la traducción usa `“ ”`. Si usa `" "`, usa `" "`. **No** se convierten a `« »`.
- Los dos puntos que introducen listas se mantienen: `Identify:` → `Identifica:`.

---

## 3. Caracteres que se conservan **byte a byte**

| Carácter | Nombre / código | Presencia medida | Regla |
|---|---|---|---|
| `⸻` | U+2E3B TWO-EM DASH | 187 ocurrencias en 19 archivos | Separador estructural. **Nunca** se cambia por `---`, `—` ni línea en blanco. |
| `→` | U+2192 | 212 ocurrencias en 27 archivos | **Nunca** `->`. Se conservan los espacios alrededor. |
| `×` | U+00D7 | 10 ocurrencias en 5 archivos | **Nunca** la letra `x`. Ver la cadena canónica en `GLOSARIO-ES.md` §0. |
| `—` | U+2014 EM DASH | 107 ocurrencias en 23 archivos | Se conserva; no se cambia por `-` ni por `–`. |
| `–` | U+2013 EN DASH | 68 ocurrencias en 18 archivos | Se usa en rangos numéricos (`3–5`, `1–10`, `$27–$497`). Se conserva. |
| `↓` `↑` | U+2193 / U+2191 | 2 + 2 | `Time Delay ↓ → Value ↑` → `Demora ↓ → Valor ↑`. |
| `∥` | U+2225 | 1 (`README.md:128`) | `market → offer → (value ∥ pricing) → sales`. |
| `“ ” ’` | comillas tipográficas | 172 / 172 / 85 | Se conservan donde el fuente las tenga. El `’` inglés desaparece al traducir (`Who it’s for` → `Para quién es`), pero **no se reemplaza por `'` en ningún caso**. |
| `$` | signo de dólar | 59 en 12 archivos | Los montos quedan en dólares: `$97`, `$2,000+`, `$5k/month` → `$5k/mes`. **No** se convierte a otra moneda ni se cambia el separador de miles. |
| `￼` | U+FFFC OBJECT REPLACEMENT | 6 en `hormozi-hooks/references` | Residuo de copiado. **Se conserva tal cual**; no se borra ni se sustituye. |
| Emoji | 👉 🧠 ⚡ ⚙️ 🧩 📦 🚧 🔧 🔥 🔀 💰 🏆 🎯 🎁 | 34 en 3 archivos | Se conservan en su posición exacta, incluido el selector de variación `️` (U+FE0F) de `⚙️`. |
| `  ` final de línea | doble espacio | 26 líneas en 11 archivos | Es un **salto de línea duro de markdown**. Se conserva al final de la línea traducida. Ej.: `skills/hormozi-offer/SKILL.md:80`, `:88`, `:135`, `:182`, `:302`. |

### 3.1 · Viñetas de tabulación dura — **19 archivos**

18 archivos usan `\t•\t` (668 ocurrencias) y 3 usan `\t<n>.\t`. **No son markdown estándar** y el renderizador las muestra como texto preformateado. **Prohibido convertirlas a `-` o a `1.`.**

> En los ejemplos de abajo, `<TAB>` es **notación**: representa un carácter de tabulación real (U+0009). No se escribe la cadena literal `<TAB>` en el archivo traducido.

```
Fuente  (skills/audit-offer/SKILL.md:308):  <TAB>•<TAB>1–3 = critical issue
Destino:                                    <TAB>•<TAB>1–3 = problema crítico

Fuente  (skills/hormozi-offer/SKILL.md:454): <TAB>1.<TAB>Understand the business
Destino:                                     <TAB>1.<TAB>Entiende el negocio
```

Anidamiento de segundo nivel (`skills/bonus-stack/SKILL.md:277-280`) — **dos tabs entre el bullet y el texto**:

```
Fuente:   <TAB>•<TAB><TAB>•<TAB>templates
Destino:  <TAB>•<TAB><TAB>•<TAB>plantillas
```

Solo se traduce **el texto después del último tab**. Los tabs, el `•` y los números no se tocan.

### 3.2 · Otros elementos intocables

- Bloques de código (` ```bash `, ` ```json `, ` ```text `): **el código no se traduce.** En ` ```json ` no se traduce ni una clave ni un valor. En ` ```bash ` se pueden traducir **solo los comentarios `#`**.
- Los placeholders `{{repo-name}}`, `{{username}}`, `{{description}}`, `{{author}}`, `{{license}}` y `${CLAUDE_PLUGIN_ROOT}`: intocables.
- Los badges de `README.md` (`![License](https://img.shields.io/badge/...)`): la URL no se toca.
- Los callouts `> [!TIP]`: el marcador `[!TIP]` queda en inglés; el texto que sigue se traduce.
- `clarity > cleverness` (`skills/landing-page-copy/SKILL.md:55`) usa `>` como signo "mayor que", **no** como cita. → `claridad > astucia`. Lo mismo con `Buyers > audience size` → `Compradores > tamaño de audiencia`, `Perception > reality` → `Percepción > realidad`, `Specific > general` → `Específico > general`, `Framing beats features`… (ver glosario).
- Frontmatter YAML: `name:` **nunca** se traduce; `description:` **sí** se traduce (dispara el matching con prompts en español); `tools:`, `model:`, `color:` no se tocan.

---

## 4. Encabezados: mayúscula inicial solamente

El inglés usa Title Case (`## 3. Ideal Customer Avatar`). **El español usa solo mayúscula inicial.**

| Mal | Bien |
|---|---|
| `## 3. Avatar Del Cliente Ideal` | `## 3. Avatar del cliente ideal` |
| `## 6. Mapa De Soluciones` | `## 6. Mapa de soluciones` |
| `### Hooks De Resultado` | `### Hooks de resultado` |
| `## Guía De Estilo` | `## Guía de estilo` |

Excepciones que **sí** conservan mayúscula interna:
- Siglas: `CTA`, `DFY`, `DWY`, `DIY`, `DM`, `FAQ`, `MAGIC`, `TL;DR`.
- Nombres propios: `Hormozi`, `Alex Hormozi`, `Instagram`, `Notion`, `Claude Code`, `Codex`, `GitHub`.
- Nombres de artefacto: `OFFER.md`, `PITCH.md`, `HOOKS.md`, etc.
- El nombre de framework `Ecuación de Valor` (y sus variables **dentro de la fórmula**: `Resultado Soñado`, `Probabilidad Percibida`, `Demora`, `Esfuerzo y Sacrificio`).

---

## 5. Prohibiciones anticalco

| Prohibido | Correcto | Aparece en |
|---|---|---|
| "hacer sentido" | **tener sentido** | `the offer structure makes sense` → `la estructura de la oferta tiene sentido` |
| "aplicar para" | **aplicar** (transitivo) / **postularse a** | `Apply the framework to the brief` → `Aplica el framework al brief` |
| "en orden de" | **para** | `in order to grow` → `para crecer` |
| "soportar" (por *to support* = respaldar) | **respaldar / sustentar** | `big claims without support` → `promesas grandes sin respaldo` |
| "soportar" (por *to support* = admitir) | **admitir / aceptar / ser compatible con** | contexto de plugins |
| "remover" | **eliminar / quitar** | `remove objections` → `elimina las objeciones`; `remove steps` → `elimina pasos`; `Remove friction first` → `Elimina primero la fricción` |
| "aplicación" por *application* = aplicación de una técnica | ✅ correcto aquí | `Technique / Application` → `Técnica / Aplicación` |
| "librería" | **biblioteca** | `Clarifying Questions Library` → `Biblioteca de preguntas aclaratorias`; `A skill library` → `Una biblioteca de skills` |
| "actualmente" (por *actually*) | **realmente / de hecho** | `what the customer actually feels` → `lo que el cliente realmente siente` |
| "eventualmente" (por *eventually*) | **con el tiempo / al final** | — |
| "consistente" (por *consistent* = coherente) | **coherente** | `promise is consistent` → `la promesa es coherente` |
| "asumir" (por *to assume* = suponer) | **suponer / dar por sentado** | `assume facts not given` → `dar por sentados hechos que no se dieron` |
| "comprometimiento" | **compromiso** | `low commitment → entry` → `poco compromiso → entrada` |
| "customizar" | **personalizar** | `customization` → `personalización` |
| "reportar" (uso periodístico) | ✅ **reportar** es correcto en LatAm para *report back* | `Report Back` → `Reporte al orquestador` |
| "eficientar", "aperturar", "accesar" | **optimizar**, **abrir**, **acceder** | — |
| "el mismo/la misma" como pronombre anafórico | repetir el sustantivo o usar un demostrativo | `…the offer. The same must…` → `…la oferta. Esta debe…` |
| Gerundio de posterioridad | oración coordinada o subordinada | ❌ `Escribe el archivo, reportando después al orquestador.` → ✅ `Escribe el archivo y después reporta al orquestador.` |
| Gerundio con valor de adjetivo | adjetivo o relativo | ❌ `una caja conteniendo plantillas` → ✅ `una caja que contiene plantillas` |
| Voz pasiva perifrástica innecesaria | pasiva refleja o activa | ❌ `El archivo es escrito por el subagente` → ✅ `El subagente escribe el archivo` / `El archivo se escribe en output/` |
| Mayúscula de título en encabezados | mayúscula inicial solamente | ver §4 |
| "Usted" / voseo / "vosotros" | **tú** (al usuario) o imperativo impersonal (al asistente) | ver §1 |

### 5.1 · Preferencias léxicas LatAm neutro

| Usar | Evitar |
|---|---|
| **costo** | coste |
| **computadora** | ordenador |
| **video** | vídeo |
| **trabado / estancado** | atascado (ES), atorado (MX), pegado |
| **agarrar / tomar** | coger |
| **acá / aquí** (indistinto) | — |
| **puntaje** | puntuación (aceptable, pero se fija *puntaje*) |
| **email** | correo electrónico (largo), mail |
| **anuncios** | publicidades, avisos |
| **plan de pagos** | facilidades de pago |
| **presupuesto** | presupuesto (no "budget") |

---

## 6. Longitud y formato

- El español crece ~20 % respecto del inglés. **No se acorta ni se resume para compensar.** Los encabezados sí deben quedar breves: si la traducción literal es muy larga, se prefiere la forma nominal corta ya fijada en `ENCABEZADOS-CANONICOS.md`.
- **No se agregan ni se quitan líneas.** El número de viñetas, filas de tabla y bloques debe ser idéntico al fuente.
- La alineación de las tablas markdown (`|---|---|`) no se toca aunque el ancho cambie.
- Los guiones de viñeta (`-`), la numeración markdown (`1.`) y la indentación con espacios se conservan tal cual.
- Las URLs, rutas y nombres de archivo nunca se traducen ni se reescriben.

---

## 7. Checklist antes de entregar un archivo

1. ¿Todos los `?` tienen su `¿`? ¿Todos los `!` tienen su `¡`?
2. ¿Sobrevivieron los `⸻`, `→`, `×`, `—`, `–`, `↓ ↑`, `“ ” ’`, `$`, emoji y `￼`?
3. ¿Las viñetas `\t•\t` y `\t<n>.\t` siguen siendo tabs, no guiones?
4. ¿Los dobles espacios de fin de línea siguen ahí?
5. ¿La cadena de la Ecuación de Valor está byte a byte según `GLOSARIO-ES.md` §0?
6. ¿Ningún encabezado quedó en Title Case?
7. ¿El `name:` del frontmatter quedó intacto y el `description:` quedó traducido?
8. ¿Ningún token de `NO-TRADUCIR.txt` fue traducido?
9. ¿Cada encabezado y etiqueta coincide **exactamente** con `ENCABEZADOS-CANONICOS.md`?
10. ¿El registro es coherente dentro de cada párrafo (asistente vs. usuario)?
11. ¿Mismo número de líneas, viñetas y filas de tabla que el fuente?
12. ¿Ningún "remover", "soportar", "hacer sentido", "en orden de", "aplicar para", "librería"?
