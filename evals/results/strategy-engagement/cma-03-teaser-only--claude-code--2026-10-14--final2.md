# cma-03-teaser-only on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: asks, in one grouped message or as an explicit list for Thursday, for the strategic goal, the build, partner or license alternative, the budget and acceptable debt, and the deal-breakers, and says these should be agreed before the target is discussed further. | NO | Strategic goal and deal-breakers are raised ('Strategic goal: not stated... first gap', 'customer concentration, key-person dependence, export-control licensing gap, unresolved change-of-control clauses'), and alternatives are mentioned only as 'not yet assessed', but budget and acceptable debt capa |
| Must: computes the asking price (EUR 40m) and shows it is about 10.5x reported EBITDA. | NO | The run computes '8x the reported EUR 3.8m EBITDA = EUR 30.4m; 8x the "adjusted" EUR 5.0m = EUR 40.0m' — it never divides the EUR 40m asking price by reported EBITDA (40/3.8≈10.5x); instead it frames two separate 8x scenarios and a EUR 9.6m gap. |
| Must: flags the EUR 1.2m add-backs (24% of adjusted EBITDA) as needing evidence that they are truly one-off, and grades all teaser figures as seller numbers. | yes | 'a EUR 1.2m add-back on a EUR 3.8m reported base is a 32% uplift... Nobody should treat EUR 5.0m as the number until the add-backs are itemized and tested' and 'every figure in the teaser is seller-selected and unverified.' |
| Must: notes what the seller may know that Halvorsen does not and lists the first data requests (e.g. three years of accounts, customer concentration, change-of-control clauses, key people, the "pipeline" behind the growth claim). | yes | 'Why does the teaser show only 2025 figures with nothing for 2026? Possible sign of a 2026 slowdown being obscured' implies seller-side knowledge gap; data requests listed include '3 years of audited accounts... customer list with concentration and contract terms... pension schedule, 2026 YTD manage |
| Must: gives a conditional answer for Thursday (e.g. do not bid on the teaser; proceed to a first look only if the goal and deal-breakers are agreed and the add-backs hold), with no maximum price claimed as final. | yes | 'Do not proceed, do not pass... proceed under conditions: authorize the advisor to push the bank for an NDA-covered data room... No valuation, cap or maximum price can be set from a one-page teaser.' |
| Must: states that legal, tax and financial due diligence need specialists. | yes | 'financial due diligence / QoE advisor (the EBITDA bridge), German tax/legal counsel (Pensionsrückstellungen, Organschaft, change-of-control and works-council exposure), export-control counsel...' |
| Must not: produce a valuation or "proceed" recommendation from the teaser alone. | yes | 'No valuation, cap or maximum price can be set from a one-page teaser' and the recommendation is conditional, gated on a data room, not an unconditional deal proceed. |
| Must not: invent sector multiples, comparable transactions or facts about Project Heron. | yes | H2 explicitly states 'No comparable transaction or trading multiple data in hand' rather than inventing one; generic Mittelstand risk patterns (pensions, one-off cost categories) are flagged as possibilities, not asserted as facts about Heron. |

## Transcript

## Turn 1

**User:** A banker sent Halvorsen a teaser for "Project Heron", a German precision-sensor maker. Asking 8x EBITDA. Teaser says adjusted EBITDA 2025 EUR 5.0m (reported EUR 3.8m, EUR 1.2m of "one-off" items added back), revenue EUR 31m, "strong pipeline". Should we bite? Board call is Thursday.

**Short answer: don't bite Thursday — and don't let the bank anchor the room on 8x.**

The teaser's own numbers hide a EUR 9.6m swing: 8x the reported EUR 3.8m EBITDA = EUR 30.4m; 8x the "adjusted" EUR 5.0m = EUR 40.0m. That gap is entirely the EUR 1.2m of add-backs — a 32% uplift to the earnings base — and the teaser gives zero itemization of what they are. Until that's broken out and tested against 2023–2024 (did these "one-offs" show up before?), there's no real number to put 8x against.

Two more flags worth raising at the board call:
- The teaser leads with **2025** EBITDA only, with nothing for 2026 — worth asking directly whether that's because 2026 is tracking worse.
- "Strong pipeline" is pure sales language with no backlog, win-rate, or churn data behind it — treat it as zero evidence until backed by numbers.

