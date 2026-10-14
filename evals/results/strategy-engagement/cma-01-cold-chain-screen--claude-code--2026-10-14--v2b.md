# cma-01-cold-chain-screen on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Runs the funnel on all eight companies with stage of drop-out, and keeps Medivan Logistik and Thermo Lane on short list despite not known to be for sale | yes | Funnel table: 8→6 (drops ColdArc, Chillbox)→5 (drops Icepath)→4 (drops Glacier Freight)→3 (drops Polar Route); short list keeps Medivan Logistik and Thermo Lane explicitly noting 'Availability unknown' |
| Values Frostline on haircut plan (~EUR42.5m) and shows seller plan (~EUR57.5m) as seller's view, graded as seller numbers | yes | 'Kestrel's haircut plan... EUR 42.5m... used for the decision' vs 'Seller's plan (12%/yr growth)... EUR 57.5m... seller case, not used for the decision' |
| Net cost synergies of about EUR14.8m, each with owner, date and one-off cost | yes | Depot consolidation 10.0 net (owner COO, from 2028, one-off 2.0) + Joint purchasing 4.8 net (owner CPO, from 2027, one-off 0.2) = EUR 14.8m total |
| Walk-away price of about EUR57.3m built from standalone plus net cost synergies, states EUR60m is above it | yes | 'Walk-away price / EUR 57.3m / Sum of the two rows above' with 'Gap (ask − walk-away) / EUR 2.7m over' |
| Shows EUR2.0m revenue synergy as upside only, outside walk-away, with no owner/date/one-off cost | yes | 'no one-off integration cost estimated, no named owner, no date... Treat as pure upside to be confirmed after close, not as consideration for the price' |
| Answer is do not proceed at EUR60m, or proceed only at/below ~EUR57m under named conditions | yes | 'Proceed under conditions with Frostline Pharma Transport, at a maximum price of EUR 57.3m... not EUR 60m as asked' |
| Names change-of-control clauses and founder dependence as deal-breaker checks or conditions | yes | 'make customer consent or contract extension a condition precedent to signing'; 'founder retention/transition agreement covering the auditor relationship' |
| Compares deal with build route (EUR35m, four years, misses 2028) | yes | 'Build alternative: EUR 35m, ~4 years — misses the 2028 deadline by itself' |
| Recommends review by someone outside the deal team | yes | 'someone outside the deal team to sanity-check the growth assumption before signing' |
| Flags legal, tax and financial due diligence for specialists | NO | Specialists listed are 'Legal... regulatory/quality... and someone outside the deal team' — no mention of tax anywhere, and no explicit 'financial due diligence' specialist flagged |
| Does not include revenue synergies in walk-away price or back-solve from asking price | yes | Walk-away price table excludes the EUR2.0m revenue synergy row ('not in price'); standalone value uses haircut FCF not back-solved from the EUR60m ask |
| Does not invent facts about targets beyond the table | yes | All figures (e.g., Medivan EUR24m revenue, Thermo Lane 27% top customer, EBITDA EUR1.9m) are presented as given data points consistent with the screening table, with no invented margins/customers/owners beyond what's cited |

## Transcript

## Turn 1

**User:** Run the Kestrel cold-chain M&A screen from the pack and tell us whether to go ahead with Frostline at the asking price. (Attached in the working directory: cma-01-input.md.)

I ran the full M&A screen (quick case) against the CEO/CFO criteria and wrote it to `case-ma-screening-kestrel-frostline.md`. Headline:

**Do not pay EUR 60m as asked. Proceed only under conditions, at a maximum price of EUR 57.3m** (Kestrel's own haircut-case standalone value of EUR 42.5m + EUR 14.8m of named, owned cost synergies). The EUR 60m ask is EUR 2.7m *above* that walk-away price — being under the EUR 65m budget ceiling doesn't mean it's good value; those are two different tests, and this deal fails the second one as priced.

Key points:
- **Screen of all 8 long-list names** (not just the ones marked "for sale"): only Frostline, Medivan Logistik, and Thermo Lane pass every must-have and deal-breaker. Polar Route fails on customer concentration (41%), ColdArc on size, Icepath on certification, Glacier Freight on regional coverage, Chillbox on both size and concentration. Only Frostline is confirmed for sale with figures to value — Medivan and Thermo Lane are real but untested backups.
- **Valuation used Kestrel's haircut FCF (EUR 3.4m), not the seller's plan (EUR 4.6m)** — the 4%-vs-12% growth assumption is the single biggest swing factor in the whole deal (EUR 15m).
- **The EUR 2.0m "revenue synergy" is excluded from the price entirely** — it's banker-sourced, has no owner, date, or one-off cost, and is flagged as pure unverified upside, consistent with the playbook's trap check on revenue synergies.
- **Three risks should shape negotiation, not just price:** (1) change-of-control clauses on 27% of revenue — make customer consent a signing condition; (2) the founder is the sole link to the pharma quality auditors, i.e., the certification itself is a key-person risk — needs a retention/transition agreement; (3) litigation status is simply unaddressed in the data and must be confirmed in legal diligence before signing, since it's an explicit deal-breaker.

Full funnel, synergy math, deal-breaker table, assumptions, and open questions are in the file.


## Files in work dir after run

- case-ma-screening-kestrel-frostline.md
- cma-01-input.md

## File written by the run: case-ma-screening-kestrel-frostline.md

# M&A screening: Kestrel Logistics, proceed with Frostline Pharma Transport at EUR 60m?

**Headline:** the EUR 60m ask sits above Kestrel's own walk-away value of ≈EUR 57.3m (haircut standalone + named cost synergies only) — EUR 2.7m too high — even though it is EUR 5m under the EUR 65m budget ceiling. Budget headroom and walk-away price are not the same test; this deal fails the second one as currently priced.

---

## Step 1: Sharpen the question

Decision question: *Is Frostline Pharma Transport worth more to Kestrel than the EUR 60m asking price, counting only synergies Kestrel can name, own and deliver, and does it beat the EUR 35m / four-year build alternative given the 2028 deadline?*

Already agreed before target discussion (September 2026, CEO/CFO): strategic goal, budget ceiling, must-haves, deal-breakers, valuation convention. No further sharpening rounds needed — proceeding straight to the screen.

## Step 2: Issue tree (instantiated)

| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Why buy | Building in-house (EUR 35m, ~4 years) misses the 2028 deadline; buying is faster | A target reaches certification + customer base in time for less than build cost | **Confirmed** — build misses 2028 by construction; acquisition is the only route tested that can hit the date |
| Screen | At least one long-list company passes all must-haves and deal-breakers | Full field screened and none passes | **Confirmed** — 3 of 8 pass (Frostline, Medivan Logistik, Thermo Lane) |
| Deal-breakers | Frostline passes every agreed deal-breaker | Any deal-breaker breached and not cured before signing | **Reshaped** — concentration test passes on the stated metric, but litigation status is unconfirmed and must be checked before signing |
| Strategic fit | Frostline closes the stated gap (GDP cert, 2–8°C, 3 home regions) | Target adds little the buyer lacks | **Confirmed** — full overlap on geography and certification |
| Standalone value | Haircut-plan value is close to the EUR 60m ask | Standalone value well below ask with no synergies to bridge it | **Reshaped** — haircut value alone (EUR 42.5m) is well below the ask; named cost synergies bridge most but not all of the gap |
| Cost synergies | Named, owned, dated synergies bridge the remaining gap | Synergies lack owners, dates or one-off costs | **Confirmed as sized, insufficient to close gap** — EUR 14.8m net, well-specified, but 42.5 + 14.8 = 57.3 < 60 |
| Execution | Integration risk is manageable with named owners | Key people or customers likely to leave on change of control | **Killed as "manageable" / open as risk** — two largest contracts (27% of revenue combined) carry change-of-control clauses; founder is the sole link to the pharma quality auditors |
| Walk-away | Price stays at or below standalone value plus net cost synergies | Price above walk-away: walk or renegotiate | **Triggered** — EUR 60m ask is EUR 2.7m above the EUR 57.3m walk-away price |

## Step 3: Deciding analyses

### a. Screening funnel — full field, not just "for sale" names

| Stage | Companies remaining | Criterion applied |
|---|---|---|
| Long list | 8 | — |
| Revenue EUR 20–80m | 6 | Drops ColdArc (95, also confirmed *not for sale*) and Chillbox Couriers (12) |
| GDP certified today | 5 | Drops Icepath (not certified) |
| Operations in ≥2 of 3 home regions | 4 | Drops Glacier Freight (1 of 3) |
| Top customer ≤30% of revenue | 3 | Drops Polar Route (41%) |
| **Short list** | **Frostline, Medivan Logistik, Thermo Lane** | Litigation and certification-continuity status not yet confirmed for any of the three |

Screened the full field of 8 before looking at who is "for sale," per the case note's own warning against availability-led screening. Only Frostline is confirmed for sale (banker teaser) with figures to value; Medivan Logistik and Thermo Lane are "not known" — genuine backups, not yet live.

Watch item: Thermo Lane's top-customer share (27%) sits close to the 30% deal-breaker line and would need an early check if it becomes the active target.

### b. Target market and position — not sized

No data on Frostline's segment growth, share, or competitive intensity was supplied. Not decisive for the price question this round; carried to Open questions since it bears on whether 12% (seller) or 4% (history) growth is the more credible forward case.

### c. Strategic fit map

Frostline already operates in all 3 of Kestrel's home regions (full geographic overlap) and holds the GDP certification Kestrel lacks. In Ansoff terms this is closest to **product development**: a new regulated capability sold into Kestrel's existing ambient-pharma customer relationships, not entry to a new customer base. Strategic fit is clear — which is exactly why it must not be allowed to paper over the financial and execution risks below (trap check 6).

### d. Standalone valuation — CFO convention, FCF / (10% − 2%)

| Case | Next-year FCF | Value (FCF / 8%) | Basis |
|---|---|---|---|
| Seller's plan (12%/yr growth) | EUR 4.6m | **EUR 57.5m** | Banker teaser / management meeting — seller case, not used for the decision |
| Kestrel's haircut plan (~4%/yr, per 2022–25 history) | EUR 3.4m | **EUR 42.5m** | Kestrel's own case — used for the decision |

The entire gap between a seller value of 57.5m and a buyer-case value of 42.5m (EUR 15m) rides on one assumption: 12% vs. 4% revenue growth. That is the single biggest swing factor in this deal — bigger than either synergy line.

### e. Synergy case — cost and revenue kept separate

Cost synergies, per the CFO's formula (run-rate / 10% − one-off cost, no phase-in):

| Synergy | Run-rate (EUR m/yr) | Value (run-rate / 10%) | One-off cost | Net value | Owner | From |
|---|---|---|---|---|---|---|
| Depot consolidation | 1.2 | 12.0 | 2.0 | **10.0** | COO | 2028 |
| Joint purchasing | 0.5 | 5.0 | 0.2 | **4.8** | CPO | 2027 |
| **Total net cost synergies** | | | | **EUR 14.8m** | | |

Both have an owner, a date and a costed one-off — they pass the synergy trap check and go into the price.

Revenue synergy — **kept out of the price, flagged as unverified upside**:
- "Cross-selling cold chain to Kestrel's ambient pharma customers," EUR 2.0m EBITDA run-rate, **no one-off integration cost estimated, no named owner, no date**, sourced from the banker's teaser (seller-side).
- This fails three of the four synergy-quality tests (owner, cost, date) and comes from the party with every incentive to inflate it. Per the case note's own trap list, revenue synergies are rarely realised as planned and belong outside the walk-away price. Treat as pure upside to be confirmed after close, not as consideration for the price.
- If priced at the CFO's own FCF multiple (illustrative only — the convention applies to FCF, not EBITDA, so this is explicitly *not* a valid use of the formula): 2.0 / 8% = EUR 25m. Flagging this number only to show how large the temptation is to fold it in — it must not be used to justify paying more for Frostline.

### f. Deal-breaker check

| Deal-breaker | Status | Evidence |
|---|---|---|
| Any single customer >30% of revenue | **Clear** | Top customer 18% |
| Certification under review or lapsed | **Clear on paper** | GDP certified today, no indication of review/lapse — but see key-person risk below |
| Unresolved litigation with a customer | **Unconfirmed** | Not addressed anywhere in the teaser or management meeting notes — must be confirmed in legal diligence before signing |

Contingent risks that are not stated deal-breakers but materially affect value:
- **Change-of-control clauses** on the two largest contracts (18% + 9% = 27% of revenue). These customers can walk or renegotiate at close; if either exits, pro-forma FCF falls below even the 3.4m haircut case, and the EUR 57.3m walk-away shrinks further.
- **Key-person / certification-continuity risk**: the founder personally holds the relationship with the pharma quality auditors. Kestrel is buying the certification as the core asset; if that relationship doesn't transfer, the asset is impaired regardless of what the balance sheet says.

### g. Outside view — not available

No data on how Kestrel's (or a comparable buyer's) past logistics acquisitions performed against their own underwriting case. Missing comparison; add to Open questions before signing — it would calibrate how much confidence to put in the 4%-vs-12% growth question.

