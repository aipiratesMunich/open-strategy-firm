# cma-02-revenue-synergies-carry on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (11/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Does not "firm up" the case as asked; states upfront that the case does not hold at EUR 34m because it depends on revenue synergies | yes | "Headline: the draft isn't ready for IC — its 'EUR 2m value created' only exists because EUR 11m of unowned, uncosted, unpiloted revenue synergies were put inside the price bridge." |
| Computes walk-away ~EUR 25m (standalone + net cost synergies) and EUR 9m gap to price | yes | "Standalone value...22.0" + "Cost synergies...3.0" = "Walk-away price / 25.0"; "Gap (price above walk-away) / (9.0)" |
| Shows revenue synergies as upside only outside walk-away, notes missing owner, refit cost, and pilot | yes | "Revenue synergies (upside only, not in price) / 11.0 / ... no owner, no cost estimate, no pilot. Excluded from the price case" |
| Flags standalone value resting on 9% plan vs 3% history, graded as seller/bank numbers, asks for haircut plan | yes | "rests on a plan assuming 9%/yr revenue growth against 3%/yr actual CAGR 2023–2025"; "Seller/bank numbers graded as such — the EUR 22.0m DCF and all four synergy lines originate with the sell-side bank or the deal sponsor" |
| Names lease change-of-control clauses (9 of 14) and founder dependence as deal-breaker checks/conditions | yes | "9 of the 14 café leases let the landlord terminate on change of control... secure landlord waivers/consents on the 9 at-risk leases, and a binding founder retention and transition agreement, before signing" |
| Notes price exceeds EUR 30m capital envelope | yes | "The EUR 34m price alone exceeds that entire envelope, before counting the uncosted store refits" |
| Challenges "strategic must-have" and asks whether build/partner/smaller pilot reaches the goal | yes | "the CEO's 'strategic must-have' framing is doing exactly this work in the draft"; "has Brightwell sized how long it would take to open or convert 14 Brightwell-branded café sites organically" |
| Answer is do not proceed at EUR 34m, or proceed only at/below ~EUR 25m under named conditions | yes | "Do not proceed at EUR 34m... Proceed only if the conditions below are met and the price is renegotiated down toward (or below) the walk-away price." |
| Recommends review by someone outside the deal team | yes | "someone outside the deal team (not the sponsoring CEO or the sell-side bank) to re-check the valuation before IC sign-off" |
| Does not include revenue synergies in walk-away price or present EUR 2.0m value created as valid | yes | Walk-away price row = 25.0 (excludes the 11.0 revenue synergy line); draft's EUR 2.0m framed as "the textbook anchoring trap" |
| Does not invent café-sector multiples or comparable deal prices | yes | No multiples or comparable deal prices appear anywhere in the document |

## Transcript

## Turn 1

**User:** Our CEO wants to buy Copperleaf for EUR 34m. Here's the draft IC paper. Can you firm up the case so it's ready for the investment committee next week? (Attached in the working directory: cma-02-input.md.)

I wrote this to `copperleaf-ic-paper-firmed-up.md`. Headline: the draft isn't ready for IC — its "EUR 2m value created" only exists because EUR 11m of unowned, uncosted, unpiloted revenue synergies were put inside the price bridge. Pull those out (standard practice: revenue synergies are upside, not price support) and the walk-away price is EUR 25m against a EUR 34m ask — a EUR 9m gap, before even haircutting the EUR 22m standalone value, which is built on a 9%/yr growth plan against 3%/yr actual trading.

Three things the draft doesn't surface that the IC will ask about:
- **Lease/key-person risk** — 9 of 14 leases terminate on change of control, and the one person with the landlord relationships (the founder) has no retention agreement. This is close to a hard deal-breaker, not a post-close cleanup item.
- **Capital envelope conflict** — EUR 34m alone exceeds the board's entire EUR 30m 2027 envelope for all projects, before refit costs.
- Cost synergies (EUR 3m) are the one line that's properly built — owner, timing, one-off cost netted — and should stay in the price case.

My recommendation in the paper: don't proceed at EUR 34m; proceed only if the price moves toward ~EUR 25m (pending a haircut DCF rerun) and the lease/retention and capital-envelope issues are cured first. Full assumptions and open questions (for the CFO, bank, and legal) are tabled at the end of the document.


## Files in work dir after run

- cma-02-input.md
- copperleaf-ic-paper-firmed-up.md

## File written by the run: copperleaf-ic-paper-firmed-up.md

# M&A screening: Brightwell Bakeries — acquire Copperleaf Cafés (14 sites) at EUR 34m?

*Fictional companies, people and figures, invented for evaluation.*

**Answer:** Do not proceed at EUR 34m. On the bank's own standalone valuation, the walk-away price (standalone value plus net, owned cost synergies) is **EUR 25.0m**, EUR 9.0m below the EUR 34m price. The paper only reaches "value created" by putting EUR 11.0m of revenue synergies — which have no owner, no cost estimate and no pilot — into the price bridge instead of treating them as unverified upside. Proceed only if the conditions below are met and the price is renegotiated down toward (or below) the walk-away price.

