# cma-03-teaser-only on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Asks for strategic goal, build/partner/license alternative, budget and acceptable debt, and deal-breakers as a grouped Thursday ask, stating these must be agreed before discussing the target further | NO | Strategic goal is raised only as an open question ('What is the strategic goal...? Who can answer: Board'); the build/partner/license alternative is dismissed as 'not yet assessed — cannot be, until the strategic goal is named' rather than posed as a question; budget and acceptable debt/leverage cap |
| Computes the asking price (EUR 40m) and shows it is about 10.5x reported EBITDA | yes | "EV ≈ 8 × 5.0m = EUR 40m" and "EV against reported EBITDA is really 40/3.8 = 10.5x, not 8x." |
| Flags the EUR 1.2m add-backs as needing evidence of being truly one-off, and grades all teaser figures as seller numbers | yes | "EUR 1.2m of add-backs is 32% of reported EBITDA... an unusually large adjustment to accept on a seller's word alone"; checklist item "Seller and banker numbers graded as such: yes — every figure above is labelled seller-sourced/unverified." |
| Notes what the seller may know that Halvorsen does not and lists first data requests (accounts history, customer concentration, change-of-control, key people, pipeline evidence) | yes | Lists data requests: "3–5 years audited financials", "customer concentration, and are there change-of-control clauses", "Founder/technical lead retention plan", and pipeline backlog/conversion evidence; frames these as unknowns only the seller/data room can resolve. |
| Gives a conditional answer for Thursday with no maximum price claimed as final | yes | "Walk-away price ... Cannot be set yet" and "Don't bite yet — and don't say no either... approve sending a data request list and a signed NDA, not approve a price." |
| States that legal, tax and financial due diligence need specialists | NO | Only "Financial due diligence (quality of earnings...) and legal (customer contracts, change-of-control clauses) need to be engaged" is stated — tax due diligence/specialists are never mentioned. |
| Must not produce a valuation or 'proceed' recommendation from the teaser alone | yes | "Do not agree to a price or a go/no-go at Thursday's board call"; walk-away price explicitly left unset. |
| Must not invent sector multiples, comparable transactions or facts about Project Heron | yes | No specific comparable deals or sector multiples are cited; thresholds like '>30% of revenue' are presented as generic default playbook criteria, not fabricated facts about Heron. |

## Transcript

## Turn 1

**User:** A banker sent Halvorsen a teaser for "Project Heron", a German precision-sensor maker. Asking 8x EBITDA. Teaser says adjusted EBITDA 2025 EUR 5.0m (reported EUR 3.8m, EUR 1.2m of "one-off" items added back), revenue EUR 31m, "strong pipeline". Should we bite? Board call is Thursday.

## Bottom line for Thursday

**Don't bite yet — and don't say no either.** The teaser alone can't support a price decision; ask the board to approve sending a data request and NDA, not a number.

**The read:** the "8x EBITDA" headline is softer than it looks.
- EUR 1.2m of add-backs is **32% of reported EBITDA (EUR 3.8m)** — an unusually large adjustment to accept on a seller's word alone. If any of it is actually recurring (common with "one-off" restructuring/legal/management-fee items that reappear every year), real earnings power is closer to EUR 3.8m than EUR 5.0m.
- It's also unclear whether the 8x is quoted on reported or adjusted EBITDA — that's a **EUR 30.4m vs. EUR 40m** swing nobody's resolved. Against reported EBITDA, the real multiple is **10.5x**, not 8x.
- "Strong pipeline" has no backlog number or conversion history behind it — treat it as zero until the data room proves otherwise.

**What to ask the banker before Thursday, in writing:** (1) is the 8x on reported or adjusted EBITDA, (2) an itemized breakdown of the EUR 1.2m with a 3-year history of similar add-backs, (3) customer concentration and change-of-control clauses, (4) what "pipeline" actually consists of.

Full quick-case writeup with the issue tree, deal-breaker checklist, and open-questions table is saved at `case-manda-heron.md` in the working directory — useful as board pre-read since it shows the reasoning, not just the verdict.


## Files in work dir after run

- case-manda-heron.md

## File written by the run: case-manda-heron.md

# M&A screening: Halvorsen, should we proceed on "Project Heron" at the banker's 8x EBITDA ask?

**Answer:** Do not agree to a price or a go/no-go at Thursday's board call. Treat this as "request data room, do not value yet" — the teaser contains an earnings-quality flag large enough that the real multiple could be meaningfully higher than advertised, and we don't yet have the standalone-value, synergy or deal-breaker evidence a walk-away price needs. The board decision this week should be: approve sending a data request list and a signed NDA, not approve a price.
**Confidence:** Low, because every number in play is a single, seller-supplied figure from a one-page teaser with no audited backup — this is exactly the "seller/banker figures only" case the M&A playbook says cannot be priced.
**Specialists and review:** Financial due diligence (quality of earnings on the EUR 1.2m add-back) and legal (customer contracts, change-of-control clauses) need to be engaged before any number is discussed with the seller; someone outside the deal team should review the walk-away case once built.

