# em-02-day-one-answer on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (9/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: runs in day-one mode: no long interview, no request for more data before giving an answer. | yes | Gives full numbered answer immediately; open questions are listed only at the end, after the recommendation. |
| Must: gives a one-sentence answer that names two specific moves. | yes | "Fund corporate catering and franchising in the 2027 budget; hold company-owned new-store growth to self-funded, high-street-only pace; park online delivery pending a margin test." |
| Must: lists hypotheses that the answer depends on, each with a numeric threshold and a kill criterion written before any data. | yes | H1–H5 table, e.g. H1: '≥20,000 orders/yr... ≥EUR 3m incremental revenue... ≥16% contribution margin' with 'Killed, or capped much lower, if average order value is below ~EUR 50...' |
| Must: ranks hypotheses by impact and uncertainty and says which one to test first. | yes | Table has Impact/Uncertainty columns; Status column says 'open — test first' (H2) and 'open — test second' (H1); text: 'test it first'. |
| Must: drafts ghost-deck titles as full-sentence findings (no topic labels), opening with SCQA. | yes | SCQA block precedes deck; titles like 'The floor is already breached' and 'Catering demand is proven, unforced' are full-sentence findings, not topic labels. |
| Must: uses the given facts correctly (e.g. suburban stores below the 14% floor argues against suburban expansion). | yes | "suburban at 13.1%, station kiosks at 11.4%... Any move that adds more suburban/kiosk floor space... pushes the wrong way on both the revenue target and the margin floor." |
| Must: flags that EUR 62m to EUR 80m is a large gap and states what would have to be true to close it. | yes | 'EUR 18m' gap flagged with CAGR context, plus section 5 'What would have to be true, and what to test first' lists required conditions. |
| Must not: present hypotheses as proven facts. | yes | All hypotheses tagged 'hypothesis'/'open' status, confidence labeled 'medium', explicit 'ASSUMPTION, needs replacing with real same-store data'. |
| Must not: invent external benchmarks as facts. | yes | Benchmark figures like platform commission '(typically 20–30%, unverified)' and peer same-store growth '~4%/yr' are explicitly hedged as unverified/conditional, not asserted as fact. |

## Transcript

## Turn 1

**User:** Give me a day-one answer. Problem statement: Which two growth moves should the Brightwell Bakeries board fund in the 2027 budget to grow revenue from EUR 62m to EUR 80m by 2031, keeping store-level margin above 14%, with about EUR 3m of capital? In scope: new stores, online delivery, corporate catering, franchising. Facts we have: 41 stores; store margin high street 16.8%, suburban 13.1%, station kiosk 11.4%; office catering orders grew from 3,100 to 9,000 between 2023 and 2026 without sales effort; online is 4% of revenue today.

# Growth strategy day-one answer: Brightwell Bakeries, 2027 budget

## 1. The gap, in numbers

| | 2026 (today) | 2031 (target) |
|---|---|---|
| Revenue | EUR 62m | EUR 80m |
| Gap | | **EUR 18m** (+29%, ~5.3%/yr CAGR) |
| Capital available | EUR 3m, 2027 budget only | |
| Margin floor | 14% store-level, every store | |

**Momentum case (ASSUMPTION, needs replacing with real same-store data):** at 1–3%/yr same-store growth and no new units, the core drifts to roughly EUR 65–70m by 2031 on its own. That leaves a **EUR 10–15m shortfall even before any new move is counted** — this is the number the four options have to close.

**A fact the board should see before choosing moves:** on today's figures, two of the three existing store formats are *already below* the 14% floor — suburban at 13.1%, station kiosks at 11.4%. Only high street (16.8%) clears it. So "stay above 14%" isn't a hypothetical risk, it's a constraint the business is currently failing in two formats out of three. Any move that adds more suburban/kiosk floor space, or adds a margin-diluting channel (e.g. delivery-platform commissions), pushes the wrong way on both the revenue target *and* the margin floor at once.

**Can the four options plausibly close EUR 18m with EUR 3m of capital?** Not comfortably, on the evidence we have today — see the hypothesis table. The honest day-one read is that the two moves below close **part** of the gap with high confidence and the rest depends on one still-open structural question (see H2).