## Step 4: Trap checks

- [x] Revenue synergies shown as upside only, outside the walk-away price — EUR 2.0m EBITDA figure excluded from the EUR 57.3m walk-away.
- [x] Every cost synergy has an owner, a date and its one-off integration cost — both lines complete (COO/2028, CPO/2027).
- [x] Walk-away price and deal-breakers agreed before diligence, unchanged — set by CEO/CFO in September 2026, before any target was named; nothing has been changed here.
- [x] Value built from the buyer's own view, not back-solved from the ask — standalone value uses Kestrel's 3.4m haircut FCF, not the seller's 4.6m plan.
- [x] Full field screened, not only targets marked "for sale" — all 8 long-list names screened on must-haves/deal-breakers before availability was considered.
- [x] Strategic fit is not used to excuse weak economics, fragile customers or key-person risk — fit is strong (full regional overlap, held certification), but the recommendation below does not let that override the change-of-control and founder risks; both are carried as price- and condition-shaping, not waived.
- [ ] **Open:** an integration thesis exists (who runs it day one, what changes, what stays untouched) — the two cost synergies have functional owners (COO, CPO), but no named overall integration lead, and no plan yet for the founder/auditor-relationship handover. Fix before signing.
- [x] Seller and banker numbers graded as such — seller's 4.6m FCF and 12% growth plan, and the banker's EUR 2.0m revenue-synergy claim, are explicitly labelled seller/banker-sourced and excluded from the headline valuation.

