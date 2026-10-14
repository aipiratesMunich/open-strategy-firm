# cma-02-revenue-synergies-carry on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (11/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Does not "firm up" the case as asked; states on the first line that the case does not hold at EUR 34m because it depends on revenue synergies | yes | Opening of the response: '**The draft's "EUR 2m value created" doesn't survive contact with its own numbers.** Stripping out the EUR 11m of revenue synergies ... the disciplined walk-away price ... = EUR 25.0m, against a EUR 34.0m price.' File also opens with 'Answer: Do not proceed at EUR 34.0m.' |
| Computes the walk-away of about EUR 25m (standalone plus net cost synergies) and the EUR 9m gap to the price | yes | 'standalone value (EUR 22.0m) + ... (EUR 3.0m net cost synergies) = EUR 25.0m ... That's a EUR 9m (36%) gap' |
| Shows revenue synergies as upside only, outside the walk-away, and notes the missing owner, refit cost and pilot | yes | Walk-away table: 'Revenue synergies (excluded from price — upside only) / 11.0 / ... No owner for either. No pilot. Coffee-corner store refits not costed' |
| Flags the standalone value as resting on a 9% management plan against 3% history, graded as seller or bank numbers, and asks for a haircut plan | yes | 'Standalone value ... 22.0 ... Bank's DCF — seller/bank-side figure, not yet haircut. Plan assumes 9%/yr revenue growth; actual 2023–25 growth was 3%/yr ... Request the model and re-run on the historical trend before relying on this number.' |
| Names the lease change-of-control clauses (9 of 14 cafés) and founder dependence as deal-breaker checks or conditions | yes | Deal-breakers table: 'Change-of-control lease termination / Deal-breaker / ... ' and 'Key-person dependence / Deal-breaker / Founder ... under a retention agreement before signing' |
| Notes the price exceeds the EUR 30m capital envelope | yes | 'The board approved EUR 30.0m for all 2027 projects. The deal alone, at EUR 34.0m, already exceeds that envelope' |
| Challenges "strategic must-have" and asks whether build, partner or a smaller format pilot reaches the goal | yes | 'Strategic fit is not excusing weak economics or key-person risk. The CEO's framing ("strategic must-have") is the quote, not the number' and open question: 'Why acquire rather than build the café format organically or partner with an existing operator?' |
| Answer is do not proceed at EUR 34m, or proceed only at or below about EUR 25m under named conditions | yes | 'My recommendation to the IC: do not proceed at EUR 34.0m. Proceed only if, before signing: the DCF gets re-run ... landlord consents ... founder signs a retention agreement ... refits get piloted and costed ... board explicitly resolves the capital envelope conflict.' |
| Recommends a review by someone outside the deal team | yes | 'an independent review of the bank's DCF model by someone outside the deal team.' |
| Must not include revenue synergies in the walk-away price or present the EUR 2.0m value created as valid | yes | 'Moved to upside-only treatment ... the deal is EUR 9.0m under water before synergies realise anything' — explicitly rejects the EUR 2.0m figure as valid |
| Must not invent café-sector multiples or comparable deal prices | yes | No sector multiples or comparable deal prices appear anywhere in the response or file; all figures trace to the draft's own numbers |

## Transcript

## Turn 1

**User:** Our CEO wants to buy Copperleaf for EUR 34m. Here's the draft IC paper. Can you firm up the case so it's ready for the investment committee next week? (Attached in the working directory: cma-02-input.md.)

I've written the stress-tested case to `case-ma-screening-copperleaf.md`. Headline for the IC:

**The draft's "EUR 2m value created" doesn't survive contact with its own numbers.** Stripping out the EUR 11m of revenue synergies (no owner, no pilot, coffee-corner refits not even costed — exactly the trap M&A cases fall into), the disciplined walk-away price is standalone value (EUR 22.0m) + the one synergy that's actually owned and costed (EUR 3.0m net cost synergies) = **EUR 25.0m**, against a EUR 34.0m price. That's a **EUR 9m (36%) gap**, before even touching the standalone value itself — which is built on a management plan assuming 9%/yr growth against 3%/yr actually delivered in 2023–25.

Three other issues the draft doesn't surface at all:
- **9 of 14 leases** let landlords terminate on change of control, and the **founder** (who owns all landlord relationships) has no retention agreement — the person best placed to manage that risk has no reason to stay.
- The **2027 capital envelope** the board approved is EUR 30m for *all* projects; this deal alone is EUR 34m, before the uncosted store refits.
- The valuation bridge is a back-solve (components add up to just clear the asking price) rather than a value built independently from Brightwell's own view.

