# em-02-day-one-answer on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (9/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: runs in day-one mode: no long interview, no request for more data before giving an answer. | yes | Answer is given immediately under 'Day-one answer' header; open questions appear only after the recommendation, not as a precondition to answering. |
| Must: gives a one-sentence answer that names two specific moves. | yes | "Fund corporate catering and franchising in the 2027 budget; do not fund a new company-owned-store push or a full online delivery build-out this cycle" |
| Must: lists hypotheses that the answer depends on, each with a numeric threshold and a kill criterion written before any data. | yes | H1–H5 table each has 'Threshold to pass' and 'Kill criterion' columns with numeric values, e.g. H3: 'Average order value ≥EUR 100... AOV <EUR 80 (lever too small)' |
| Must: ranks hypotheses by impact and uncertainty and says which one to test first. | yes | Section titled 'Ranked hypotheses'; H2 flagged 'Yes — biggest range, biggest swing factor' as the key test-first item, with H1 noted as foundational. |
| Must: drafts ghost-deck titles as full-sentence findings (no topic labels), opening with SCQA. | yes | Ghost deck opens with Situation/Complication/Question/Answer, then lists full sentences like "New stores are the wrong 2027 bet: the only available formats sit below the margin floor..." |
| Must: uses the given facts correctly (e.g. suburban stores below the 14% floor argues against suburban expansion). | yes | "the only formats with available sites (suburban 13.1%, kiosk 11.4%) already sit below the 14% margin floor" |
| Must: flags that EUR 62m to EUR 80m is a large gap and states what would have to be true to close it. | yes | "Gap to close with new levers ... ≈ EUR 11–13m" and Section 5 "What would have to be true... Catering's margin and average order value have to clear 14%... Franchise economics have to produce margin at or above... A franchisee pipeline of at least 8 units by 2031 has to be realistic" |
| Must not: present hypotheses as proven facts. | yes | Ghost deck items explicitly labeled '(hypothesis)'; overall confidence stated as 'low-to-medium'. |
| Must not: invent external benchmarks as facts. | yes | Assumptions table marks figures like capex and growth rate as '[ASSUMPTION]' with basis 'not given, generic... range' rather than asserting them as facts. |

## Transcript

## Turn 1

**User:** Give me a day-one answer. Problem statement: Which two growth moves should the Brightwell Bakeries board fund in the 2027 budget to grow revenue from EUR 62m to EUR 80m by 2031, keeping store-level margin above 14%, with about EUR 3m of capital? In scope: new stores, online delivery, corporate catering, franchising. Facts we have: 41 stores; store margin high street 16.8%, suburban 13.1%, station kiosk 11.4%; office catering orders grew from 3,100 to 9,000 between 2023 and 2026 without sales effort; online is 4% of revenue today.

# Growth strategy: Brightwell Bakeries, which two growth moves to fund in the 2027 budget to close the EUR 62m → EUR 80m gap by 2031 (margin floor 14%, capital ~EUR 3m)

**Day-one answer — not yet decidable with full confidence; here is the provisional view and what would firm it up.**

## 1. The gap, and whether the levers on the table can plausibly close it

| | 2027 | 2031 (target) |
|---|---|---|
| Revenue, target | EUR 62m | EUR 80m |
| Revenue, momentum case (no new action) | EUR 62m | **≈ EUR 68m** [ASSUMPTION: 2.5%/yr like‑for‑like, range 1–4%] |
| **Gap to close with new levers** | | **≈ EUR 11–13m** |
| Required blended CAGR to hit target | | ≈ 6.6%/yr |
| Constraints | capital ≈ EUR 3m, store margin floor 14%, decision: 2027 budget | |

Sizing the two levers I'd put forward (detail below): corporate catering ≈ EUR 1–4m incremental revenue by 2031, franchising ≈ EUR 3–7m. Combined base case lands around **EUR 5–8m incremental**, which closes most but not all of the EUR 11–13m gap — I'm not stretching assumptions to force a fit. The remaining EUR 3–6m either needs a faster catering/franchise ramp than the base case, a third smaller lever (e.g. a bounded delivery pilot), or the board accepting the target closes in 2032 rather than 2031.

## 2. The day-one answer

**Fund corporate catering and franchising in the 2027 budget; do not fund a new company-owned-store push or a full online delivery build-out this cycle** — catering has already proven unprompted demand (orders +190% in three years with zero sales effort) and franchising is the only capital-light way to add store count against a EUR 3m ceiling, while new stores are capital-hungry and the only formats with available sites (suburban 13.1%, kiosk 11.4%) already sit below the 14% margin floor.

**Confidence: low-to-medium** — the two chosen levers rest on assumptions (average catering order value, franchisee pipeline, wholesale/royalty margin) that aren't in the data given and materially change the size of each lever.

## 3. Ranked hypotheses, thresholds and kill criteria

