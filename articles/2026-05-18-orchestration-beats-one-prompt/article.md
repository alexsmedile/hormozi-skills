---
title: "Why \"build me an offer\" is the wrong prompt"
type: launch
date: 2026-05-18
status: draft
---

# Why "build me an offer" is the wrong prompt

Ask a model to build you a business offer and it will. You'll get a competent
page of text — an avatar, a value proposition, a price, a few bullet points of
copy. It reads well. And it's thin in a way that's hard to put your finger on
until you try to sell from it.

The reason isn't the model. It's the prompt. "Build me an offer" asks one pass
of attention to hold the whole job at once: research the market, structure the
offer, engineer the bonuses, anchor the price, pre-empt the objections, write
the hooks, draft the landing page. Each of those is real work that depends on
the one before it. Compressed into a single response, none of them gets done
properly — you get the average of all of them.

## The job doesn't fit in one prompt

A complete offer system isn't one task. It's a pipeline with a dependency order:

```
market research → offer structure → (value engineering ∥ pricing) → sales layer
```

You can't price an offer you haven't structured. You can't write objection-
killing copy before you know what the objections are. You can't pick a hook
without an angle to hook into. When a single prompt tries to produce all of it
in one shot, it has to guess the early stages to get to the later ones — and
every downstream section inherits the guess.

The visible symptom is vagueness. The offer "helps people grow their business."
The price is a round number with no story behind it. The landing page has
sections but no spine. None of that is a writing problem. It's a structure
problem: the work was never broken into the stages it actually has.

## A library that runs the pipeline as a pipeline

**hormozi-skills** is a skill library for coding agents that turns a business
idea into a complete, sellable offer — by treating offer-building as the
multi-stage job it actually is.

One orchestrator, five specialized subagents, seventeen standalone skills. You
describe your business in plain language — a rough idea, an existing offer, a
brain dump, a sales page you're not happy with. The orchestrator interviews you
one question at a time, detects which funnel stage you're in, and delegates to
the subagents in dependency order:

| Subagent | Produces |
|---|---|
| `sub-market` | `MARKET_RESEARCH.md` — validated niche, pain map, demand signals |
| `sub-offer` | `OFFER.md`, `OFFER_ANGLES.md` — Grand Slam Offer + 8 ranked angles |
| `sub-value` | `OFFER_AUDIT.md`, `VALUE_PERCEPTION.md`, `BONUS_STACK.md` |
| `sub-pricing` | `PRICING.md`, `OBJECTIONS.md` — anchored price + belief shifts |
| `sub-sales` | `PITCH.md`, `HOOKS.md`, `LANDING_PAGE.md` |

Eleven files, written to `output/` in one session, plus a `SUMMARY.md` with the
one-paragraph offer, the key decisions, the top three actions, and the best hook
to use today.

The method behind the stages is borrowed — Alex Hormozi's offer frameworks
gave the pipeline its shape and its vocabulary. But the point of this library
isn't the frameworks. It's that a method with a definite order should be *run*
in that order, by a system built for it, instead of flattened into one request.

## Why the subagents matter

The split isn't organizational tidiness. It's what makes each stage good.

Every subagent receives a fully structured brief and has no memory of the
conversation — it sees only its inputs and its job. `sub-pricing` gets the
finished offer and nothing else; it spends its entire attention on the price,
the tiers, the justification story. `sub-sales` gets the offer and the
objections already mapped, so its hooks hook into something real instead of
something invented.

That's the difference from one prompt. A single pass divides its attention
across seven jobs. Seven focused passes, each handed exactly what the stage
before it produced, do each job with the whole model behind it. The
orchestrator also detects your stage — raw idea, broken offer, missing sales
layer, service business to productize — and runs only the subagents you
actually need, so a working offer that just needs hooks doesn't get re-researched
from scratch.

## Skills work standalone, too

The pipeline is the headline, but you don't have to run the whole thing. All
seventeen skills are user-invocable on their own. `audit-offer` scores and
rewrites an offer you already have. `pricing-strategy` does the price anchoring
in isolation. `landing-page-copy` takes an existing offer and writes the page.
Each works with no prior context — useful when you don't need the orchestrator,
just one stage of it.

## Why it matters

The failure mode this fixes is specific: an offer that reads fine and converts
badly, because it was generated as one undifferentiated blob instead of built
stage by stage. You don't notice the missing structure until the offer is in
front of a buyer and the price has no story, the bonuses don't answer an
objection, and the hook doesn't connect to an angle.

Hormozi's frameworks — the Grand Slam Offer, the value equation, obstacle
reversal, bonus engineering, price anchoring, hook architecture — are a method
with a definite order. hormozi-skills runs them in that order. It doesn't give
you advice about building an offer. It builds one.

```bash
/plugin marketplace add alexsmedile/hormozi-skills
/plugin install hormozi-skills@hormozi-skills
```
