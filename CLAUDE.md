# CLAUDE.md

Este archivo le da a Claude Code (claude.ai/code) la guía para trabajar con el código de este repositorio.

## Primera ejecución: instalación

En el primer uso, pregúntale al usuario dónde instalar las skills y los agentes:

> "¿Dónde instalo hormozi-skills-es?
> - **Proyecto** (por defecto) — `.claude/` en la carpeta del proyecto actual. Solo disponible en este proyecto.
> - **Usuario** — `~/.claude/` en tu carpeta personal. Disponible en todos los proyectos.
>
> Presiona Enter para usar la opción por defecto (proyecto)."

**Por defecto:** a nivel de proyecto (`.claude/` en el directorio de trabajo actual).

La instalación copia `skills/` y `agents/` dentro del directorio `.claude/` elegido:

```bash
# Proyecto (por defecto)
cp -r skills/ agents/ .claude/

# Usuario (global)
cp -r skills/ agents/ ~/.claude/
```

> **Importante:** después de instalar, hay que reiniciar Claude Code para que las nuevas skills y agentes queden disponibles.

---

## Qué es esto

Una biblioteca de skills para que los agentes de código construyan sistemas de oferta inspirados en Hormozi. Sin pipeline de build — solo contenido. Cada carpeta de `skills/` es una skill de agente independiente; `agents/` contiene un orquestador y cinco subagentes.

## Arquitectura

### Sistema de dos capas

**Skills** (`skills/<name>/SKILL.md`) — independientes, invocables por el usuario. Cada una tiene un `name` y un `description` en el frontmatter. Algunas tienen una subcarpeta `references/` con material de apoyo que la skill lee en tiempo de ejecución.

**Agentes** (`agents/<name>.md`) — orquestador + subagentes. El frontmatter incluye `name`, `description`, `tools`, `model` y, opcionalmente, `color`.

- `hormozi-orchestrator` es el punto de entrada. Entrevista al usuario, detecta la etapa del embudo (A–E), arma un brief estructurado y delega a los subagentes en orden de dependencia.
- Los cinco agentes `sub-*` son internos — solo reciben briefs del orquestador y nunca entrevistan al usuario directamente.

### Orden de dependencia de los subagentes

```
sub-market → sub-offer → sub-value → sub-pricing → sub-sales
```

`sub-value` y `sub-pricing` pueden correr en paralelo cuando ya existe una oferta.

### Salida

Todos los documentos generados se escriben en `output/`. El orquestador produce un `output/SUMMARY.md` final cuando todos los subagentes terminan. La carpeta `output/` se distribuye vacía (`.gitkeep`).

## Convención de estructura de las skills

Cada skill vive en `skills/<name>/SKILL.md`. Si una skill necesita material de referencia, va en `skills/<name>/references/`. Ningún otro archivo debe ir dentro de una carpeta de skill.

Cada agente vive en `agents/<name>.md` — plano, sin subcarpetas.

## Agregar una skill nueva

1. Crea `skills/<skill-name>/SKILL.md` con `name` y `description` en el frontmatter.
2. Si necesita documentos de referencia, agrégalos a `skills/<skill-name>/references/`.
3. Agrégala a la tabla de skills en `README.md`.

## Agregar un subagente nuevo

1. Crea `agents/sub-<name>.md` con `name`, `description`, `tools` y `model` en el frontmatter.
2. Márcalo como interno en la descripción: "Subagente interno. Solo lo llama hormozi-orchestrator."
3. Define su archivo (o archivos) de salida en `output/`.
4. Conéctalo al mapa de etapas de la Fase 3 y a la lógica de delegación de la Fase 4 del orquestador.
5. Agrégalo a la tabla de agentes en `README.md`.

## Reglas clave de diseño

- Los subagentes reciben un brief completamente estructurado — no tienen memoria de la conversación.
- Toda la salida se escribe en `output/`, ruta relativa a la raíz del repo.
- Las skills son para el usuario; los subagentes son unidades de ejecución internas. No mezcles los dos roles.
