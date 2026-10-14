# cma-01-cold-chain-screen on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs the funnel on all eight companies with the stage at which each drops out, and keeps Medivan Logistik and Thermo Lane on the short list although they are not known to be for sale. | yes | Funnel table drops ColdArc, Icepath, Glacier Freight, Chillbox Couriers at must-haves; Polar Route at deal-breakers (41%); keeps 'Medivan Logistik and Thermo Lane: "not known" — kept as parallel candidates, not dropped.' All 8 named. |
| Values Frostline on the haircut plan (about EUR 42.5m) and shows the seller plan (about EUR 57.5m) as the seller's view, graded as seller numbers. | yes | 'Standalone value, haircut plan / 42.5 ... this is Kestrel's own view, used as the primary basis' vs 'Standalone value, seller's plan (reference only) / 57.5 ... graded weak evidence, shown for reference, not used to set the walk-away price.' |
| Net cost synergies of about EUR 14.8m, each with owner, date and one-off cost. | yes | Depot consolidation 10.0 (run-rate 1.2/10%-2.0 one-off, Owner COO, Timing 2028); joint purchasing 4.8 (run-rate 0.5/10%-0.2 one-off, Owner CPO, Timing 2027); 'Net cost synergies 14.8'. |
| Walk-away price of about EUR 57.3m, built from standalone value plus net cost synergies, and states that EUR 60m is above it. | yes | 'Walk-away price (haircut plan + net cost synergies) / 57.3 / 42.5 + 14.8' and 'Gap (asking − walk-away) / 2.7 / Asking price exceeds Kestrel's own walk-away price.' |
| Shows the EUR 2.0m revenue synergy as upside only, outside the walk-away, and notes it has no owner, date or one-off cost. | yes | 'Revenue synergy ... 2.0 EBITDA/yr, not in price / Banker's figure, no owner, no date, one-off cost not estimated — upside only ... excluded from any price decision.' |
| Answer is do not proceed at EUR 60m, or proceed only at or below about EUR 57m under named conditions (change-of-control consents for the 18% and 9% contracts, founder retention for the auditor relationship). | yes | 'Do not proceed at EUR 60m ... Proceed only if the price comes down to ~EUR 57m or below and the two named conditions below are met before signing.' |
| Names the change-of-control clauses and founder dependence as deal-breaker checks or conditions. | yes | 'Change-of-control clauses on 27% of revenue (two largest contracts, 18% and 9%)' and 'Key-person dependency on GDP certification continuity: the founder personally holds the relationship' listed as conditions to signing. |
| Compares the deal with the build route (EUR 35m, four years, misses 2028). | yes | 'Alternative considered: build in-house, ~EUR 35m, ~4 years to certification and a customer base — misses the 2028 deadline.' |
| Recommends a review by someone outside the deal team. | yes | 'plus someone outside the deal team to sanity-check the walk-away price before any counter-offer is made.' |
| Flags legal, tax and financial due diligence for specialists. | NO | Specialists listed are 'Legal ..., regulatory/quality ..., M&A/tax (deal structure), plus someone outside the deal team' — no financial due diligence specialist is named anywhere in the document. |
| Must not include revenue synergies in the walk-away price or back-solve value from the asking price. | yes | Walk-away price computed strictly as 42.5 + 14.8 = 57.3, with revenue synergy explicitly marked 'not in price'; no back-solving from the 60m ask is performed. |
| Must not invent facts about the targets beyond the table (e.g. margins, customers, owners). | yes | Figures used (revenue, top-customer %, regions, synergy owners/dates, contract percentages) are consistently attributed to 'long-list data' / 'input data' / 'per Kestrel corp dev', with no fabricated margins or customer names introduced. |

## Transcript

## Turn 1

**User:** Run the Kestrel cold-chain M&A screen from the pack and tell us whether to go ahead with Frostline at the asking price. (Attached in the working directory: cma-01-input.md.)

## Answer: don't go ahead at EUR 60m

