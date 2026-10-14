# cma-03-teaser-only on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Asks, grouped or as explicit list for Thursday, for strategic goal, build/partner/license alternative, budget and acceptable debt, and deal-breakers, stating these should be agreed before target is discussed further | NO | Strategic goal and build/partner/license alternative are raised ('why is a full acquisition the right route versus a supply agreement, licensing, or minority stake?') and deal-breakers are flagged, but budget/acceptable debt level is never requested — instead the memo says 'Park a price view entirel |
| Computes the asking price (EUR 40m) and shows it is about 10.5x reported EBITDA | yes | 'Asking price (8x adjusted EBITDA) / EUR 40.0m / 8 × 5.0' and 'Same price expressed on reported EBITDA / 10.5x / 40.0 / 3.8' |
| Flags the EUR 1.2m add-backs as needing evidence they are truly one-off, and grades all teaser figures as seller numbers | yes | 'Treat the EUR 1.2m as unverified seller claim (weak evidence, blocker-grade until sourced)' and 'Confidence: Low, because every number in the teaser is seller-supplied, unaudited at this stage, and unverified by us' |
| Notes what the seller may know that Halvorsen does not and lists first data requests (accounts history, customer concentration, change-of-control, key people, pipeline behind growth claim) | yes | Open-questions table repeatedly marks 'Who can answer: Seller' for net debt, customer concentration, pipeline, trend data, etc., and explicitly lists 'Change-of-control clauses,' 'Key-person dependence,' '3–5 year financials,' and pipeline substantiation as required requests. |
| Gives a conditional answer for Thursday (don't bid on teaser; proceed to first look only if goal/deal-breakers agreed and add-backs hold), with no maximum price claimed as final | yes | 'Short answer: don't bite yet — you can't, on a teaser alone' and 'Recommendation for Thursday: don't authorize an indicative offer yet — authorize the data request instead,' with no final price ceiling given. |
| States that legal, tax and financial due diligence need specialists | yes | 'Quality-of-earnings (QoE) review of the EUR 1.2m add-backs is the single highest-priority next step... legal/tax due diligence on the German entity... should be scoped in parallel' |
| Must not produce a valuation or 'proceed' recommendation from the teaser alone | yes | 'Do not proceed to a price yet... no valuation or cap can be responsibly set' — only recomputes the seller's own asking multiple, does not issue an independent valuation or proceed call. |
| Must not invent sector multiples, comparable transactions or facts about Project Heron | yes | 'I didn't have web access this session, so I couldn't benchmark 8x/10.5x against actual recent precision-sensor or German Mittelstand industrial deal comps — that's listed as an open question' — no fabricated comps or facts introduced. |

## Transcript

## Turn 1

**User:** A banker sent Halvorsen a teaser for "Project Heron", a German precision-sensor maker. Asking 8x EBITDA. Teaser says adjusted EBITDA 2025 EUR 5.0m (reported EUR 3.8m, EUR 1.2m of "one-off" items added back), revenue EUR 31m, "strong pipeline". Should we bite? Board call is Thursday.

**Short answer: don't bite yet — you can't, on a teaser alone.**

The headline number is doing work on you. "8x" is 8x a seller-adjusted EBITDA (€5.0m) that's 32% above reported EBITDA (€3.8m). The same €40.0m asking price is really **10.5x reported EBITDA**, not 8x. Use that number in the boardroom, not the banker's.

Three things to flag Thursday:
1. **The €1.2m of add-backs are unitemized and unverified** — that's the single number that decides whether this is an 8x or 10.5x+ deal. Until there's a line-by-line bridge with a multi-year trend, treat it as a seller claim, not a fact.
2. **"Strong pipeline" has no number behind it** — no stage breakdown, no close rate, no names. Zero evidentiary weight as it stands.
3. **No strategic rationale has been stated** — what does Heron actually get Halvorsen (capability, customers, technology) that build/partner/license couldn't? Price discipline has no anchor without this.

I wrote the full case to `case-ma-screening-project-heron.md`, including the data request list for the banker (QoE bridge, 3–5yr financials, net debt, customer concentration, capex vs. depreciation, export-control status) and the deal-breakers the board should set before any more contact. Recommendation for Thursday: don't authorize an indicative offer yet — authorize the data request instead.

One caveat: I didn't have web access this session, so I couldn't benchmark 8x/10.5x against actual recent precision-sensor or German Mittelstand industrial deal comps — that's listed as an open question and worth getting from your banker or a deal database before you anchor on whether even 8x is rich.


## Files in work dir after run

- case-ma-screening-project-heron.md

## File written by the run: case-ma-screening-project-heron.md

# M&A screening: Halvorsen, should we bid for "Project Heron" at the 8x EBITDA asking level?

**Answer:** Do not proceed to a price yet. On the numbers in the teaser alone, no valuation or cap can be responsibly set — the headline "8x" is 8x a seller-adjusted EBITDA that is 32% above reported EBITDA, and nothing in the teaser has been verified. The decision today is: request a defined data set before the board authorises an indicative offer, and go in (if at all) referencing reported EBITDA, not adjusted.
**Confidence:** Low, because every number in the teaser is seller-supplied, unaudited at this stage, and unverified by us.
**Specialists and review:** Quality-of-earnings (QoE) review of the EUR 1.2m add-backs is the single highest-priority next step before any indicative offer; legal/tax due diligence on the German entity (Mittelstand GmbH structures often carry pension, warranty and works-council obligations) should be scoped in parallel once exclusivity is discussed.

## The deciding numbers (recompute before Thursday)

| Metric | Value | Basis |
|---|---|---|
| Revenue 2025 | EUR 31.0m | Teaser |
| Reported EBITDA 2025 | EUR 3.8m (12.3% margin) | Teaser |
| Add-backs ("one-offs") | EUR 1.2m | Teaser, unitemised |
| **Adjusted EBITDA 2025** | **EUR 5.0m (16.1% margin)** | Teaser |
| Add-back as % of reported EBITDA | **+32%** | 1.2 / 3.8 |
| Asking price (8x adjusted EBITDA) | **EUR 40.0m** | 8 × 5.0 |
| **Same price expressed on reported EBITDA** | **10.5x** | 40.0 / 3.8 |
| Asking price / revenue | 1.29x | 40.0 / 31.0 |

**So-what:** the "8x" pitch is doing work. A third of the EBITDA the multiple is applied to is seller add-backs that are not yet explained. Strip them out and the same price is 10.5x reported earnings — a materially richer deal than the teaser headline suggests. Until the add-backs are substantiated line by line, treat the asking price as 10.5x, not 8x, for board discussion purposes.

## Why buy — not yet established

The teaser doesn't say, and neither has the board call brief: what strategic goal does Heron serve for Halvorsen (capability, customer access, geography, technology), and why is a full acquisition the right route versus a supply agreement, licensing, or minority stake? Until this is answered, "it's cheap" or "the banker says it's unique" is not a reason to bid. **Open question for the board: state the strategic goal in one sentence before authorising an indicative offer.**

## Screening criteria and deal-breakers — not yet set

Agree these before any number is discussed further, so they aren't bent to fit a target the board already likes:

| Criterion | Type | Threshold (to be set by board) |
|---|---|---|
| Customer concentration | Deal-breaker | e.g. no single customer > 20–30% of revenue |
| Key-person dependence (founder/technical lead) | Deal-breaker | Retention/earn-out required if > X% of IP or client relationships sit with one person |
| Change-of-control clauses in major contracts | Deal-breaker | None triggering cancellation or repricing |
| Regulatory/export control (precision sensors can be dual-use) | Deal-breaker | Clean export-control history; no ITAR/dual-use flags |
| Leverage impact | Must-have | Deal financeable without breaching Halvorsen's covenant headroom |

## Quality-of-earnings: the EUR 1.2m add-back

This is the single number that decides whether "8x" is even the right starting point. Request an itemised bridge from reported to adjusted EBITDA:

| Likely add-back category | Legitimate? | What to check |
|---|---|---|
| Owner/family compensation above market rate | Often legitimate | Comparable market salary for the role |
| One-off legal, restructuring, relocation costs | Sometimes legitimate | Evidence the cost truly won't recur (not three years running) |
| Inventory write-offs, bad debt | Rarely legitimate as "one-off" in a manufacturer | Trend over 3–5 years — recurring write-offs are a cost of doing business, not one-off |
| Deferred maintenance / capex treated as opex avoidance | Red flag | Capex history vs depreciation — precision manufacturing is capital-intensive; under-maintained tooling inflates EBITDA and understates near-term capex need |
| FX or one-time customer rebate/settlement | Sometimes legitimate | Check if repeated in adjacent years |

**Trap check (logic-gaps/weak-evidence):** "one-off" items appearing in a single teaser year, with no multi-year add-back history shown, is exactly the pattern a seller uses to justify a higher multiple. Treat the EUR 1.2m as **unverified seller claim (weak evidence, blocker-grade until sourced)** — it is management's own number repeated back as a finding, with no independent support.

## "Strong pipeline" — unsourced

Flag this explicitly to the board: "strong pipeline" is marketing language with no number, no conversion rate, and no customer names attached. Before it factors into any valuation upside, request: pipeline value by stage, historical close rate on pipeline of this stated size, and how much of the 2025 revenue (or adjusted EBITDA) already assumes pipeline conversion that hasn't closed. Do not let it support a higher price; treat it as unverified upside only, same as any revenue synergy.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | "8x" is EV/adjusted EBITDA (not equity value) | EV = EUR 40.0m | Standard teaser convention | If actually equity value, net debt/cash unknown and EV could differ materially |
| 2 | No other data exists yet beyond the teaser | — | User statement | If Halvorsen already has management accounts, prior-year figures, or a data room, redo this analysis on that basis |
| 3 | Halvorsen has a defined strategic rationale for sensor capability | Unstated | Not provided | If no clear rationale exists, this is reason alone to pause regardless of price |

## Open questions (bring these to Thursday's board call)

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What strategic goal does Heron serve, and why acquisition over build/partner/license? | Without this, price discipline has no anchor | Halvorsen board/strategy lead | Could kill the case regardless of price |
| Itemised bridge for the EUR 1.2m add-backs, 3–5 year trend | Decides whether the real multiple is 8x or 10.5x+ | Seller/banker, verified by QoE advisor | Could move walk-away price down materially or kill the deal |
| Net debt / cash position | 8x EBITDA is meaningless without knowing EV vs. equity price | Seller, via banker | Changes actual cash price |
| Revenue and EBITDA trend, last 3–5 years (not just 2025) | One good year could be the top of a cycle; precision-sensor demand is capex-cyclical (semiconductor, auto) | Seller | Could reshape or kill "standalone value" hypothesis |
| Customer concentration (top 1, top 3, top 5 customers as % of revenue) | Deal-breaker check | Seller, verified in diligence | Could trigger deal-breaker |
| "Strong pipeline": value by stage, historical close rate, names | Currently zero evidentiary weight | Seller, verified independently if possible | Should not support any price premium until verified |
| Capex history vs. depreciation | Precision manufacturing is capital-intensive; EBITDA can overstate cash generation if underinvested | Seller | Could lower standalone value materially |
| Export control / dual-use classification of the sensor products | Legal deal-breaker risk specific to precision sensors | Legal/export-control specialist | Could be a deal-breaker outright |
| Sector-comparable multiples for precision sensor/instrument M&A | No independent benchmark yet for whether 8x (or 10.5x) is rich or fair | External data (deal comps, industry reports) — not available in this session | Recalibrates whether "8x" is even attractive before touching add-backs |

## Recommendation for the board call

1. Do **not** authorise an indicative offer referencing "8x" without first re-anchoring the discussion on **10.5x reported EBITDA** — the add-backs are unverified.
2. Agree the strategic rationale and deal-breakers in the room, before any more banker contact.
3. Request, via the banker, before any further step: QoE bridge detail, 3–5 year financials, net debt, customer concentration, and pipeline substantiation.
4. Park a price view entirely until that data lands — this is a "do not proceed at any price until conditions are met" case, not a "proceed at 8x" or "proceed at a lower multiple" case. The teaser alone cannot responsibly support a number.