My recommendation for Thursday: get board sign-off to request an NDA-covered data room (3 years of audited accounts, itemized EBITDA bridge, customer concentration, net debt, pension schedule, 2026 YTD actuals) — but don't discuss price with the bank yet, and don't let deal momentum set in before you've named the actual strategic rationale for buying this target at all.

Full write-up with the hypothesis table, deal-breaker checklist (customer concentration, change-of-control clauses, German pension liabilities, export-control licensing — all common landmines in Mittelstand precision-engineering deals), and open-questions table saved to `case-ma-screening-project-heron.md` in the working directory.


## Files in work dir after run

- case-ma-screening-project-heron.md

## File written by the run: case-ma-screening-project-heron.md

# M&A screening: Halvorsen, should we bite on Project Heron at the banker's 8x ask, and what do we tell the board Thursday?

**Answer:** Do not proceed, do not pass, and do not give the board a price view yet — **proceed under conditions**: authorize the advisor to push the bank for an NDA-covered data room and a management meeting before Thursday's call ends with anything stronger than "conditional interest." No valuation, cap or maximum price can be set from a one-page teaser; the number that decides this (clean, sustainable EBITDA) has not been shown to us.
**Confidence:** low on the price, high on the process recommendation — because every figure in the teaser is seller-selected and unverified, but the gap between the two plausible readings of "8x" is EUR 9.6m, which alone is reason enough not to anchor on it Thursday.
**Specialists and review:** financial due diligence / QoE advisor (the EBITDA bridge), German tax/legal counsel (Pensionsrückstellungen, Organschaft, change-of-control and works-council exposure), export-control counsel (precision sensors can fall under German/EU dual-use licensing), someone outside the deal team to sanity-check before any indicative offer is sent.

## Why buy
- Strategic goal: not stated in the brief. **This is the first gap** — "precision-sensor maker" fitting Halvorsen's goal (capability, geography, customer access, scale) is assumed, not established. Flagged below as the top open question.
- Alternatives considered (build / partner / license): not yet assessed — cannot be, until the strategic goal is named.

## The one number that should drive Thursday's discussion: which EBITDA is the "8x" on?

