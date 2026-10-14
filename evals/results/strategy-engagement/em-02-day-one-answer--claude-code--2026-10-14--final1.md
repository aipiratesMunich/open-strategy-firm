# em-02-day-one-answer on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (9/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs in day-one mode: no long interview, no request for more data before giving an answer | yes | Gives full answer immediately, flagging missing data as assumptions (e.g. 'ASSUMPTION — confirm actual 2023-26 like-for-like growth rate') rather than stopping to ask questions |
| Gives a one-sentence answer that names two specific moves | yes | 'Fund corporate catering and online delivery in the 2027 budget; do not fund broad new-store capital or franchising this cycle.' |
| Lists hypotheses with numeric threshold and kill criterion written before any data | yes | H2: Threshold 'Average order value ≥ €100...', Kill criterion 'If avg. order value is low (<€50)...'; H3: Threshold 'penetration benchmark ≥ 8%', Kill criterion 'if category penetration tops out near today's 4-6%' |
| Ranks hypotheses by impact and uncertainty and says which one to test first | yes | 'Test first?' column marks H2 'Yes — first (cheapest, strongest evidence)', H3 'Second', H4/H5 'Kill fast'; text reiterates 'Catering (H2) is the cheapest and strongest-evidenced branch and should be sized first' |
| Ghost-deck titles as full-sentence findings opening with SCQA | yes | Section 4 opens with Situation/Complication/Question/Answer, followed by numbered full sentences like 'Brightwell needs roughly €13m of revenue beyond what the current estate delivers on its own by 2031.' |
| Uses given facts correctly (suburban below 14% floor argues against suburban expansion) | yes | 'two of three existing formats (suburban 13.1%, kiosk 11.4%) already sit at or under the 14% floor' used to argue against funding new-store capital |
| Flags EUR 62m to EUR 80m as a large gap and states what would have to be true to close it | yes | 'Gap ... €18m (+29%, ~5.2% CAGR)' and section 5 'For this answer to hold: (a) catering's growth is real demand... (b) average catering order value is high enough... (c) online delivery economics don't quietly erode margin... (d) the 14% floor is meant to apply per-format...' |
| Must not present hypotheses as proven facts | yes | Ghost-deck items explicitly labeled '(hypothesis)'; overall answer rated 'Confidence: low-medium' and hedged with 'plausibly', 'central estimate' |
| Must not invent external benchmarks as facts | yes | The 8-12% online penetration figure and 1-2%/yr LFL growth are explicitly flagged as assumptions needing confirmation, e.g. 'a bakery/QSR delivery-penetration benchmark to replace the 8-12% online assumption' |

## Transcript

## Turn 1

**User:** Give me a day-one answer. Problem statement: Which two growth moves should the Brightwell Bakeries board fund in the 2027 budget to grow revenue from EUR 62m to EUR 80m by 2031, keeping store-level margin above 14%, with about EUR 3m of capital? In scope: new stores, online delivery, corporate catering, franchising. Facts we have: 41 stores; store margin high street 16.8%, suburban 13.1%, station kiosk 11.4%; office catering orders grew from 3,100 to 9,000 between 2023 and 2026 without sales effort; online is 4% of revenue today.

# Growth strategy, day-one answer: Brightwell Bakeries 2027 budget

## 1. The gap, and whether the four moves can plausibly close it

| | Today (2026) | Target (2031) |
|---|---|---|
| Revenue | €62m | €80m |
| Gap | | **€18m** (+29%, ~5.2% CAGR) |

**Momentum case (no new action):** not given, so flagged as an assumption — a mature 41-store estate with no new investment typically grows like-for-like at ~1–2%/yr. At 1.5%/yr, €62m becomes **~€66.8m by 2031**, leaving a **momentum gap of ~€13.2m**. *(ASSUMPTION — confirm actual 2023-26 like-for-like growth rate; this is the single most important number missing from this answer.)*

Of the four levers in scope, two are capital-heavy or slow (new stores, franchising) and two are capital-light channels that are already growing on their own (catering, online). Sizing them on wide, labelled ranges (below), the two capital-light levers plausibly close **roughly half to all of the €13.2m gap** — central estimate about two-thirds. That means €3m probably **cannot fully close the gap on its own**; the board should expect to either accept a residual gap of a few €m, extend the runway, or free a small amount of additional capital later. It should not expect four levers funded at once — the brief's own €3m ceiling rules that out.

## 2. Day-one answer

