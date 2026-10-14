# em-02-day-one-answer on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs in day-one mode: no long interview, no request for more data before giving an answer | yes | Answer given immediately in Turn 1 with no clarifying questions asked first. |
| Gives a one-sentence answer that names two specific moves | yes | "Fund a high-street-only new-store rollout and a formalized corporate catering unit; hold online delivery as a cheap pilot... and defer franchising..." |
| Lists hypotheses with numeric threshold and kill criterion written before any data | yes | Table H1–H6 each with 'Threshold' and 'Kill criterion' columns, e.g. H3: 'Threshold: ≥4 viable... sites' / 'Kill criterion: <3–4 sites available → lever drops below EUR 4m' |
| Ranks hypotheses by impact/uncertainty and says which one to test first | yes | 'Test first?' column marks H1–H4 'Yes'; closing line: 'The full engagement would test the high-street site pipeline and catering's real P&L first — those two facts move the ranking most' |
| Drafts ghost-deck titles as full-sentence findings (no topic labels), opening with SCQA | yes | Section 4 opens with 'Situation—Complication—Question—Answer' then numbered full-sentence findings like '1. The core alone reaches only ~EUR 67m by 2031, leaving a ~EUR 13m gap too large for one move alone to close.' |
| Uses given facts correctly (e.g. suburban below 14% floor argues against suburban expansion) | yes | 'at 13.1% and 11.4%, suburban and station-kiosk formats sit below the 14% floor today' |
| Flags EUR 62m→80m as a large gap and states what would have to be true to close it | yes | 'Gap / / EUR 18m (+29%, ~5.3% CAGR)' and section 5 'What would have to be true' lists site availability, catering order value, momentum assumption accuracy, online delivery economics. |
| Must not present hypotheses as proven facts | yes | All ghost-deck findings explicitly tagged '(hypothesis)'; momentum growth tagged 'ASSUMPTION... not given, needs checking'. |
| Must not invent external benchmarks as facts | NO | 'third-party delivery commissions (typically 25–30%) would likely push online delivery below it too' — stated as a flat, unsourced fact (unlike the LFL growth figure, which was explicitly flagged as an unverified ASSUMPTION), and used to help rule out online delivery. |

## Transcript

## Turn 1

**User:** Give me a day-one answer. Problem statement: Which two growth moves should the Brightwell Bakeries board fund in the 2027 budget to grow revenue from EUR 62m to EUR 80m by 2031, keeping store-level margin above 14%, with about EUR 3m of capital? In scope: new stores, online delivery, corporate catering, franchising. Facts we have: 41 stores; store margin high street 16.8%, suburban 13.1%, station kiosk 11.4%; office catering orders grew from 3,100 to 9,000 between 2023 and 2026 without sales effort; online is 4% of revenue today.

## Day-one answer: Brightwell Bakeries, which two growth moves for the 2027 budget

### 1. The gap, and whether the four moves can plausibly close it

| | 2026 (today) | 2031 (target) |
|---|---|---|
| Revenue | EUR 62m | EUR 80m |
| Gap | | **EUR 18m** (+29%, ~5.3% CAGR) |

Momentum case (ASSUMPTION: 1.5–2%/yr like-for-like growth, typical for a mature bakery retailer with no new levers — not given, needs checking against recent LFL data): EUR 62m grows to roughly **EUR 67m** by 2031. That leaves a **momentum gap of ~EUR 13m** that new moves have to find — within a ~EUR 3m capital budget and without any store-format or channel falling below 14% margin.

That constraint already rules two of the four options in or out before any sizing: at 13.1% and 11.4%, **suburban and station-kiosk formats sit below the 14% floor today**, and third-party delivery commissions (typically 25–30%) would likely push online delivery below it too unless run through an owned click-and-collect model. So the real choice is narrower than "pick two of four" — it's "which two are structurally margin-safe and big enough to matter."

### 2. Day-one answer

**Fund a high-street-only new-store rollout and a formalized corporate catering unit; hold online delivery as a cheap pilot (not a funded move) until its margin economics are proven, and defer franchising until Finance confirms how its revenue counts toward the EUR 80m target.**

Base case: ~5–6 new high-street stores (~EUR 2–2.2m of capital) adding EUR 6–8m by 2031, plus a catering scale-up (~EUR 0.5–0.8m of capital) adding EUR 2–3m — together closing roughly 60–85% of the EUR 13m momentum gap, both comfortably above the 14% floor. The residual EUR 2–5m is stated openly, not closed by stretching these two levers.

