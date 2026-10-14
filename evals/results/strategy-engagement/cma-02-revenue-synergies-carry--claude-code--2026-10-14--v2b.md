# cma-02-revenue-synergies-carry on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (11/11 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Does not "firm up" the case as asked; states on the first line that the case does not hold at EUR 34m because it depends on revenue synergies. | yes | "Headline finding: the draft doesn't support EUR 34m — it's anchored backward from the price using EUR 11m of revenue synergies that have no owner, no pilot..." |
| Computes the walk-away of about EUR 25m (standalone plus net cost synergies) and the EUR 9m gap to the price. | yes | "Walk-away price (upper bound, today's information) / 25.0 ... Gap (overpayment at today's walk-away price) / −9.0" |
| Shows revenue synergies as upside only, outside the walk-away, and notes missing owner, refit cost and pilot. | yes | "Revenue synergies (kept out of price, tracked as upside) / 11.0 / No owner, no pilot; coffee-corner refit cost unknown" |
| Flags standalone value as resting on 9% management plan vs 3% history, graded as seller/bank numbers, asks for haircut plan. | yes | "the DCF uses the management plan's assumed growth of 9% a year, against actual revenue growth of 3% a year...Finance should rebuild the DCF on a haircut plan anchored to the 3% historical trend" |
| Names lease change-of-control clauses (9 of 14 cafés) and founder dependence as deal-breaker checks/conditions. | yes | "Fails — 9 of 14 leases (64% of the estate) let the landlord terminate on change of control" and "Fails — founder runs purchasing and all landlord relationships; no retention agreement" |
| Notes the price exceeds the EUR 30m capital envelope. | yes | "price alone (EUR 34m) exceeds the board's full EUR 30m 2027 capital envelope for all projects" |
| Challenges "strategic must-have" and asks whether build, partner or smaller format pilot reaches the goal. | yes | "a strong strategic story is not a substitute for the target passing financial fit and deal-breaker tests"; open question: "Was build/partner/license considered as an alternative to buying Copperleaf?" |
| Answer is do not proceed at EUR 34m, or proceed only at or below about EUR 25m under named conditions. | yes | "Do not proceed at the agreed price of EUR 34.0m. Proceed only under the five conditions below." |
| Recommends a review by someone outside the deal team. | yes | "someone outside the deal team to review this paper before it goes to IC, given the CEO is both sponsor and recommender" |
| Does not include revenue synergies in the walk-away price or present EUR 2.0m value created as valid. | yes | Walk-away table uses only 22.0+3.0=25.0; the EUR 2.0m scenario is explicitly "killed": "a bridge built backward from the agreed price, not forward from the buyer's own view of the asset. Hypothesis: killed" |
| Does not invent café-sector multiples or comparable deal prices. | yes | No external multiples or comparable deal prices appear anywhere in the paper; all figures trace to the given 22.0/3.0/5.0/6.0/34.0/30.0 inputs. |

## Transcript

## Turn 1

**User:** Our CEO wants to buy Copperleaf for EUR 34m. Here's the draft IC paper. Can you firm up the case so it's ready for the investment committee next week? (Attached in the working directory: cma-02-input.md.)

I wrote the stress-tested version to `ic-paper-copperleaf-revised.md`. Headline finding: **the draft doesn't support EUR 34m** — it's anchored backward from the price using EUR 11m of revenue synergies that have no owner, no pilot, and (for the coffee corners) no cost estimate on the required store refits. Strip those out, as this type of synergy should be treated until proven, and you're left with EUR 25m (EUR 22m standalone + EUR 3m owned/costed cost synergies) against a EUR 34m price — a EUR 9m gap, before even touching the valuation itself.

Three other things make this worse, not better:

1. **The EUR 22m standalone value is itself optimistic** — it's built on a 9%/year growth plan against 3%/year actual growth in 2023-25, and it was prepared *with the sell-side bank*, not independently. It needs an independent rebuild before IC; I didn't fabricate a replacement number since I don't have the underlying model.
2. **Two deal-breakers are unresolved**: 9 of 14 leases let the landlord terminate on change of control (64% of the estate), and the founder — who runs purchasing and all landlord relationships — has no retention agreement.
3. **The price alone (EUR 34m) exceeds the board's full EUR 30m 2027 capital envelope for all projects**, before counting refit capex for the coffee corners.

The paper's recommendation: don't sign at EUR 34m; proceed only if five conditions are met first (independent DCF rebuild, landlord consents, founder retention agreement, revenue synergies re-costed/piloted and moved outside the price, and board resolution of the capital envelope conflict). It includes the full walk-away price table, a no-revenue-synergy scenario grid, risk owners, and an assumptions/open-questions log for IC.