**Fund corporate catering and online delivery in the 2027 budget; do not fund broad new-store capital or franchising this cycle.** Catering is already growing ~43%/yr with zero sales effort (3,100→9,000 orders, 2023–26) — rare, free evidence of demand pull. Online is a small base (4% of revenue) with room to scale toward a category norm. Both run on the existing 41-store production backbone, so they need modest capital (~€1–1.5m each) rather than real estate. New stores should be held back because two of three existing formats (suburban 13.1%, kiosk 11.4%) already sit at or under the 14% floor, and €3m buys too few high-street sites to move the needle. Franchising is a legitimate later-stage lever but typically takes 18–24 months to stand up (legal pack, training, pipeline) before it produces revenue, which fits poorly inside a 2027–2031 window being decided now.

**Confidence: low-medium**, because the catering and online sizing both rest on assumed order values and penetration benchmarks, not client data — this is a day-one read to unblock the budget conversation, not a sized business case.

## 3. Ranked hypotheses

| # | Hypothesis | Threshold | Kill criterion | Test first? |
|---|---|---|---|---|
| H1 | Gap/momentum: the core alone misses the target by a material margin | Momentum gap > €8m by 2031 | If actual LFL growth already tracks >4%/yr, most of the gap closes without new levers — shift weight to protecting the core | Yes — frames everything else |
| H2 | Corporate catering: organic, no-effort demand converts into €2–6m of incremental revenue for ~€1–1.5m capital | Average order value ≥ €100 and growth not a one-off return-to-office bump | If avg. order value is low (<€50) or 2023–26 growth was a pandemic-recovery effect now flattening in 2026, the lever is much smaller than it looks | **Yes — first** (cheapest, strongest evidence) |
| H3 | Online delivery: scaling 4%→8-12% of revenue adds €4–7m for ~€1–1.5m capital | Comparable bakery/QSR delivery penetration benchmark ≥ 8% | If category penetration tops out near today's 4-6%, or aggregator/delivery fees push store-level margin under 14%, lever is smaller or margin-dilutive | Second |
| H4 | New stores: only high-street format clears the margin floor with headroom | High-street sites available in volume within €3m | If store counts by format aren't known, or high-street sites aren't available at volume, this lever is capital-inefficient vs. H2/H3 this cycle | Kill fast — needed mainly to confirm "don't fund" |
| H5 | Franchising: could add footprint without company capital | Time-to-first-franchised-unit revenue ≤ 2029 | If stand-up (legal, training, recruitment) runs past 2029, or royalty economics don't map to the "store-level margin" metric, defer past this budget | Kill/defer fast |

## 4. Ghost deck

**Situation:** Brightwell operates 41 stores generating €62m; the board wants €80m by 2031, funded with ~€3m in the 2027 budget, with store-level margin held above 14%.
**Complication:** Two of the four candidate levers (new stores, franchising) are capital-heavy or slow, and the existing estate already shows margin strain outside high street, right as two under-funded channels show unprompted organic demand growth.
**Question:** Which two of the four levers should the board fund in 2027 to plausibly close the gap within €3m without breaching the margin floor?
**Answer:** Fund corporate catering and online delivery; hold back broad new-store capital and defer franchising.

1. *(hypothesis)* Brightwell needs roughly €13m of revenue beyond what the current estate delivers on its own by 2031.
2. *(hypothesis)* Corporate catering has grown ~43%/yr with zero sales effort, and ~€1–1.5m in production/logistics and account management could turn it into a €2–6m revenue stream by 2031.
3. *(hypothesis)* Online delivery sits at just 4% of revenue; ~€1–1.5m to scale the channel toward 8–12% could add €4–7m by 2031.
4. *(hypothesis)* New company-owned stores should not be broadly funded in 2027: suburban and kiosk formats already sit at or under the 14% floor, and €3m buys too few high-street sites to matter.
5. *(hypothesis)* Franchising is a real medium-term lever but doesn't fit this budget cycle: typical 18–24 month stand-up time and royalty economics sit awkwardly against a 2027-2031 window and a store-level margin metric.
6. *(hypothesis)* Even optimistically, catering and online together close somewhere between half and all of the gap — the board should decide now how it wants the remainder closed.

## 5. What would have to be true, and what the full engagement tests first

For this answer to hold: (a) catering's growth is real demand, not a return-to-office blip that's already flattening; (b) average catering order value is high enough to be worth the capex; (c) online delivery economics don't quietly erode margin once platform/last-mile fees are counted; (d) the 14% floor is meant to apply per-format to company-operated stores, not as a blended group number that catering/online could mask.

A full engagement would open with four things this day-one pass had to assume: the actual 2023-26 like-for-like growth rate of the core; current catering revenue and average order value; store counts by format (to know how much of the 41 is already sub-14%); and a bakery/QSR delivery-penetration benchmark to replace the 8-12% online assumption. Catering (H2) is the cheapest and strongest-evidenced branch and should be sized first.


## Files in work dir after run


