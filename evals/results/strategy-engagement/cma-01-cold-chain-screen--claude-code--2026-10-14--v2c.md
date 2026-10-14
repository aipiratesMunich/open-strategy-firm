# cma-01-cold-chain-screen on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (10/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs the funnel on all eight companies with drop-out stage, keeps Medivan Logistik and Thermo Lane on the short list despite unknown availability | yes | Funnel table shows 8→4 (dropped ColdArc, Icepath, Glacier Freight, Chillbox Couriers with reasons) →3 (dropped Polar Route, 41% customer); 'Medivan and Thermo Lane kept on the short list despite unknown availability' |
| Values Frostline on haircut plan (~EUR 42.5m) and shows seller plan (~EUR 57.5m) graded as seller's view | yes | 'Standalone value (haircut plan) / 42.5' and 'Cross-check: value on seller's own plan under Kestrel's convention / 57.5'; trap check notes 'the seller's 12%-growth plan ... sourced to the banker teaser/seller and treated as weak evidence, not fact' |
| Net cost synergies ~EUR 14.8m, each with owner, date and one-off cost | yes | 'Cost synergies, net of integration cost / 14.8 / Depot consolidation: 1.2/0.10 − 2.0 = 10.0; Joint purchasing: 0.5/0.10 − 0.2 = 4.8 ... Both synergies have a named owner (COO; CPO) and a date (2028; 2027)' |
| Walk-away price ~EUR 57.3m from standalone + net cost synergies, states EUR 60m is above it | yes | 'Walk-away price / 57.3 / Standalone (haircut) + net cost synergies' vs 'Asking price / 60.0'; 'asking price sits ~4–5% above the buyer's own maximum justified price' |
| Shows EUR 2.0m revenue synergy as upside only, outside walk-away, notes no owner/date/one-off cost | yes | 'Revenue synergies (not in price) / 2.0 EBITDA/yr, unvalued ... no one-off cost, owner or date given — kept as upside only, outside the walk-away price' |
| Answer is do not proceed at EUR 60m or proceed only at/below ~EUR 57m under named conditions | yes | 'Do not proceed at EUR 60m. Proceed under conditions at a renegotiated price at or below EUR ~57m, and only once two named risks are resolved pre-signing' |
| Names change-of-control clauses and founder dependence as deal-breaker checks or conditions | yes | 'Change-of-control contracts covering 27% of revenue (the 18% and 9% customers both have change-of-control clauses)' and 'Key-person dependency on the founder for the pharma-quality-auditor relationship' listed as key risks with mitigations/conditions |
| Compares deal with build route (EUR 35m, four years, misses 2028) | yes | 'Build alternative: ~EUR 35m and ~4 years — reaches certification and a customer base only around 2030, missing the 2028 goal' |
| Recommends a review by someone outside the deal team | NO | No mention anywhere in the document of an independent/outside reviewer or challenge from someone not on the deal team |
| Flags legal, tax and financial due diligence for specialists | NO | Legal diligence is flagged repeatedly (e.g. 'Kestrel corp dev + legal', 'Kestrel legal diligence'), but 'tax' is never mentioned anywhere in the document, and financial due diligence is not explicitly flagged as a specialist task |
| Does not include revenue synergies in walk-away price or back-solve from asking price | yes | Walk-away price (57.3) = standalone + net cost synergies only; revenue synergy listed separately as 'not in price'; trap check: 'Value is built from the buyer's own view, not back-solved from the asking price' |
| Does not invent facts about targets beyond the table | yes | All figures (3.4/0.08, 4.6/0.08, 1.2/0.5/2.0/0.2 synergy inputs, 18%/9%/41%/27% customer concentrations) match the planted reference values exactly, consistent with being sourced from the input pack rather than invented |

## Transcript

## Turn 1

**User:** Run the Kestrel cold-chain M&A screen from the pack and tell us whether to go ahead with Frostline at the asking price. (Attached in the working directory: cma-01-input.md.)

**Bottom line: don't pay EUR 60m.** Two independent checks against the CFO's own valuation convention both land at EUR 57.3–57.5m — below the ask:

