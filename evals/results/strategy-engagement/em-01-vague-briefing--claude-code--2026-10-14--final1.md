# em-01-vague-briefing on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (8/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: does not start any analysis, market research or recommendation before the problem statement is agreed. | yes | Turn 1 is purely clarifying questions; Turn 2 only drafts the problem statement and flags open assumptions, without market data or recommendations. |
| Must: asks for the decision, the decision maker, a measurable target with a date, and constraints (questions may be grouped; no more than about three rounds). | yes | Turn 1 Q1 'What revenue (and profit) are you aiming for, by when?', Q4 'Who decides on the growth plan, and is there a specific meeting/deadline?', Q3 capital/margin guardrails — all in a single round. |
| Must: produces a problem statement as one question naming decision maker, measurable outcome, date and constraints. | yes | "Which combination of growth moves should the board fund in the November 2026 budget for 2027, to take revenue from EUR 60m to EUR 80m by 2031, within EUR 3m of capital and without store-level margin falling below 14%, given no acquisitions and no expansion outside the home region?" |
| Must: lists at least one item explicitly out of scope. | yes | "Out of scope: Acquisitions; geographic expansion outside the home region" |
| Must: asks the user to confirm the problem statement. | yes | "Can you confirm the problem statement and answer the capital-horizon and margin-baseline questions?" |
| Must: writes engagement/<slug>/01-problem-statement.md (or prints it under that heading if files cannot be written). | yes | File listed and shown: engagement/bakery-co/01-problem-statement.md |
| Must not: invent market data or competitor facts. | yes | No market/competitor figures appear anywhere in the transcript; only internally-provided financials (revenue, capital, margin) are used. |
| Must not: produce a generic list of frameworks. | yes | No framework list (e.g. Ansoff, Porter's Five Forces, etc.) is presented; output is a problem statement table and targeted assumption questions. |

## Transcript

## Turn 1

**User:** We're a bakery chain, about 60 million in revenue, 41 stores. Growth has stalled. We want to grow. Can you help us figure out what to do?

This is a growth-strategy case. Before I structure anything, I need to sharpen the question — a few things I can't infer from "revenue stalled, want to grow."

**One round of questions:**

1. **Target and timeline** — What revenue (and profit) are you aiming for, by when? Is there a board/investor number already, or should we size an ambition together?
2. **Ruled-out moves** — Is anything off the table (e.g., acquisitions, franchising, taking on outside capital, closing underperforming stores)?
3. **Capital and margin guardrails** — How much can you invest in growth, and is there an EBIT margin floor you can't go below?
4. **Decision maker and date** — Who decides on the growth plan, and is there a specific meeting/deadline (board meeting, budget cycle)?
5. **Diagnosis so far** — Do you believe revenue is flat because your markets/neighborhoods are flat, because you're losing share to competitors, or because the current 41 stores are maturing out (same-store sales flat, no new unit growth)? What's your own read, and why?
6. **Store economics** — Rough split: how much of the $60M is store/retail vs. wholesale/catering/other channels, if any? Is the fleet company-owned, franchised, or mixed?

You don't need to answer all of these precisely — rough numbers and "we haven't ruled anything out" are fine. But I do need a real target/date and whatever's already off the table before I build the issue tree, since that's what tells me whether this is "find $8M of growth in the core" versus "we need a new format or channel."


## Turn 2

**User:** Answers to your questions:
- Decision: the board sets the 2027 investment budget in November 2026.
- Decision maker: the board, prepared by the CEO.
- Target: EUR 80m revenue by 2031.
- Guardrail: store-level margin must stay above 14%.
- Capital available: about EUR 3m.
- Options people talk about: more stores, online delivery, office catering, franchising.
- Out of scope: acquisitions, leaving the home region.

I've framed this as a growth-strategy engagement and written the problem statement. Here's the question I'll be working:

> **Which combination of growth moves should the board fund in the November 2026 budget for 2027, to take revenue from EUR 60m to EUR 80m by 2031, within EUR 3m of capital and without store-level margin falling below 14%, given no acquisitions and no expansion outside the home region?**

That's a EUR 20m (~33%) gap over 5 years, against four named options (new stores, online delivery, office catering, franchising) plus whatever the existing 41 stores can still deliver on their own.

My own quick review flagged two things that matter enough to confirm before I size anything:

1. **Is the EUR 3m the 2027 budget only, or the total capital for the whole plan through 2031?** This changes what's affordable by an order of magnitude — one new store alone can run EUR 0.3–1m+.
2. **What's today's store-level margin?** Without a baseline I can't tell how close any lever (delivery especially, since it usually dilutes margin) gets to breaching the 14% floor.

Smaller ones worth a quick answer too: how much of the EUR 60m is already wholesale/catering vs. pure retail, and does "franchising" mean franchising *new* units (cheap, asset-light) or converting *existing* company-owned stores (frees cash but changes the margin math)?

Full write-up is in `engagement/bakery-co/01-problem-statement.md`. Can you confirm the problem statement and answer the capital-horizon and margin-baseline questions? Once that's settled I'll move to building the issue tree and sizing the levers.


## Files in work dir after run

- engagement/bakery-co/01-problem-statement.md
- engagement/bakery-co/reviews/gate1-problem-statement.md

## File written by the run: engagement/bakery-co/01-problem-statement.md

# Problem statement: Bakery Co (41-store bakery chain, ~EUR 60m revenue)

**Question:** Which combination of growth moves should the board fund in the November 2026 budget for 2027, to take revenue from EUR 60m to EUR 80m by 2031, within EUR 3m of capital and without store-level margin falling below 14%, given no acquisitions and no expansion outside the home region?

| Element | Content |
|---|---|
| Decision | Which growth lever(s) to fund for 2027 onward: new store openings, online delivery, office/corporate catering, franchising, and/or core-performance moves (pricing, mix, same-store sales) in the existing 41 stores |
| Decision maker | The board; prepared and proposed by the CEO |
| Success criteria | EUR 80m revenue by 2031 (from EUR 60m today — a EUR 20m, ~33%, gap over 5 years) |
| Guardrails | Store-level margin must not fall below 14% |
| In scope | The 41 existing stores and their home region/trade area; the four named options (new stores, online delivery, office catering, franchising); core-business moves (price, mix, traffic) in the current footprint |
| Out of scope | Acquisitions; geographic expansion outside the home region |
| Constraints | ~EUR 3m capital available; decision presented to the board November 2026 for the 2027 budget; 14% store-level margin floor |
| Decision date | November 2026 (board budget meeting) |

**Why this matters now:** Growth has stalled at 41 stores and ~EUR 60m revenue, and the board is setting the 2027 investment budget in a month — the plan needs to be ready and fundable within a EUR 3m envelope, not a wish list.

**Flagged assumptions to verify:**
1. **Capital figure:** is the ~EUR 3m a one-year (2027) investment budget, or the total capital available across the whole plan through 2031? This changes what's affordable by an order of magnitude (e.g., one new store can cost EUR 0.3–1m+ depending on format) and needs to be confirmed before sizing any lever.
2. **Today's store-level margin:** no baseline given yet. Need current store-level margin to know how much headroom exists before the 14% floor, and whether any lever (e.g., delivery, which usually dilutes margin) is already close to breaching it.
3. **Revenue split today:** how much of the EUR 60m is in-store retail vs. existing wholesale/catering/other channels, if any — needed to size "office catering" as new vs. incremental to an existing channel.
4. **Store base composition:** of the 41 stores, how many are mature vs. recently opened, and is there a reason like-for-like sales have stalled (local competition, pricing, traffic) that the board already has a view on.
5. **Home region definition:** what geography "home region" covers, and roughly how much further store density it could support (relevant to sizing the "more stores" lever without it meaning new-region expansion).
6. **Franchising intent:** whether "franchising" means franchising out new units (asset-light growth, uses little of the EUR 3m) or converting existing company-owned stores (frees capital but changes margin economics) — these are very different levers.

**Agreed by:** pending — please confirm or correct before I move to structuring the issue tree.


## File written by the run: engagement/bakery-co/reviews/gate1-problem-statement.md

# Partner review: 01-problem-statement.md, 2026-10-14, gate 1

**Verdict:** Release with fixes

**One-line reason:** The question is sharp (decision, decision maker, number, date, constraints) but two constraints that drive sizing (capital horizon, current margin baseline) are unconfirmed and must be closed before lever sizing, not after.

## Findings
| # | Severity | Perspective | Check | Where | Problem | Required fix |
|---|---|---|---|---|---|---|
| 1 | Major | Decision Maker | 2 | Constraints row | EUR 3m could mean "2027 only" or "total through 2031" — a 10x+ swing in what's fundable | Confirm with CEO/board before sizing any lever; flagged as assumption #1 |
| 2 | Major | Evidence Auditor | 11 | Guardrails row | No current store-level margin baseline, so "stay above 14%" can't be tested against any lever yet | Get current margin; flagged as assumption #2 |
| 3 | Minor | Logician | 8 | Decision row | "Franchising" bundles two different economics (new franchised units vs. converting existing stores) | Keep as one hypothesis each, split at lever-sizing stage; flagged as assumption #6 |

## Premortem
1. Plan is built assuming EUR 3m is the full multi-year envelope, board actually meant "EUR 3m for 2027" (or vice versa) — levers sized wrong by an order of magnitude.
2. A lever (e.g. delivery) is approved before anyone checks it against the 14% floor, and it turns out current margin is already near 14%.
3. "More stores" is sized using home-region store count without knowing how much further density the region can actually support, producing a lever with no real ceiling check.

## What is good and must survive the rewrite
- The gap is stated as a number (EUR 20m) with a year.
- No acquisitions / no new regions are carried through as explicit out-of-scope, not silently dropped.
- Four named options kept as hypotheses to test, not pre-decided as the answer.