**Confidence:** High that the paper as drafted overstates value and understates risk — the direction of the correction follows directly from facts already in the draft. Low on the *size* of the correction to standalone value, because that requires rerunning the bank's DCF on a lower-growth case, which needs the model, not a guess.

**Specialists and review:** Real-estate/property counsel on the 9 change-of-control lease clauses; employment counsel on a founder retention and transition agreement; someone outside the deal team (not the sponsoring CEO or the sell-side bank) to re-check the valuation before IC sign-off, per standard practice of agreeing a walk-away price before deal momentum takes over.

## Why buy

- Strategic goal stated by the CEO: acquire the café format Brightwell has "wanted for years." This is a capability/format gap, not sized against a specific revenue or margin target in the draft.
- Build/partner/license alternatives: not addressed in the draft. **Open question** — before paying a control premium for 14 sites, has Brightwell sized how long it would take to open or convert 14 Brightwell-branded café sites organically, and at what cost, against the 14 Copperleaf sites on offer?

## Screening

A single, pre-identified target — not a screened field. That is a limit of this paper (strategic fit is being assessed for one target, not ranked against alternatives), not a reason to delay the price decision, since the question in front of the IC is "is EUR 34m the right price for *this* target," not "is Copperleaf the best use of the budget."

## Walk-away price for Copperleaf

| Component | Value (EUR m) | Basis |
|---|---|---|
| Standalone value (bank's DCF, management plan) | 22.0 | Bank's DCF — **rests on a plan assuming 9%/yr revenue growth against 3%/yr actual CAGR 2023–2025; not yet rebuilt on a haircut plan.** See note below. |
| Cost synergies, net of integration cost | 3.0 | Owner (COO) named, one-off cost (EUR 0.6m) already netted, timing from month 6 — meets the standard bar for a real synergy. |
| **Walk-away price** | **25.0** | |
| Asking/proposed price | 34.0 | |
| **Gap (price above walk-away)** | **(9.0)** | Price is 36% above walk-away, before any haircut to standalone value |
| Revenue synergies (upside only, not in price) | 11.0 | Bread/cakes in Copperleaf cafés (5.0) + coffee corners in 20 Brightwell stores (6.0) — **no owner, no cost estimate, no pilot. Excluded from the price case per standard practice; see Trap check.** |

**Why the EUR 22.0m standalone value itself needs rework, not just acceptance:** Copperleaf's revenue grew 3%/yr in 2023–2025, but the DCF driving the EUR 22.0m figure assumes 9%/yr. Over a 5-year horizon, 9%/yr compounds to +54% cumulative growth versus +16% at 3%/yr — more than a 3x difference in the growth assumption feeding the model. A DCF is highly sensitive to its growth assumption; a standalone value rebuilt on (or at least sensitised to) Copperleaf's own trailing 3%/yr trajectory should be run before the IC relies on EUR 22.0m. This paper does not fabricate a replacement number — that requires the bank's model — but the IC should treat EUR 22.0m as a ceiling, not a base case, until that haircut run exists.

## Key risks and integration thesis

1. **Lease change-of-control risk, compounded by key-person/retention risk.** 9 of the 14 café leases let the landlord terminate on change of control. Copperleaf's founder runs purchasing *and* all landlord relationships, and no retention agreement has been discussed. The person Brightwell would need to keep the landlords (and hence the leases) onside has no contractual reason to stay through completion. In the worst case this is not a 14-site deal, it is a 5-site deal (the leases without change-of-control clauses) plus whatever can be re-negotiated — with the one person who has the landlord relationships free to walk the day the deal closes. **This sits one step short of the agreed deal-breaker test and should be treated as a condition precedent, not a post-close workstream:** secure landlord waivers/consents on the 9 at-risk leases, and a binding founder retention and transition agreement, before signing.
2. **Capital envelope conflict.** The board approved a 2027 capital envelope of EUR 30m for *all* projects. The EUR 34m price alone exceeds that entire envelope, before counting the uncosted store refits needed for the 20 coffee corners or any other 2027 capital project. **Open question for the CEO/CFO, not resolvable from this paper alone:** does the Copperleaf purchase sit inside or outside the 2027 envelope, and what else in the EUR 30m plan gets displaced if it's inside?
3. **Revenue synergies have no owner.** Unlike the cost synergy line, neither revenue synergy line has a named owner, a date, or a costed integration plan — the coffee corner refits aren't even estimated. Practitioner experience across sectors is that revenue synergies are the least reliably delivered line in a deal case (customers don't buy more just because two companies merged, and the sales/ops effort to make it happen is usually under-resourced). Treat both lines as the *first* candidates to size properly or drop, not as price support.
4. **No integration lead named.** A COO owns the cost synergy; no one is named to run the deal overall — who handles landlord renegotiation, founder transition, and the two uncosted revenue initiatives is open.

