# cma-01-cold-chain-screen on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs the funnel on all eight companies with the stage at which each drops out, and keeps Medivan Logistik and Thermo Lane on the short list although not known to be for sale | yes | 'Failed must-haves: ColdArc..., Icepath..., Glacier Freight..., Chillbox...Failed deal-breaker: Polar Route (top customer 41%)' plus 'Medivan and Thermo Lane availability "not known" — not ruled out, just not disclosed' and 'worth a direct approach' |
| Values Frostline on haircut plan (~EUR 42.5m) and shows seller plan (~EUR 57.5m) as seller's view | yes | Table: 'Seller's plan (12%/year growth)...EUR 57.5m' vs 'Kestrel's haircut plan...EUR 42.5m'; 'Standalone value used for the walk-away price is the haircut figure, EUR 42.5m' |
| Net cost synergies of about EUR 14.8m, each with owner, date and one-off cost | yes | Depot consolidation 1.2/yr, one-off 2.0, owner COO, date 2028; Joint purchasing 0.5/yr, one-off 0.2, owner CPO, date 2027; 'Net cost synergies EUR 14.8m' |
| Walk-away price of about EUR 57.3m, built from standalone value plus net cost synergies, and states EUR 60m is above it | yes | 'Walk-away price EUR 57.3m' = 42.5m + 14.8m; 'Gap EUR 2.7m over walk-away' |
| Shows EUR 2.0m revenue synergy as upside only, outside the walk-away, noting no owner/date/one-off cost | yes | 'Cross-sell...not sized...not named...not dated. Upside only — excluded from price....no owner, no one-off cost, no date' |
| Answer is do not proceed at EUR 60m, or proceed only at/below ~EUR 57m under named conditions | yes | 'Do not proceed at EUR 60m. Proceed only if the price is renegotiated to EUR 57.3m or below...and two execution risks are resolved before signing' |
| Names change-of-control clauses and founder dependence as deal-breaker checks/conditions | yes | 'Change-of-control clauses on the two largest contracts (18% and 9%...)' and 'Founder holds the personal relationship with the pharma quality auditors' |
| Compares the deal with the build route (EUR 35m, four years, misses 2028) | yes | 'Build alternative: EUR 35m and about four years — from today (2026) that lands in 2030, missing the 2028 target' |
| Recommends a review by someone outside the deal team | yes | 'independent review of this case recommended before signing given deal momentum' |
| Flags legal, tax and financial due diligence for specialists | NO | Specialists listed are 'Legal..., regulatory/quality..., financial due diligence...' — no mention of tax due diligence anywhere in the document |
| Must not include revenue synergies in the walk-away price or back-solve value from the asking price | yes | Walk-away table explicitly lists 'Revenue synergies (not in price)...Upside only, excluded per trap check', and standalone value is derived from haircut FCF, not asking price |
| Must not invent facts about the targets beyond the table | yes | Failure reasons (revenue thresholds, certification, region count, customer concentration) match the reference must-have/deal-breaker criteria without added unsupported detail |

## Transcript

## Turn 1

**User:** Run the Kestrel cold-chain M&A screen from the pack and tell us whether to go ahead with Frostline at the asking price. (Attached in the working directory: cma-01-input.md.)

**Bottom line: don't pay EUR 60m.** Kestrel's own-view walk-away price for Frostline is **EUR 57.3m** (EUR 42.5m standalone value on the haircut plan + EUR 14.8m of named, owned cost synergies) — EUR 2.7m below the asking price. Full case is in `case-ma-screening-kestrel-frostline.md`.

Key points:
- **Build is ruled out** on timing (4 years misses the 2028 deadline), so acquisition is the right route.
- **Screening funnel**: of 8 targets, only Frostline, Medivan Logistik and Thermo Lane clear the must-haves and deal-breakers. Polar Route fails on customer concentration (41%); ColdArc, Icepath, Glacier Freight, Chillbox fail other must-haves. Frostline has the best regional fit (3 of 3) but is the only one confirmed for sale — Medivan and Thermo Lane are worth a direct approach so Frostline isn't negotiated as the only option.
- **Valuation gap is the swing factor**: seller's plan (12%/yr growth) implies EUR 57.5m; Kestrel's haircut on actual 2022-25 history (~4%/yr) implies EUR 42.5m. The walk-away price is built on the haircut, not the seller's plan.
- **Revenue synergy (EUR 2.0m EBITDA cross-sell) is excluded from price** — it's a banker-teaser figure with no owner, date, or cost, so it's upside only, per the standard trap check.
- **Two unresolved risks** keep confidence at medium rather than high: change-of-control clauses on contracts worth 27% of revenue combined, and the founder's personal hold on the GDP auditor relationship (certification continuity risk).

Recommendation: negotiate the price down to ≤EUR 57.3m and make customer consent on the two major contracts plus a documented auditor-relationship handover plan signing conditions. If the seller won't move and those risks can't be cured, walk.


## Files in work dir after run

- case-ma-screening-kestrel-frostline.md
- cma-01-input.md

## File written by the run: case-ma-screening-kestrel-frostline.md

