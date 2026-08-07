---
name: create-plugin
description: Esta skill se debe usar cuando el usuario pide "crear un plugin", "hacer un plugin de GitHub", "convertir mi repo en un plugin", "crear un plugin de Claude Code", "crear un plugin de Codex", "publicar mis skills como plugin" o "montar un marketplace de plugins". Genera la estructura completa de archivos de un repo que funciona a la vez como plugin de Claude Code y de Codex, con soporte de marketplace.
---

# Skill: Creador de plugins (Claude Code + Codex)

## Propósito

Genera el andamiaje de un repo de GitHub que funciona como plugin de Claude Code y de Codex a la vez. Entrega el contenido de cada archivo listo para copiar y los comandos git de todos los archivos requeridos.

---

## Paso 1: reunir las entradas

Hazle estas preguntas al usuario (todas juntas):

1. **Nombre del repo** — en kebab-case (ej. `my-skills`)
2. **Usuario u organización de GitHub** — (ej. `alexsmedile`)
3. **Descripción del plugin** — una frase
4. **Nombre del autor**
5. **¿Qué contiene este plugin?** — marca todo lo que aplique:
   - Skills (`skills/`)
   - Agentes (`agents/`)
   - Hooks (`hooks/hooks.json`)
   - Servidores MCP (`.mcp.json`)
6. **Licencia** — por defecto: `MIT`

No avances hasta tener al menos: nombre del repo, usuario de GitHub, descripción y nombre del autor.

---

## Paso 2: generar la estructura de archivos

Muestra el árbol de directorios completo según lo que haya elegido y después entrega el contenido de cada archivo listo para copiar.

### Archivos siempre requeridos

#### `.claude-plugin/plugin.json`

```json
{
  "name": "{{repo-name}}",
  "version": "1.0.0",
  "description": "{{description}}",
  "author": {
    "name": "{{author}}"
  },
  "homepage": "https://github.com/{{username}}/{{repo-name}}",
  "repository": "https://github.com/{{username}}/{{repo-name}}",
  "license": "{{license}}",
  "keywords": []
}
```

> Las skills y los agentes de `skills/` y `agents/` se autodetectan — no hace falta indicar rutas en `plugin.json`.

#### `.claude-plugin/marketplace.json`

```json
{
  "name": "{{repo-name}}",
  "owner": {
    "name": "{{author}}"
  },
  "metadata": {
    "description": "{{description}}",
    "version": "1.0.0"
  },
  "plugins": [
    {
      "name": "{{repo-name}}",
      "source": "./",
      "description": "{{description}}",
      "version": "1.0.0",
      "author": {
        "name": "{{author}}"
      },
      "homepage": "https://github.com/{{username}}/{{repo-name}}",
      "repository": "https://github.com/{{username}}/{{repo-name}}",
      "license": "{{license}}",
      "category": "productivity"
    }
  ]
}
```

#### `.codex-plugin/plugin.json`

```json
{
  "name": "{{repo-name}}",
  "version": "1.0.0",
  "description": "{{description}}",
  "author": {
    "name": "{{author}}"
  },
  "homepage": "https://github.com/{{username}}/{{repo-name}}",
  "repository": "https://github.com/{{username}}/{{repo-name}}",
  "license": "{{license}}",
  "skills": "./skills/"
}
```

#### `.codex-plugin/marketplace.json`

```json
{
  "name": "{{repo-name}}",
  "interface": {
    "displayName": "{{repo-name}}"
  },
  "plugins": [
    {
      "name": "{{repo-name}}",
      "source": {
        "source": "local",
        "path": "./"
      },
      "category": "Productivity"
    }
  ]
}
```

#### `.gitignore`

```
.DS_Store
**/.DS_Store
output/*
!output/.gitkeep
```

#### `output/.gitkeep`

Archivo vacío — mantiene la carpeta `output/` bajo seguimiento de git.

---

### Si se eligieron skills: `skills/example-skill/SKILL.md`

```markdown
---
name: example-skill
description: Reemplaza esta descripción con frases disparadoras específicas. Úsala cuando el usuario pida "..."
---

# Skill: Ejemplo

Describe qué hace esta skill y cómo se usa.
```

> Renombra `example-skill/` con el nombre real de tu skill. La skill se invoca como `/{{repo-name}}:example-skill`.

---

### Si se eligieron agentes: `agents/example-agent.md`

```markdown
---
name: example-agent
description: Reemplaza esto con lo que hace este agente y cuándo invocarlo.
tools: Read, Write, Bash
model: sonnet
---

# Agente: Ejemplo

Describe acá el rol, la especialidad y el comportamiento del agente.
```

> Renómbralo con el nombre real de tu agente.

---

### Si se eligieron hooks: `hooks/hooks.json`

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'File changed'"
          }
        ]
      }
    ]
  }
}
```

---

### Si se eligieron servidores MCP: `.mcp.json`

```json
{
  "mcpServers": {
    "example-server": {
      "command": "${CLAUDE_PLUGIN_ROOT}/bin/server",
      "args": []
    }
  }
}
```

---

## Paso 3: reglas críticas

Enúncialas con claridad antes de que el usuario cree ningún archivo:

| Regla | Detalle |
|------|--------|
| `skills/` y `agents/` en la **raíz del repo** | Nunca dentro de `.claude-plugin/` ni de `.codex-plugin/` |
| Nombre del plugin = namespace de las skills | Plugin `foo` → las skills corren como `/foo:skill-name` |
| `plugin.json` funciona por autodetección | No hace falta listar las rutas `skills` ni `agents`, salvo que uses ubicaciones personalizadas |
| NO agregues `skills`/`agents` a `marketplace.json` | Provoca un error de validación de esquema con el `strict: true` por defecto |
| `source: "./"` en marketplace.json | Apunta a la raíz del repo — es lo correcto para repos de un solo plugin |

---

## Paso 4: configuración de git + comandos de instalación

Entrega esto exactamente igual, sustituyendo los valores del usuario:

```bash
# Create repo (if not exists)
gh repo create {{username}}/{{repo-name}} --public

# Init and push
git init
git add .
git commit -m "feat: initial plugin scaffold"
git remote add origin https://github.com/{{username}}/{{repo-name}}.git
git push -u origin main
```

**Instalar en Claude Code:**
```
/plugin marketplace add {{username}}/{{repo-name}}
/plugin install {{repo-name}}@{{repo-name}}
```

**Recargar después de los cambios:**
```
/reload-plugins
```

**Probar en local sin instalar:**
```bash
claude --plugin-dir ./
```

---

## Paso 5: después de instalar

Las skills llevan namespace: `/{{repo-name}}:skill-name`  
Los agentes aparecen en `/agents`

Para actualizar: publica en GitHub y después `/plugin marketplace update {{repo-name}}`

Sube la `version` en `plugin.json` y `marketplace.json` en cada release — Claude Code usa la versión para detectar actualizaciones.
