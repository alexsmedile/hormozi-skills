# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## First Run: Installation

On first use, ask the user where to install the skills and agents:

> "Where should I install hormozi-skills?
> - **Project** (default) — `.claude/` in the current project folder. Only available in this project.
> - **User** — `~/.claude/` in your home directory. Available in all projects.
> - **Local** — `.claude.local/` in the current project folder. Not committed to git.
>
> Press Enter to use the default (project)."

**Default:** project-level (`.claude/` in the current working directory).

Installation copies `skills/` and `agents/` into the chosen `.claude/` directory:

```bash
# Project (default)
cp -r skills/ agents/ .claude/

# User (global)
cp -r skills/ agents/ ~/.claude/

# Local (project, not committed)
cp -r skills/ agents/ .claude.local/
```

> **Important:** After installation, Claude Code must be restarted for the new skills and agents to be available.

---

## What This Is

A skill library for coding agents to build Hormozi-inspired offer systems. No build pipeline — content only. Each `skills/` folder is a standalone agent skill; `agents/` contains an orchestrator and five subagents.

## Architecture

### Two-Layer System

**Skills** (`skills/<name>/SKILL.md`) — standalone, user-invocable. Each has a frontmatter `name` and `description`. Some have a `references/` subfolder with supporting material the skill reads at runtime.

**Agents** (`agents/<name>.md`) — orchestrator + subagents. Frontmatter includes `name`, `description`, `tools`, `model`, and optionally `color`.

- `hormozi-orchestrator` is the entry point. It interviews the user, detects funnel stage (A–E), builds a structured brief, and delegates to subagents in dependency order.
- The five `sub-*` agents are internal — they receive briefs from the orchestrator only and never interview the user directly.

### Subagent Dependency Order

```
sub-market → sub-offer → sub-value → sub-pricing → sub-sales
```

`sub-value` and `sub-pricing` can run in parallel when an offer already exists.

### Output

All generated documents write to `output/`. The orchestrator produces a final `output/SUMMARY.md` after all subagents complete. The `output/` folder ships empty (`.gitkeep`).

## Skill Structure Convention

Every skill lives at `skills/<name>/SKILL.md`. If a skill needs reference material, it goes in `skills/<name>/references/`. No other files belong inside a skill folder.

Every agent lives at `agents/<name>.md` — flat, no subfolders.

## Adding a New Skill

1. Create `skills/<skill-name>/SKILL.md` with frontmatter `name` and `description`.
2. If it needs reference docs, add them to `skills/<skill-name>/references/`.
3. Add it to the skills table in `README.md`.

## Adding a New Subagent

1. Create `agents/sub-<name>.md` with frontmatter `name`, `description`, `tools`, `model`.
2. Mark it internal in the description: "Internal subagent. Called by hormozi-orchestrator only."
3. Define its output file(s) in `output/`.
4. Wire it into the orchestrator's Phase 3 stage map and Phase 4 delegation logic.
5. Add it to the agents table in `README.md`.

## Key Design Rules

- Subagents receive a fully structured brief — they have no memory of the conversation.
- All output lands in `output/` relative to the repo root.
- Skills are user-facing; subagents are internal execution units. Do not mix the two roles.
- `_archive/` holds deprecated versions — do not delete, do not edit.