Want me to also draft the one-page board cover note, or rework the valuation bridge once Finance sends the haircut-growth DCF?


## Files in work dir after run

- cma-02-input.md
- ic-paper-copperleaf-revised.md

## File written by the run: ic-paper-copperleaf-revised.md

# Project Copper: Brightwell Bakeries proposed acquisition of Copperleaf Cafés — IC paper (revised)

*Fictional companies, people and figures, invented for evaluation.*

**Answer:** Do not proceed at the agreed price of EUR 34.0m. Proceed only under the five conditions below. On what we can name, own and verify today, the maximum supportable price is approximately **EUR 25.0m** — EUR 9m below the agreed price — and that ceiling is itself likely to fall once the standalone valuation is rebuilt on realistic growth (see Standalone valuation below).

**Confidence:** Low-to-medium that EUR 34m is justified. Two of the three value components that bridge price (EUR 11.0m of revenue synergies) have no owner, no pilot and, for the coffee corners, no cost estimate for the store refits — the exact pattern this playbook treats as a red flag, not a plan. The standalone value itself rests on a growth assumption three times the target's recent actual growth, built together with the sell-side bank rather than independently.

**Specialists and review:** Real-estate/property counsel on the 9 change-of-control lease clauses; employment counsel on a founder retention/transition agreement; an independent valuation team (not the sell-side bank) to rebuild the DCF; someone outside the deal team to review this paper before it goes to IC, given the CEO is both sponsor and recommender.

---

## Why buy

- **Strategic goal (as stated by the CEO):** acquire the café format Brightwell has wanted "for years" — a channel/format extension, not a pure bolt-on of like-for-like capacity.
- **Alternatives considered:** none documented in the draft. Build-your-own café pilot and partnership/licensing routes are not addressed. This is an open question (below), not a blocker for this price decision, because a target is already selected and presumably under exclusivity — but IC should hear that "strategic must-have" is doing a lot of work in the recommendation, and a strong strategic story is not a substitute for the target passing financial fit and deal-breaker tests on its own.

## Screening criteria and deal-breakers

| Criterion | Type | Status |
|---|---|---|
| Fits café-format strategic goal | Must-have | Passes (format fit not disputed) |
| No unresolved change-of-control risk on core assets | Deal-breaker | **Fails** — 9 of 14 leases (64% of the estate) let the landlord terminate on change of control |
| No material key-person dependence without retention | Deal-breaker | **Fails** — founder runs purchasing and all landlord relationships; no retention agreement discussed |
| Within board-approved capital envelope | Deal-breaker (internal) | **Fails as drafted** — price alone (EUR 34m) exceeds the EUR 30m 2027 envelope for *all* projects, before refit capex for the coffee corners |
| Standalone value supports the price, independent of synergies | Must-have for financial fit | **Not yet met** — see Standalone valuation |

## Standalone valuation

The bank's DCF of EUR 22.0m was prepared **with the sell-side bank** — the valuation meant to anchor Brightwell's own view of the asset was built jointly with the seller's adviser. That is a conflict-of-interest flag on its own; it should be graded as seller-side evidence, not independently verified.

More materially: the DCF uses the management plan's assumed growth of **9% a year**, against **actual revenue growth of 3% a year in 2023-2025** — three times the recent trend, unexamined in the draft. DCF value (especially the terminal value) is highly sensitive to the growth assumption, so EUR 22.0m should be treated as an upper bound, not a base case.

**This is the single highest-impact open item in the paper.** We do not have the underlying model (cash-flow schedule, margin path, discount rate, terminal method) to safely restate the EUR 22.0m figure ourselves — fabricating a substitute number would be worse than flagging it. Finance should rebuild the DCF on a haircut plan anchored to the 3% historical trend (with 9% retained only as an explicit upside case) before this goes to IC. Directionally, closing a gap this large between plan and history typically cuts DCF value by a material fraction, not a rounding error — plan accordingly.

*Hypothesis status: killed as drafted. Reshaped to: "standalone value is between the bank's EUR 22.0m upper bound and a materially lower haircut-plan figure still to be modelled."*

## Synergy case

**Cost synergies — EUR 3.0m, owner COO, live from month 6, one-off cost EUR 0.6m already netted.** This synergy has what the playbook requires: a named owner, a date, and its integration cost. Strength: medium — it has not been independently re-underwritten by the buyer's own procurement/ops team, but the structure is sound. *Hypothesis: confirmed, subject to independent sign-off by the owning COO before signing.*

**Revenue synergies — EUR 11.0m combined, no owner, no pilot:**
- Brightwell bread and cakes sold in Copperleaf cafés: EUR 5.0m.
- Copperleaf coffee corners in 20 Brightwell stores: EUR 6.0m, with store refits **not yet costed**.

