# cg-03-minimal-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (3/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes the gap (EUR 9m, about 29%) and required growth rate (about 9% a year 2026-2029), contrasted with flat history | NO | '~29% total, roughly 6-7% CAGR' — the 29% is right but 6-7% is substantively wrong vs the correct ~8.9%/yr, and EUR 9m figure is never stated |
| Asks a short, grouped set of questions (revenue breakdown, margin floor, capital, decision-makers, market vs share), no more than ~3 rounds, proceeds without waiting if no more data | NO | No structured question set is asked; the assistant only asks whether to run the full process or give a fast take |
| Produces an issue tree from the gap with momentum/core/adjacencies/portfolio branches, each with hypothesis and kill criterion | NO | No issue tree appears anywhere in the transcript |
| Keeps inorganic moves out of scope or names them as ruled out by the board | yes | 'M&A ruled out means it's organic growth only (pricing, new products, new channels/geographies, share gain)' |
| States the analysis order (momentum case and market vs share split first) | NO | No explicit analysis order is given; only a general note to find out 'why it's been flat' before picking a lever |
| Gives a provisional answer/most likely shape of the answer, explicitly labelled as hypotheses with low confidence and reason | NO | No labelled hypothesis or confidence level is given — only a vague 'something structural has to change' |
| Open-questions table in skill's format (question, why it matters, who can answer, effect on answer) | NO | No table of any kind appears in the transcript |
| Must not invent textile market growth rates, competitor names, or benchmark figures as facts | yes | No invented market/competitor/benchmark figures appear |
| Must not deliver a generic list of growth frameworks or ideas unconnected to the EUR 9m gap | yes | Response stays tied to the 31m→40m gap rather than listing generic frameworks |

## Transcript

## Turn 1

**User:** Pellworth Textiles. Revenue 31m in 2026, flat for years. Board wants 40m by 2029. No M&A. That's all I've got right now, what's your take?

This is exactly the kind of growth-strategy question the strategy-engagement skill is built for — flat revenue with a hard board target and M&A ruled out means it's organic growth only (pricing, new products, new channels/geographies, share gain), and I'd want to sharpen the brief before guessing at levers.

Quick gut take: 31m→40m by 2029 is ~29% total, roughly 6-7% CAGR, off a base that's been flat for years — so something structural has to change (not just "sell harder"). The honest first move is figuring out *why* it's been flat (lost share, shrinking end-market, pricing stuck, capacity-constrained) before picking a growth lever, since the fix differs a lot by cause.

Want me to run the full strategy-engagement process on this (problem statement → issue tree → hypotheses → research → recommendation), or do you just want a fast take on likely levers right now?


## Files in work dir after run


