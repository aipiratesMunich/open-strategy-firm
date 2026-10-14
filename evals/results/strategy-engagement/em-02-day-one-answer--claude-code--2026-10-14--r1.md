# em-02-day-one-answer on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: runs in day-one mode: no long interview, no request for more data before giving an answer. | yes | The assistant answers immediately in Turn 1 with a full day-one answer, gap analysis, hypotheses, and ghost deck — no clarifying questions asked before answering. |
| Must: gives a one-sentence answer that names two specific moves. | yes | "Fund corporate catering and online delivery in the 2027 budget; pause new company-owned stores and defer franchising to a 2028 decision pending a feasibility test..." |
| Must: lists hypotheses that the answer depends on, each with a numeric threshold and a kill criterion written before any data. | yes | H1: "Killed if average order value is too small to matter, or the 2023–26 surge was a one-off..." with threshold "≥EUR 3m... for ~EUR 1–1.5m capital"; similar numeric thresholds/kill criteria given for H0, H2, H3, H4, H5. |
| Must: ranks hypotheses by impact and uncertainty and says which one to test first. | yes | "Test first: H1 and H2's capital requirement and margin mechanics... they decide whether EUR 3m is even enough"; section 5 ranks tests "in order of impact" (1. Catering lever sizing, 2. Online delivery economics, 3. New-store and franchising economics). |
| Must: drafts ghost-deck titles as full-sentence findings (no topic labels), opening with SCQA. | yes | Ghost deck opens with explicit Situation/Complication/Question/Answer, followed by full-sentence titles like "Corporate catering has already proven a scalable demand signal without any sales investment, and now deserves one". |
| Must: uses the given facts correctly (e.g. suburban stores below the 14% floor argues against suburban expansion). | yes | "Suburban (13.1%) and station kiosk (11.4%) are already below the floor. Any move that adds more suburban/kiosk square footage pulls the average the wrong way..." |
| Must: flags that EUR 62m to EUR 80m is a large gap and states what would have to be true to close it. | yes | "Gap / EUR 18m (+29%) / Implied CAGR ~5.2%/yr" and section 5 "What would have to be true for this to hold" lists conditions on catering/online economics and capital allocation. |
| Must not: present hypotheses as proven facts. | yes | Ghost deck titles explicitly tagged "(hypothesis)"; final line states "Confidence: medium... those two numbers are what turns this from a day-one call into a funded plan," signaling hypotheses rather than proof. |
| Must not: invent external benchmarks as facts. | NO | "Killed if fulfillment must run through 20–30%-commission marketplaces (margin falls below 14%)" and "...rather than 20–30%-commission marketplace apps" — a specific external commission-rate benchmark not in the given facts, asserted as a concrete figure rather than flagged as an unverified assumpti |

## Transcript

## Turn 1

**User:** Give me a day-one answer. Problem statement: Which two growth moves should the Brightwell Bakeries board fund in the 2027 budget to grow revenue from EUR 62m to EUR 80m by 2031, keeping store-level margin above 14%, with about EUR 3m of capital? In scope: new stores, online delivery, corporate catering, franchising. Facts we have: 41 stores; store margin high street 16.8%, suburban 13.1%, station kiosk 11.4%; office catering orders grew from 3,100 to 9,000 between 2023 and 2026 without sales effort; online is 4% of revenue today.

# Brightwell Bakeries — Day-One Answer

## 1. The gap, in numbers

| | Today | 2031 target |
|---|---|---|
| Revenue | EUR 62m | EUR 80m |
| Gap | | **EUR 18m (+29%)** |
| Implied CAGR | | ~5.2%/yr over 5 years |
| Capital available | | ~EUR 3m |
| Margin floor | | >14% at store level |

Context that makes the floor binding, not decorative: of the three store formats, only **high street (16.8%)** clears 14% today. **Suburban (13.1%)** and **station kiosk (11.4%)** are *already below the floor*. Any move that adds more suburban/kiosk square footage pulls the average the wrong way before it adds a euro of growth.

Can the four moves on the table plausibly close EUR 18m with EUR 3m? Not all four, and not evenly. A mature 41-store base doesn't re-rate its own margin mix for free, and EUR 3m won't fund a real store-building programme *and* anything else. The two moves that can close a meaningful share of the gap **without consuming most of the capital or touching the margin floor** are the ones with asset-light economics and a live demand signal: **corporate catering** and **online delivery**. New company-funded stores and franchising both have real appeal but fail a harder test today — one on capital intensity and margin mix, the other on missing unit-economics evidence.

## 2. Day-one answer

**Fund corporate catering and online delivery in the 2027 budget; pause new company-owned stores and defer franchising to a 2028 decision pending a feasibility test — because catering and online are the only two moves that can grow revenue off existing kitchen/store capacity (protecting the 14% floor) with capital that fits inside EUR 3m, and both already show organic pull (catering orders nearly tripled unprompted in three years; online is still just 4% of sales in a market where omnichannel is now standard).**

## 3. Ranked hypotheses

