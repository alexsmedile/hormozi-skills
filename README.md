# hormozi-skills

**Turn any business idea into a complete, sellable offer — using Alex Hormozi's frameworks.**

![License](https://img.shields.io/badge/license-MIT-blue)
![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-blueviolet)
![Platform](https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Codex%20%7C%20Cursor-lightgrey)
![Inspired by](https://img.shields.io/badge/inspired%20by-Alex%20Hormozi-orange)

---

> A skill library for coding agents. Plug it in, describe your business, and get a complete offer system — market research, offer structure, pricing, pitch, hooks, landing page — written to files in one session.

---

## The Problem

Building a compelling offer is hard. Most founders, coaches, and consultants either:

- Write vague offers that don't convert — *"I help people grow their business"*
- Price wrong — too low to be taken seriously, too high without justification
- Skip the sales layer entirely — no hooks, no pitch, no landing page copy

**hormozi-skills** solves this end-to-end. One orchestrator, five specialized subagents, 17 skills, 11 output files.

---

## Quick Start

### Claude Code

Add the marketplace, then install the plugin:

```bash
/plugin marketplace add alexsmedile/hormozi-skills
/plugin install hormozi-skills@hormozi-skills
```

Then invoke the `hormozi-orchestrator` agent or a specific skill.

### Codex

Install directly from GitHub:

```bash
codex plugin install https://github.com/alexsmedile/hormozi-skills
```

### Manual Install

If you want the raw skill files instead of the plugin flow:

```bash
# Clone the skill library
git clone https://github.com/alexsmedile/hormozi-skills
cd hormozi-skills

# Copy skills and agents into your Claude config
cp -r skills/ agents/ ~/.claude/
```

> [!TIP]
> Describe your business in plain language — rough idea, brain dump, or existing offer. The orchestrator interviews you, detects your stage, and builds everything from there.

---

## 📦 What You Get

11 output files written to `output/` in one session:

| File | What's Inside |
|------|--------------|
| `MARKET_RESEARCH.md` | Validated niche, pain map, demand signals |
| `OFFER.md` | Full Grand Slam Offer — avatar, obstacles, solution map, value stack |
| `OFFER_ANGLES.md` | 8 positioning angles, ranked |
| `OFFER_AUDIT.md` | Score per dimension + priority fixes |
| `VALUE_PERCEPTION.md` | Improved naming, packaging, framing |
| `BONUS_STACK.md` | Objection-killing bonus structure with perceived value |
| `PRICING.md` | Value-anchored price, tiers, justification story |
| `OBJECTIONS.md` | Hidden beliefs, belief shifts, DM-ready responses |
| `PITCH.md` | Short / medium / long pitch versions |
| `HOOKS.md` | 30+ hooks across 10 types, ranked |
| `LANDING_PAGE.md` | Full landing page copy, section by section |

---

## 🧠 Skills Library

Use any skill standalone — no orchestrator needed:

| Skill | Purpose |
|-------|---------|
| `hormozi-offer` | Build a Grand Slam Offer from scratch → `OFFER.md` |
| `hormozi-pitch` | Pitch deck and sales narrative |
| `hormozi-hooks` | Hook and headline generation (30+ hooks) |
| `audit-offer` | Score and rewrite an existing weak offer |
| `bonus-stack` | Build a bonus stack that kills objections |
| `business-model` | Choose and structure the right business model |
| `dfy-dwy-diy` | Frame offer as DFY / DWY / DIY tiers |
| `effort-reduction` | Reduce perceived effort in the offer |
| `idea-to-product` | Turn rough idea into productized offer |
| `landing-page-copy` | Generate landing page copy from an existing offer |
| `market-research` | Research market pain and demand signals |
| `objection-destroyer` | Map and neutralize common objections |
| `offer-angles` | Generate multiple positioning angles |
| `pricing-strategy` | Price anchoring and packaging |
| `productize` | Productize a service business |
| `value-accelerator` | Increase perceived value |
| `value-perception` | Improve how value is communicated |

> [!TIP]
> Skip the orchestrator and call any skill directly: `/audit-offer`, `/pricing-strategy`, `/landing-page-copy` — each works standalone with no prior context needed.

---

## 🔀 Agent System

```
hormozi-orchestrator
├── sub-market    → MARKET_RESEARCH.md
├── sub-offer     → OFFER.md + OFFER_ANGLES.md
├── sub-value     → OFFER_AUDIT.md + VALUE_PERCEPTION.md + BONUS_STACK.md
├── sub-pricing   → PRICING.md + OBJECTIONS.md
└── sub-sales     → PITCH.md + HOOKS.md + LANDING_PAGE.md
```

**Dependency order:** market → offer → (value ∥ pricing) → sales

The orchestrator detects your funnel stage (idea / broken offer / needs sales layer / service scaling) and runs only the subagents you need.

---

## ⚙️ How It Works

1. **Intake** — give the orchestrator anything: a raw idea, existing offer, brain dump, or sales page
2. **Interview** — focused questions one at a time, each with a suggested answer
3. **Stage detection** — classifies your situation (Stage A–E), shows which subagents will run
4. **Delegation** — spawns subagents in dependency order, passing structured briefs
5. **Summary** — produces `output/SUMMARY.md`: one-paragraph offer, key decisions, top 3 actions, best hook to use today

---

## Repo Structure

```
hormozi-skills/
├── skills/     # 17 standalone agent skills
├── agents/     # Orchestrator + 5 subagents
├── output/     # Generated offer documents (starts empty)
└── input/      # Drop existing offers, notes, or sales pages here
```

---

## Who This Is For

- Founders, coaches, consultants, and freelancers building offers
- Anyone applying Hormozi's methodology who wants AI execution, not just AI advice
- Coding agents running offer-generation pipelines

## Who This Is Not For

- Generic copywriters looking for fill-in-the-blank templates — this thinks, it doesn't just fill
- Developers needing a code library — this is prompt-based, agent-native
- People who want a one-shot answer without iteration — the orchestrator interviews you

---

## Frameworks

Built on Alex Hormozi's offer methodology from *$100M Offers* and *$100M Leads*:

- Grand Slam Offer construction
- Dream outcome × likelihood × time delay × effort equation
- Obstacle → solution reversal
- Value stack and bonus engineering
- Guarantee design (unconditional / conditional / effort-based)
- Price anchoring and perceived value
- Hook architecture (pattern interrupt, identity, outcome, curiosity)

---

## Credits

Inspired by Alex Hormozi's work. Built for coding agents by [@alexsmedile](https://github.com/alexsmedile).
