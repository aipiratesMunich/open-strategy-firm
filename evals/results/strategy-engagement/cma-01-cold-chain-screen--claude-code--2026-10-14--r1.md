# cma-01-cold-chain-screen on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (10/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs the funnel on all eight companies with the stage at which each drops out, keeping Medivan Logistik and Thermo Lane on the short list though not known to be for sale | NO | Funnel table shows 'After must-haves / 3 (Frostline, Medivan Logistik, Thermo Lane)' then 'After deal-breakers (on data given) / 3 (unchanged) / No long-list company with a pass on must-haves failed a named deal-breaker' — this is self-contradictory, since the same document's 'Eliminated and why' li |
| Values Frostline on the haircut plan (~EUR 42.5m) and shows the seller plan (~EUR 57.5m) as the seller's view, graded as seller numbers | yes | 'Standalone value, haircut plan / EUR 42.5m / ... Kestrel's own haircut' vs 'Standalone value, seller's plan / EUR 57.5m / ... seller/banker figure, not used for the walk-away' |
| Net cost synergies of about EUR 14.8m, each with owner, date and one-off cost | yes | 'Cost synergy — depot consolidation / EUR 10.0m / ... owner COO, from 2028' and 'Cost synergy — joint purchasing / EUR 4.8m / ... owner CPO, from 2027' summing to 'Net cost synergies / EUR 14.8m' |
| Walk-away price of about EUR 57.3m built from standalone value plus net cost synergies, with EUR 60m stated as above it | yes | 'Walk-away price / EUR 57.3m / Haircut standalone value + net cost synergies' and 'Gap (asking − walk-away) / EUR 2.7m over' |
| Shows the EUR 2.0m revenue synergy as upside only, outside the walk-away, noting no owner/date/one-off cost | yes | 'Revenue synergies (not in price) / EUR 2.0m EBITDA run-rate ... no owner, no date, no one-off cost estimate — shown as upside only, excluded from the walk-away price' |
| Answer is do not proceed at EUR 60m, or proceed only at/below ~EUR 57m under named conditions | yes | 'Do not proceed at EUR 60m ... Proceed only under conditions: renegotiate to at or below ~EUR 57m, and clear the two open risk items below before signing.' |
| Names change-of-control clauses and founder dependence as deal-breaker checks or conditions | yes | 'Contract continuity: the two largest contracts (18% and 9% of revenue, 27% combined) carry change-of-control clauses ... make this a condition precedent' and 'Key-person / certification continuity: the founder personally holds the relationship with the pharma quality auditors ... Mitigation: founde |
| Compares the deal with the build route (EUR 35m, four years, misses 2028) | yes | 'Build alternative: EUR 35m, ~4 years to certification and a customer base — misses the 2028 deadline. Acquisition is the right route on timing' |
| Recommends a review by someone outside the deal team | yes | 'someone outside the deal team to review before signing given the banker-sourced teaser' |
| Flags legal, tax and financial due diligence for specialists | yes | 'Specialists and review: legal (change-of-control consents, litigation confirmation), tax/financial due diligence (haircut plan and FCF build)' |
| Does not include revenue synergies in the walk-away price or back-solve value from the asking price | yes | Walk-away price table computes 'EUR 57.3m / Haircut standalone value + net cost synergies' with revenue synergies listed in a separate 'not in price' row |
| Does not invent facts about the targets beyond the table | NO | 'Thermo Lane / Passes must-haves (2 of 3 regions, top customer 27%, just under the 30% deal-breaker)' introduces a specific customer-concentration figure for Thermo Lane that matches, suspiciously, the exact combined 18%+9%=27% figure used for Frostline's change-of-control contracts, with no corrobo |

## Transcript

## Turn 1

**User:** Run the Kestrel cold-chain M&A screen from the pack and tell us whether to go ahead with Frostline at the asking price. (Attached in the working directory: cma-01-input.md.)

## Recommendation: do not proceed at EUR 60m

**Walk-away price on Kestrel's own view: EUR 57.3m** — the asking price is about **EUR 2.7m above it**. Full screen, numbers and conditions saved to `case-ma-screening-kestrel-frostline.md`. Key points:

**Screening funnel (full long list, not just "for sale" names):** Of 8 targets, only Frostline, Medivan Logistik and Thermo Lane clear the must-haves and deal-breakers. Polar Route (41% top customer), ColdArc (revenue too high), Icepath (not GDP certified), Glacier Freight (1 of 3 regions) and Chillbox Couriers (revenue too low, 35% top customer) are out. Only Frostline is known to be for sale — Medivan and Thermo Lane should be approached in parallel so this isn't a decision against a field of one.