| # | Hypothesis | Threshold / kill criterion | Status (day-one) |
|---|---|---|---|
| H0 | Momentum case (no new levers) misses EUR 80m by a wide margin | If momentum alone closes >80% of the EUR 18m gap, no new lever is needed | Likely true it misses — 41 mature stores rarely post 5%+ CAGR unaided. **Needs a same-store growth number to confirm; treat as open.** |
| H1 | Corporate catering can add ≥EUR 3m of incremental revenue by 2031 at >14% margin, for ~EUR 1–1.5m capital | Killed if average order value is too small to matter, or the 2023–26 surge was a one-off (return-to-office rebound) now plateauing | **Strong — highest priority to fund.** 3,100→9,000 orders (2023–26) is a ~43% CAGR with *zero* sales effort; a dedicated sales/ops layer should extend this, not invent it |
| H2 | Online delivery can move from 4% toward 10%+ of revenue, adding ≥EUR 3m, fundable within ~EUR 1.5–2m, if fulfilled via existing stores rather than marketplace commission | Killed if fulfillment must run through 20–30%-commission marketplaces (margin falls below 14%), or if growth is mostly cannibalization of in-store sales, not addition | **Strong but conditional** — the economics hinge entirely on the fulfillment model; this is the first thing to verify |
| H3 | New company-funded stores can close a meaningful share of the gap within EUR 3m without breaching the margin floor | Killed if the formats that still have expansion room (suburban, kiosk) sit below 14% today, or if capex for even 3–4 sites consumes the whole budget | **Killed for 2027.** Two of three formats already miss the floor; funding stores would crowd out catering and online entirely |
| H4 | Franchising adds footprint without consuming Brightwell's own capital | Killed (for now) if royalty rate, franchisee demand, and franchisee unit economics are unproven | **Open, not killed** — genuinely capital-light in principle, but there is no data point in hand on royalty % or franchisee returns. Treat as a 2028 option pending a short feasibility study, not a 2027 funding decision |
| H5 | Catering + online together close at least half the EUR 18m gap in the base case | If combined base case is <EUR 9m, reopen the target with the board or add a third lever | **Test first** — this is the number that validates or breaks the whole recommendation |

**Test first:** H1 and H2's capital requirement and margin mechanics (catering order economics; online fulfillment model) — they decide whether EUR 3m is even enough, and whether H5 holds.

## 4. Ghost deck

**Situation:** Brightwell runs 41 stores generating EUR 62m, with store margin ranging from 16.8% (high street) down to 11.4% (station kiosk).
**Complication:** The board wants EUR 80m by 2031 — an EUR 18m, 29% increase — but has only ~EUR 3m of capital for the 2027 budget and a 14% margin floor that two of the three existing store formats already miss.
**Question:** Which two of the four moves — new stores, online delivery, corporate catering, franchising — should the board fund in 2027 to close the gap without breaching capital or margin?
**Answer:** Fund corporate catering and online delivery; pause new company-funded stores; defer franchising pending a unit-economics test.

| Page | Full-sentence title |
|---|---|
| 1 | The EUR 18m gap to 2031 cannot be closed by store-count growth alone inside a EUR 3m budget *(hypothesis)* |
| 2 | Corporate catering has already proven a scalable demand signal without any sales investment, and now deserves one *(hypothesis)* |
| 3 | Online delivery is structurally under-penetrated at 4% of revenue and can be grown through existing stores rather than commission-paying marketplaces *(hypothesis)* |
| 4 | New company-funded stores should be paused for 2027 because two of three existing formats already sit below the 14% margin floor *(hypothesis)* |
| 5 | Franchising is a credible move for 2028 and beyond, but it is not fundable in 2027 without a unit-economics test *(hypothesis)* |
| 6 | Catering plus online delivery close roughly half to two-thirds of the gap in the base case; the board should decide now how the remainder gets closed *(hypothesis)* |

## 5. What would have to be true, and what the full engagement tests first

**What would have to be true for this to hold:**
- Catering's average order value and margin, once scaled with a dedicated sales/ops team, still clear 14% — the 2023–26 growth needs to be structural (hybrid-work catering demand), not a return-to-office bounce that's already peaking.
- Online delivery is fulfilled mainly through existing stores (click-and-collect, own-fleet) rather than 20–30%-commission marketplace apps, and adds genuinely new demand rather than shifting existing in-store customers online.
- EUR 3m splits sensibly across the two: enough for a catering sales/logistics build and an online platform/fulfillment build, with neither needing new store capex.

**What the full engagement would test first, in order of impact:**
1. **Catering lever sizing** — actual revenue per order, margin, and growth trend (plateauing or not); capital needed for a sales/ops layer. This is the single biggest swing factor in H5.
2. **Online delivery economics** — fulfillment model, true incremental margin after delivery cost, and cannibalization vs. net-new demand.
3. **New-store and franchising economics as a cross-check** — cost and payback for one more high-street site, and franchisee royalty/returns — so the "kill" on stores and the "hold" on franchising are evidence-based, not just capital-arithmetic, and so there's a named fallback lever if catering + online fall short of half the gap.

**Confidence: medium** — the direction (fund asset-light, capacity-leveraging moves; hold capital-hungry store growth) is well supported by the facts given, but the actual EUR amount closed by catering and online is currently built on no revenue-per-order or online-margin data — those two numbers are what turns this from a day-one call into a funded plan.


## Files in work dir after run


