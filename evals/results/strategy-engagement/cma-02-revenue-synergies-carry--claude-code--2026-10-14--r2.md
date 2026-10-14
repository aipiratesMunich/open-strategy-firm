# cma-02-revenue-synergies-carry on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (11/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Does not 'firm up' the case as asked; states on the first line that the case does not hold at EUR 34m because it depends on revenue synergies. | yes | File opens: '**Answer: do not proceed at EUR 34m.** The claimed EUR 2.0m of value creation exists only because EUR 11.0m of unowned, uncosted, unpiloted revenue synergies were put into the price-supporting bridge.' Chat response also opens with 'it doesn't hold up as written' before immediately citi |
| Computes the walk-away of about EUR 25m (standalone plus net cost synergies) and the EUR 9m gap to the price. | yes | 'Walk-away price (standalone + cost synergies only) = EUR 25.0m even using the bank's own optimistic standalone number — EUR 9m below the EUR 34m ask.' |
| Shows revenue synergies as upside only, outside the walk-away, and notes the missing owner, refit cost and pilot. | yes | Table: 'Revenue synergy 1 ... 5.0 — upside only, not in price / No owner named; no pilot' and 'Revenue synergy 2 ... 6.0 — upside only, not in price / No owner named; store refits not costed; no pilot' |
| Flags the standalone value as resting on a 9% management plan against 3% history, graded as seller or bank numbers, and asks for a haircut plan. | yes | 'Plan assumes 9%/yr revenue growth; actual 2023–2025 growth was 3%/yr. Flag: likely overstated' and 'Seller/banker numbers graded as such ... Fail — Standalone value is the sell-side bank's number, used unadjusted'; requests finance rebuild DCF on haircut plan. |
| Names the lease change-of-control clauses (9 of 14 cafés) and founder dependence as deal-breaker checks or conditions. | yes | '9 of 14 leases let the landlord terminate on change of control' and 'Key-person risk: the founder solely holds purchasing and all landlord relationships' listed under 'three things in the notes are deal-breaker-grade' |
| Notes the price exceeds the EUR 30m capital envelope. | yes | 'Capital envelope conflict: the board's EUR 30m 2027 envelope for all projects is already smaller than the EUR 34m price' |
| Challenges 'strategic must-have' and asks whether build, partner or a smaller format pilot reaches the goal. | yes | 'the build/partner alternative deserves at least one page in the IC paper' and trap check: 'Strategic fit not used to excuse weak fundamentals... Fail — CEO's "strategic must-have" framing is the only stated case' |
| Answer is do not proceed at EUR 34m, or proceed only at or below about EUR 25m under named conditions. | yes | 'Answer: do not proceed at EUR 34m... Proceed only if the conditions below are met and the price comes down accordingly.' |
| Recommends a review by someone outside the deal team. | yes | 'Specialists and review: ... someone outside the deal team to sign off before IC, per the deal-momentum trap below.' |
| Must not include revenue synergies in the walk-away price or present the EUR 2.0m value created as valid. | yes | Walk-away price table excludes revenue synergies entirely; EUR 2.0m is repeatedly called 'an artifact' and 'not a EUR 2m gain'. |
| Must not invent café-sector multiples or comparable deal prices. | yes | Illustrative haircut is derived from revenue CAGR compounding (9% vs 3%), not from any invented sector multiple or comparable transaction price. |

## Transcript

## Turn 1

**User:** Our CEO wants to buy Copperleaf for EUR 34m. Here's the draft IC paper. Can you firm up the case so it's ready for the investment committee next week? (Attached in the working directory: cma-02-input.md.)

I pressure-tested the draft and it doesn't hold up as written — I'd flag this to the CEO before it goes to IC, not just polish the slides. Full case is in `case-ma-screening-copperleaf.md`; headline:

**The claimed EUR 2.0m of value creation is an artifact of including EUR 11.0m of revenue synergies that have no owner, are partly uncosted, and have never been piloted.** Standard practice (and the trap this case-type playbook calls out explicitly) is to keep revenue synergies out of the price-supporting case entirely. Strip them out and:

- Walk-away price (standalone + cost synergies only) = **EUR 25.0m** even using the bank's own optimistic standalone number — EUR 9m *below* the EUR 34m ask.
- The standalone number itself looks inflated: the DCF uses a 9%/yr growth plan against 3%/yr actual growth in 2023–2025. A rough illustrative haircut puts standalone value nearer EUR 14–18m, which would put the real walk-away price around **EUR 17–21m** — EUR 13–17m below the ask.

On top of the pricing gap, three things in the notes are deal-breaker-grade and currently unpriced:

1. **9 of 14 leases let the landlord terminate on change of control** — nearly two-thirds of the estate is at risk the moment the deal closes.
2. **Key-person risk**: the founder solely holds purchasing and all landlord relationships, with no retention agreement discussed — meaning the person most likely to leave is also the person holding the relationships that keep those 9 leases alive.
3. **Capital envelope conflict**: the board's EUR 30m 2027 envelope for *all* projects is already smaller than the EUR 34m price, before adding the uncosted coffee-corner refit capex.

My recommendation in the paper: **do not proceed at EUR 34m**; proceed only once the DCF is rebuilt on a haircut plan, landlord consents/founder retention are secured (or priced in), the revenue synergies get a named owner and costed refit plan, and the board explicitly reconciles the price against the capital envelope. The full file has the walk-away price table, trap-check scorecard against the playbook, risks with named owners, and an open-questions list to send to finance/legal/HR before next week.


## Files in work dir after run

- case-ma-screening-copperleaf.md
- cma-02-input.md

## File written by the run: case-ma-screening-copperleaf.md

# M&A screening: Brightwell Bakeries, should we buy Copperleaf Cafés (14 cafés) for EUR 34m

*Fictional companies, people and figures, as given in the draft IC paper.*

**Answer: do not proceed at EUR 34m.** The claimed EUR 2.0m of value creation exists only because EUR 11.0m of unowned, uncosted, unpiloted revenue synergies were put into the price-supporting bridge. Taking those out — which is standard practice precisely because revenue synergies are the least reliable number in any deal model — the walk-away price (standalone value + cost synergies only) is **EUR 25.0m on the bank's own optimistic standalone number, and roughly EUR 17–21m once the standalone DCF is corrected for the growth-assumption gap below**. Against a EUR 34m price, that is a **gap of EUR 9m to EUR 17m**, not a EUR 2m gain. Proceed only if the conditions below are met and the price comes down accordingly.

