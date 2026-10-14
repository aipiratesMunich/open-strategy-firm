# em-01-vague-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Does not start any analysis, market research or recommendation before the problem statement is agreed | yes | Turn 1 contains only clarifying questions; turn 2 produces the problem statement itself with no market analysis or recommendation. |
| Asks for the decision, the decision maker, a measurable target with a date, and constraints (grouped, ≤3 rounds) | yes | Turn 1 single round asks for target/timeline, what's ruled out (constraints), 'who decides and when...specific meeting or budget cycle' (decision/decision maker). |
| Produces a problem statement as one question naming decision maker, measurable outcome, date and constraints | yes | "What combination of growth moves should the Board fund in the November 2026 2027 investment budget to grow revenue from ~EUR 60m to EUR 80m by 2031, within an EUR 3m capital envelope and without store-level margin falling below 14%..." |
| Lists at least one item explicitly out of scope | yes | "Out of scope / Acquisitions; geographic expansion outside the home region" |
| Asks the user to confirm the problem statement | yes | "Do you agree with this problem statement? Reply yes, or correct it..." |
| Writes engagement/<slug>/01-problem-statement.md | yes | File written: engagement/bakery-co/01-problem-statement.md |
| Does not invent market data or competitor facts | yes | Assistant explicitly flags unknowns ('Flagged assumptions to verify') rather than inventing figures like margin baseline, trend data, or competitor info. |
| Does not produce a generic list of frameworks | yes | Output is a problem statement table, not a framework list. |

## Transcript

## Turn 1

**User:** We're a bakery chain, about 60 million in revenue, 41 stores. Growth has stalled. We want to grow. Can you help us figure out what to do?

This is a growth-strategy case. Before I structure anything, I need to sharpen the question — right now "we want to grow" is an ambition, not a decision I can build an issue tree around.

A few questions to get us to a sharp problem statement:

1. **Target and timeline** — Is there a specific revenue/profit target and year (e.g., board-set, investor-driven), or should we work from "meaningfully reaccelerate growth" over a horizon you pick (e.g., 3 years)? What's driving the need to grow now — new investor, succession, lease renewals, competitive pressure?
2. **What's "stalled," precisely** — Flat total revenue, or flat/declining same-store sales offset by unit growth (or vice versa)? Roughly how has revenue moved over the last 2–3 years, and how has store count changed in that time?
3. **What's already ruled out or fixed** — Is new-unit expansion, franchising, M&A (buying competitors), or taking on outside capital off the table? Any constraints on capital available, or a margin floor you won't go below?
4. **Who decides and when** — Is this you, a founder/owner group, or a board, and is there a specific meeting or budget cycle this needs to feed into?
5. **Format/channel today** — Are all 41 stores the same format (retail bakery-café), one geography, mostly company-owned vs. franchised, and is wholesale/B2B (grocery, restaurants) already part of the mix or nonexistent?

You don't need to answer all five in detail — even rough numbers and "no hard constraint, just don't blow up margin" is enough for me to write a first problem statement.


## Turn 2

**User:** Answers to your questions:
- Decision: the board sets the 2027 investment budget in November 2026.
- Decision maker: the board, prepared by the CEO.
- Target: EUR 80m revenue by 2031.
- Guardrail: store-level margin must stay above 14%.
- Capital available: about EUR 3m.
- Options people talk about: more stores, online delivery, office catering, franchising.
- Out of scope: acquisitions, leaving the home region.

# Problem statement: Bakery Co

**Question:** What combination of growth moves should the Board fund in the November 2026 2027 investment budget to grow revenue from ~EUR 60m to EUR 80m by 2031, within an EUR 3m capital envelope and without store-level margin falling below 14%, given that acquisitions and expansion outside the home region are ruled out?

| Element | Content |
|---|---|
| Decision | Which growth moves (candidates on the table: more company stores, online delivery, office catering, franchising) to fund in the 2027 investment budget, and in what mix/sequence |
| Decision maker | The Board; prepared and proposed by the CEO |
| Success criteria | EUR 80m revenue by FY2031 (from ~EUR 60m today) |
| Guardrails | Store-level margin must not fall below 14% |
| In scope | Core/same-store performance; new company stores; franchising; online delivery; office catering/B2B; pricing — all within the home region |
| Out of scope | Acquisitions; expansion outside the home region |
| Constraints | ~EUR 3m capital; decision ready for Nov 2026 Board meeting; 41 existing stores as base |
| Decision date | November 2026 |

**Flagged assumptions to verify (I don't have these yet):**
1. Where the EUR 80m / 2031 target came from (board ambition vs. investor/lender covenant vs. succession plan) — affects how much flex there is if the gap doesn't close organically.
2. The actual "stalled" baseline: revenue trend and same-store-sales trend over the last 2–3 years, separate from store-count changes.
3. Current store-level margin — is 14% already tight, or is there headroom to invest?
4. Whether franchising exists today in any form.
5. Whether EUR 3m is a one-year (2027) figure or recurs annually through 2031.
6. How much "home region" whitespace is left for new company stores.

Do you agree with this problem statement? Reply yes, or correct it — and if you have rough numbers on assumptions 2–6, that'll let me size the gap properly in the next step.


## Files in work dir after run

- engagement/bakery-co/01-problem-statement.md

## File written by the run: engagement/bakery-co/01-problem-statement.md

# Problem statement: Bakery Co (41-store chain, ~EUR 60m revenue)

**Question:** What combination of growth moves should the Board fund in the November 2026 2027 investment budget to grow revenue from ~EUR 60m to EUR 80m by 2031, within an EUR 3m capital envelope and without store-level margin falling below 14%, given that acquisitions and expansion outside the home region are ruled out?

| Element | Content |
|---|---|
| Decision | Which growth moves (candidates on the table: more company stores, online delivery, office catering, franchising) to fund in the 2027 investment budget, and in what mix/sequence |
| Decision maker | The Board; prepared and proposed by the CEO. No other blocker named. |
| Success criteria | EUR 80m revenue by FY2031 (from ~EUR 60m today) |
| Guardrails | Store-level margin must not fall below 14% |
| In scope | Same-store/core performance; new company-owned stores; franchising; online delivery; office catering/B2B; pricing; within the home region |
| Out of scope | Acquisitions; geographic expansion outside the home region |
| Constraints | ~EUR 3m capital available; decision must be ready for the Board's November 2026 budget meeting; 41 existing stores as the current base |
| Decision date | November 2026 (Board sets the 2027 investment budget) |

**Why this matters now:** Growth has stalled and the Board is about to commit 2027 capital; a flagged assumption below is the deeper "why" (investor, succession, or competitive pressure) since it hasn't been stated yet.

**Flagged assumptions to verify:**
1. The EUR 80m-by-2031 target's origin and rationale (board ambition, investor/lender covenant, succession plan, competitive benchmark) is not yet known — matters for how hard the guardrails can flex if the gap can't be closed organically.
2. "Stalled growth" baseline is not yet quantified: current YoY revenue trend, same-store sales trend vs. store-count trend over the last 2–3 years.
3. Current store-level margin today (is it already near the 14% floor, or is there headroom?).
4. Whether franchising already exists in any form today, or would be entirely new.
5. Whether the EUR 3m capital is a one-year (2027) figure only, or indicative of each year's budget through 2031.
6. Definition of "home region" (which geography/market, and whether any whitespace remains within it for new stores).

**Agreed by:** pending user confirmation