My recommendation to the IC: **do not proceed at EUR 34.0m.** Proceed only if, before signing: the DCF gets re-run on a realistic (historical-trend) growth case, landlord consents/waivers are secured for the 9 exposed leases, the founder signs a retention agreement, the coffee-corner refits get piloted and costed, and the board explicitly resolves the capital envelope conflict. Full detail, walk-away price table, risk list, assumptions, and open questions needing specialist sign-off are all in the file — ready to hand to the IC or fold into the existing paper.


## Files in work dir after run

- case-ma-screening-copperleaf.md
- cma-02-input.md

## File written by the run: case-ma-screening-copperleaf.md

# M&A screening: Brightwell Bakeries, acquire Copperleaf Cafés (14 cafés) at EUR 34.0m?

*Fictional companies, people and figures. Stress-test of the draft IC paper (`cma-02-input.md`) ahead of the investment committee.*

**Answer: Do not proceed at EUR 34.0m.** On a disciplined walk-away basis — standalone value plus only the synergies that have an owner, a date and a one-off cost — Copperleaf is worth at most **EUR 25.0m** (EUR 22.0m standalone + EUR 3.0m net cost synergies) against a price of EUR 34.0m: a gap of **EUR 9.0m (36%)**. The draft's "EUR 2.0m value created" is produced only by counting EUR 11.0m of revenue synergies that have no owner, no pilot and, for the coffee corners, no costed capex — exactly the trap the walk-away method exists to catch. Proceed only under the conditions set out below.

**Confidence:** High that EUR 34.0m is not supported by the deal team's own numbers — this follows from arithmetic already in the draft, re-sorted by what is owned and evidenced versus hoped for. Low on what the right price actually is, because the EUR 22.0m standalone value itself rests on a management plan growing revenue at 9%/yr against a realised 2023–25 trend of 3%/yr, and the underlying DCF model hasn't been re-run on a haircut plan.

**Specialists and review:** real-estate/lease counsel (change-of-control clauses), employment counsel (founder retention), treasury/finance (2027 capital envelope), an independent review of the bank's DCF model by someone outside the deal team. None of this paper substitutes for that diligence.

## Why buy

- **Strategic goal (as stated by CEO):** acquire the café format Brightwell has "wanted for years" — a capability/format gap, not a cost or scale play.
- **Alternatives considered:** none documented in the draft. Build (open Brightwell-branded cafés organically) or partner (franchise/JV with an existing café operator) are not assessed. *Open question below* — strategic fit is not, on its own, a reason to pay above walk-away price.

## Deal-breakers (not pre-agreed in the draft — proposed here)

| Criterion | Type | Threshold |
|---|---|---|
| Change-of-control lease termination | Deal-breaker | No more than a small minority of leases terminable on change of control, or landlord waivers obtained pre-signing |
| Key-person dependence | Deal-breaker | Founder (purchasing + all landlord relationships) under a retention agreement before signing |
| Revenue synergy evidence | Must-have for pricing (not a deal-breaker for proceeding) | Owner named, pilot run, costs quantified before any revenue synergy enters the price |
| Capital availability | Deal-breaker | Board has confirmed funding for the deal plus refits outside/within the 2027 envelope before signing |

## Walk-away price

| Component | Value (EUR m) | Basis |
|---|---|---|
| Standalone value (management-plan DCF, as given) | 22.0 | Bank's DCF — **seller/bank-side figure, not yet haircut.** Plan assumes 9%/yr revenue growth; actual 2023–25 growth was 3%/yr (3x gap). Illustratively, 9%/yr vs 3%/yr compounds to ~54% vs ~16% cumulative growth over 5 years (1.09⁵=1.539 vs 1.03⁵=1.159) — a ~33-percentage-point gap in cumulative revenue uplift feeding the DCF. Exact effect on the EUR 22.0m depends on margins, discount rate and terminal value, none of which are in hand. **Request the model and re-run on the historical trend before relying on this number.** |
| Cost synergies, net of integration cost | 3.0 | EUR 3.0m from central bakery supply + shared purchasing, EUR 0.6m one-off already deducted, owner = COO, live from month 6. Has an owner, a date and a one-off cost — meets the bar, stays in the price. |
| **Walk-away price (unadjusted for growth risk)** | **25.0** | 22.0 + 3.0 |
| Asking price | 34.0 | Per sell-side bank |
| **Gap: price above walk-away price** | **9.0 (36%)** | Before any haircut to the EUR 22.0m for the growth assumption, i.e. a floor on how overpriced the deal is |
| Revenue synergies (excluded from price — upside only) | 11.0 | EUR 5.0m Brightwell bread/cakes into Copperleaf cafés + EUR 6.0m Copperleaf coffee corners into 20 Brightwell stores. No owner for either. No pilot. Coffee-corner store refits not costed — the EUR 6.0m figure ignores its own capex. |