## 2. Day-one answer

**Fund corporate catering and franchising in the 2027 budget; hold company-owned new-store growth to self-funded, high-street-only pace; park online delivery pending a margin test.**

Reasoning in one line: catering and franchising are the only two of the four moves that add revenue *without* buying more sub-floor store format or consuming the scarce EUR 3m on store capex — catering rides existing kitchen capacity and a proven, unforced demand signal; franchising shifts store-level capex and margin risk to the franchisee and asks Brightwell to fund only the program, not the buildings.

**Confidence: medium.** The catering demand signal is real and already evidenced (3,100 → 9,000 orders, 2023–26, with zero sales effort). The franchising case is directionally sound but its *size* swings 10x depending on one unanswered question: does Brightwell consolidate franchisee revenue, or only book a royalty? That single fact could make franchising the biggest lever on the table or too small to matter — test it first.

## 3. Ranked hypotheses

| # | Hypothesis (testable, with threshold) | Impact | Uncertainty | Test / analysis | Kill criterion | Status |
|---|---|---|---|---|---|---|
| H2 | Franchising can add ≥EUR 5m of **consolidated group revenue** by 2031 via 10+ signed units, for ≤EUR 1.5m of program investment (manuals, training, legal, pilot support) | high | high | Pull the actual franchise structure/legal model; model consolidated vs. royalty-only revenue | Killed as a revenue lever (though may survive as a brand/cash lever) if the model is royalty-only — a 6–8% royalty on unit sales cuts H2's revenue contribution by ~90% | open — test first |
| H1 | Corporate catering can scale from ~9,000 to ≥20,000 orders/yr by 2031, yielding ≥EUR 3m incremental revenue, at ≥16% contribution margin, on <EUR 1m of sales/ops/kitchen investment | high | medium | Pull actual average order value and current catering revenue/margin from the P&L (not estimated); size production-capacity ceiling of existing kitchens | Killed, or capped much lower, if average order value is below ~EUR 50, or if volume past ~15,000 orders needs a new central kitchen costing >EUR 1.5m | open — test second |
| H3 | New company-owned stores cannot be the primary 2027-funded lever: EUR 3m funds only ~10–15 units at an assumed EUR 200–300k capex each, consuming the whole growth budget | medium | low | Pull actual capex on the last 3 store openings by format | Killed (new stores become viable as a primary lever) if real capex is materially below EUR 100k/unit, e.g. a smaller kiosk-format rollout | open |
| H4 | Scaling online delivery risks pushing blended margin below the 14% floor once platform commission (typically 20–30%, unverified) and packaging/logistics cost are applied | medium | low–medium | Pull actual contribution margin on the existing 4% online revenue, and confirm channel (owned site/app vs. third-party marketplace) | Killed (online delivery reinstated as a lever) if today's online channel is already owned (no marketplace commission) and already clears 14% contribution margin | open |
| H5 | Without new action, same-store growth of 1–3%/yr leaves 2031 revenue at EUR 65–70m, a EUR 10–15m shortfall | high | medium | Pull actual same-store sales trend, last 3 years | Shortfall is smaller than assumed if comparable high-street bakery peers are growing same-store sales above ~4%/yr | open — foundational, test alongside H1/H2 |

## 4. Ghost deck

**Opening (SCQA)**
- **Situation:** Brightwell runs 41 stores and EUR 62m revenue, with store-level margin ranging from 16.8% on high street down to 11.4% at station kiosks.
- **Complication:** The board wants EUR 80m by 2031 while holding every store above a 14% margin floor that two of three existing formats already miss, on only ~EUR 3m of 2027 capital.
- **Question:** Which two of new stores, online delivery, corporate catering and franchising should the board fund in 2027?
- **Answer:** Corporate catering and franchising — the two moves that grow revenue without buying more sub-floor floor space or spending the scarce capital on store buildout.

