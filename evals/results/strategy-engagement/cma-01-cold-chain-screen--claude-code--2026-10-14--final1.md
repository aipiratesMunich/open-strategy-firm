# cma-01-cold-chain-screen on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (10/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs the funnel on all eight companies with drop-out stage, keeps Medivan Logistik and Thermo Lane on the short list although not known to be for sale | yes | Funnel table lists all 8 (Frostline, Polar Route, Medivan, Thermo Lane after must-haves; removed Icepath, Glacier Freight, ColdArc, Chillbox at must-haves; Polar Route removed at deal-breakers) and short list keeps 'Medivan Logistik' and 'Thermo Lane' ranked 2/3 with note 'not known for sale... wort |
| Values Frostline on haircut plan (~EUR42.5m) and shows seller plan (~EUR57.5m) as seller's view, graded as seller numbers | yes | 'Standalone value, haircut plan (Kestrel's own view) / EUR 42.5m' vs 'Standalone value, seller's plan (reference only, not used) / EUR 57.5m' |
| Net cost synergies ~EUR14.8m, each with owner, date, one-off cost | yes | 'Depot consolidation... EUR 10.0m... Owner: COO. Timing: 2028' and 'Joint purchasing... EUR 4.8m... Owner: CPO. Timing: 2027' summing to 'Net cost synergies EUR 14.8m' |
| Walk-away price ~EUR57.3m built from standalone value plus net cost synergies, states EUR60m is above it | yes | 'Walk-away price (haircut plan + net cost synergies) / EUR 57.3m / EUR 42.5m + EUR 14.8m' and 'Gap (asking price − walk-away price) / EUR 2.7m above walk-away' |
| Shows EUR2.0m revenue synergy as upside only, outside walk-away, notes no owner/date/one-off cost | yes | 'Revenue synergies (not in price, upside only) / EUR 2.0m EBITDA/yr, uncosted ... no owner, no date, no one-off cost estimated — weak evidence, kept entirely out of the price per the trap check.' |
| Answer is do not proceed at EUR60m, or proceed only at/below ~EUR57m under named conditions | yes | Headline: 'Do not proceed at EUR 60m.' with conditions on change-of-control consents and founder retention listed |
| Names change-of-control clauses and founder dependence as deal-breaker checks/conditions | yes | 'Change-of-control exposure on 27% of revenue. The two largest contracts (18% and 9% of revenue)... Mitigation: get written consent...' and 'Key-person risk on the GDP audit relationship... Mitigation: retention or transition agreement with the founder' |
| Compares deal with build route (EUR35m, four years, misses 2028) | yes | 'internal build costs EUR 35m and takes about four years to certification and a customer base — starting now (Sept 2026) that lands around 2030, missing the 2028 target.' |
| Recommends a review by someone outside the deal team | NO | No mention anywhere in the transcript of an independent/outside reviewer; recommendation only covers counter-offer terms and diligence conditions. |
| Flags legal, tax and financial due diligence for specialists | NO | Document mentions 'Legal/regulatory due diligence' and 'Commercial due diligence' but tax due diligence is never mentioned, and financial due diligence for specialists is not explicitly flagged (only 'Kestrel's finance team builds a proper contract-level FCF bridge'). |
| Must not include revenue synergies in walk-away price or back-solve from asking price | yes | Walk-away price computed as haircut standalone value plus net cost synergies only ('EUR 42.5m + EUR 14.8m'), revenue synergy explicitly excluded, and standalone value derived from Kestrel's own haircut plan 'not back-solved from seller numbers' |
| Must not invent facts about targets beyond the table | yes | All figures (revenues, regions, certification status, customer concentration) are presented as sourced from the pack/teaser with no unsupported embellishment detected |

## Transcript

## Turn 1

**User:** Run the Kestrel cold-chain M&A screen from the pack and tell us whether to go ahead with Frostline at the asking price. (Attached in the working directory: cma-01-input.md.)

**Do not proceed at EUR 60m.** Full screen written to `case-m-and-a-kestrel-frostline.md`. Headline:

- **Funnel:** 8 targets → 4 pass must-haves → 3 pass deal-breakers (Polar Route killed, top customer 41%) → only Frostline is confirmed for sale today; Medivan and Thermo Lane pass on paper but availability is unknown.
- **Walk-away price (Kestrel's own haircut plan + net cost synergies):** EUR 42.5m + EUR 14.8m = **EUR 57.3m**, i.e. **below** the EUR 60m ask.
- The deal only clears EUR 60m if you believe the seller's 12%/yr growth plan (vs. ~4%/yr actual 2022–2025) — that assumption alone is worth the EUR 15m gap between the seller's and Kestrel's standalone value.
- Two unpriced risks make EUR 57.3m optimistic, not conservative: change-of-control clauses on 27% of revenue (two contracts), and the founder personally holding the GDP auditor relationship. The EUR 2.0m revenue synergy is seller-sourced, unowned, and uncosted — kept entirely out of the price as upside.

**Recommendation:** counter at ≤EUR 55m, conditional on written customer consent on the two change-of-control contracts and a founder retention/transition plan for the auditor relationship before signing. If the seller won't move and those two risks aren't cleared, walk — don't anchor on the EUR 60m ask or on deal momentum.


## Files in work dir after run

- case-m-and-a-kestrel-frostline.md
- cma-01-input.md

## File written by the run: case-m-and-a-kestrel-frostline.md

# M&A screening: Kestrel Logistics, should Kestrel proceed with Frostline Pharma Transport at the EUR 60m asking price?

**Answer:** Do not proceed at EUR 60m. On Kestrel's own (haircut) plan, Frostline's walk-away price is about **EUR 57.3m** — below the EUR 60m ask — and that number ignores two unpriced risks (change-of-control exposure on 27% of revenue, and key-person/certification risk tied to the founder) that would both push the realistic number lower. Counter at or below **EUR 55m**, conditional on clearing those two risks in diligence; if the seller won't move off EUR 60m and the risks aren't cleared, walk.

**Confidence:** medium — the valuation arithmetic is solid and uses the CFO's own convention and Kestrel's own haircut plan, not the seller's. Confidence is capped at medium because the deal's viability is sensitive to two facts not yet confirmed (customer consent on the change-of-control contracts; continuity of the GDP auditor relationship without the founder), and because Medivan and Thermo Lane were not checked for availability.

## Why buy
- Strategic goal: certified pharma cold-chain capability (GDP, 2–8°C) in Kestrel's three home regions, operating by 2028.
- Alternatives considered: internal build costs EUR 35m and takes about four years to certification and a customer base — starting now (Sept 2026) that lands around 2030, missing the 2028 target. Build is ruled out on timing, not cost; acquisition is the right route *in principle*. (Partner, license routes not evidenced in the pack — not assessed.)

## Screening criteria and deal-breakers
| Criterion | Type | Threshold |
|---|---|---|
| GDP certification | Must-have | Held today |
| Revenue | Must-have | EUR 20m–80m |
| Home-region operations | Must-have | At least 2 of 3 |
| Customer concentration | Deal-breaker | No single customer > 30% of revenue |
| Certification status | Deal-breaker | Not under review or lapsed |
| Litigation | Deal-breaker | No unresolved customer litigation |

## Funnel
| Stage | Number of companies | Criteria applied |
|---|---|---|
| Long list | 8 | Kestrel corp-dev long list |
| After must-haves | 4 (Frostline, Polar Route, Medivan, Thermo Lane) | Removed: Icepath (no GDP cert), Glacier Freight (1 of 3 regions), ColdArc (EUR 95m revenue, above range), Chillbox Couriers (EUR 12m revenue, below range) |
| After deal-breakers | 3 (Frostline, Medivan, Thermo Lane) | Removed: Polar Route (top customer 41% of revenue, breaches 30% cap) |
| After availability | 1 confirmed actionable (Frostline) | Frostline confirmed for sale (banker teaser). Medivan and Thermo Lane are "not known" for sale — not ruled out, just not actionable today; worth a direct approach so Frostline isn't the only option on the table. |

## Short list
| Target | Strategic fit | Standalone value | Net cost synergies | Revenue synergies (upside only) | Deal-breaker flags | Rank |
|---|---|---|---|---|---|---|
| Frostline | 3 of 3 home regions, GDP certified today, in Kestrel's size range | EUR 42.5m (haircut plan) – EUR 57.5m (seller plan, not credible, see below) | EUR 14.8m, net of integration cost | EUR 2.0m EBITDA/yr claimed (banker source, unsized one-off cost) | None of the three agreed deal-breakers breached; two unagreed but material flags (see risks) | 1 (only actionable target) |
| Medivan Logistik | 2 of 3 regions, GDP certified, EUR 24m revenue | Not assessed — availability unknown | Not assessed | Not assessed | Passes must-haves and deal-breakers on paper | 2 (contingent on availability) |
| Thermo Lane | 2 of 3 regions, GDP certified, EUR 27m revenue | Not assessed — availability unknown | Not assessed | Not assessed | Passes must-haves and deal-breakers on paper (27% top customer, under the 30% cap but close to it) | 3 (contingent on availability) |

## Walk-away price for Frostline

Per the CFO's convention: standalone value = next-year FCF / (10% − 2%); cost synergies = run-rate / 10%, less one-off cost, no phase-in; revenue synergies shown separately, not in the price.

| Component | Value | Basis |
|---|---|---|
| Standalone value, haircut plan (Kestrel's own view) | EUR 42.5m | EUR 3.4m FCF / 8%. Haircut plan uses Frostline's actual 2022–2025 growth (~4%/yr), not the seller's 12%/yr plan. |
| Standalone value, seller's plan (reference only, not used) | EUR 57.5m | EUR 4.6m FCF / 8%. Rests on 12%/yr revenue growth with no evidence in the pack beyond the seller's own plan — three times the historical rate. Not used for the walk-away price (buyer's own view, not back-solved from seller numbers). |
| Depot consolidation, net of integration cost | EUR 10.0m | (EUR 1.2m run-rate / 10%) − EUR 2.0m one-off. Owner: COO. Timing: 2028. |
| Joint purchasing, net of integration cost | EUR 4.8m | (EUR 0.5m run-rate / 10%) − EUR 0.2m one-off. Owner: CPO. Timing: 2027. |
| **Net cost synergies** | **EUR 14.8m** | Sum of the two lines above. |
| **Walk-away price (haircut plan + net cost synergies)** | **EUR 57.3m** | EUR 42.5m + EUR 14.8m |
| **Asking price** | **EUR 60.0m** | Banker indication |
| **Gap (asking price − walk-away price)** | **EUR 2.7m above walk-away** | Asking price exceeds what Kestrel's own numbers support, before accounting for the risks below |
| Revenue synergies (not in price, upside only) | EUR 2.0m EBITDA/yr, uncosted | Cross-sell to Kestrel's ambient pharma customers. Figure comes from the banker's teaser (seller-side), no owner, no date, no one-off cost estimated — weak evidence, kept entirely out of the price per the trap check. |

Note: even crediting the seller's own (unsupported) growth plan, standalone value plus net cost synergies would be EUR 57.5m + EUR 14.8m = EUR 72.3m, comfortably above the EUR 60m ask. In other words, **the entire case for paying EUR 60m depends on believing 12%/yr growth that the last four years don't support.** On Kestrel's own haircut view, the ask is already above walk-away.

## Key risks and integration thesis
1. **Change-of-control exposure on 27% of revenue.** The two largest contracts (18% and 9% of revenue) contain change-of-control clauses and could be terminated or renegotiated on acquisition. Neither customer individually breaches the 30% concentration deal-breaker, but together they are large enough that losing both would materially cut the haircut-plan FCF (illustratively, if both contracts left and FCF fell roughly in proportion, FCF drops to about EUR 2.5m and standalone value to about EUR 31m — pushing the walk-away price to roughly EUR 46m, well under the ask). Mitigation: get written consent or extension from both customers before signing; owner: Kestrel corp-dev / legal, before signing.
2. **Key-person risk on the GDP audit relationship.** The founder personally holds the relationship with the pharma quality auditors. Losing the founder post-close risks the certification relationship that the whole deal depends on (GDP certification is a must-have). Mitigation: retention or transition agreement with the founder covering the auditor relationship specifically, not just a generic non-compete; owner: HR/integration lead, before signing.
3. **Revenue synergy unsized and seller-sourced.** The EUR 2.0m cross-sell synergy has no named owner, no date, and no one-off cost estimate, and comes from the banker's teaser. Treat as zero in the price; if it materialises, it's additional upside. Owner to be named before it can be counted on in the integration case.
4. **Integration thesis incomplete.** The pack names owners and dates for the two cost synergies (COO/2028 for depots, CPO/2027 for purchasing) but says nothing about who runs integration overall, what changes on day one, or what stays untouched (e.g., the founder's customer and auditor relationships in the short term). This needs to exist before signing, not after.

## What would change the answer
1. If both change-of-control customers confirm in writing they will continue post-close, the EUR 2.7m risk overhang shrinks and a price closer to EUR 60m becomes defensible — though still above the base-case walk-away.
2. If diligence finds a signed, contracted pipeline (not just aspiration) supporting growth meaningfully above the historical 4%/yr, the standalone value should move up from the EUR 42.5m haircut case toward the seller's plan, raising the walk-away price.
3. If the founder's auditor relationship can be cleanly transitioned (documented in a retention agreement) before signing, the key-person risk on certification is largely closed.
4. If GDP certification turns out to be under review, or any customer litigation surfaces, that is a deal-breaker as agreed with the CEO/CFO — the answer becomes "do not proceed at any price" regardless of the above.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Kestrel's haircut plan (not the seller's plan) is the right base case for standalone value | EUR 3.4m next-year FCF | CFO convention implies buyer's own view, not back-solved from seller numbers; haircut plan reflects actual 2022–2025 history | Commercial due diligence finds a contracted (not aspirational) pipeline supporting faster growth |
| 2 | No pending certification review or customer litigation exists beyond what's disclosed in the teaser | Treated as clear | Nothing flagged in the pack | Legal/regulatory due diligence finds either — this is an agreed deal-breaker |
| 3 | Cost synergies (depot consolidation, joint purchasing) are not materially dependent on the two change-of-control contracts | Full EUR 14.8m counted | Depot and purchasing savings are operational/fleet-wide, not tied to specific customer contracts, per the pack's description | Diligence shows depot volumes are concentrated in the flagged accounts |
| 4 | Downside scenario (27% of revenue lost) scales FCF roughly in proportion to revenue lost | Illustrative FCF ~EUR 2.5m, value ~EUR 31m | Simplification for sizing the risk only, not a modeled figure | Kestrel's finance team builds a proper contract-level FCF bridge |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Will the two change-of-control customers (27% of revenue combined) consent to continue, or can contracts be extended, before signing? | Single largest swing factor on value; could cut walk-away price by ~EUR 11m if both are lost | Frostline management / Kestrel legal, customer outreach | Confirms or kills the deal at any price near the ask |
| Can the founder's relationship with the pharma quality auditors be retained or formally transitioned? | GDP certification is a must-have; losing it post-close breaks the deal's core rationale | Kestrel HR/integration, Frostline founder | Determines whether certification continuity is a manageable risk or a blocker |
| Is there any pending or threatened litigation with a customer not disclosed in the teaser? | Agreed deal-breaker | Legal due diligence | Breach kills the deal outright |
| Is GDP certification currently under review, and when is the next renewal? | Agreed deal-breaker | Regulatory/quality due diligence | Breach kills the deal outright |
| Are Medivan Logistik and Thermo Lane actually for sale, and at what price? | Backup targets and negotiating leverage if Frostline talks stall | Kestrel corp-dev, banker outreach | Could open an alternative route or improve terms with Frostline |
| What specifically supports the seller's 12%/yr growth plan versus the ~4%/yr historical rate — signed pipeline or aspiration? | Determines whether standalone value should sit nearer EUR 42.5m or EUR 57.5m | Commercial due diligence, Frostline contract backlog | Could raise the walk-away price materially if credible |