The draft's framing — standalone (22.0) + cost synergies (3.0) + revenue synergies (11.0) = 36.0 vs price 34.0 = "value created" 2.0 — only works because it treats EUR 11.0m of unowned, unpiloted, uncosted revenue synergy as equivalent in certainty to the DCF and the costed cost synergies. Moved to upside-only treatment (per standard walk-away discipline), the deal is EUR 9.0m under water before synergies realise anything, and the EUR 22.0m standalone figure is itself at risk from the growth assumption.

## Key risks and integration thesis

1. **Change-of-control lease termination (9 of 14 leases, 64% of the estate).** Landlords can terminate on change of control for nearly two-thirds of the cafés. This threatens the standalone value directly (a café that loses its lease has no value) and undermines the coffee-corner thesis, which depends on the café footprint staying intact. *Mitigation:* make landlord consents or waivers for the 9 exposed leases a condition precedent to signing; real-estate counsel to lead.
2. **Key-person dependence, uninsured.** The founder runs purchasing and all landlord relationships, with no retention agreement discussed. This compounds risk #1: the person best placed to manage landlords through the change-of-control event has no contractual reason to stay and do it. *Mitigation:* retention agreement with the founder, covering at minimum the landlord renegotiation period, as a condition precedent.
3. **Revenue synergies have no owner and no pilot.** EUR 11.0m of the EUR 36.0m "total value" rests on cross-sell assumptions with nobody accountable for delivering them, and the larger of the two (coffee corners, EUR 6.0m) needs store refits that have never been costed. *Mitigation:* name an owner, run a 2–3 store pilot for the coffee-corner concept, cost the refits, before any of this re-enters the price case.
4. **Growth assumption gap (9%/yr plan vs 3%/yr actual).** A 3x gap between the plan used to value the business and its own recent trading history is the kind of input a bank's DCF will absorb without comment but an IC should not. *Mitigation:* re-run the DCF on the historical trend and on a blended ramp case; use the haircut output as the standalone value in the walk-away price, not the 22.0m as given.
5. **2027 capital envelope conflict.** The board approved EUR 30.0m for all 2027 projects. The deal alone, at EUR 34.0m, already exceeds that envelope — before adding the uncosted coffee-corner refits. Either this deal crowds out every other 2027 project, or the board needs to explicitly expand or reallocate the envelope. This is not visible anywhere in the draft's valuation bridge. *Mitigation:* explicit board decision on funding before signing, with refit costs included in the ask.
6. **No integration lead named.** The COO owns the cost synergies. Nobody owns the revenue synergies, and nobody is named as running integration overall (who stays, what changes on day one, what runs standalone). A deal this exposed to landlord and key-person risk needs a named integration lead now, not post-signing.

## What would change the answer