| # | Section | Action title | Body sketch | Workplan row | Status |
|---|---|---|---|---|---|
| 1 | Exec summary | Fund corporate catering and franchising in 2027; hold new stores to self-funded high-street pace; park online delivery | — | — | hypothesis |
| 2 | 1. The floor is already breached | Suburban (13.1%) and kiosk (11.4%) formats already sit below the 14% margin floor the board wants to hold, so new growth must not add more of either | Bar chart: store margin by format vs. 14% line | H3/H4 | hypothesis |
| 3 | 2. Catering demand is proven, unforced | Office catering orders nearly tripled from 3,100 to 9,000 between 2023 and 2026 with no sales effort, the strongest demand signal in the portfolio | Line chart: order volume 2023–26; table: implied revenue and margin once order value is confirmed | H1 | hypothesis |
| 4 | 3. Franchising is the only capital-light route to more stores | At EUR 3m of capital, company-owned expansion buys at most 10–15 units; franchising converts that capex into franchisee-funded units, but the revenue gain to Brightwell depends entirely on whether franchisee sales are consolidated | Decision table: consolidated vs. royalty-only revenue impact by 2031 | H2 | hypothesis |
| 5 | 4. Online delivery is parked, not killed | At 4% of revenue with unverified contribution margin, delivery is held back until platform commission and packaging cost are shown to clear 14% | Table: current online contribution margin vs. 14% floor | H4 | hypothesis |
| 6 | 5. The remaining gap | Even with catering and franchising funded, a residual gap likely remains against the EUR 18m target and the board should see it stated, not plugged | Waterfall: momentum case → catering → franchising → remaining gap | H5, H1, H2 | hypothesis |

**Titles-only read-through:** yes — they carry the logic from "the floor is already breached" through to "here's the residual gap, stated openly," without needing the bodies.

## 5. What would have to be true, and what to test first

For this day-one answer to survive a real engagement:
- **Catering's average order value and current margin** have to be good enough that H1 clears a few million euros of revenue, not a few hundred thousand — pull this from the P&L before anything else; it's one query, not a study.
- **Franchising has to consolidate franchisee revenue** (or the board has to accept it as a brand/cash lever, not a revenue lever) — this is the single fact most likely to overturn this recommendation, so it's the first call to make with Brightwell's own legal/finance team.
- **New-store capex per unit** has to genuinely be EUR 200–300k, not EUR 80–100k — if it's cheap enough, a selective high-street-only store program could outcompete both chosen levers and this answer would flip.

**First week of a full engagement:** resolve H2 (franchise revenue model) and H1 (catering order economics) in parallel — they're both one-document pulls from Brightwell's own finance team, not external research, and between them they decide whether this day-one answer holds, needs rebalancing toward new high-street stores, or forces the board to accept a smaller 2031 target.

## Assumptions used above

| # | Assumption | Value used | Would change the answer if |
|---|---|---|---|
| 1 | Same-store growth, no new action | 1–3%/yr | Actual trend is flat or negative → gap is closer to the full EUR 18m, raising the bar for both chosen levers |
| 2 | Average corporate catering order value | EUR 70–200 (wide, unverified) | Real figure resolves H1's size — this is a one-query fix, not a real unknown |
| 3 | New-store capex | EUR 200–300k/unit | If much lower, new stores re-enter as a primary 2027 lever |
| 4 | Franchise unit economics if consolidated | ~EUR 1–1.5m revenue/unit, comparable to current store average | Franchise format (kiosk-sized vs. high-street-sized) changes this materially |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Does the franchise model consolidate franchisee sales or pay Brightwell a royalty only? | Decides whether franchising is a EUR 1–2m or EUR 8–15m+ lever | Brightwell finance/legal | Could promote or demote franchising entirely |
| What is the actual average corporate catering order value and current contribution margin? | Decides H1's real size | Brightwell finance (order-level data already exists) | Sizes the catering lever precisely instead of in a wide range |
| What did the last 2–3 new stores actually cost to open, by format? | Decides whether new stores are too capital-hungry to fund in 2027 | Brightwell finance/ops | Could reopen new stores as a funded 2027 move |
| Is today's 4% online revenue sold via owned channels or a commissioned marketplace, and at what contribution margin? | Decides whether online delivery is really margin-dilutive or just unsized | Brightwell finance | Could reinstate online delivery as a funded move |


## Files in work dir after run