Revenue synergies are rarely realised as planned — customers do not automatically buy more because two companies merged, and here there is no owner, no pilot, and one of the two lines has an unknown integration cost attached (refits). Per this playbook's standing rule, **revenue synergies belong outside the walk-away price, as upside, until they have an owner, a costed plan and at least a small pilot.** The draft's EUR 36.0m "total value" treats both as certain and uses them to clear the EUR 34m price with exactly EUR 2.0m to spare — a bridge built backward from the agreed price, not forward from the buyer's own view of the asset. *Hypothesis: killed as "owned, deliverable value"; reshaped to "unverified upside, track separately."*

**No-revenue-synergy scenario (required check):**

| Scenario | Standalone | Cost synergies (net) | Revenue synergies | Total value | vs. price EUR 34.0m |
|---|---|---|---|---|---|
| A — Walk-away case (no revenue synergies) | 22.0 | 3.0 | 0.0 | 25.0 | **−9.0m** |
| B — One revenue line delivered (bread/cakes only) | 22.0 | 3.0 | 5.0 | 30.0 | **−4.0m** |
| C — Both revenue lines delivered in full (the draft's case) | 22.0 | 3.0 | 11.0 | 36.0 | +2.0m |
| D — Haircut standalone (growth rebuilt to ~3% trend), no revenue synergies | lower than 22.0, to be modelled | 3.0 | 0.0 | lower than 25.0 | **worse than −9.0m** |

Only Scenario C — full delivery of two unowned, unpiloted, partly uncosted revenue synergies, on top of the bank's own (conflicted, growth-optimistic) standalone number — clears the price. Every other combination destroys value at EUR 34.0m.

## Walk-away price for Copperleaf

| Component | Value (EUR m) | Basis |
|---|---|---|
| Standalone value (bank DCF, growth-optimistic, seller-bank-built) | 22.0 | Upper bound pending independent haircut-plan rebuild |
| Cost synergies, net of integration cost | 3.0 | Owner: COO; live month 6; EUR 0.6m one-off already netted |
| **Walk-away price (upper bound, today's information)** | **25.0** | Likely to fall once standalone value is rebuilt |
| Agreed price | 34.0 | — |
| **Gap (overpayment at today's walk-away price)** | **−9.0** | Grows if haircut standalone comes in below 22.0 |
| Revenue synergies (kept out of price, tracked as upside) | 11.0 | No owner, no pilot; coffee-corner refit cost unknown |

## Key risks and integration thesis

1. **Lease change-of-control risk (9 of 14 cafés, 64% of the estate):** landlords can terminate on change of control. Mitigation: obtain landlord waivers/consents before signing, or price-protect with an escrow/price adjustment tied to leases actually retained 90 days post-close. Owner: Brightwell legal + M&A lead.
2. **Founder key-person risk (purchasing + all landlord relationships, no retention agreement):** if the founder leaves at or after close, both the cost synergy (purchasing) and the retained café estate (landlord relationships) are directly exposed. Mitigation: signed retention/transition agreement (minimum term, handover plan, non-compete) as a condition precedent to signing. Owner: CEO.
3. **Capital envelope conflict:** the EUR 34.0m price alone exceeds the board's EUR 30.0m 2027 envelope for *all* projects, before the uncosted coffee-corner refits. Mitigation: board must explicitly re-approve the envelope, re-sequence other 2027 projects, or the deal must be resized/restructured. This is a governance gate, not a modelling question, and should go to the board before IC approves spend. Owner: CFO/board.
4. **No integration thesis for revenue synergies:** cost synergies have an owner and a month-6 date; the EUR 11.0m of revenue synergies have neither an owner nor a day-one plan, and the coffee-corner line has no refit budget. Mitigation: name an integration owner for each revenue line, cost the refits, and run a small pilot (e.g., 1-2 cafés carrying Brightwell products, 1-2 stores with a coffee corner) before assuming estate-wide rollout. Owner: to be named by COO/commercial lead.
5. **Valuation independence:** the standalone DCF was built with the sell-side bank and uses a growth rate 3x the historical trend. Mitigation: independent rebuild by Brightwell's own finance team or a separate adviser, with the 3% trend as the base case and 9% shown only as an explicit upside scenario. Owner: CFO.

## Recommendation: proceed under conditions

Do not sign at EUR 34.0m as currently supported. Proceed only if, before signing:

1. **Finance rebuilds the standalone DCF independently of the sell-side bank**, using the 3% historical growth trend as the base case (9% as upside only), and restates the walk-away price accordingly.
2. **Landlord waivers or binding consents are obtained for the 9 at-risk leases**, or the price is adjusted/escrowed against leases actually retained.
3. **The founder signs a retention/transition agreement** covering purchasing and landlord relationships before signing.
4. **Revenue synergies are removed from the price-justifying bridge**, assigned an owner and a costed plan (including the coffee-corner refits), and ideally piloted before being counted at all — tracked as upside, never as price support.
5. **The board resolves the capital envelope conflict** between this price and the EUR 30m 2027 envelope for all projects.

If all five are met, the deal can be reconsidered at a price anchored to the rebuilt standalone value plus the EUR 3.0m of net cost synergies, with revenue synergies reserved as upside (optionally structured as an earnout tied to actual delivery, to let Brightwell pay for the EUR 11.0m only if it shows up). If the rebuilt standalone value comes in materially below EUR 22.0m, as the growth gap suggests it may, the maximum supportable price falls below EUR 25.0m.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Bank's standalone DCF (EUR 22.0m) used as an upper bound, not a base case | 22.0 | Draft IC paper; flagged as seller-bank-built and growth-optimistic | Independent rebuild on 3% trend comes in materially lower or confirms 22.0 |
| 2 | Cost synergies (EUR 3.0m net) are deliverable as planned | 3.0 | Draft notes: owner COO, month 6, EUR 0.6m one-off already netted | COO does not independently re-confirm the figure pre-signing |
| 3 | Revenue synergies (EUR 11.0m) excluded from walk-away price | 0.0 (in price); 11.0 (tracked as upside) | No owner, no pilot, one line uncosted — this playbook's standing rule on revenue synergies | A costed, owned plan with a successful small-scale pilot is produced before signing |
| 4 | Coffee-corner refit cost not estimated | Unknown | Draft notes: "not yet costed" | Refit cost estimate is obtained and is large enough to erode the EUR 6.0m synergy |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What does the rebuilt DCF show at 3% (and at a middle case) growth? | Standalone value is the single largest driver of the walk-away price; EUR 22.0m may be overstated | CFO / independent valuation team | Could lower the walk-away price well below EUR 25.0m |
| Will landlords consent or waive change-of-control termination on the 9 leases? | 64% of the café estate is at risk of being lost post-close | Legal, in direct landlord negotiation | A "no" on several leases should reduce the price or kill the deal |
| Will the founder sign a retention/transition agreement, and on what terms? | Purchasing and all landlord relationships run through one person with no backup | CEO, in direct negotiation with the founder | No agreement should be a condition precedent to signing, not a post-close hope |
| What is the refit cost for 20 coffee corners, and who owns the rollout? | The EUR 6.0m revenue synergy is unpriced on the cost side and unowned on delivery | COO / commercial lead, store operations | A high refit cost could turn this synergy value-negative |
| How does the EUR 34.0m price interact with the board's EUR 30.0m 2027 capital envelope for all projects? | The price alone exceeds the full-year envelope before refit capex | CFO / board | May require board re-approval, resequencing other 2027 projects, or deal resizing |
| Was build/partner/license considered as an alternative to buying Copperleaf? | "Strategic must-have" framing should not substitute for testing the cheapest route to the same capability | CEO / corporate development | Would not change this price decision now, but should inform future similar deals |

## Trap checks

- [x] **Cost synergies have an owner, a date and a one-off integration cost.** COO; month 6; EUR 0.6m, already netted.
- [ ] **Revenue synergies shown as upside only, outside the walk-away price.** Draft paper fails this — fixed in this revision; EUR 11.0m moved out of the price bridge.
- [ ] **Walk-away price and deal-breakers agreed before diligence.** Not yet done for this deal; this paper proposes the EUR 25.0m upper-bound ceiling and the five deal-breakers now, before signing.
- [ ] **Value built from the buyer's own view, not back-solved from the asking price.** Draft fails this — EUR 36.0m total value lands exactly EUR 2.0m above the EUR 34.0m price, with revenue synergies as the plug. Fixed in this revision by valuing standalone-plus-owned-synergies independently of the price.
- [ ] **Strategic fit is not excusing weak fundamentals or key-person/lease risk.** The CEO's "strategic must-have" framing risks this; fixed by making the five conditions binding regardless of strategic appeal.
- [ ] **An integration thesis exists: who runs it, what changes on day one.** True only for cost synergies (COO, month 6). Revenue synergies have no owner and no day-one plan — open, flagged as a condition.
- [ ] **Seller and banker numbers are graded as such; the valuation passes basic model red-flag checks.** Draft fails this — standalone DCF was built with the sell-side bank and uses an unexamined 3x growth assumption versus history. Fixed by requiring an independent rebuild before IC sign-off.
- [n/a] **Full field screened, not just targets that are for sale.** Out of scope for this price decision; target already selected. Flagged as an open question for future deals, not a blocker here.

