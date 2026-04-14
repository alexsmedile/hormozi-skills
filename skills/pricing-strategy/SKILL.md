---
name: pricing-strategy
description: Set the right price anchored to value, not guesswork. Use when pricing feels random, conversions are low due to price resistance, or you want to introduce tiers. Analyzes outcome value, delivery model, and market expectations to produce pricing range, strategy, tiers, psychological pricing, and a price justification story — outputs PRICING.md.
---

# Skill: Pricing Strategy (Value Anchoring Engine)

## Purpose
Set the right price based on value, not guesswork.

This skill ensures the price:
- reflects the outcome
- feels justified to the buyer
- matches the delivery model
- maximizes conversions and revenue

It improves:
- perceived value
- positioning
- profitability

---

## When to Use
Activate this skill when:
- pricing feels random or uncertain
- conversions are low due to price resistance
- the offer feels “too cheap” or “too expensive”
- you want to introduce tiers
- you’re launching a new offer
- you need a clear pricing story

---

## Inputs
This skill works with:
- an `OFFER.md`
- a product or service description
- value stack
- delivery model (DFY, DWY, DIY)
- target audience

---

## Core Outcome
The assistant produces:
- a price anchored to value
- pricing tier structure (if needed)
- price positioning strategy
- psychological pricing suggestions
- a clear price justification story

---

## Assistant Behavior

### 1. Understand the value
Extract:
- the core outcome
- how much that outcome is worth
- urgency of the problem
- financial or emotional impact

Then summarize:

> This offer helps X achieve Y, which is worth Z in terms of time, money, or status.

---

### 2. Analyze the delivery model
Identify:
- DIY → lower price, volume-based
- DWY → mid-tier pricing
- DFY → premium pricing

Then assess:
- level of support
- level of customization
- level of effort saved

---

### 3. Anchor price to outcome
Estimate value based on:
- money gained
- time saved
- pain avoided
- opportunity unlocked

Frame it like:

> If this helps achieve X, then even a fraction of that value justifies the price.

---

### 4. Define pricing range
Create a realistic range based on:
- market expectations
- delivery model
- complexity
- competition (if known)

Output:
- low-end price
- mid-range price
- premium price

---

### 5. Choose pricing strategy

Select one:

#### Volume (Low-Ticket)
- low price
- high volume
- simple delivery
- fast decision

#### Margin (High-Ticket)
- high price
- lower volume
- high support
- strong transformation

#### Hybrid
- entry offer + core offer + premium

Explain tradeoffs:
- speed vs profit
- scale vs depth
- simplicity vs customization

---

### 6. Build pricing tiers (if needed)

Structure:

- Tier 1: Entry (DIY)
- Tier 2: Core (DWY)
- Tier 3: Premium (DFY)

For each:
- what’s included
- who it’s for
- price point
- value difference

---

### 7. Apply psychological pricing

Suggest:
- price anchoring (show higher value first)
- charm pricing (e.g. 27, 97, 297)
- round pricing for premium (e.g. 1000+)
- tier contrast (clear jumps in value)

Explain:
- why this pricing feels right
- how it influences perception

---

### 8. Build the price justification story

Create a simple narrative:

Structure:
1. Restate the outcome
2. Show what it’s worth
3. Compare to alternatives
4. Anchor total value stack
5. Reveal price as “small” relative to value

Example:
> If this helps you get X, which is worth Y, then paying Z is a small step.

---

### 9. Stress test the price

Check:
- does it feel cheap (low trust)?
- does it feel expensive (low clarity)?
- does it match the outcome?
- does it match the audience’s ability to pay?

Adjust if needed.

---

### 10. Suggest pricing experiments

Recommend:
- A/B testing price points
- introducing payment plans
- testing discounts vs bonuses
- early-bird pricing

---

## Output Format

```md
# PRICING.md

## 1. Value Analysis
- Outcome
- Why it matters
- Estimated value

## 2. Delivery Model Impact
- Model (DIY, DWY, DFY)
- Pricing implications

## 3. Pricing Range
- Low price
- Mid price
- High price

## 4. Recommended Pricing Strategy
- Strategy type
- Reasoning

## 5. Pricing Tiers (if applicable)

### Tier 1
- Name
- What’s included
- Price

### Tier 2
- Name
- What’s included
- Price

### Tier 3
- Name
- What’s included
- Price

## 6. Psychological Pricing
- Techniques used
- Why they work

## 7. Price Justification Story
- Narrative

## 8. Risk Check
- Potential issues
- Adjustments

## 9. Pricing Experiments
- Tests to run
```


⸻

Decision Rules

Price higher when:
	•	outcome is valuable
	•	effort is low for the customer
	•	speed is high
	•	delivery includes DFY elements

Price lower when:
	•	outcome is uncertain
	•	delivery is DIY
	•	trust is low
	•	market is price-sensitive

Use tiers when:
	•	audience has different budgets
	•	multiple delivery levels exist
	•	upsell potential is strong

Avoid underpricing when:
	•	it reduces trust
	•	it signals low value
	•	it attracts the wrong audience

⸻

Before vs After Example

Before
	•	Random price: $49

After
	•	Value stack: $500+
	•	Anchored price: $97
	•	Justified by outcome and speed

⸻

Style Guidelines
	•	tie price to outcome, not features
	•	keep explanation simple
	•	avoid overcomplication
	•	make price feel logical
	•	make decision easy

⸻

Success Criteria

The skill works when:
	•	price feels fair and justified
	•	value clearly exceeds price
	•	buyers hesitate less
	•	positioning improves
	•	revenue increases