## What the teaser actually says, read carefully

| Line | Value | What it implies |
|---|---|---|
| Revenue 2025 | EUR 31m | — |
| Reported EBITDA 2025 | EUR 3.8m | Reported margin 12.3% |
| Add-backs ("one-off items") | EUR 1.2m | **31.6% of reported EBITDA** — a large adjustment relative to the base it's adjusting |
| Adjusted EBITDA 2025 | EUR 5.0m | Adjusted margin 16.1% |
| Ask | 8x EBITDA | Ambiguous which EBITDA — see below |

**The ambiguity that changes the price by ~30%:** teasers almost always quote the multiple against the larger, adjusted figure, so the working assumption is EV ≈ 8 × 5.0m = **EUR 40m**. If the banker actually means 8x *reported* EBITDA, EV = 8 × 3.8m = **EUR 30.4m**. That's a EUR 9.6m swing nobody has resolved yet — the first question to put to the banker, in writing, before Thursday.

At the EUR 40m reading: EV/Revenue ≈ 1.3x, and EV against reported EBITDA is really 40/3.8 = **10.5x**, not 8x. The "8x" headline is only true if you accept the EUR 1.2m add-back at face value.

**Why the add-back is the thing to pressure-test first:** EUR 1.2m is not a rounding item — it's near a third of reported earnings. A one-off that size needs a name, a date, and proof it won't recur. "One-off" items that repeat in every annual teaser (moving costs, one-time legal fees, management-change costs that show up again next year under a different label) are the single most common way sellers manufacture an 8x story out of a 10-11x company. We have zero visibility into what the EUR 1.2m actually is, which means the real earnings power of Heron could be anywhere from EUR 3.8m to EUR 5.0m — a 32% range on the number the entire price rests on.

**"Strong pipeline"** is marketing language with no figure attached — no backlog value, no signed-vs-pipeline split, no conversion history. Treat it as zero until the data room produces an order book. This is the revenue-synergy trap in different clothes: upside we don't own, priced in by the seller as if we already do.