# M&A screening: Kestrel, should we buy Frostline Pharma Transport at the EUR 60m asking price?

**Answer:** Do not proceed at EUR 60m. Proceed only if the price is renegotiated to **EUR 57.3m or below** (Kestrel's own walk-away price) **and** two execution risks are resolved before signing. At 60m, the asking price sits EUR 2.7m above what Kestrel's own haircut plan plus named, owned cost synergies support — the standalone haircut value of EUR 42.5m plus EUR 14.8m of net cost synergies is EUR 57.3m, against an asking price of EUR 60m.

**Confidence:** medium, because the walk-away gap is small (about 5% of asking price, inside normal negotiation range) but rests on an unverified haircut forecast and two unquantified risk items (contract change-of-control exposure, founder key-person dependence on certification). Would change to high if diligence confirms the 4%/year historical growth rate and the two flagged risks are cured; would change to "do not proceed at any price" if either risk crystallises.

**Specialists and review:** Legal (change-of-control clauses, litigation, GDP certification status), regulatory/quality (GDP re-certification dependency on the founder), financial due diligence (verify the 2022-2025 revenue history behind the haircut), independent review of this case recommended before signing given deal momentum.

## Why buy

- Strategic goal: certified pharma cold-chain capability (GDP, 2-8°C) in all three Kestrel home regions by 2028.
- Build alternative: EUR 35m and about four years — from today (2026) that lands in 2030, missing the 2028 target. **Hypothesis "build beats buy" killed**: acquisition is the right route given the deadline.

## Screening criteria and deal-breakers

| Criterion | Type | Threshold |
|---|---|---|
| GDP certified today | Must-have | Held now, not under review/lapsed |
| Revenue | Must-have | EUR 20m–80m |
| Home-region coverage | Must-have | At least 2 of 3 |
| Single-customer concentration | Deal-breaker | Any customer > 30% of revenue |
| Certification status | Deal-breaker | Under review or lapsed |
| Customer litigation | Deal-breaker | Any unresolved litigation with a customer |

## Funnel

| Stage | Number of companies | Criteria applied |
|---|---|---|
| Long list | 8 | Public registers, websites, one banker teaser |
| After must-haves | 3 (Frostline, Medivan Logistik, Thermo Lane) | GDP certified, EUR 20-80m revenue, ≥2 of 3 regions |
| After deal-breakers | 3 (no change) | No disclosed breach of concentration/cert/litigation deal-breakers |
| Confirmed for sale | 1 (Frostline) | Medivan and Thermo Lane availability "not known" — not ruled out, just not disclosed |

Failed must-haves: ColdArc (revenue 95m, over range; also not for sale), Icepath (not GDP certified), Glacier Freight (1 of 3 regions), Chillbox Couriers (revenue 12m, under range). Failed deal-breaker: Polar Route (top customer 41% of revenue).

**Trap check:** the long list was screened on the full field first, not only on what the banker brought. Two targets that clear every criterion (Medivan Logistik, Thermo Lane) are not confirmed for sale — worth a direct approach in parallel so Frostline is not the only option on the table. This is outside the scope of the asking-price question but belongs in the next workplan step.

## Strategic fit

Frostline is the strongest geographic fit of the three qualifying targets: operations in all 3 of 3 home regions versus 2 of 3 for Medivan and Thermo Lane. It closes the stated capability gap directly (GDP-certified, 2-8°C, pharma cold-chain) rather than needing further build-out in the third region.

## Standalone valuation (buyer's view, CFO convention: value = next-year FCF / (10% − 2%) = FCF / 8%)

| Case | Next-year FCF | Value |
|---|---|---|
| Seller's plan (12%/year growth) | EUR 4.6m | EUR 4.6m / 8% = **EUR 57.5m** |
| Kestrel's haircut plan (history: ~4%/year growth, 2022-2025) | EUR 3.4m | EUR 3.4m / 8% = **EUR 42.5m** |

The EUR 15m gap between seller's plan and the haircut plan is the single biggest swing factor in this case. **Standalone value used for the walk-away price is the haircut figure, EUR 42.5m** — built from Frostline's own trading history, not the seller's growth assumption.

## Synergy case

| Synergy | Type | Run-rate | One-off cost | Value (run-rate / 10% − one-off) | Owner | Date | Status |
|---|---|---|---|---|---|---|---|
| Depot consolidation (3 overlapping depots) | Cost | EUR 1.2m/yr | EUR 2.0m | 1.2/0.10 − 2.0 = **EUR 10.0m** | COO | 2028 | Owned, dated — counted in price |
| Joint purchasing | Cost | EUR 0.5m/yr | EUR 0.2m | 0.5/0.10 − 0.2 = **EUR 4.8m** | CPO | 2027 | Owned, dated — counted in price |
| **Net cost synergies** | | | | **EUR 14.8m** | | | |
| Cross-sell cold chain to ambient pharma customers | Revenue | EUR 2.0m EBITDA | not estimated | not sized | not named | not dated | **Upside only — excluded from price.** Sourced from the banker's teaser (seller-side), no owner, no one-off cost, no date: treat as a hope, not a number, until Kestrel names an owner and a plan. |

## Walk-away price for Frostline

| Component | Value | Basis |
|---|---|---|
| Standalone value (haircut plan) | EUR 42.5m | FCF 3.4m / 8%, Kestrel's haircut of seller's plan on 2022-2025 history |
| Cost synergies, net of integration cost | EUR 14.8m | Depot consolidation + joint purchasing, both owned and dated |
| **Walk-away price** | **EUR 57.3m** | Sum of the above |
| Asking price | EUR 60.0m | Banker teaser |
| Gap | **EUR 2.7m over walk-away** | Asking price exceeds Kestrel's own-view value |
| Revenue synergies (not in price) | EUR 2.0m EBITDA, un-costed | Upside only, excluded per trap check |
| Budget ceiling (for reference) | EUR 65.0m | Agreed with CEO/CFO; asking price is within this ceiling, but the ceiling is not the test — walk-away price is |

## Key risks and integration thesis

1. **Change-of-control clauses on the two largest contracts (18% and 9% of revenue, 27% combined).** If either customer does not consent or renews on worse terms post-acquisition, actual FCF falls below even the haircut case. Mitigation: make consent or renewal from both customers a signing condition; owner: Kestrel corp dev + Frostline management, before signing.
2. **Founder holds the personal relationship with the pharma quality auditors.** GDP certification is a must-have the whole deal depends on; if that relationship is not transferable, re-certification risk rises after the founder exits. Mitigation: require a documented handover plan and founder retention/consulting period through re-certification; owner: COO, before signing.
3. **Integration thesis:** COO runs depot consolidation (2028) and the CPO runs joint purchasing (2027); both are named and dated. No owner yet exists for the cross-sell revenue synergy — until one is named, it stays outside the price.

## What would change the answer

1. If diligence confirms Frostline's historical growth was closer to the seller's 12%/year plan than the 4%/year haircut, standalone value rises toward EUR 57.5m and the walk-away price would clear the EUR 60m asking price on its own.
2. If either of the two major customers refuses to consent to change of control, revenue (and the standalone value this case is built on) falls further below the haircut case — strengthens "do not proceed."
3. If the seller will not move off EUR 60m and the two risk items cannot be cured before signing, the answer becomes "do not proceed at any price" rather than "proceed under conditions."
4. If Medivan Logistik or Thermo Lane turn out to be approachable at a price below their own walk-away values, Frostline stops being the only option and loses negotiating leverage over the seller.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | CFO's valuation convention applied literally to both seller and haircut plans | FCF / (10%−2%) = FCF / 8% | Given by CFO | CFO specifies a different convention or adjusts the risk-free/growth spread |
| 2 | Cost synergies discounted flat at 10%, no growth, no phase-in | Run-rate / 10% − one-off cost | Given by CFO | CFO specifies phase-in or a different rate |
| 3 | No undisclosed litigation or certification review beyond what the teaser states | None assumed | Absence of disclosure in teaser/management meeting | Legal DD finds pending litigation or a certification review — deal-breaker, kills the deal outright |
| 4 | Revenue synergy of EUR 2.0m EBITDA is unverified seller-side (banker teaser) figure | Excluded entirely from price | Trap check: revenue synergies are upside only | Kestrel names an owner, a plan and a cost — it would still stay outside the walk-away price per the agreed convention, but could support a higher stretch price if the buyer chooses to pay for some of it |
| 5 | The 18%/9% change-of-control contracts are separate from, and additive to, the 18% top-customer figure already in the long-list table | 27% combined revenue at risk | Teaser figures read together | Data room shows different customer overlap or contract terms |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Will the two customers behind the change-of-control contracts (18%, 9% of revenue) consent to or survive the change of control? | 27% of revenue at risk; could push actual value below the haircut case | Frostline management / legal DD | If either refuses: standalone value falls further below 57.3m, strengthens "do not proceed at 60m" |
| Is there a documented plan for the founder's auditor relationships to transfer post-acquisition? | GDP certification is a must-have the whole deal rests on | Frostline founder / Kestrel regulatory & quality team | If no credible handover plan exists: certification continuity risk, a near deal-breaker |
| Is there any pending litigation or certification review not disclosed in the teaser? | Both are agreed deal-breakers | Legal due diligence | A hit kills the deal outright regardless of price |
| Can the 2022-2025 historical revenue growth (~4%/year) be verified from underlying accounts, and is the haircut conservative enough? | Standalone value swings EUR 42.5m-57.5m on this single assumption | Financial due diligence on Frostline's data room | A verified rate above 4% moves the walk-away price toward or above 60m |
| Are Medivan Logistik and Thermo Lane open to approach despite "not known" for-sale status? | Tests whether Frostline is genuinely the best option or just the only one disclosed | Kestrel corporate development | A credible alternative at a lower price improves Kestrel's negotiating position on Frostline |
| Who would own the cross-sell revenue synergy, and what would it cost to execute? | Currently a banker number with no owner, date or cost — cannot be sized or trusted | Kestrel commercial/sales leadership | Only affects upside case, not the walk-away price, per the agreed convention |

