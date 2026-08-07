# AGENTS.md

Guía para Codex y cualquier otro agente de código que trabaje sobre este repositorio.

## Qué es esto

Una biblioteca de skills para agentes de código, construida sobre los frameworks de oferta de Alex Hormozi. No hay pipeline de build: es contenido, nada más. Cada carpeta de `skills/` es una skill de agente independiente; `agents/` contiene un orquestador y cinco subagentes.

---

## Arquitectura

### Sistema de dos capas

**Skills** (`skills/<name>/SKILL.md`) — independientes e invocables por el usuario. Cada una lleva `name` y `description` en el frontmatter. Algunas traen una subcarpeta `references/` con material de apoyo que la skill lee en tiempo de ejecución.

**Agentes** (`agents/<name>.md`) — orquestador + subagentes. El frontmatter incluye `name`, `description`, `tools`, `model` y, opcionalmente, `color`.

- `hormozi-orchestrator` es el punto de entrada. Entrevista al usuario, detecta la etapa del embudo (A–E), arma un brief estructurado y delega en los subagentes en orden de dependencia.
- Los cinco agentes `sub-*` son internos: solo reciben briefs del orquestador y nunca entrevistan al usuario directamente.

### Orden de dependencia de los subagentes

```
sub-market → sub-offer → sub-value → sub-pricing → sub-sales
```

`sub-value` y `sub-pricing` pueden correr en paralelo cuando ya existe una oferta, lo que acorta la cadena a `sub-market → sub-offer → (sub-value ∥ sub-pricing) → sub-sales`.

### Salida

Todos los documentos generados se escriben en `output/`. El orquestador produce un `output/SUMMARY.md` final cuando terminan todos los subagentes. La carpeta `output/` se publica vacía (`.gitkeep`).

---

## Convención de estructura de una skill

Cada skill vive en `skills/<name>/SKILL.md`. Si necesita material de referencia, va en `skills/<name>/references/`. Ningún otro archivo pertenece dentro de la carpeta de una skill.

Cada agente vive en `agents/<name>.md`: plano, sin subcarpetas.

---

## Cómo agregar una skill nueva

1. Crea `skills/<skill-name>/SKILL.md` con `name` y `description` en el frontmatter.
2. Si necesita documentos de referencia, agrégalos en `skills/<skill-name>/references/`.
3. Agrégala a la tabla de skills del `README.md`.

## Cómo agregar un subagente nuevo

1. Crea `agents/sub-<name>.md` con `name`, `description`, `tools` y `model` en el frontmatter.
2. Márcalo como interno en la descripción: "Subagente interno. Solo lo llama hormozi-orchestrator."
3. Define sus archivos de salida dentro de `output/`.
4. Conéctalo al mapa de etapas de la Fase 3 y a la lógica de delegación de la Fase 4 del orquestador.
5. Agrégalo a la tabla de agentes del `README.md`.

---

## Reglas de diseño clave

- Los subagentes reciben un brief completamente estructurado: no tienen memoria de la conversación.
- Toda la salida cae en `output/`, relativo a la raíz del repo.
- Las skills son de cara al usuario; los subagentes son unidades de ejecución internas. No mezcles los dos roles.
- El `name` del frontmatter es el identificador de invocación: no lo renombres sin actualizar todas las referencias.
- Los nombres de los archivos generados (`OFFER.md`, `PITCH.md`, `PRICING.md`…) son un contrato entre el agente que los produce y el que los consume: no los cambies.
- `_archive/` guarda versiones deprecadas: no las borres ni las edites.