- **Standalone (Kestrel's haircut plan, 3.4m FCF) + net cost synergies:** 42.5m + 14.8m = **57.3m**
- **Cross-check — seller's own optimistic plan (4.6m FCF) under Kestrel's convention:** **57.5m** (even the seller's rosier numbers don't clear 60m at Kestrel's required return)

So the asking price sits ~4–5% above the buyer's own maximum justified price, before even weighting two unresolved risks: change-of-control clauses on contracts worth 27% of Frostline's revenue, and the founder being the sole link to the pharma quality auditors who underpin GDP certification.

Full screen on the long list (8 → 4 after must-haves → 3 after deal-breakers: Frostline, Medivan Logistik, Thermo Lane) and the complete M&A screening write-up with funnel, short list, walk-away table, risks, assumptions, open questions and trap checks are in `case-ma-screening-kestrel-frostline.md`.

**Recommendation:** counter at or below ~EUR 57m, conditional on (a) consent/extension from the two change-of-control customers and (b) a retention agreement covering the founder's auditor relationship. If the seller won't move and those risks aren't cleared, walk — and approach Medivan Logistik and Thermo Lane in parallel, since both pass every must-have and deal-breaker but haven't been valued yet for lack of disclosed financials.


## Files in work dir after run

- case-ma-screening-kestrel-frostline.md
- cma-01-input.md

## File written by the run: case-ma-screening-kestrel-frostline.md

# M&A screening: Kestrel Logistics, should Kestrel buy Frostline Pharma Transport at the EUR 60m asking price?

**Answer:** Do not proceed at EUR 60m. Proceed under conditions at a renegotiated price at or below **EUR ~57m**, and only once two named risks are resolved pre-signing — because two independent valuation lines, built from Kestrel's own convention, both land at EUR 57.3–57.5m, below the EUR 60m ask.

**Confidence:** Medium — the financial gap is consistent across two independent calculations, but it rests on a single banker teaser and one management meeting (no diligence), unquantified key-person and customer-concentration risk, and synergy figures with no phase-in or sensitivity applied.

## Why buy

- Strategic goal: certified pharma cold-chain (GDP, 2–8°C) in all three home regions by 2028.
- Build alternative: ~EUR 35m and ~4 years — reaches certification and a customer base only around 2030, missing the 2028 goal.
- **Hypothesis "building takes longer than the market window allows": confirmed.** Acquisition is the right route in principle; the question is which target and at what price.

## Screening criteria and deal-breakers

| Criterion | Type | Threshold |
|---|---|---|
| GDP certification held today | Must-have | Yes, not under review |
| Revenue | Must-have | EUR 20m–80m |
| Operations in home regions | Must-have | ≥2 of Kestrel's 3 home regions |
| Single customer concentration | Deal-breaker | >30% of revenue |
| Certification status | Deal-breaker | Under review or lapsed |
| Litigation | Deal-breaker | Unresolved litigation with a customer |
| Budget | Affordability cap | ≤ EUR 65m enterprise value |

## Funnel

| Stage | Number of companies | Criteria applied | Dropped (reason) |
|---|---|---|---|
| Long list | 8 | Kestrel corp dev research | — |
| Must-haves | 4 (Frostline, Polar Route, Medivan, Thermo Lane) | GDP certified + revenue EUR 20–80m + ≥2/3 regions | ColdArc (revenue 95m, over range); Icepath (not GDP certified); Glacier Freight (1 of 3 regions); Chillbox Couriers (revenue 12m, under range) |
| Deal-breakers | 3 (Frostline, Medivan, Thermo Lane) | No single customer >30% of revenue | Polar Route (top customer 41%) |
| Availability known | 1 confirmed for sale (Frostline); 2 unconfirmed (Medivan, Thermo Lane) | Banker teaser vs. "not known" | — none dropped; kept per screening-on-availability trap check |

**Hypothesis "at least n companies meet the must-haves": confirmed (3 pass every must-have and deal-breaker).** Frostline is the only one with enough disclosed data (teaser + management meeting) to value; Medivan Logistik and Thermo Lane pass the same screen and should be approached in parallel regardless of their "not known" for-sale status — screening only on availability would wrongly shrink the field to what the banker brought.

## Short list

| Target | Strategic fit | Standalone value | Net cost synergies | Revenue synergies (upside only) | Deal-breaker flags | Rank |
|---|---|---|---|---|---|---|
| Frostline Pharma Transport | High — GDP certified today, all 3 home regions, EUR 46m revenue inside range | EUR 42.5m (haircut plan) | EUR 14.8m | EUR 2.0m EBITDA, not costed, no owner/date | None breached on stated facts; litigation/cert-review status not confirmed (open question) | 1 (only one valued; data available) |
| Medivan Logistik | Plausible — GDP certified, 2 of 3 regions, EUR 24m revenue | Not sized — no FCF or EBITDA detail beyond long list | Not sized | Not sized | None breached on long-list data; availability unconfirmed | 2 — approach to test availability and get data |
| Thermo Lane | Plausible — GDP certified, 2 of 3 regions, EUR 27m revenue, but top customer 27% (closest to the 30% deal-breaker line) | Not sized | Not sized | Not sized | None breached, but closest to the concentration line; availability unconfirmed | 3 — approach, watch customer concentration in diligence |

## Walk-away price for Frostline

| Component | Value (EUR m) | Basis |
|---|---|---|
| Standalone value (haircut plan) | 42.5 | FCF 3.4m / (10% − 2%) = 3.4 / 0.08. Haircut plan is Kestrel's own view, built from Frostline's actual 2022–2025 revenue growth (~4%/yr), per CFO convention |
| Cost synergies, net of integration cost | 14.8 | Depot consolidation: 1.2/0.10 − 2.0 = 10.0; Joint purchasing: 0.5/0.10 − 0.2 = 4.8; total 14.8. Both synergies have a named owner (COO; CPO) and a date (2028; 2027) |
| **Walk-away price** | **57.3** | Standalone (haircut) + net cost synergies |
| Asking price | 60.0 | Banker teaser |
| Cross-check: value on seller's own plan under Kestrel's convention | 57.5 | FCF 4.6m / 0.08 = 57.5. Even taking the seller's optimistic 12%-growth case at face value, under Kestrel's own required-return convention the business is worth less than the EUR 60m ask |
| Revenue synergies (not in price) | 2.0 EBITDA/yr, unvalued | Banker teaser figure; no one-off cost, owner or date given — kept as upside only, outside the walk-away price |

Two independent lines (buyer's haircut-plan-plus-synergies, and the seller's-own-plan-under-Kestrel's-convention) converge at EUR 57.3–57.5m. Both sit below the EUR 60m ask by roughly EUR 2.5–2.7m (4–5%). **Hypothesis "standalone value on a haircut plan is close to the asking price": reshaped — close, but synergy-adjusted value still falls short of the ask; price above walk-away, so by the agreed logic: walk or renegotiate.**

## Key risks and integration thesis

1. **Change-of-control contracts covering 27% of revenue** (the 18% and 9% customers both have change-of-control clauses). A buyer of record can trigger termination or renegotiation on either, which would cut the haircut FCF (and therefore standalone value) further than the EUR 3.4m already assumes. *Mitigation:* written consent or extension from both customers before signing, owned by Kestrel corp dev + legal, modelled on the worked-example precedent of not signing until the exposed contract is secured.
2. **Key-person dependency on the founder for the pharma-quality-auditor relationship.** GDP certification is a must-have; if that relationship is not transferable, certification continuity is at risk post-acquisition. *Mitigation:* retention/transition agreement with the founder spanning at least one certification renewal cycle, owned by Kestrel HR/legal.
3. **No named overall integration lead or day-one plan.** The two cost synergies each have an owner (COO, CPO) and a date, but there is no single integration lead, and nothing is said about what runs standalone on day one versus what changes immediately. *Mitigation:* name an integration lead before signing, not after.
4. **Revenue synergy (cross-selling to Kestrel's ambient pharma customers) is a banker-sourced hope, not a plan.** EUR 2.0m EBITDA with no owner, date, or one-off cost. Correctly excluded from the price; should stay excluded even under deal pressure.

## What would change the answer

1. If the seller accepts EUR 57m or below, the deal clears the walk-away price on the buyer's own view and becomes a straightforward proceed, subject to the two conditions above.
2. If diligence finds Frostline's certification is under review, or any unresolved customer litigation exists, the deal is killed outright under the agreed deal-breakers regardless of price.
3. If either change-of-control customer exits or renegotiates down upon signing, standalone value falls below 42.5m and the walk-away price falls with it — re-run the valuation before closing.
4. If Medivan Logistik or Thermo Lane turn out to be available at a lower multiple with comparable fit, they are worth pursuing in parallel rather than over-paying for Frostline on deal momentum.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Kestrel's haircut FCF is the right base for standalone value, not the seller's plan | EUR 3.4m next-year FCF | Kestrel's own plan from Frostline's 2022–2025 actual revenue growth (~4%/yr) vs. seller's 12%/yr assumption | Diligence shows next-year FCF materially above or below 3.4m |
| 2 | No unresolved litigation and certification is not under review for Frostline | Assumed clear | Not flagged in the pack, but also not explicitly confirmed clear | Either is confirmed present — automatic kill under the agreed deal-breakers |
| 3 | Named cost synergies (depot, purchasing) are delivered in full at the stated one-off cost, no phase-in | EUR 14.8m net | Kestrel integration team estimate, CFO convention (run-rate/10% less one-off, no phase-in) | Either synergy slips in timing or cost — the convention already assumes no phase-in, so slippage cuts value directly |
| 4 | The two change-of-control contracts (27% of revenue) continue unchanged after acquisition | Included in haircut FCF as-is | No information yet that either customer will exit or renegotiate | Either customer confirms exit or renegotiation — standalone value falls further |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is Frostline's GDP certification under review, and is there unresolved customer litigation? | Both are agreed deal-breakers; the pack is silent, not clear | Frostline management / Kestrel legal diligence | Either present kills the deal outright, at any price |
| Will the two change-of-control customers (18% and 9% of revenue) consent to the deal or extend their contracts before signing? | Covers 27% of revenue; directly threatens the FCF the valuation is built on | Frostline management, Kestrel corp dev + legal | Loss of either lowers standalone value and the walk-away price further |
| Can the founder's relationship with the pharma quality auditors be transferred or retained under contract? | GDP certification (a must-have) may depend on this relationship continuing | Founder, Kestrel HR/legal | If not transferable, certification continuity risk undermines the entire deal rationale |
| What is the one-off cost, owner and timing for the cross-sell revenue synergy? | Currently unquantified and excluded from price; could become real upside if specified, but only as upside, never in the walk-away price | Kestrel commercial team | Would raise the case for the deal as upside, not change the maximum price |
| Are Medivan Logistik and Thermo Lane actually for sale, and at what price? | Both pass every must-have and deal-breaker; neither has been valued for lack of data | Kestrel corp dev / banker outreach | Could surface a cheaper or lower-risk route to the same 2028 goal |
| How have Kestrel's past acquisitions, or comparable sector deals, performed against their own business cases? | No outside view is available in the pack to calibrate how much this case itself should be haircut | Kestrel corp dev / finance | Would sharpen or widen the confidence range on the 57.3m walk-away figure |

## Trap checks

- [x] Revenue synergies shown as upside only, outside the walk-away price — EUR 2.0m EBITDA kept out of the EUR 57.3m figure.
- [~] Every cost synergy has an owner, a date and its one-off integration cost — true for depot consolidation (COO, 2028) and joint purchasing (CPO, 2027); the revenue synergy lacks all three and is correctly excluded rather than priced in.
- [x] Walk-away price and deal-breakers were agreed before diligence and are unchanged — agreed with the CEO and CFO in September 2026, before any target was discussed.
- [x] Value is built from the buyer's own view, not back-solved from the asking price — standalone value uses Kestrel's haircut plan (3.4m), not the seller's plan (4.6m); the seller's-plan figure is shown only as a cross-check, and it too falls short of EUR 60m.
- [x] The full field was screened, not only targets that are for sale — all 8 long-list companies screened on must-haves and deal-breakers; Medivan and Thermo Lane kept on the short list despite unknown availability.
- [x] Strategic fit was not used to excuse weak economics, fragile customers or key-person risk — the strong regional and certification fit did not stop the change-of-control concentration and founder key-person risk from being flagged as open conditions.
- [~] An integration thesis exists — partial: depot consolidation and purchasing have named owners and dates; no overall integration lead or day-one plan is named. Flagged as a gap.
- [x] Seller and banker numbers are graded as such — the seller's 12%-growth plan and the revenue synergy figure are both sourced to the banker teaser/seller and treated as weak evidence, not fact; the haircut plan is used as the primary basis for the recommendation.