**Walk-away math for Frostline (CFO convention, FCF/(10%−2%)):**
- Standalone value, haircut plan: 3.4 / 0.08 = **EUR 42.5m** (not the seller's 4.6m plan → 57.5m)
- Net cost synergies: depot consolidation (1.2/0.10 − 2.0 = 10.0m) + joint purchasing (0.5/0.10 − 0.2 = 4.8m) = **EUR 14.8m**
- Walk-away = 42.5 + 14.8 = **EUR 57.3m**, vs. asking **EUR 60m**
- The EUR 2.0m EBITDA cross-sell revenue synergy is banker-sourced, has no owner/date/cost, and is correctly kept out of the price as upside only.

**Two things could independently kill the deal regardless of price**, both unresolved in the pack: whether the 27% of revenue under change-of-control contracts survives the sale, and whether there's any unresolved customer litigation (an agreed deal-breaker not addressed anywhere in the pack). The founder's personal hold on the pharma-auditor relationship is a third risk needing a retention/transition plan.

**Bottom line:** negotiate toward ~EUR 57m or below, and treat customer consents, litigation confirmation, and founder transition as conditions precedent to signing — not post-close cleanup.


## Files in work dir after run

- case-ma-screening-kestrel-frostline.md
- cma-01-input.md

## File written by the run: case-ma-screening-kestrel-frostline.md

# M&A screening: Kestrel Logistics, should Kestrel buy Frostline Pharma Transport at the EUR 60m asking price?

**Answer:** Do not proceed at EUR 60m. Walk-away price on Kestrel's own view is **EUR 57.3m** (haircut-plan standalone value EUR 42.5m + net cost synergies EUR 14.8m); the EUR 60m asking price is about EUR 2.7m above that. Proceed only under conditions: renegotiate to at or below ~EUR 57m, and clear the two open risk items below before signing.
**Confidence:** medium — the walk-away arithmetic rests on Kestrel's own haircut plan and the CFO's pre-agreed valuation convention (strong evidence), but two items that could move the number are unresolved (contract continuity on 27% of revenue, litigation status), and the only growth and revenue-synergy figures in the pack are seller/banker-sourced.
**Specialists and review:** legal (change-of-control consents, litigation confirmation), tax/financial due diligence (haircut plan and FCF build), someone outside the deal team to review before signing given the banker-sourced teaser.

## Why buy
- Strategic goal: certified pharma cold-chain capability (GDP, 2–8°C) in Kestrel's three home regions by 2028.
- Build alternative: EUR 35m, ~4 years to certification and a customer base — misses the 2028 deadline. Acquisition is the right route on timing; confirmed, not killed, by the data given.

## Screening criteria and deal-breakers
| Criterion | Type | Threshold |
|---|---|---|
| GDP certification held today | Must-have | Yes, not under review/lapsed |
| Revenue | Must-have | EUR 20–80m |
| Home-region operations | Must-have | At least 2 of 3 |
| Single customer share | Deal-breaker | > 30% of revenue |
| Certification status | Deal-breaker | Under review or lapsed |
| Customer litigation | Deal-breaker | Unresolved litigation with a customer |

## Funnel
| Stage | Number of companies | Criteria applied |
|---|---|---|
| Long list | 8 | All companies on corp-dev list |
| After must-haves | 3 (Frostline, Medivan Logistik, Thermo Lane) | GDP yes; revenue 20–80m; ≥2 of 3 home regions |
| After deal-breakers (on data given) | 3 (unchanged) | No long-list company with a pass on must-haves failed a named deal-breaker |
| For-sale / approachable now | 1 confirmed (Frostline); 2 unknown | "For sale" status, checked last, per the screening-on-availability trap |

Eliminated and why: ColdArc (revenue EUR 95m, above range) — also not for sale; Icepath (not GDP certified); Glacier Freight (1 of 3 regions); Chillbox Couriers (revenue EUR 12m, below range, and top customer 35% > 30%); Polar Route (top customer 41% > 30%, deal-breaker).

## Short list
| Target | Strategic fit | Standalone value | Net cost synergies | Revenue synergies (upside only) | Deal-breaker flags | Rank |
|---|---|---|---|---|---|---|
| Frostline Pharma Transport | High — 3 of 3 regions, GDP certified, revenue in range | EUR 42.5m (haircut plan) | EUR 14.8m | EUR 2.0m EBITDA run-rate (banker-sourced, not costed) | None breached on data given; two risk items below need clearing | 1 (only target with a live process) |
| Medivan Logistik | Passes must-haves (2 of 3 regions) | Not built — no banker figures available | Not built | Not built | None on data given; availability unknown | 2 — approach in parallel |
| Thermo Lane | Passes must-haves (2 of 3 regions, top customer 27%, just under the 30% deal-breaker) | Not built | Not built | Not built | None on data given; availability unknown | 2 — approach in parallel |

Running a single banker-sourced target without checking the other two passes the screening-on-availability trap. Medivan and Thermo Lane should be approached now so the decision on Frostline is not made against a field of one.

## Walk-away price for Frostline Pharma Transport
| Component | Value | Basis |
|---|---|---|
| Standalone value, seller's plan | EUR 57.5m | FCF EUR 4.6m / (10%–2%) = 4.6/0.08; seller/banker figure, not used for the walk-away |
| Standalone value, haircut plan | **EUR 42.5m** | FCF EUR 3.4m / (10%–2%) = 3.4/0.08; Kestrel's own haircut of seller's plan against 2022–25 history (~4% a year growth) |
| Cost synergy — depot consolidation | EUR 10.0m | 1.2/0.10 − 2.0 one-off = 12.0 − 2.0; owner COO, from 2028 |
| Cost synergy — joint purchasing | EUR 4.8m | 0.5/0.10 − 0.2 one-off = 5.0 − 0.2; owner CPO, from 2027 |
| Net cost synergies | EUR 14.8m | Sum of the two lines above |
| **Walk-away price** | **EUR 57.3m** | Haircut standalone value + net cost synergies |
| Asking price | EUR 60.0m | Banker teaser |
| Gap (asking − walk-away) | **EUR 2.7m over** | Asking price exceeds Kestrel's own walk-away price |
| Revenue synergies (not in price) | EUR 2.0m EBITDA run-rate (≈ EUR 20m if capitalised the same way) | Cross-sell to Kestrel's ambient pharma customers; banker's teaser figure; no owner, no date, no one-off cost estimate — shown as upside only, excluded from the walk-away price per the CFO's convention and because it is seller-sourced and unowned |

Note on the budget: Kestrel's EUR 65m enterprise-value cap is not the binding constraint here — both the asking price (EUR 60m) and the walk-away price (EUR 57.3m) sit under it. The binding constraint is that the asking price exceeds Kestrel's own view of value.

## Key risks and integration thesis
1. **Contract continuity:** the two largest contracts (18% and 9% of revenue, 27% combined) carry change-of-control clauses. If either lapses on acquisition, realised FCF falls well below the haircut plan. Mitigation: obtain written consents or waivers from both customers before signing; make this a condition precedent, not a post-close task. Owner: not yet named — add before signing.
2. **Key-person / certification continuity:** the founder personally holds the relationship with the pharma quality auditors. GDP certification is listed as currently held, but that relationship is not described as transferable. Mitigation: founder retention/transition agreement with a named successor relationship owner, in place before or at signing.
3. **Litigation status unconfirmed:** the pack does not state whether Frostline has any unresolved customer litigation — one of the agreed deal-breakers. This must be confirmed, not assumed, in legal due diligence before signing.
4. **Integration thesis incomplete:** cost synergies have named owners and dates (COO/2028, CPO/2027), but no overall integration lead or day-one plan is named yet. Name one before signing.

## What would change the answer
1. If the seller agrees a price at or below ~EUR 57m, the deal clears Kestrel's own walk-away price and the recommendation flips to proceed, subject to risks 1–3 being cleared.
2. If either of the two change-of-control contracts cannot be preserved (consent refused), re-run the haircut FCF without that revenue; at 27% of revenue the walk-away price would very likely fall below even a reduced asking price, and the recommendation hardens to do not proceed at any price tested so far.
3. If diligence finds unresolved customer litigation, the deal-breaker is breached and the deal does not proceed regardless of price, unless cured before signing.
4. If Medivan Logistik or Thermo Lane turns out to be available at a price below their own (not yet built) walk-away value, Kestrel should compare before committing to Frostline alone.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Kestrel's haircut plan (FCF EUR 3.4m) is the right base case, not the seller's plan (EUR 4.6m) | EUR 3.4m next-year FCF | Kestrel's own haircut against 2022–25 actual growth (~4%/yr) vs. seller's assumed 12%/yr | Seller's growth plan is independently verified in diligence as credible |
| 2 | Revenue synergy of EUR 2.0m EBITDA is real but unowned/uncosted, so excluded from price | Excluded from walk-away; shown as upside only | Banker's teaser figure; no one-off cost, owner or date given | A named owner, date and one-off cost are provided and it survives a no-revenue-synergy sensitivity check |
| 3 | No other long-list company besides Frostline currently has an active sale process | Only Frostline treated as "live" | "For sale" column: yes for Frostline; "not known" for Medivan and Thermo Lane | Medivan or Thermo Lane confirm availability |
| 4 | GDP certification is currently valid and not under review (per long-list table) | Deal-breaker not breached | Long-list table marks Frostline "yes" with no "under review" flag | Diligence finds the certification status has changed since the teaser |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is there any unresolved customer litigation at Frostline? | Explicit agreed deal-breaker; not addressed anywhere in the pack | Legal due diligence / target management | Breach kills the deal outright regardless of price |
| Will the two change-of-control customers (18%, 9% of revenue) consent to the change of control? | 27% of revenue at risk; haircut FCF assumes this revenue continues | Target management, then direct customer contact during diligence | Loss of either contract likely pushes walk-away price below any realistic asking price |
| Is the founder's auditor relationship transferable, or does it require a retention/transition agreement? | GDP certification maintenance and quality-audit continuity depend on it today | Target management (founder), Kestrel QA lead | No transition plan raises execution risk materially; may require a holdback or earn-out tied to retention |
| Will Medivan Logistik or Thermo Lane confirm they are for sale, and at what price? | Both passed must-haves and deal-breakers on the data given; screening only Frostline repeats the availability trap | Corporate development, outreach | A better-priced alternative could beat Frostline on walk-away economics |
| Who will lead integration, and what is the day-one plan? | Synergy lines have owners and dates, but no named overall integration lead | Kestrel COO / deal sponsor | Missing this is a condition to fix before signing, not a reason to kill the deal |