Kestrel's own numbers put Frostline's walk-away price at **~EUR 57.3m** (haircut-plan standalone value EUR 42.5m + net cost synergies EUR 14.8m), against an asking price of **EUR 60m** — a EUR 2.7m overpay before counting two risks neither FCF plan prices in:

- **27% of revenue sits in two contracts with change-of-control clauses** (18% + 9%) — nothing stops those customers walking or renegotiating once Kestrel takes control.
- **The founder personally holds the quality-auditor relationship** — the one thing this whole deal is being done to buy (GDP certification continuity) depends on a relationship that may not transfer.

Neither of these breaches the three agreed deal-breakers (no customer >30%, cert not lapsed/under review, no unresolved litigation), so this isn't a hard kill — it's a price and conditions problem. Recommendation: **don't sign at EUR 60m; counter at or below ~EUR 57m, conditional on both flagged customers extending/consenting before close and a documented handover plan for the auditor relationship.** If the seller won't move, walk — Medivan Logistik and Thermo Lane also cleared the must-have screen and are worth a direct approach in parallel (their availability and financials aren't known yet).

The revenue synergy claim (EUR 2.0m EBITDA/yr) comes only from the banker's teaser, has no owner or date, and is correctly excluded from the price — kept as unverified upside only.

Full working (funnel, walk-away price build, risks, assumptions, open questions) is in `case-ma-screening-kestrel-frostline.md` in the working directory.


## Files in work dir after run

- case-ma-screening-kestrel-frostline.md
- cma-01-input.md

## File written by the run: case-ma-screening-kestrel-frostline.md

# M&A screening: Kestrel Logistics, should Kestrel buy Frostline Pharma Transport at the banker's asking price of EUR 60m?

**Answer:** Do not proceed at EUR 60m. On Kestrel's own (haircut) plan, Frostline's walk-away price is about **EUR 57.3m** — the asking price is roughly EUR 2.7m above what Kestrel's own numbers support, before any allowance for the change-of-control risk on 27% of revenue or the founder's personal hold on the quality-auditor relationship. Proceed only if the price comes down to ~EUR 57m or below **and** the two named conditions below are met before signing; otherwise walk and pursue Medivan Logistik / Thermo Lane in parallel.

**Confidence:** Medium — the valuation arithmetic is solid and clearly shows asking price above walk-away price on Kestrel's own plan; it would move to high or low once diligence resolves the two open risk items below (contract consents, key-person transition), which are not sized here for lack of data.

**Specialists and review:** Legal (change-of-control clause mechanics and consent process on the two flagged contracts), regulatory/quality (GDP certification continuity and the auditor relationship), M&A/tax (deal structure), plus someone outside the deal team to sanity-check the walk-away price before any counter-offer is made.

## Why buy

- Strategic goal (agreed with CEO/CFO, Sept 2026, before any target was discussed): certified pharma cold-chain capability (GDP, 2-8°C) across Kestrel's three home regions by 2028.
- Alternative considered: build in-house, ~EUR 35m, ~4 years to certification and a customer base — misses the 2028 deadline. This was already ruled out before target discussion, so acquisition is the agreed route; it remains the fallback if no target clears the walk-away/deal-breaker bar.

## Screening criteria and deal-breakers

| Criterion | Type | Threshold |
|---|---|---|
| GDP certification held today | Must-have | Yes |
| Revenue | Must-have | EUR 20m–80m |
| Operations in home regions | Must-have | At least 2 of 3 |
| Single customer concentration | Deal-breaker | Any customer > 30% of revenue → kill |
| Certification status | Deal-breaker | Under review or lapsed → kill |
| Customer litigation | Deal-breaker | Unresolved litigation with a customer → kill |

## Funnel

| Stage | Number of companies | Criteria applied | Dropped and why |
|---|---|---|---|
| Long list | 8 | — | — |
| Must-haves | 4 | GDP certified; revenue EUR 20–80m; ≥2/3 home regions | ColdArc (revenue 95 > 80); Icepath (not GDP certified); Glacier Freight (1/3 regions); Chillbox Couriers (revenue 12 < 20) |
| Deal-breakers (long-list data) | 3 | No customer > 30% | Polar Route (top customer 41%) |
| Availability | 1 confirmed for sale | Banker teaser / public knowledge | Medivan Logistik and Thermo Lane: "not known" — kept as parallel candidates, not dropped (screening ranked on fit first, not on who is openly for sale) |

Short list after this pass: **Frostline** (for sale, priced), **Medivan Logistik** and **Thermo Lane** (fit the must-haves and the long-list deal-breaker test, availability unconfirmed).

## Short list

| Target | Strategic fit | Standalone value | Net cost synergies | Revenue synergies (upside only) | Deal-breaker flags | Rank |
|---|---|---|---|---|---|---|
| Frostline | Strong — GDP certified, 3/3 home regions, revenue 46m mid-range | EUR 42.5m (haircut plan) / EUR 57.5m (seller plan) | EUR 14.8m | EUR 2.0m EBITDA/yr, unowned, undated — weak evidence | None of the 3 agreed deal-breakers breached on data in hand; two contracts (27% of revenue) carry change-of-control clauses — not an agreed deal-breaker but a material undiced risk | 1 (only priced, for-sale target) |
| Medivan Logistik | Meets must-haves (24m revenue, GDP yes, 2/3 regions, top customer 22%) | Not sized — no FCF, synergy or price data available | Not sized | Not sized | None visible on long-list data | 2 — confirm availability, request data |
| Thermo Lane | Meets must-haves (27m revenue, GDP yes, 2/3 regions, top customer 27%, closest to the 30% line) | Not sized — no FCF, synergy or price data available | Not sized | Not sized | None visible on long-list data; customer concentration close to the line — check closely if pursued | 3 — confirm availability, request data |

## Walk-away price for Frostline

Valuation convention per CFO: value = next-year free cash flow / (10% − 2%); cost synergies = run-rate / 10% less one-off cost, no phase-in; revenue synergies shown separately, not in price.

| Component | Value (EUR m) | Basis |
|---|---|---|
| Standalone value, haircut plan | 42.5 | FCF 3.4 / 8%. Haircut built from 2022–2025 actual revenue growth (~4%/yr) vs. seller's 12%/yr plan — this is Kestrel's own view, used as the primary basis per the "value from the buyer's own view" rule |
| Standalone value, seller's plan (reference only) | 57.5 | FCF 4.6 / 8%. Rests on the seller's unverified 12%/yr growth assumption — graded weak evidence, shown for reference, not used to set the walk-away price |
| Cost synergy — depot consolidation | 10.0 | Run-rate 1.2 / 10% = 12.0, less one-off cost 2.0. Owner: COO. Timing: 2028 |
| Cost synergy — joint purchasing | 4.8 | Run-rate 0.5 / 10% = 5.0, less one-off cost 0.2. Owner: CPO. Timing: 2027 |
| **Net cost synergies** | **14.8** | Sum of the two above |
| **Walk-away price (haircut plan + net cost synergies)** | **57.3** | 42.5 + 14.8 |
| Asking price | 60.0 | Banker teaser |
| **Gap (asking − walk-away)** | **2.7** | Asking price exceeds Kestrel's own walk-away price |
| Revenue synergy (cross-sell to ambient pharma customers) | 2.0 EBITDA/yr, not in price | Banker's figure, no owner, no date, one-off cost not estimated — upside only, weak evidence, excluded from any price decision per the trap rule on revenue synergies |

Budget check: EUR 60m asking price is inside the agreed EUR 65m enterprise-value budget cap, so the budget is not the binding constraint — the buyer's-own-view walk-away price (EUR 57.3m) is, and it is already below the asking price.

## Key risks and integration thesis

1. **Change-of-control clauses on 27% of revenue** (two largest contracts, 18% and 9%): neither the seller's plan nor Kestrel's haircut plan appears to price in the chance these customers exit or renegotiate at change of control. Mitigation: make signing conditional on both customers consenting or extending their contracts before close — the same condition the worked example in this playbook applies when a deal-breaker-sized risk surfaces late. Owner: Kestrel corp dev + legal, before signing.
2. **Key-person dependency on GDP certification continuity**: the founder personally holds the relationship with the pharma quality auditors. The entire strategic rationale for this deal is certified capability — if that relationship does not transfer, the asset Kestrel is paying for is at risk. Mitigation: founder retention/earn-out tied to a defined handover period, or documented evidence the auditor relationship is institutional rather than personal, confirmed before signing. Owner: COO + regulatory/quality specialist.
3. **Revenue synergy reliance**: the only named revenue synergy comes from the banker's own teaser, has no owner, no date and no one-off cost — classic overstatement risk. Treated here as upside only, excluded from the price decision; no further action needed unless it later gets an owner and a cost.
4. **Integration thesis**: depot consolidation (2028, COO) and joint purchasing (2027, CPO) are owned and dated; no integration owner or plan has been named for the sales/customer-facing side (where the change-of-control and key-person risks sit) — this needs naming before signing, not after.

## What would change the answer

1. If the seller drops the price to Kestrel's walk-away price (~EUR 57.3m) or below, and both customers with change-of-control clauses commit to extend before signing, and a credible handover plan for the quality-auditor relationship is documented — proceed.
2. If diligence shows the 27% of at-risk revenue carries disproportionately high margin (i.e., losing it cuts FCF by more than its revenue share suggests), the walk-away price falls further below the current EUR 57.3m estimate and even a price cut to EUR 57m would not clear the bar.
3. If Medivan Logistik or Thermo Lane turn out to be available and their FCF/synergy economics clear a lower bar than Frostline's, they become the preferred route and reduce pressure to stretch on Frostline's price.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Kestrel's own view of Frostline's growth (haircut plan) is the right basis for the walk-away price, not the seller's 12%/yr plan | FCF 3.4m next year | 2022–2025 actual growth ~4%/yr, per Kestrel corp dev | Seller's growth plan were independently verified (e.g., signed contracts already backing the 12%/yr) |
| 2 | "Two largest contracts" (18%, 9%) are two different customers, not the same one split across contracts | Treated as two separate customer risks, neither alone breaching the 30% deal-breaker | Input data | They were the same customer, which would push combined concentration to 27% for one customer — still under 30%, but close enough to merit the same contract-consent condition |
| 3 | No unresolved customer litigation or certification-under-review issue exists at Frostline beyond what's stated | Deal-breaker check passes on data in hand | Teaser plus first management meeting; not yet confirmed in formal diligence | Diligence found either condition, which would breach an agreed deal-breaker and end the deal regardless of price |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Will the two customers with change-of-control clauses (18%, 9% of revenue) consent or extend before signing? | Unresolved, this risk is not priced into either FCF plan and could cut the walk-away price further | Frostline management / Kestrel legal in diligence | Confirmed extension keeps walk-away price at ~57.3m; no extension should drop the price further or kill the deal |
| Can the founder's auditor relationship be documented/transferred, or is it genuinely personal and non-transferable? | The deal's entire rationale is certified capability; losing auditor continuity undermines that | Frostline founder / Kestrel regulatory specialist | Non-transferable relationship adds a material risk discount or a founder retention cost not yet in the synergy case |
| Are Medivan Logistik and Thermo Lane actually for sale, and can revenue/FCF/synergy data be obtained? | They passed the must-have and long-list deal-breaker screen but are unpriced and unsized | Kestrel corp dev, via direct approach | Either becoming available and pricing below its own walk-away value would create a stronger alternative than Frostline at 60m |
| Does Frostline's at-risk 27% of revenue carry higher, lower or average margin versus the rest of the book? | Determines how much further the walk-away price should fall if those two contracts are not secured | Frostline management, in diligence | Above-average margin on the at-risk revenue lowers the walk-away price below 57.3m |
| Is there any unresolved litigation or certification-review status not disclosed in the teaser/first meeting? | This is an agreed deal-breaker; a breach ends the deal regardless of price | Formal legal/regulatory due diligence | A breach found here overrides the price discussion entirely — do not proceed at any price |