## Step 5: Answer page

**Answer:** Proceed under conditions with Frostline Pharma Transport, at a maximum price of **EUR 57.3m** (Kestrel's own walk-away: haircut standalone value EUR 42.5m plus net cost synergies EUR 14.8m) — not EUR 60m as asked. Kestrel can afford up to EUR 65m on budget, but EUR 60m already pays EUR 2.7m above what Kestrel's own case supports; close that gap in negotiation or by securing the conditions below, or walk.

**Confidence:** Medium — the arithmetic is solid and fully sourced, but it rests on one unverified assumption (which growth case, 4% or 12%, is right — a EUR 15m swing) and two unresolved facts (litigation status; whether the auditor relationship survives the founder) that could each move the answer on their own.

**Specialists and review:** Legal (change-of-control clause review and litigation confirmation), regulatory/quality (GDP certification continuity and the auditor relationship independent of the founder), and someone outside the deal team to sanity-check the growth assumption before signing — this is a screening valuation, not due diligence or a fairness opinion.

### Why buy
- Strategic goal: GDP-certified pharma cold-chain capability (2–8°C) across Kestrel's three home regions by 2028.
- Build alternative: EUR 35m, ~4 years — misses the 2028 deadline by itself. Acquisition is the only route tested that can hit the date, which is why "why buy" is confirmed, not why the price should be paid as asked.

### Screening criteria and deal-breakers
| Criterion | Type | Threshold |
|---|---|---|
| GDP certified today | Must-have | Yes |
| Revenue | Must-have | EUR 20–80m |
| Home-region operations | Must-have | ≥2 of 3 |
| Top customer share | Deal-breaker | ≤30% of revenue |
| Certification status | Deal-breaker | Not under review or lapsed |
| Customer litigation | Deal-breaker | None unresolved |

### Funnel
| Stage | Companies | Criteria applied |
|---|---|---|
| Long list | 8 | — |
| After revenue band | 6 | Drops ColdArc, Chillbox Couriers |
| After certification | 5 | Drops Icepath |
| After region coverage | 4 | Drops Glacier Freight |
| After concentration deal-breaker | 3 | Drops Polar Route |

### Short list
| Target | Strategic fit | Standalone value (haircut) | Net cost synergies | Revenue synergies (upside only) | Deal-breaker flags | Rank |
|---|---|---|---|---|---|---|
| Frostline Pharma Transport | Full regional + certification overlap | EUR 42.5m | EUR 14.8m | EUR 2.0m EBITDA (unverified, banker-sourced) | Litigation unconfirmed; CoC clauses on 27% of revenue; founder/auditor key-person risk | 1 (only confirmed-for-sale candidate) |
| Medivan Logistik | Passes must-haves, smaller (EUR 24m rev) | Not sized — no seller figures | Not sized | Not sized | Availability unknown; litigation/CoC unknown | 2 (approach to test availability) |
| Thermo Lane | Passes must-haves, smallest EBITDA (EUR 1.9m) | Not sized — no seller figures | Not sized | Not sized | Top customer 27% — close to the 30% line; availability unknown | 3 (approach, watch concentration) |

### Walk-away price for Frostline
| Component | Value | Basis |
|---|---|---|
| Standalone value (haircut plan) | EUR 42.5m | 3.4m FCF / 8%, Kestrel's own case |
| Cost synergies, net of integration cost | EUR 14.8m | Depot consolidation (10.0m) + joint purchasing (4.8m), CFO formula |
| **Walk-away price** | **EUR 57.3m** | Sum of the two rows above |
| Asking price | EUR 60.0m | Banker teaser |
| Gap (ask − walk-away) | **EUR 2.7m over** | — |
| Budget ceiling (for reference only) | EUR 65.0m | CEO/CFO, agreed before target discussion |
| Revenue synergies (not in price) | EUR 2.0m EBITDA/yr | Banker teaser; no owner, date or one-off cost — upside only |

### Key risks and integration thesis
1. **Growth assumption gap (4% history vs. 12% seller plan — EUR 15m swing):** drives almost the entire standalone-value uncertainty. Mitigation: underwrite on the haircut case only; treat any upside from faster growth as reason to pay less, not evidence to pay more. Owner: CFO, before signing.
2. **Change-of-control clauses on 27% of revenue (two largest contracts):** could cut FCF further after close. Mitigation: make customer consent or contract extension a condition precedent to signing, as in the worked precedent in this playbook; price any customer that doesn't consent out of the standalone value. Owner: deal lead + legal, before signing.
3. **Founder is the sole link to the pharma quality auditors:** the certification is the asset being bought; if the relationship doesn't transfer, so does the risk of losing it. Mitigation: founder retention/transition agreement covering the auditor relationship for a defined post-close period, verified independently of the founder's own assurance. Owner: HR/integration lead, before signing.
4. **Litigation status unconfirmed:** this is an explicit deal-breaker category that the data simply doesn't address. Mitigation: legal confirmation before signing; if unresolved litigation exists, it kills the deal per the agreed deal-breaker, regardless of price. Owner: legal, before signing.
5. **No named overall integration lead or day-one plan**, beyond the two synergy owners (COO, CPO). Mitigation: name an integration lead and a day-one plan (what changes, what stays untouched, especially customer-facing and auditor-facing continuity) before signing, not after.

### What would change the answer
1. If the seller agrees a price at or below EUR 57.3m, or structures an earn-out that pays the EUR 2.7m gap only if growth exceeds the 4% haircut case, proceed without further conditions on price.
2. If either flagged customer (18% or 9% of revenue) does not consent to change of control, standalone value falls further below EUR 57.3m and the maximum price should be cut accordingly, or the deal should walk.
3. If legal diligence finds unresolved litigation with a customer, this is a deal-breaker as agreed in September 2026: do not proceed at any price unless cured before signing.
4. If the founder will not commit to a retention/transition agreement covering the auditor relationship, treat the certification itself as at risk and discount the standalone value, or walk.
5. If Medivan Logistik or Thermo Lane turn out to be for sale at a price below their own (not yet sized) standalone value, run this same screen on them as parallel options — don't let deal momentum on Frostline foreclose them.

## Assumptions
| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | FCF scales roughly linearly with the assumed revenue-growth rate between the 4% and 12% cases, over this narrow range | Used only to illustrate that ~5.4%/yr growth (not the full 12%) would be enough to justify EUR 60m once cost synergies are included | Linear interpolation between the two stated FCF figures (3.4m at 4%, 4.6m at 12%) | Frostline's actual FCF sensitivity to growth is materially non-linear (e.g. due to fixed-cost operating leverage) |
| 2 | No phase-in period for cost synergies | Full run-rate value from year one, per CFO convention | CFO's stated valuation convention | Kestrel's own convention changes, or integration takes materially longer than the stated "from" dates (2027/2028) |
| 3 | The EUR 2.0m revenue synergy is excluded entirely from the price | EUR 0m contribution to walk-away price | Banker-sourced, no owner/date/cost, playbook trap check on revenue synergies | Kestrel's own commercial team independently validates a specific, owned, dated cross-sell pipeline with named customers |
| 4 | Litigation and certification-continuity status are treated as unresolved, not as "pass" | Not counted as confirmed in the deal-breaker check | Absence of any statement on litigation in the source materials | Legal diligence confirms no unresolved litigation and the auditor relationship is shown to be institutional, not personal to the founder |

## Open questions
| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is there any unresolved litigation with a Frostline customer? | This is an explicit, agreed deal-breaker; silence in the teaser is not confirmation | Frostline's legal counsel / Kestrel legal diligence | Unresolved litigation kills the deal regardless of price |
| Will the two change-of-control customers (18% and 9% of revenue) consent to the transaction? | Determines whether the haircut FCF case (and therefore the walk-away price) actually holds post-close | Those two customers, via Frostline / Kestrel corp dev | Non-consent lowers standalone value and the maximum price further below EUR 57.3m |
| Does the pharma-auditor relationship depend solely on the founder, or is it institutional? | The certification is the asset being bought; a personal relationship is a single point of failure | Frostline founder / Kestrel quality & regulatory team | If purely personal and the founder won't commit to transition, discount standalone value or walk |
| Is 4%/yr or 12%/yr the more credible forward growth rate for Frostline? | EUR 15m value swing — the single largest uncertainty in this valuation | Frostline's own forward bookings/pipeline; Kestrel corp dev market view | Shifts the standalone value anywhere between EUR 42.5m and EUR 57.5m |
| Are Medivan Logistik and Thermo Lane actually for sale, and at what price? | Both pass the must-have/deal-breaker screen and are untested backups | Kestrel corp development, banker outreach | Could provide a lower-risk or lower-price alternative path to the same strategic goal |
| How have Kestrel's (or comparable buyers') past logistics acquisitions performed against their own underwriting case? | Outside view on how much to trust this kind of projection | Kestrel corp development / M&A track record | Would sharpen confidence in which growth case (4% vs. 12%) to trust |

## Trap checks (summary)
All eight trap checks from the M&A screening playbook were run in Step 4 above; seven pass with evidence, one is open (no named overall integration lead / founder-transition plan yet) and is carried into the recommendation as a signing condition, not waived.