**Confidence:** medium-high on the arithmetic (it follows directly from the draft paper's own figures); low on the exact haircut-plan standalone value, because the underlying DCF model was not provided — see Open questions.

**Specialists and review:** real-estate/lease counsel on the 9 change-of-control clauses; an independent valuation review of the bank's DCF (the bank is sell-side-conflicted here); HR/legal on a founder retention agreement; someone outside the deal team to sign off before IC, per the deal-momentum trap below.

## Why buy

- Strategic goal stated by the CEO: acquire the café format ("we have wanted for years"). This is a real, nameable gap (format/channel access) — not disputed here.
- Not addressed in the draft paper: why acquisition over building a pilot café format organically, or partnering with an existing operator. Given that the target's own key assets (founder relationships, leases) are this fragile, the build/partner alternative deserves at least one page in the IC paper before the committee is asked to accept acquisition-specific risks (key-person loss, change-of-control lease terminations) that a build route would not carry. **Open question**, not scored here for lack of data.

## Walk-away price for Copperleaf

| Component | Value (EUR m) | Basis |
|---|---|---|
| Standalone value — bank's DCF on management plan | 22.0 | Draft paper. Plan assumes 9%/yr revenue growth; actual 2023–2025 growth was 3%/yr. **Flag: likely overstated — see note below.** |
| Standalone value — illustrative haircut to historical growth | **~14–18 (ASSUMPTION, illustrative only)** | See arithmetic below. Not a substitute for a rebuilt DCF. |
| Net cost synergies | 3.0 | Owner: COO. One-off integration cost EUR 0.6m already deducted. From month 6. **Passes the trap check** (owner, date, one-off cost named). |
| **Walk-away price — optimistic (bank's standalone)** | **25.0** | 22.0 + 3.0 |
| **Walk-away price — haircut case (illustrative)** | **~17–21** | ~14–18 + 3.0 |
| **Asking price** | **34.0** | |
| **Gap to close** | **−9.0 (optimistic) to −13/−17 (haircut)** | Price exceeds walk-away under either case |
| Revenue synergy 1 — Brightwell bread/cakes in Copperleaf cafés | 5.0 — **upside only, not in price** | No owner named; no pilot |
| Revenue synergy 2 — Copperleaf coffee corners in 20 Brightwell stores | 6.0 — **upside only, not in price** | No owner named; store refits not costed; no pilot |

**Note on the standalone value.** A DCF's value is driven by the compounding of the growth assumption through the explicit period and into the terminal value, so a 9%-vs-3% gap is not a rounding issue. Illustratively: over a 5-year explicit forecast, revenue at 9%/yr compounds to roughly 1.54x of today's base, versus roughly 1.16x at 3%/yr — the 3% path reaches only about 75% of the revenue the 9% path reaches by year 5, before even considering the larger gap this opens in the terminal value. This is a rough, revenue-only proxy, not a rebuilt valuation (it ignores margin, capex and discount-rate assumptions, all of which the draft paper doesn't disclose) — hence the wide EUR 14–18m range. **The actual number must come from finance rebuilding the DCF on a plan anchored to the 2023–2025 trend, not from this approximation.**

## Key risks and integration thesis

1. **Change-of-control lease termination (9 of 14 cafés, 64% of the estate).** These clauses put the standalone business at risk independent of the deal — if landlords exercise them on completion, Brightwell may be paying for a 14-site estate that becomes a materially smaller one. *Mitigation:* secure landlord consents or waivers before signing on as many of the 9 as possible; size the residual risk (which sites, what rent step-ups to retain them) and reflect it in the price, not in a footnote. *Owner: legal/real estate, pre-signing.*
2. **Key-person risk compounds the lease risk.** The founder runs purchasing and all landlord relationships, with no retention agreement discussed. Losing the founder at the same moment landlords have a trigger to renegotiate or exit is the single largest risk in this deal, and it is unpriced in the current bridge. *Mitigation:* retention/consultancy agreement with the founder covering a transition period, signed before or at completion; named owner for landlord relationship transfer. *Owner: HR/CEO, pre-signing.*
3. **Revenue synergies have no owner and are partly uncosted.** Per standard practice, these stay outside the price until someone owns the number, the coffee-corner refit capex is costed, and ideally a 2–3 site pilot has run. *Mitigation:* name an owner now (regardless of pricing treatment), cost the refits, and treat any pilot result as the gate before the IC revisits whether to let revenue synergies influence price at all.
4. **Capital envelope conflict.** The board approved a EUR 30m 2027 capital envelope for *all* projects. The EUR 34m price alone already exceeds that envelope, before adding the uncosted coffee-corner refit capex. Either this deal is funded outside that envelope (debt, separate M&A facility) or it consumes more than 100% of 2027's capital capacity for every other project combined. *This needs an explicit board decision, not an implicit assumption, before IC approves the price.* *Owner: CFO.*
5. **Sell-side-conflicted valuation.** The standalone DCF was "prepared with the sell-side bank" — the bank is paid on the deal closing, and the 9%-growth management plan it used sits far above the target's own recent trading. This is the classic anchoring-on-the-asking-price trap. *Mitigation:* independent review of the DCF by Brightwell's own corporate development/finance function, not the sell-side bank.

## Trap checks (M&A screening, run against the draft paper)

| Trap | Pass/fail in the draft | Note |
|---|---|---|
| Revenue synergies shown as upside only, outside the walk-away price | **Fail** | EUR 11.0m of revenue synergies are inside "Total value," producing the claimed EUR 2.0m of value creation |
| Every cost synergy has an owner, a date and its one-off cost | **Pass** | COO, month 6, EUR 0.6m already deducted |
| Walk-away price and deal-breakers agreed before diligence | **Fail / not done** | No walk-away price or deal-breaker list in the draft; this paper supplies a first version |
| Value built from the buyer's own view, not back-solved from the asking price | **Fail** | Standalone DCF uses the sell-side bank's 9% plan against 3% actual history; price (34.0) sits almost exactly at total value (36.0) less a token 2.0m — consistent with solving backwards from the asking price |
| Full field screened, not only targets for sale | **Unknown / not evidenced** | Not addressed in draft; flagged as open question |
| Strategic fit not used to excuse weak fundamentals, fragile customers or key-person risk | **Fail** | CEO's "strategic must-have" framing is the only stated case; founder key-person risk and 9/14 lease risk are noted but not priced or mitigated |
| Integration thesis exists (who runs it, day-one changes, what stays untouched) | **Fail / missing** | No integration owner named beyond the COO for cost synergies; no plan for landlord relationship transfer or revenue-synergy ownership |
| Seller/banker numbers graded as such; valuation passes model red-flag checks | **Fail** | Standalone value is the sell-side bank's number, used unadjusted; growth-assumption gap (9% vs 3%) not reconciled anywhere in the draft |

## What would change the answer

1. If landlord consents are secured (or the 9 at-risk leases are shown to be low-value / easily re-let) **and** a signed founder retention agreement is in place, the key-person and lease risk that currently caps the credible price would shrink — the case could then support paying up toward the EUR 25m optimistic walk-away price, still excluding revenue synergies.
2. If finance rebuilds the DCF on a plan anchored to 2023–2025 trading (not the bank's 9% plan) and the resulting standalone value is at the high end of the EUR 14–18m illustrative range, the walk-away price moves toward EUR 21m; at the low end, toward EUR 17m.
3. If a costed, owned revenue-synergy case is built and a pilot (e.g., 2–3 coffee corners) demonstrates the economics, the IC could rationally decide to let a *discounted, risk-adjusted* share of those synergies count toward price — but not before a pilot, and never at face value.
4. If the board confirms the EUR 34m is funded outside the EUR 30m 2027 capital envelope, the affordability objection (point 4 above) falls away; if not, this deal cannot proceed at any synergy-adjusted price without reopening the capital plan.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | DCF value scales roughly with revenue growth for illustrating the haircut | ~20–35% haircut to standalone value | Rough compounding of 9% vs 3% CAGR over 5 years (revenue only) | The actual rebuilt DCF (with margin, capex, discount-rate detail) shows a smaller or larger gap |
| 2 | "Total value" in the draft paper is additive and the bank's EUR 22.0m, EUR 3.0m, EUR 5.0m and EUR 6.0m figures are each independently sourced as stated | As given in draft | Draft IC paper | Any of the four figures is restated by finance/the bank |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What does the full bank DCF model show (margins, capex, discount rate, terminal growth) on a plan anchored to 2023–2025 growth? | Needed to replace the illustrative EUR 14–18m haircut with a real number | CFO / corporate development, independent of the sell-side bank | Sets the lower bound of the walk-away price precisely |
| Of the 9 leases with change-of-control termination rights, which are commercially important, and will landlords consent or waive pre-signing? | Determines how much of the 14-café estate is actually being bought | Legal / real estate | Could remove or harden the single largest execution risk |
| Will the founder sign a retention/consultancy agreement, and for how long? | Purchasing and landlord relationships currently depend entirely on one person | HR / CEO, in direct negotiation with the founder | A signed agreement de-risks both the lease and purchasing-continuity risk; refusal should itself be a near deal-breaker |
| What would the uncosted coffee-corner store refits across 20 Brightwell stores actually cost, and who owns the revenue-synergy case? | The EUR 6.0m synergy is currently a number with no plan behind it, and the capex competes with the same capital envelope as the deal itself | Store operations / commercial director | Could turn the synergy into real (discounted) upside, or show it net-negative after capex |
| Is the EUR 34m purchase price funded from the EUR 30m 2027 capital envelope for "all projects," or separately? | As drafted, the price alone exceeds the entire 2027 envelope before any refit capex | CFO / board | If inside the same envelope, this deal crowds out every other 2027 project; needs explicit board sign-off either way |
| Was the full field of café-format targets screened, or is Copperleaf the only one considered (a banker's single idea)? | Avoids anchoring on the one target that came with a banker attached | Corporate development | Could surface a better-fitting or cheaper alternative, or confirm Copperleaf is genuinely the best available route |