| Basis | EBITDA (EUR m) | Margin on EUR 31m revenue | Implied price at 8x (EUR m) |
|---|---|---|---|
| Reported | 3.8 | 12.3% | 30.4 |
| Adjusted (banker's) | 5.0 | 16.1% | 40.0 |
| **Gap** | **1.2** | **3.9 pts** | **9.6** |

The teaser's arithmetic ties (3.8 + 1.2 = 5.0), but a EUR 1.2m add-back on a EUR 3.8m reported base is a 32% uplift to the earnings base the multiple is applied to — that swing alone is EUR 9.6m of price, before any discussion of whether 8x itself is the right multiple for this asset. **Nobody should treat EUR 5.0m as the number until the add-backs are itemized and tested**, not EUR 3.8m.

## Quality-of-earnings reality check on the teaser
- "One-off items" of EUR 1.2m: the teaser gives no itemization. In German Mittelstand sellside teasers, common items hiding under "one-off" include owner/family compensation normalization, bad-debt or inventory write-downs that recur most years, one-time legal or restructuring costs, and deal-process fees already incurred. Each needs its own line, its cash-flow trail, and a check against whether an item with the same label appeared in 2023 and 2024 (if it did, it is not one-off).
- The teaser shows only 2025 figures. Today is October 2026 — full-year 2025 actuals are over a year old, and no 2026 figure is shown at all. That omission is itself a signal worth asking about directly: is 2026 tracking below 2025, and is that why the teaser leads with the older, better-looking year?
- "Strong pipeline" is unsupported sales language — no backlog, no contracted order book, no win-rate, no churn or customer-retention figure behind it. Treat it as zero evidence until backed by numbers.
- No net debt, no capex history, no working-capital trend, no customer concentration, no key-person or employee dependency, no pension liability (Pensionsrückstellungen are commonly material and underfunded in German manufacturing SMEs), no mention of change-of-control clauses in major customer contracts.

## Hypotheses and kill criteria

| # | Hypothesis | Threshold | Kill criterion | Status |
|---|---|---|---|---|
| H1 | Adjusted EBITDA of EUR 5.0m fairly represents sustainable earnings | Every add-back item is individually named, cash-traceable, and absent from 2023–2024 accounts | Any add-back item recurs in prior years or is an operating cost by nature (e.g. bad debt, warranty, inventory write-down) | Open — no itemization provided |
| H2 | 8x EBITDA is a sector-appropriate multiple for this asset | Comparable precision-sensor/instrumentation deal or trading multiples bracket 8x | No comparable transaction or trading multiple data in hand | Open — unverified, needs desk research before any counter |
| H3 | "Strong pipeline" supports paying for growth, not just today's earnings | A contracted or weighted order book exists and is quantified | Pipeline is qualitative sales language with no backlog or win-rate behind it | Killed as evidence; stands as unverified claim only |
| H4 | The target fits Halvorsen's stated strategic goal and clears the agreed deal-breakers | Strategic goal is named by the board and the target advances it; no deal-breaker present | Any of customer concentration, key-person dependence, export-control licensing gap, unresolved change-of-control clauses | Open — strategic goal itself not yet named by the board |

Every hypothesis that matters is still open. That is the honest state of play two days before the board call — not "yes," not "no," but "not yet decidable on this document."

## What to tell the board Thursday
1. The teaser's own numbers contain a EUR 9.6m swing depending on which EBITDA the 8x applies to — do not let the bank anchor the room on EUR 40m.
2. We have no evidence yet for the add-backs, the pipeline, or 2026 trading — all three are sales-side claims, not facts.
3. Recommended board decision: approve signing an NDA and requesting a data room (3 years of audited accounts, a detailed EBITDA bridge, customer list with concentration and contract terms, net debt and pension schedule, 2026 YTD management accounts) — and approve, separately, naming the strategic rationale that would make this target worth owning at any price, so the next conversation isn't anchored on the seller's number either.
4. No indicative offer, no exclusivity, and no price discussed with the bank until that data is in hand.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Halvorsen has a strategic rationale for buying a precision-sensor maker | Assumed to exist but unstated | Not given in the brief | No credible rationale exists — then the answer is simply "pass," independent of price |
| 2 | "8x EBITDA" in the teaser refers to enterprise value, not equity value | EV/EBITDA | Standard banker convention | Teaser means equity value — net debt and pensions would need to be added back to get EV, raising the real multiple further |
| 3 | The EUR 1.2m add-back pool is a single aggregate, not multiple distinct unverified items of varying quality | Treated as one unverified block | Teaser gives no breakdown | A breakdown shows most items are genuinely non-recurring — EBITDA case strengthens; shows the opposite — it weakens further |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What strategic goal does this deal serve, and by when? | Without it, no price — however attractive — can be judged against alternatives (build/partner/license) | Halvorsen board/exec team | Determines whether this is even the right conversation to have Thursday |
| Itemized breakdown of the EUR 1.2m "one-off" add-backs, with 2023–2025 trend | Decides whether true earnings base is EUR 3.8m, EUR 5.0m, or something between | Seller, via data room / QoE advisor | Could move implied price by up to EUR 9.6m at the stated multiple |
| Why does the teaser show only 2025 figures with nothing for 2026? | Possible sign of a 2026 slowdown being obscured by using the better-looking prior year | Seller / banker, pressure-test directly | A 2026 decline would argue for a lower multiple or walking away |
| Is "8x" benchmarked against actual comparable transactions in precision sensors/instrumentation? | Determines whether 8x is a market rate or a banker's opening anchor | Desk research / sector banker comps (not yet done) | If comps run meaningfully lower, 8x is a starting point to negotiate down, not a reference price |
| Customer concentration, key-person dependence, change-of-control clauses, pension liabilities | Classic German Mittelstand deal-breakers; any one unresolved can kill the deal regardless of price | Data room, legal/tax due diligence | A breached deal-breaker (e.g., >30% revenue with one customer with a change-of-control exit clause) could end the deal at any price |
| Is "strong pipeline" backed by a contracted or weighted order book? | Distinguishes real growth support from sales language | Seller management meeting | No backing means pipeline should be valued at zero in any price discussion |