### 3. Ranked hypotheses

| # | Hypothesis | Threshold | Kill criterion | Test first? |
|---|---|---|---|---|
| H1 | Momentum alone reaches only ~EUR 67m by 2031, leaving a ~EUR 13m gap | Gap > EUR 10m → real growth moves needed | If actual LFL growth is already >4%/yr, gap is smaller and the ask shrinks | **Yes** — resizes everything else |
| H2 | Suburban/kiosk formats and commission-based online delivery sit below the 14% floor by default | Any format/channel margin <14% excluded unless mitigated | If online delivery can run profitably via owned click-and-collect (>14% contribution margin), reinstate it | **Yes** — cheap to check, changes the shortlist |
| H3 | New high-street stores are the single largest safe lever: ~EUR 6–8m by 2031 for ~EUR 2m capital | ≥4 viable, affordable high-street sites available 2027–29 without heavy cannibalization | <3–4 sites available → lever drops below EUR 4m | **Yes** — biggest swing factor |
| H4 | Corporate catering is the cheapest, most de-risked lever: EUR 2–3m for <EUR 1m capital | Avg. order value ≥EUR 80–100 and growth ≥15%/yr post-formalization | If order value is much lower (e.g. coffee-and-pastry trays, <EUR 30) or the 3,100→9,000 growth was a one-off hybrid-work rebound already plateauing, lever shrinks below EUR 1m | **Yes** — single biggest data gap |
| H5 | Franchising's contribution to the EUR 80m is undefined: royalty-only recognition ≈ <EUR 1m; wholesale-supply model ≈ EUR 3–5m | This is a definitional, not a market, question | Board confirms EUR 80m = consolidated statutory revenue, royalties only → deprioritize for 2027 | Yes, but it's a one-conversation fix, not a market test |
| H6 | High-street stores + catering close 60–85% of the gap, not all of it | ≥60% gap closure from the two kept levers is an acceptable board case | If combined base case <50% of gap, add franchising (once H5 resolved) rather than stretch H3/H4 assumptions | After H1–H4 |

### 4. Ghost deck

**Situation** — Brightwell runs 41 stores on EUR 62m revenue, with margin varying sharply by format: high street 16.8%, suburban 13.1%, station kiosk 11.4%.
**Complication** — The board wants EUR 80m by 2031 while holding every store above 14% margin, with only ~EUR 3m of capital for 2027 — and two of the four formats/channels on the table already sit at or below that floor.
**Question** — Which two of new stores, online delivery, corporate catering, and franchising should the board fund in 2027?
**Answer** — Fund high-street store growth and a formal corporate catering unit; defer online delivery and franchising until their margin/accounting risks are resolved.

1. *(hypothesis)* The core alone reaches only ~EUR 67m by 2031, leaving a ~EUR 13m gap too large for one move alone to close.
2. *(hypothesis)* Two of the four options are already below the 14% floor by format or channel economics — suburban/kiosk expansion and commission-based online delivery — and should be ruled out by default.
3. *(hypothesis)* A disciplined high-street-only rollout is the single largest safe lever, adding an estimated EUR 6–8m by 2031 for ~EUR 2m of capital.
4. *(hypothesis)* Corporate catering's organic order growth (3,100→9,000 since 2023, with zero sales effort) is revealed demand, not a forecast, and converts to EUR 2–3m of margin-accretive revenue for under EUR 1m of capital.
5. *(hypothesis)* Franchising could add EUR 3–5m or almost nothing to the EUR 80m target depending on one unresolved revenue-recognition question — resolve it, don't fund around it.
6. *(hypothesis)* Together, high-street stores and catering close 60–85% of the momentum gap within budget and above the margin floor; the remaining gap is closed by a second tranche or a revised target, not by stretching these two levers.

### 5. What would have to be true, and what the full engagement tests first

- At least 4–6 affordable, available high-street (or equivalent) sites exist for 2027–29 without significant cannibalization of the existing 41 stores.
- Corporate catering's real average order value and fully-loaded margin support EUR 2–3m from under EUR 1m of capital — currently unverified; this and H4's growth durability are the single biggest data gaps.
- The 1.5–2% momentum assumption isn't already wrong in either direction.
- Online delivery's assumed poor economics actually hold for Brightwell's model — a margin-safe click-and-collect variant would change the shortlist.

The full engagement would test the high-street site pipeline and catering's real P&L first — those two facts move the ranking most and could overturn this recommendation if they come back weak.


## Files in work dir after run