| # | Hypothesis | Threshold to "pass" | Kill criterion | Test first? |
|---|---|---|---|---|
| H1 | Momentum case leaves an ~EUR 11–13m gap to the 2031 target | Momentum growth 1–4%/yr | Undisclosed initiatives already push like-for-like above 4%/yr → gap and lever ranking both need rework | Yes — foundational |
| H2 | Franchising can add EUR 3–7m revenue by 2031 within ~EUR 1–1.5m infrastructure capex, without breaching the margin floor | ≥8 franchised units signed by 2031; wholesale/royalty margin ≥14% | Franchisee pipeline can't support >8 units, or if the 14% floor is meant group-wide and wholesale supply margin to franchisees tests below it | **Yes — biggest range, biggest swing factor** |
| H3 | Corporate catering can add EUR 2–4m revenue by 2031 at ≥14% margin, on existing kitchen capacity | Average order value ≥EUR 100; catering gross margin ≥14% | AOV <EUR 80 (lever too small) or catering margin tests below 14% (fails the constraint it was chosen to protect) | Yes — cheap to verify, high confidence lever |
| H4 | New company-owned stores are not the best 2027 bet | High-street-only pipeline of 6+ sites at >16% margin absorbing the full EUR 3m | If such a pipeline exists, re-test this lever against franchising | Quick confirmatory check |
| H5 | Online delivery is not one of the two funded moves this cycle | Contribution margin after platform/delivery/packaging costs tested ≥14% | If a bounded pilot or comparable-operator data shows ≥14% contribution margin, promote delivery ahead of one of the other two in 2028 | Quick confirmatory check, revisit 2028 |

## 4. Ghost deck

**Situation:** Brightwell is a 41-store bakery chain earning EUR 62m, with a board target of EUR 80m by 2031 and a 14% store-margin floor.
**Complication:** The core alone plausibly reaches only ~EUR 68m by 2031, and the obvious growth lever — new stores — is capital-heavy and the only available formats already undercut the margin floor.
**Question:** Which two growth moves, fundable within ~EUR 3m, close the most of the remaining ~EUR 11–13m gap without breaching 14% store margin?
**Answer:** Fund corporate catering and franchising; park new stores and delivery pending further evidence.

1. *(hypothesis)* "The core closes about half the gap on its own — the 2031 target needs roughly EUR 11–13m of new growth, not EUR 18m."
2. *(hypothesis)* "Corporate catering has already proven demand without a sales effort and is the cheapest euro of growth on the table."
3. *(hypothesis)* "New stores are the wrong 2027 bet: the only available formats sit below the margin floor, and EUR 3m buys too few of the format that doesn't."
4. *(hypothesis)* "Franchising converts the capital constraint into the plan's main store-growth engine."
5. *(hypothesis)* "Together, catering and franchising close most — not all — of the gap; the board should decide now how to treat the residual EUR 3–6m."
6. *(hypothesis)* "Online delivery is the one to watch for 2028, not fund in 2027, until its margin after platform and delivery costs is proven."

## 5. What would have to be true, and what the full engagement tests first

For this answer to hold:
- Catering's margin and average order value have to clear 14% and ~EUR 100+/order respectively — currently unverified.
- Franchise economics (royalty-only vs. central wholesale-supply model) have to produce margin at or above the group's 14% floor, and the board has to clarify whether the 14% floor applies to company-operated stores only or system-wide — this single clarification could change the whole recommendation.
- A franchisee pipeline of at least 8 units by 2031 has to be realistic — not yet tested against any comparable rollout.

The full engagement would start exactly there: (1) get actual catering order economics and margin, (2) get Brightwell's intended franchise model and test it against comparable bakery/QSR franchise rollouts (outside view, not inside-view extrapolation of the 190% growth rate), and (3) get board clarification on what "store-level margin" means for franchised units before sizing either lever further.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Momentum (no new action) growth rate | 2.5%/yr (range 1–4%) | Typical bakery like-for-like; not given | Actual momentum is >4%/yr → gap shrinks, lever mix may not need to change but urgency does |
| 2 | Average corporate catering order value | EUR 100–150 | Not given; order *count* only | AOV is materially lower (<EUR 80) → catering too small to be one of the two bets |
| 3 | New-store capex | EUR 300–400k/store | Not given, generic retail bakery fit-out range | Actual capex much lower → new stores become capital-competitive again |
| 4 | Franchise royalty / wholesale-supply margin | 20% blended, revenue EUR 3–7m by 2031 on ~10–15 units | Not given; generic bakery-franchise pattern | Franchise model is royalty-only and thin → lever shrinks well below EUR 3m |
| 5 | "Store-level margin above 14%" scope | Applied to company-operated stores; franchised units' P&L assumed separate | Not specified in the brief | If floor applies group-wide including supply margin to franchisees → franchising lever needs re-sizing |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is Brightwell's intended franchise economic model (royalty-only vs. central commissary/wholesale supply)? | Franchising is the larger of the two levers and its size swings 2–3x depending on the model | CFO / commercial director | Could promote or demote franchising relative to the other options |
| What is corporate catering's actual margin and average order value today? | Catering was chosen partly *because* it should protect the 14% floor — unverified | Finance / catering ops | Could kill or shrink H3 |
| Does the 14% floor apply only to the 41 company-operated stores, or group-wide (incl. franchise supply, catering, delivery)? | Changes which levers are even eligible | Board | Could change the entire recommendation |
| Is there a confirmed high-street site pipeline that could absorb EUR 3m at >16% margin? | Only scenario where new stores would re-enter contention | Property/expansion team | Could reopen H4 |
| What would online delivery's contribution margin look like after platform fees, delivery cost and packaging? | Currently the reason delivery was excluded from the two funded moves | Finance, or a bounded pilot | Could promote delivery into the 2028 budget ahead of a weaker lever |


## Files in work dir after run


