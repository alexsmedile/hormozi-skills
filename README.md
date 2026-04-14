# hormozi-skills

Coding agent skill library for building Hormozi-inspired offer systems.

Converts raw business ideas into structured, actionable offer documents using a multi-agent pipeline.

---

## Structure

```
hormozi-skills/
├── skills/          # Individual agent skills
├── agents/          # Orchestrator + subagents
├── output/          # Generated offer documents (OFFER.md, etc.)
└── .claude/         # Agent config (memory, settings)
```

---

## Quick Start

Copy `skills/` and `agents/` into your coding agent's config folder (e.g. `.claude/` for Claude Code, or equivalent for your tool), then invoke any skill or the orchestrator directly.

```bash
cp -r skills/ agents/ .claude/
```

Start with the orchestrator for a full offer build, or call any skill individually for a focused task.

---

## Skills

| Skill | Purpose |
|-------|---------|
| `hormozi-offer` | Full Grand Slam Offer builder → `OFFER.md` |
| `hormozi-pitch` | Pitch deck and sales narrative |
| `hormozi-hooks` | Hook and headline generation |
| `audit-offer` | Audit and rewrite existing offer |
| `bonus-stack` | Build bonus stack with perceived value |
| `business-model` | Choose and structure business model |
| `dfy-dwy-diy` | Frame offer as DFY / DWY / DIY tiers |
| `effort-reduction` | Reduce perceived effort in offer |
| `idea-to-product` | Turn rough idea into productized offer |
| `landing-page-copy` | Generate landing page copy from offer |
| `market-research` | Research market, pain, and demand signals |
| `objection-destroyer` | Map and neutralize common objections |
| `offer-angles` | Generate multiple positioning angles |
| `pricing-strategy` | Price anchoring and packaging strategy |
| `productize` | Productize a service |
| `value-accelerator` | Increase perceived value of an offer |
| `value-perception` | Improve how value is communicated |

---

## Agents

| Agent | Role |
|-------|------|
| `hormozi-orchestrator` | Master orchestrator — intake, interview, route to subagents |
| `sub-market` | Market and avatar research |
| `sub-offer` | Offer structure and value stack |
| `sub-pricing` | Pricing, packaging, guarantee |
| `sub-sales` | Sales copy and messaging |
| `sub-value` | Value perception and positioning |

---

## Usage

### Run orchestrator

Start from any business idea, notes, or existing offer:

```
/hormozi-orchestrator
```

The orchestrator interviews you, routes to subagents, and writes final documents to `output/`.

### Run individual skill

```
/hormozi-offer
/audit-offer
/landing-page-copy
```

---

## Output

Generated files land in `output/`. Typical outputs:

- `OFFER.md` — full offer document
- `PITCH.md` — sales narrative
- `HOOKS.md` — headline and hook library
- `LANDING.md` — landing page copy

---

## Frameworks

Built on Alex Hormozi's offer methodology from *$100M Offers* and *$100M Leads*:

- Grand Slam Offer construction
- Dream outcome mapping
- Obstacle → solution reversal
- Value stack and bonus engineering
- Guarantee design
- Pricing psychology