## Why buy
- Strategic goal for Heron specifically: **not stated in the brief** — open question for the board (capability/technology adjacency to Halvorsen's existing line, market access in Germany, or something else?).
- Alternatives (build/partner/license) considered: not yet assessed — cannot be, until the strategic goal is named.

## Screening criteria and deal-breakers
| Criterion | Type | Threshold |
|---|---|---|
| Strategic fit with Halvorsen's stated goal | Must-have | To be set by the board Thursday |
| Customer concentration | Deal-breaker (default) | No single customer >30% of revenue, pending confirmation |
| Change-of-control clauses on key contracts | Deal-breaker (default) | None unresolved at signing |
| Key-person dependence | Must-have, weighted | Founder/technical lead retention plan exists |
| Earnings quality (this teaser's add-backs) | Deal-breaker candidate | One-off items are genuinely non-recurring and documented |

## Funnel
| Stage | Number of companies | Criteria applied |
|---|---|---|
| Long list | 1 (Heron only) | None — this is a single banker-sourced target |

**Trap flag:** this is "screening on availability" — ranking by what the banker brought rather than screening the field. If precision sensors is a genuine strategic priority, the board should ask whether Heron is the best target or just the one with a banker attached, before spending diligence budget on it exclusively.

## Short list
| Target | Strategic fit | Standalone value | Net cost synergies | Revenue synergies (upside only) | Deal-breaker flags | Rank |
|---|---|---|---|---|---|---|
| Project Heron | Not yet assessed | Not computable from teaser | Not yet assessed | Not yet assessed ("strong pipeline" unverified) | Unknown — no customer/contract data | N/A — pre-screening |

## Walk-away price for Project Heron
**Not computable from a one-page teaser.** Per the case rules, when only seller/banker figures exist, the right answer is no valuation, no cap, no maximum price — the answer is the next step and the conditions under which a price can be set.

| Component | Value | Basis |
|---|---|---|
| Standalone value (haircut plan) | Not available | Needs 3–5 years audited financials, not one year of adjusted figures |
| Cost synergies, net of integration cost | Not available | Needs Halvorsen's own cost base to compare against |
| **Walk-away price** | **Cannot be set yet** | — |
| Asking price | EUR ~30.4m–40m (ambiguous, see above) | 8x on reported vs. adjusted EBITDA |
| Revenue synergies (not in price) | Not available | "Strong pipeline" unverified |

## Key risks and integration thesis
1. **Earnings quality risk:** EUR 1.2m of add-backs (32% of reported EBITDA) unexplained — mitigation: require an itemised bridge and 3-year history of adjustments before any offer; owner: deal lead + external QoE advisor.
2. **Single-source target risk:** only the banker's view exists — mitigation: confirm via one independent channel (industry contact, customer reference call) before committing diligence spend; owner: deal lead.
3. **Pipeline overstatement risk:** "strong pipeline" has no backing number — mitigation: request signed-order backlog and historical pipeline-to-revenue conversion rate; owner: commercial diligence workstream.
4. Integration thesis: **not yet written** — too early; this is normal at teaser stage, but the board should not treat the deal as further along than it is.

## What would change the answer
1. If the banker confirms the 8x is on *reported* EBITDA (EV ≈ EUR 30.4m) and the add-backs are verified as genuinely non-recurring, the effective price looks much closer to 8x real earnings and the deal clears the first filter.
2. If the EUR 1.2m turns out to be recurring (e.g., normal annual restructuring, bad-debt write-offs, or management fees that repeat), real adjusted EBITDA is closer to EUR 3.8m and the true multiple is closer to 10.5x — at that point the board should treat 8x as a negotiating opener to push down, not an attractive entry price.
3. If customer concentration or a change-of-control clause breaches Halvorsen's deal-breakers, recommendation becomes do-not-proceed regardless of price (per the playbook's own worked precedent).

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | "8x EBITDA" is quoted against the adjusted figure | EV ≈ EUR 40m | Standard teaser convention (sellers quote off the larger number) | Banker confirms it's 8x reported EBITDA → EV ≈ EUR 30.4m |
| 2 | Halvorsen has an unstated strategic rationale for precision sensors | Treated as open, not assumed | Not in the brief | Board states the goal Thursday — revisit strategic fit branch |
| 3 | The EUR 1.2m add-back is treated as unverified, not accepted at face value | Range EUR 3.8m–5.0m EBITDA | No breakdown provided in teaser | Itemised QoE bridge narrows the range |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is the 8x multiple quoted on reported or adjusted EBITDA? | Changes implied EV by ~EUR 9.6m | Banker | Resets the entire price-anchor discussion |
| What exactly are the EUR 1.2m "one-off" items, and have similar add-backs appeared in prior years? | Determines true earnings power; recurring "one-offs" are the classic teaser red flag | Seller, via data room / QoE advisor | Could move real EBITDA anywhere in the EUR 3.8m–5.0m range |
| What is the strategic goal this acquisition serves for Halvorsen, and by when? | Without it, strategic fit and the build/partner/license alternative can't be tested | Board | Could kill the deal on strategic grounds regardless of price |
| What is customer concentration, and are there change-of-control clauses on major contracts? | Default deal-breakers per the playbook | Data room | Could be an immediate do-not-proceed, independent of price |
| What does "strong pipeline" consist of — signed backlog vs. unconverted leads, and historical conversion rate? | Currently a zero-evidence claim being used to justify the price | Seller / commercial diligence | Determines whether any revenue upside can be named at all, and it stays out of the price either way |
| 3–5 years of audited financials and EBITDA bridges | Needed to build a haircut-plan standalone valuation | Data room | Only this enables an actual walk-away price |
| Net debt and working capital position | Needed to go from EV to an equity price | Data room | Changes the actual cash price regardless of EBITDA multiple |

## Trap checks
- [x] Revenue synergies shown as upside only, outside any price: yes — "strong pipeline" explicitly excluded from any valuation above; zero value assigned until evidenced.
- [ ] Every cost synergy has an owner, a date and its one-off integration cost: **open** — no synergy case exists yet at teaser stage; flagged as a workplan item once Halvorsen's strategic goal is confirmed.
- [x] Walk-away price and deal-breakers agreed before diligence starts: deal-breakers are drafted above (customer concentration, change-of-control, key-person) pending board confirmation; no walk-away price set yet, by design — that is the point of this answer.
- [x] Value built from buyer's own view, not back-solved from the asking price: yes — this note explicitly declines to anchor on the 8x headline and instead recomputes the implied multiple against reported earnings.
- [ ] Full field screened, not only targets for sale: **open/no** — Heron is the only target in view; flagged above as the "screening on availability" trap for the board to weigh in on.
- [x] Strategic fit not used to excuse weak economics: n/a yet — no strategic fit case has been made, so nothing to excuse; recommendation is explicitly to not let deal momentum substitute for that case.
- [ ] Integration thesis exists: **open** — correctly not written yet at this stage; named as a later workplan step, not skipped.
- [x] Seller and banker numbers graded as such: yes — every figure above is labelled seller-sourced/unverified; none is presented as fact.

