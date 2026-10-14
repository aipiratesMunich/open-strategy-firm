# cg-03-minimal-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (4/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes the gap (EUR 9m, about 29%) and growth rate (~9%/yr 2026-2029), contrasted with flat history | yes | "31m → 40m by 2029 is +29% in three years, roughly 9%/yr compounding — a sharp break from a trend of zero" |
| Asks short grouped questions, ≤3 rounds, proceeds without waiting if user has no more data | NO | Response frames 5 questions as a hard gate ('Before I can size anything honestly, I need a few answers — guessing at these would just be inventing numbers') and ends by asking permission to proceed ('Want me to run this as a full growth-strategy case?') rather than demonstrating it will proceed on i |
| Produces an issue tree from the gap with momentum/core/adjacencies/portfolio branches, each with hypothesis and kill criterion | NO | No structured issue tree is given; only a loose list of 'two or three levers' (price/mix, wallet share, one new adjacency) with no momentum or portfolio branch and no explicit kill criteria. |
| Keeps inorganic moves out of scope or names them as ruled out by the board | yes | "with no M&A, this almost certainly can't come from 'more of the same, harder.'" |
| States analysis order (momentum case and market vs share split first) | NO | No explicit statement of analysis sequencing is given; question 1 touches market-vs-share but no stated order of momentum case first. |
| Gives a provisional hypothesis explicitly labelled with confidence low and reason | NO | Hypothesis is labelled ('My day-one hypothesis, to be killed or confirmed once I have the above') but no explicit confidence level ('low confidence') is stated anywhere. |
| Open-questions table in skill's format (question, why it matters, who can answer, effect on answer) | NO | Questions are a plain numbered list (1-5) with no table, no 'who can answer' column, and no 'effect on the answer' column. |
| Must not invent textile market growth rates, competitor names, or benchmark figures as facts | yes | No specific invented market growth rate, competitor name, or benchmark figure is stated as fact; only a general heuristic ('usually top out in the low single digits') is offered, not presented as a sourced fact. |
| Must not deliver a generic list of growth frameworks/ideas unconnected to the EUR 9m gap | yes | The proposed levers (price/mix reset, wallet-share recapture, one new adjacency) are explicitly tied to closing 'the gap' rather than presented as a generic framework list. |

## Transcript

## Turn 1

**User:** Pellworth Textiles. Revenue 31m in 2026, flat for years. Board wants 40m by 2029. No M&A. That's all I've got right now, what's your take?

Quick math first: flat revenue for years, then 31m → 40m by 2029 is +29% in three years, roughly 9%/yr compounding — a sharp break from a trend of zero. That gap is the real story here, and it's worth saying plainly: with no M&A, this almost certainly can't come from "more of the same, harder." Before I can size anything honestly, I need a few answers — guessing at these would just be inventing numbers:

1. **Why has it been flat?** Shrinking/flat market with stable share, or a market that's actually growing while Pellworth loses share? Opposite problems, opposite fixes.
2. **Margin floor and capital available.** Is the board open to margin dilution or investment to get to 40m, or must margin hold and capital stay near zero?
3. **What's the book made of?** Rough split of revenue by segment/channel (e.g., private label vs branded, domestic vs export, B2B vs retail) and who the 3-5 largest customers are.
4. **Installed base / wallet share.** Do existing customers buy adjacent things (finishing, logistics, private-label lines) from competitors today?
5. **Has anything already been tried** (price increases, new geographies, new products) and what happened?

My day-one hypothesis, to be killed or confirmed once I have the above: a 9%/yr target from a flat base rarely closes on pricing or share alone — those usually top out in the low single digits for a mature textiles business. The likely shape of an answer is **two or three levers**, not one: (a) a price/mix reset if Pellworth is underpriced versus comparable quality, (b) winning back wallet share in the existing customer base on adjacent services or SKUs, and (c) one genuinely new adjacency (new geography, channel, or a step up the value chain like finished goods instead of fabric) carrying the part the core can't. If the core can't plausibly deliver more than half the gap, that's the moment to tell the board the target itself needs revisiting rather than stretching assumptions to hit 40m on paper.

Want me to run this as a full growth-strategy case — I'd build the gap/momentum case and size each lever with whatever data you can share, flagging anything I can't verify as an assumption?


## Files in work dir after run