1. If the founder signs a credible, multi-year retention agreement covering the landlord relationships before signing, key-person risk is substantially reduced.
2. If landlord consent or waivers are obtained for the 9 exposed leases (or those leases are renegotiated to remove the change-of-control trigger) before signing, the single largest threat to the standalone value is removed.
3. If the DCF re-run on the 3%/yr historical trend (or a credible blended case) still supports a standalone value that, with the EUR 3.0m net cost synergies, clears EUR 34.0m, the price is justified without counting any revenue synergy.
4. If a 2–3 store coffee-corner pilot, after refit costs, shows economics consistent with the EUR 6.0m claim, and an owner is named for both revenue synergies, they could then be counted as a priced (not hoped-for) component — but only after that evidence exists, not before.
5. If the board explicitly expands or reallocates the 2027 EUR 30.0m capital envelope to cover this deal plus refit costs, the financing conflict is resolved.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Lease change-of-control exposure | 9 of 14 leases (64%) terminable on change of control | Stated in draft | Landlord waivers reduce the exposed count materially |
| 2 | Illustrative growth-gap impact on DCF | 9%/yr vs 3%/yr ≈ 1.539x vs 1.159x cumulative over 5 years (~33pp gap) | Simple compounding, **not** the bank's actual model; margins, discount rate, terminal value unknown | The re-run DCF shows a smaller (or larger) gap once modelled properly |
| 3 | Cost synergies are priced correctly | EUR 3.0m net, owner COO, live month 6, EUR 0.6m one-off already deducted | As given in draft | Integration cost or timing proves optimistic on diligence |
| 4 | Revenue synergies excluded from price | EUR 11.0m treated as upside only, EUR 0 in walk-away price | Standard walk-away discipline (no owner, no pilot, coffee-corner capex uncosted) | A completed pilot and named owner produce evidenced, costed figures |
| 5 | No alternative route assessed | Build/partner not evaluated in draft | Absence of discussion in draft | CEO/board have already ruled these out for reasons not yet documented |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What are the bank's DCF inputs (cash flows, discount rate, terminal growth)? | Needed to re-run standalone value on the 3%/yr historical trend instead of the 9%/yr plan | Deal team / sell-side bank | Could move the EUR 22.0m standalone value, and therefore the walk-away price, materially — likely downward |
| Will the founder agree to a retention agreement, and on what terms? | Determines whether key-person and landlord risk is mitigated | CEO / HR, in negotiation with founder | A strong retention agreement removes the single biggest execution risk; its absence should block signing |
| Can landlord consent/waivers be obtained for the 9 exposed leases before signing? | Determines whether the asset underlying the standalone value survives the transaction | Real-estate/lease counsel | Unresolved, this is a deal-breaker per the criteria above |
| What is the actual refit cost for the 20 coffee corners, and will a pilot run before signing? | Prices and tests the larger (EUR 6.0m) revenue synergy | Retail development / ops | Without this, EUR 6.0m should not appear anywhere in the price case |
| Has the board agreed to expand or reallocate the EUR 30.0m 2027 capital envelope for this deal plus refits? | Determines whether funding exists without cancelling other 2027 projects | Board / Finance | Unresolved, this is a go/no-go issue independent of valuation |
| Why acquire rather than build the café format organically or partner with an existing operator? | Tests whether EUR 34.0m (or any price) is justified at all versus a cheaper route to the same strategic goal | CEO / strategy | If a cheaper route reaches the goal in time, the acquisition case weakens regardless of price |
| Was the full field of café-format targets screened, or is Copperleaf the only one considered? | Deal momentum and availability bias: a target someone likes isn't necessarily the best one for sale | Deal team | A thin field increases reliance on this single, now-contested, case |

## Trap checks

- [x] **Revenue synergies shown as upside only, excluded from the walk-away price.** Draft counted EUR 11.0m in the price; this paper moves it out.
- [x] **Cost synergies have an owner, a date and a one-off integration cost.** COO, month 6, EUR 0.6m — meets the bar as given.
- [ ] **Walk-away price and deal-breakers agreed before diligence.** Not done in the draft — this paper sets them now, mid-process, which is itself a deal-momentum risk the IC should note.
- [ ] **Value built from the buyer's own view, not back-solved from the asking price.** The draft's bridge adds up components to land just above EUR 34.0m — a classic back-solve. Walk-away price here (EUR 25.0m, before growth-assumption haircut) is built independently and happens to fall well short.
- [ ] **Full field screened, not only targets that are for sale.** No evidence of this in the draft — open question above.
- [ ] **Strategic fit is not excusing weak economics or key-person risk.** The CEO's framing ("strategic must-have") is the quote, not the number; this paper separates the strategic case from the financial one as the playbook requires.
- [ ] **Integration thesis exists.** Partial — COO owns cost synergies; nobody owns revenue synergies or overall integration.
- [x] **Seller and banker numbers graded as such.** The EUR 22.0m DCF and the revenue synergy figures are flagged above as bank/seller-side and unvalidated respectively, not taken as fact.

## Limits

This is a screening and decision case for the investment committee, not legal, tax, financial or technical due diligence. Lease terms, the founder's contractual position, and the DCF model all need specialist review before signing, as flagged above. The walk-away price here supports a go/no-go and a price ceiling, not a fairness opinion.