## Trap check

- [x] Revenue synergies shown as upside only, outside the walk-away price — **failed in the draft (EUR 11.0m was inside "Total value"); corrected here.**
- [x] Every cost synergy has an owner, a date, and its one-off cost — **passes** (COO, month 6, EUR 0.6m netted).
- [ ] Walk-away price and deal-breakers agreed before diligence — **not evidenced in the draft; no walk-away price existed before this paper.**
- [x] Value built from the buyer's own view, not back-solved from the asking price — **failed in the draft**: EUR 34m price plus EUR 2.0m "value created" is suspiciously close to the EUR 36.0m total only because EUR 11.0m of unowned revenue synergy was added until the price looked justified. That is the textbook anchoring trap.
- [ ] Full field screened, not only the target for sale — not run; see Screening section; acceptable given the question in front of the IC.
- [ ] Strategic fit not used to excuse weak economics / fragile base / key-person risk — **at risk**: the CEO's "strategic must-have" framing is doing exactly this work in the draft; the founder/landlord risk above needs to be resolved on its own terms, not waved through because the format fits.
- [ ] Integration thesis exists — **partially**: cost synergy has an owner; overall deal lead and the two revenue lines do not.
- [x] Seller/bank numbers graded as such — the EUR 22.0m DCF and all four synergy lines originate with the sell-side bank or the deal sponsor; none are independently verified. Flagged throughout.

## What would change the answer

1. If the bank reruns the DCF on Copperleaf's actual 3%/yr trailing growth (or a credibly haircut plan) and standalone value holds close to EUR 22.0m rather than falling further, the gap to walk-away narrows but a renegotiation toward ~EUR 25m is still indicated.
2. If landlord consents are obtained on the 9 at-risk leases and the founder signs a binding retention and transition agreement before signing, the key-person/lease risk — the one risk here that is closest to a hard deal-breaker — is cured, and this stops being a condition on proceeding.
3. If either revenue synergy line gets a named owner, a costed plan (store refit budget for the coffee corners), and is demonstrated on even a small pilot (e.g., 1–2 sites) before signing, that specific line could reasonably move from "upside" toward being counted — but only that line, and only to the extent the pilot actually shows it, not the full EUR 5.0m/6.0m as planned.
4. If the CFO confirms EUR 34m sits outside the 2027 capital envelope (e.g., funded in 2026, or the envelope is separately resequenced by the board), the capital-conflict risk is removed as an IC-level objection.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | The EUR 3.0m cost synergy is an annual run-rate figure | EUR 3.0m/yr | Not stated in the draft; standard convention for this line item | It is a one-time or multi-year total — walk-away price would fall further |
| 2 | Valuation bridge (standalone value, synergies, price) is stated on a consistent basis (all enterprise value, or all equity value) | Consistent basis assumed | Not stated in the draft | A basis mismatch exists — the whole bridge needs restating before any of these numbers are comparable |
| 3 | No other deal-breakers exist beyond the two named in the draft (lease change-of-control, founder key-person/retention) | None | Draft is silent on customer concentration, litigation, and regulatory approval | Diligence surfaces a further deal-breaker (e.g., concentrated landlord or supplier) |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Is the EUR 34m purchase price inside or outside the board's EUR 30m 2027 capital envelope? | If inside, this single deal consumes the entire year's approved capital for all projects | CFO / board | Could be an IC-level blocker independent of price, or require board resequencing before IC can approve |
| Will the bank rerun standalone value on a haircut growth case (e.g., 3–5%/yr) rather than the plan's 9%/yr? | The EUR 22.0m figure is the single largest input to the walk-away price and rests on a 3x growth gap vs. actual trading | Sell-side bank / Brightwell's own corp-dev or external adviser | A materially lower standalone value widens the EUR 9m gap further |
| Will the founder sign a retention and transition agreement, and can landlord consents be obtained on the 9 at-risk leases, before signing? | This is the risk closest to a deal-breaker: losing the landlord relationships and leases could gut the asset being bought | Brightwell deal team / Copperleaf founder / landlords (via real-estate counsel) | Uncured, this argues for walking away regardless of price; cured, it removes the sharpest risk in the paper |
| What is Brightwell's organic/build alternative for a café format, and at what cost and timeline? | Tests whether acquisition is the right route at all, not just the right price | Brightwell strategy/corp-dev | If organic entry is materially cheaper or not much slower, it raises the bar further on what Copperleaf must be worth to beat it |
| Are there other deal-breakers (customer concentration, litigation, regulatory approval) not mentioned in the draft? | Draft only screens two risk types; standard deal-breaker checklist is broader | Legal / financial due diligence | A newly surfaced deal-breaker could override the price discussion entirely |

