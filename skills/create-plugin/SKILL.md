---
name: create-plugin
description: This skill should be used when the user asks to "create a plugin", "make a GitHub plugin", "turn my repo into a plugin", "create a Claude Code plugin", "create a Codex plugin", "publish my skills as a plugin", or "set up a plugin marketplace". Scaffolds the complete file structure for a repo that works as both a Claude Code and Codex plugin with marketplace support.
---

# Skill: Plugin Creator (Claude Code + Codex)

## Purpose

Scaffold a GitHub repo that works as a plugin for both Claude Code and Codex simultaneously. Outputs ready-to-copy file contents and git commands for every required file.

---

## Step 1: Gather Inputs

Ask the user these questions (all at once):

1. **Repo name** — kebab-case (e.g. `my-skills`)
2. **GitHub username or org** — (e.g. `alexsmedile`)
3. **Plugin description** — one sentence
4. **Author name**
5. **What does this plugin contain?** — pick all that apply:
   - Skills (`skills/`)
   - Agents (`agents/`)
   - Hooks (`hooks/hooks.json`)
   - MCP servers (`.mcp.json`)
6. **License** — default: `MIT`

Do not proceed until you have at least: repo name, GitHub username, description, and author name.

---

## Step 2: Generate File Structure

Show the full directory tree based on their selections, then output every file's content ready to copy.

### Always-required files

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

> Skills and agents in `skills/` and `agents/` are auto-discovered — no paths needed in `plugin.json`.

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

Empty file — keeps the `output/` folder tracked by git.

---

### If skills selected: `skills/example-skill/SKILL.md`

```markdown
---
name: example-skill
description: Replace this description with specific trigger phrases. Use when the user asks to "..."
---

# Skill: Example

Describe what this skill does and how to use it.
```

> Rename `example-skill/` to your actual skill name. Skill is invoked as `/{{repo-name}}:example-skill`.

---

### If agents selected: `agents/example-agent.md`

```markdown
---
name: example-agent
description: Replace with what this agent does and when to invoke it.
tools: Read, Write, Bash
model: sonnet
---

# Agent: Example

Describe the agent's role, expertise, and behavior here.
```

> Rename to your actual agent name.

---

### If hooks selected: `hooks/hooks.json`

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

### If MCP servers selected: `.mcp.json`

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

## Step 3: Critical Rules

State these clearly before the user creates any files:

| Rule | Detail |
|------|--------|
| `skills/` and `agents/` at **repo root** | Never inside `.claude-plugin/` or `.codex-plugin/` |
| Plugin name = skill namespace | Plugin `foo` → skills run as `/foo:skill-name` |
| `plugin.json` is auto-discovery | No need to list `skills` or `agents` paths unless using custom locations |
| Do NOT add `skills`/`agents` to `marketplace.json` | Causes schema validation error with default `strict: true` |
| `source: "./"` in marketplace.json | Points at repo root — correct for single-plugin repos |

---

## Step 4: Git Setup + Install Commands

Output these exactly, substituting the user's values:

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

**Install in Claude Code:**
```
/plugin marketplace add {{username}}/{{repo-name}}
/plugin install {{repo-name}}@{{repo-name}}
```

**Reload after changes:**
```
/reload-plugins
```

**Test locally without installing:**
```bash
claude --plugin-dir ./
```

---

## Step 5: After Install

Skills are namespaced: `/{{repo-name}}:skill-name`  
Agents appear in `/agents`

To update: push to GitHub, then `/plugin marketplace update {{repo-name}}`

Bump `version` in `plugin.json` and `marketplace.json` with each release — Claude Code uses version to detect updates.
