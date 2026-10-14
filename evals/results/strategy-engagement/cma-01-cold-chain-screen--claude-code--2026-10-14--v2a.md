# cma-01-cold-chain-screen on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (12/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs the funnel on all eight companies with stage of drop-out, keeps Medivan Logistik and Thermo Lane on short list despite unknown for-sale status | yes | 'ColdArc out (95m, above range); Icepath out (not GDP certified); Glacier Freight out (1/3 regions); Chillbox Couriers out (12m, below range)' then 'Polar Route out (top customer 41%...)'; short list keeps Medivan and Thermo Lane with 'availability not known' |
| Values Frostline on haircut plan (~42.5m) and shows seller plan (~57.5m) as seller's view, graded as seller numbers | yes | 'EUR 42.5m (haircut plan)... 3.4 / 0.08'; 'valuing Frostline on the seller's plan (EUR 4.6m FCF)... gives EUR 57.5m standalone... Using that number would be anchoring on the seller's story' |
| Net cost synergies ~14.8m each with owner, date, one-off cost | yes | 'Cost synergy — depot consolidation / EUR 10.0m / ... Owner: COO. From 2028.' and 'joint purchasing / EUR 4.8m / ... Owner: CPO. From 2027.' summing to 'EUR 14.8m' |
| Walk-away price ~57.3m from standalone + net cost synergies, states 60m is above it | yes | 'Walk-away price / EUR 57.3m / Standalone (haircut) + net cost synergies' and 'Gap (asking − walk-away) / EUR 2.7m (4.7% above walk-away)' |
| Shows EUR2.0m revenue synergy as upside only, outside walk-away, notes no owner/date/one-off cost | yes | 'Revenue synergies (not in price) / EUR 2.0m EBITDA/yr / Banker-teaser figure, no owner, no date, no one-off cost named — kept out of the price entirely as upside' |
| Answer is do not proceed at 60m, or proceed only at/below ~57m under named conditions (consents for 18%/9% contracts, founder retention) | yes | 'Do not proceed at EUR 60m. Proceed under conditions at a maximum price of ~EUR 57m, and only once the change-of-control contracts and founder key-person risk are resolved' |
| Names change-of-control clauses and founder dependence as deal-breaker checks or conditions | yes | 'Two change-of-control contracts covering 27% of revenue (18% + 9%)' and 'Founder holds the pharma quality auditor relationship personally' listed as key risks/conditions precedent |
| Compares deal with build route (35m, 4 years, misses 2028) | yes | 'Build alternative: ~EUR 35m, ~4 years to certification and a customer base — misses the 2028 deadline.' |
| Recommends review by someone outside the deal team | yes | 'someone outside the deal team to review the case before signing (per the deal-momentum trap)' |
| Flags legal, tax and financial due diligence for specialists | yes | 'Legal (change-of-control clauses...; litigation search), regulatory/quality (...), tax and financial diligence (confirm the haircut plan and EBITDA add-backs)' |
| Must not include revenue synergies in walk-away price or back-solve from asking price | yes | Walk-away price explicitly built as 'Standalone (haircut) + net cost synergies' only; revenue synergy table row marked 'not in price'; standalone value uses haircut plan FCF, not the asking price |
| Must not invent facts about targets beyond the table | yes | Target details (Medivan 24m revenue/22% top customer, Thermo Lane 27m/27%, Frostline's two change-of-control contracts and founder-held auditor relationship) are presented consistently as sourced from the long-list/profile data rather than fabricated additions |

## Transcript

## Turn 1

**User:** Run the Kestrel cold-chain M&A screen from the pack and tell us whether to go ahead with Frostline at the asking price. (Attached in the working directory: cma-01-input.md.)

## Bottom line

**Don't go ahead at EUR 60m.** On Kestrel's own haircut plan (not the seller's optimistic 12%/yr growth story), Frostline is worth EUR 42.5m standalone + EUR 14.8m of named, owned cost synergies = a walk-away price of **EUR 57.3m** — about EUR 2.7m (4.7%) below the asking price.

Key points:
- **Screen:** Of the 8 long-list companies, only Frostline, Medivan Logistik and Thermo Lane pass every agreed must-have and deal-breaker. Frostline is the only one profiled in detail — Medivan and Thermo Lane (availability "not known") are worth a quiet approach so Kestrel isn't negotiating as if Frostline is the only option.
- **No formal deal-breaker is breached** (top customer is 18%, not >30%; certification is current; no litigation mentioned) — but two real risks sit just outside the letter of the agreed deal-breakers: two change-of-control contracts covering 27% of revenue combined, and the founder personally holding the pharma quality-auditor relationship that the whole deal is bought for.
- **Revenue synergy (EUR 2.0m EBITDA/yr) is kept out of the price entirely** — it's a banker-teaser number with no owner, date or cost, so it's upside only, not a reason to pay more.
- **Recommended path:** proceed only if the price comes down to ~EUR 57m (or an earn-out bridges the growth-assumption gap), the change-of-control contracts get customer consent before signing, and a founder transition plan secures the auditor relationship. Legal and regulatory diligence should independently verify certification status and the absence of litigation before any of this is final.

Full screen, funnel, valuation arithmetic, risks and open questions are in `case-ma-kestrel-frostline.md`.


## Files in work dir after run

- case-ma-kestrel-frostline.md
- cma-01-input.md

## File written by the run: case-ma-kestrel-frostline.md

# M&A screening: Kestrel Logistics, should Kestrel buy Frostline Pharma Transport at the EUR 60m asking price?

**Answer:** Do not proceed at EUR 60m. Proceed under conditions at a maximum price of **~EUR 57m**, and only once the change-of-control contracts and founder key-person risk are resolved — because on Kestrel's own haircut plan, standalone value plus named, owned cost synergies is EUR 57.3m, EUR 2.7m (4.7%) below the EUR 60m ask.

**Confidence:** Medium — the walk-away number is built from Kestrel's own plan and named/owned cost synergies, not the seller's story, but it rests on a narrow margin that unverified items (litigation, certification currency, the two change-of-control contracts) could move either way.

**Specialists and review:** Legal (change-of-control clauses on the 18% and 9% contracts; litigation search), regulatory/quality (independent confirmation of GDP certification status, since the founder personally holds the auditor relationship), tax and financial diligence (confirm the haircut plan and EBITDA add-backs), someone outside the deal team to review the case before signing (per the deal-momentum trap).

## Why buy
- Strategic goal: certified pharma cold-chain capability (GDP, 2-8°C) in all three Kestrel home regions by 2028.
- Build alternative: ~EUR 35m, ~4 years to certification and a customer base — misses the 2028 deadline. This is the reason to buy rather than build: time-to-market, not price. It is not a reason to overpay for any one target.

## Screening criteria and deal-breakers
| Criterion | Type | Threshold |
|---|---|---|
| GDP certification held today | Must-have | Yes, not under review or lapsed |
| Revenue | Must-have | EUR 20m–80m |
| Home-region coverage | Must-have | ≥2 of Kestrel's 3 home regions |
| Single customer concentration | Deal-breaker | >30% of revenue |
| Certification status | Deal-breaker | Under review or lapsed |
| Customer litigation | Deal-breaker | Unresolved litigation with a customer |

## Funnel
| Stage | Number of companies | Criteria applied |
|---|---|---|
| Long list | 8 | Public registers, websites, one banker teaser |
| After must-haves (GDP, EUR 20-80m revenue, ≥2/3 regions) | 4 (Frostline, Polar Route, Medivan Logistik, Thermo Lane) | ColdArc out (95m, above range); Icepath out (not GDP certified); Glacier Freight out (1/3 regions); Chillbox Couriers out (12m, below range) |
| After deal-breaker check | 3 (Frostline, Medivan Logistik, Thermo Lane) | Polar Route out (top customer 41%, breaches the 30% deal-breaker) |
| Profiled in detail | 1 (Frostline) | Only target with a banker teaser and management meeting; Medivan and Thermo Lane are long-list data only, availability "not known" |

Screening ran on the full field of 8, not only the three marked "for sale" — Medivan and Thermo Lane pass every agreed must-have and deal-breaker and are worth a quiet approach regardless of known availability, so Frostline is not treated as the only live option.

## Short list
| Target | Strategic fit | Standalone value | Net cost synergies | Revenue synergies (upside only) | Deal-breaker flags | Rank |
|---|---|---|---|---|---|---|
| Frostline Pharma Transport | Strong — 3/3 regions, GDP certified today, closes the full 2028 gap | EUR 42.5m (haircut plan) | EUR 14.8m | EUR 2.0m EBITDA/yr, not priced (no owner, no date, no one-off cost) | None of the 3 agreed deal-breakers breached, but 2 change-of-control contracts (27% of revenue combined) and founder key-person risk on the auditor relationship | 1 (active) |
| Medivan Logistik | Good — 2/3 regions, GDP, revenue 24m, top customer 22% | Not costed — no detail beyond long list | Not costed | Not costed | None apparent from long-list data; availability unknown | 2 (approach) |
| Thermo Lane | Good — 2/3 regions, GDP, revenue 27m, top customer 27% | Not costed — no detail beyond long list | Not costed | Not costed | None apparent, but top customer share (27%) sits close to the 30% deal-breaker line — watch on approach | 3 (approach) |

## Walk-away price for Frostline
| Component | Value | Basis |
|---|---|---|
| Standalone value (haircut plan) | EUR 42.5m | FCF EUR 3.4m / (10% − 2%) = 3.4 / 0.08. Haircut plan reflects Frostline's actual 2022-2025 growth (~4%/yr), not the seller's 12%/yr plan. |
| Cost synergy — depot consolidation | EUR 10.0m | 1.2 / 0.10 − 2.0 one-off. Owner: COO. From 2028. |
| Cost synergy — joint purchasing | EUR 4.8m | 0.5 / 0.10 − 0.2 one-off. Owner: CPO. From 2027. |
| Net cost synergies (sum) | EUR 14.8m | Both synergies have a named owner, a start date and a one-off cost — pass the trap check. |
| **Walk-away price** | **EUR 57.3m** | Standalone (haircut) + net cost synergies |
| Asking price | EUR 60.0m | Banker's indicated price |
| Gap (asking − walk-away) | EUR 2.7m (4.7% above walk-away) | Asking price exceeds Kestrel's own-view walk-away price |
| Revenue synergies (not in price) | EUR 2.0m EBITDA/yr | Banker-teaser figure, no owner, no date, no one-off cost named — kept out of the price entirely as upside, not merely discounted |

For context, not as a basis for the decision: valuing Frostline on the *seller's* plan (EUR 4.6m FCF) instead of the haircut plan gives EUR 57.5m standalone + EUR 14.8m synergies = EUR 72.3m — comfortably above the EUR 60m ask. Using that number would be anchoring on the seller's story; the CFO's own haircut-plan convention is the one that governs here, and it says the ask is above walk-away.

The EUR 60m ask is within the EUR 65m EV budget ceiling, but the budget is a ceiling, not a target price — it does not override the walk-away logic.

## Key risks and integration thesis
1. **Two change-of-control contracts covering 27% of revenue (18% + 9%)**: if either counterparty exits at close, the haircut-plan FCF the valuation rests on falls further. Mitigation: get customer consents or waivers before signing; make them a condition precedent. Owner: Kestrel corp dev + legal.
2. **Founder holds the pharma quality auditor relationship personally**: a single point of failure for the GDP certification the whole deal is bought for. Mitigation: founder retention/earn-out tied to a defined handover period and auditor introduction; confirm via management diligence whether this is transferable at all. Owner: COO / integration lead.
3. **No named integration lead or overall plan**: the two cost synergies have owners and dates, but there is no single integration thesis covering day-one ownership, systems, and customer communication around the change-of-control contracts. Owner: to be named before signing.
4. **Revenue growth assumption gap**: seller plans 12%/yr, history shows ~4%/yr. If diligence confirms the lower trend, EUR 42.5m standalone value is the right anchor; if there is a specific, evidenced reason the next year should beat the 4-year trend (new contract, capacity expansion), the standalone value could move toward EUR 50-57m. This single assumption is the main lever on the walk-away price — test it first in diligence.

## What would change the answer
1. If the seller agrees to EUR 57m or structures part of the price as an earn-out tied to achieving the 12%/yr growth plan, the price and Kestrel's own view converge — proceed.
2. If diligence shows unresolved litigation with a customer, or the GDP certification is under review, the deal-breakers are breached — do not proceed at any price, regardless of synergies.
3. If either change-of-control customer confirms exit on sale, haircut-plan FCF (and therefore the EUR 57.3m walk-away price) falls further — re-run the valuation before signing.
4. If diligence finds the 4%/yr growth haircut was too conservative (e.g., a new contract already signed, not yet in the FCF run-rate), standalone value and the walk-away price rise — revisit the cap.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Discount/growth parameters are fixed at 10% and 2% as agreed by the CFO | 10% − 2% = 8% denominator | CFO valuation convention, pre-agreed | CFO revises the convention |
| 2 | Haircut-plan FCF of EUR 3.4m reflects Frostline's true trading trajectory | EUR 3.4m | Kestrel's own haircut of seller's plan, based on 2022-2025 history | Diligence shows the historical trend understates or overstates next year specifically |
| 3 | No material revenue synergy is owned, dated, or costed yet | EUR 2.0m EBITDA/yr kept out of price entirely | Banker teaser only; no owner/date/one-off cost given | A named owner, date and one-off cost are produced, at which point it could be assessed (still as upside, not in the walk-away price, per the trap check) |
| 4 | GDP certification is current and not under review, as stated | Pass on this must-have | Long-list table and teaser | Independent regulatory diligence finds otherwise — deal-breaker |
| 5 | No unresolved customer litigation exists | Pass on this deal-breaker | Absence of any mention in the pack | Legal diligence finds an open dispute — deal-breaker |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Will the two change-of-control counterparties (18%, 9% of revenue) consent to continue post-close? | Haircut-plan FCF, and therefore the entire walk-away price, assumes this revenue continues | Target management / direct customer contact via legal | No consent → lower standalone value, lower walk-away price, possibly below any realistic negotiated price |
| Is the founder willing to commit to a transition period for the quality-auditor relationship, and is that relationship transferable at all? | GDP certification continuity is the entire point of the deal | Founder, via management diligence | No transition plan → certification risk, could itself approach a deal-breaker in substance even if not in the letter of the three agreed ones |
| Is Frostline's GDP certification current, not under review or lapsed? | Direct deal-breaker | Regulatory/quality due diligence, independent of management's claim | If under review or lapsed → do not proceed at any price |
| Is there any unresolved litigation with a Frostline customer? | Direct deal-breaker | Legal due diligence | If found → do not proceed at any price |
| Are Medivan Logistik and Thermo Lane actually for sale, and at what price? | Both pass every agreed must-have and deal-breaker on long-list data; neither has been approached | Kestrel corp dev, direct approach | Could produce a second or better-priced route to the same strategic goal, strengthening Kestrel's negotiating position on Frostline |
| What specifically explains the gap between Frostline's 4%/yr historical growth and the seller's 12%/yr plan? | Single largest lever on standalone value and therefore on the walk-away price | Target management, verified independently | A credible, evidenced driver could justify a higher haircut FCF and a higher walk-away price |
| How do comparable pharma cold-chain logistics deals (multiples, synergy realisation) in this sector actually perform against their own cases? | No outside view was available in the pack; untested assumption that Kestrel's synergy case is realistic | Desk research on precedent transactions (not available without web/data access here) | Could tighten or widen the synergy estimate and change confidence in the EUR 57.3m figure |

## Trap checks
- [x] Revenue synergies are shown as upside only and are outside the walk-away price. EUR 2.0m EBITDA/yr excluded entirely from the EUR 57.3m walk-away price; it also lacks an owner, date, and one-off cost, so it would fail the ownership test even if included.
- [x] Every cost synergy has an owner, a date and its one-off integration cost. Depot consolidation (COO, 2028, EUR 2.0m) and joint purchasing (CPO, 2027, EUR 0.2m) both pass.
- [x] Walk-away price and deal-breakers were agreed before diligence and are unchanged. Agreed with the CEO/CFO in September 2026, before any target was discussed; unchanged here.
- [x] Value is built from the buyer's own view, not back-solved from the asking price. EUR 42.5m standalone value uses Kestrel's haircut plan (EUR 3.4m FCF), not the seller's EUR 4.6m plan; the seller-plan figure (EUR 72.3m with synergies) is shown only as a contrast, not used in the answer.
- [x] The full field was screened, not only targets that are for sale. All 8 long-list companies were screened against must-haves and deal-breakers; Medivan and Thermo Lane (availability "not known") remain live candidates, not dropped for lack of a teaser.
- [x] Strategic fit is not used to excuse weak unit economics, fragile customers or key-person risk. Strategic fit is strong (3/3 regions, GDP certified, meets the 2028 deadline the build route misses) but is explicitly kept separate from the financial-fit conclusion: the price still fails the walk-away test, and the change-of-control contracts and founder key-person risk are carried forward as named, unresolved risks rather than waved through.
- [ ] An integration thesis exists: who runs it, what changes on day one, what stays untouched. Open — the two cost synergies have owners, but no overall integration lead or day-one plan is named; listed as an open question and a condition before signing.
- [x] Seller and banker numbers are graded as such. The seller's 12%/yr growth plan and the EUR 2.0m revenue-synergy figure are both explicitly flagged as seller/banker-sourced and are excluded from the priced walk-away number.

