# cg-02-healthy-core-illusion on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes Corvina's market share and shows it fell (8.0% to about 7.3%), and states that 4% growth in a 9% market is share loss, not a healthy core. | yes | "wholesale share falls from 8.0% (2023) → 7.3% (2025) → 6.0% (2029)" and "'Healthy core' is a mislabel... flat-to-rising revenue in a market growing faster is share loss, not health" |
| Sizes what holding share would be worth (about EUR 73m in 2029, or about EUR 12 to 13m above the plan's core) and makes the cause of share loss the first question to answer. | NO | No figure resembling EUR 73m (holding 2025 share at 9%/yr) or the EUR 12-13m delta appears anywhere; the lever table only shows a EUR 58-63m range for core, and 'cause of share loss' is listed as the 5th of 6 next steps, not elevated as the first question. |
| Shows the franchise carries almost the whole gap and treats the 0 to 110 cafés ramp as unproven: widens the range, compares with comparable franchise launches or names that comparison as missing, and notes no operator is signed. | yes | "carries almost the whole plan with no comparable-launch evidence and no signed pipeline"; franchise range widened to "EUR 3–14m—wide range because: zero operators signed, no stated royalty rate..."; "no comparable-launch benchmark given" |
| Flags that the 9% market growth comes from a trade association figure quoted second-hand and should be checked at the source. | yes | "Trade association yearbook 2025, as quoted in Corvina's own investor update (single, secondhand source)" and next step "Verify the 9%/yr market-growth figure against a primary source (not a secondhand quote)" |
| Concludes the plan as drafted is not the right plan (or not yet), and gives a reordered answer: fix the core share loss first, franchise as an option or later lever with a proof point. | NO | Concludes "No, not as drafted" and demotes franchise to "option, not 'keep'—needs a signed-pipeline proof point", but never issues a directive to fix core share loss first; the core lever decision is merely "keep, but reframe as momentum" and 'decide core strategy' is ranked 5th of 6 next steps, not |
| Shows profit next to revenue or flags that the plan lacks it, and checks the 8% EBIT floor or names it as unknown. | yes | "No EBIT figure appears anywhere" and Assumption 3: "Group and segment EBIT margin... Not available — treated as unknown"; next step to "test against the 8% floor" |
| Shows the remaining gap openly under its own levers. | yes | "the realistic 2029 total is closer to EUR 65–68m, a remaining gap of EUR 7–10m (9–13% of target)" |
| Must not: accept "our core is healthy" or the EUR 14m franchise figure at face value. | yes | "'Healthy core' as an unqualified label — killed" and franchise de-rated to "EUR 3–14m" / "≈ EUR 7m" base case |
| Must not: invent reasons for the share loss (competitor names, price levels, customer quotes) as facts; it may list them as hypotheses to test. | yes | Options like "pricing, named-competitor share recapture, installed-base upsell" are offered as prospective response levers/open questions, not asserted causes; no specific competitor, price level, or quote is stated as fact. |

## Transcript

## Turn 1

**User:** The Corvina management team has drafted their growth plan. Pressure-test it and give me the answer page: is this the right plan to reach EUR 75m by 2029? (Attached in the working directory: cg-02-input.md.)

I pressure-tested the plan and saved the full answer page to `case-growth-strategy-corvina.md`. Bottom line:

**No — not as drafted.** Two findings kill the "nothing to see here" framing:

1. **"Healthy core" is a mislabel.** Using management's own cited market growth (9%/yr since 2023) against their own core growth (4%/yr), wholesale share falls from 8.0% (2023) → 7.3% (2025) → 6.0% (2029) — a 24% relative share loss. The core isn't growing slower than a flat market; it's losing ground in a market management itself says is booming.

2. **The plan is really one lever, not two.** The core contributes nothing beyond rolling the 2023-25 trend forward — it's the momentum case, not an initiative. 61% of all new revenue to 2029 (EUR 14m of EUR 22.8m) rests on a café-franchise business with **zero signed operators**, an undisclosed per-café economic model (the EUR 127k/café implied average isn't stated anywhere), and a 0→110-unit ramp with no comparable-launch benchmark.

3. **The margin target is never addressed.** The investors set three constraints — revenue, ≥8% EBIT margin, ≤EUR 6m capital — and the plan only engages with the first. No EBIT figure appears anywhere, even though franchise build costs (team, brand, flagship) are likely margin-dilutive before royalty income matures.

4. **Even the revenue math is off by EUR 0.17m**, not the "none" the memo claims — small in isolation, but a sign the plan hasn't been pressure-tested internally.

The full page includes the gap table, lever-by-lever sizing with ranges and evidence grades, a de-rated base case (realistic 2029 total closer to EUR 65-68m), killed claims, risks, next steps, assumptions, open questions, and trap checks against the growth-strategy playbook.


## Files in work dir after run

- case-growth-strategy-corvina.md
- cg-02-input.md

## File written by the run: case-growth-strategy-corvina.md

# Growth strategy: Corvina Coffee Roasters, does the 2026-2029 plan credibly close the gap to EUR 75m revenue at ≥8% EBIT margin within EUR 6m capital?

**Answer:** No, not as drafted. "Healthy core" is a mislabel: on management's own market figure, wholesale share falls from 8.0% (2023) to 6.0% (2029) — a 24% relative share loss — while the core is presented as the safe half of the plan. The other 61% of all new revenue between 2025 and 2029 (EUR 14m of EUR 22.8m) is pinned on a franchise business with zero signed operators, an unstated per-café economic model, and a 0→110-unit ramp with no comparable-launch benchmark. The plan states a revenue total but never once states an EBIT number, against a margin floor that is one of only three constraints the investors actually set. On the plan's own arithmetic there is also a EUR 0.17m revenue gap, not "none." This is not a plan that is EUR 6m and one franchise rollout away from done; it is a revenue table standing in for a growth plan.

**Confidence:** High that the plan as drafted does not responsibly close the gap — the share-loss and margin-silence findings follow directly from management's own numbers, not from new data. Medium on the specific replacement range below — core and franchise ranges rest on thin, partly assumed inputs that only management can firm up (see Open questions).

## The gap

| EUR m | 2025 | 2029 (plan) | 2029 (target) |
|---|---|---|---|
| Core wholesale | 52.0 | 60.8 | — |
| Café franchise | 0 | 14.0 | — |
| **Total** | **52.0** | **74.8** | **75.0** |
| Constraints | capital ≤ EUR 6m, EBIT margin ≥ 8%, ruled out: not stated | | |

Two things the plan summary hides:
- **The core is not a lever, it's the momentum case.** 60.8m is simply 52m rolled forward at the 2023-2025 trend (4.08% CAGR, management rounds to 4%). No initiative is proposed to change that trajectory — the entire "plan" consists of one new lever (franchise) layered on top of a do-nothing core.
- **The arithmetic itself is EUR 0.17m short of EUR 75.0m**, not "none" as stated — immaterial in size, but telling: a plan that rounds its own shortfall to zero is a plan not yet pressure-tested internally.

## Core wholesale: market-share decomposition (the "healthy core" claim)

| Year | Market (EUR m, trade-assoc. yearbook, 9%/yr since 2023) | Core wholesale (EUR m) | Core share of market |
|---|---|---|---|
| 2023 | 600.0 | 48.0 | 8.00% |
| 2025 | 712.9 | 52.0 | 7.29% |
| 2029 (plan) | 1,006.3 | 60.8 | 6.05% |

Management's own cited market growth (9%/yr) against its own core growth (4%/yr) produces a **24% relative share loss from 2023 to 2029** — the core goes from a top wholesale player gaining ground to one shrinking relative to the category it operates in. "Solid growth in a competitive market" is true only in absolute EUR; relative to the market management itself quotes, the core is in retreat. This is the market-growth-vs-share-growth trap by the book: flat-to-rising revenue in a market growing faster is share loss, not health, and the two call for opposite responses (defend share vs. harvest a maturing core).

This does not by itself prove the 4%/yr plan is wrong — a deliberate decision to cede low-value volume while protecting margin could be a reasonable strategy. But the memo frames it as unqualified good news with no such rationale, and proposes zero levers (pricing, named-competitor share recapture, installed-base upsell) to arrest the slide. That is the gap to close with management, not a reason to kill the core line outright.

## Levers

| Lever | Revenue base case 2029 | Range | EBIT effect (EUR) | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Core wholesale (pure momentum, no new initiative) | EUR 60.8m | EUR 58–63m depending on whether share loss accelerates or the core defends price/share | Not stated by management | Unstated (residual ≤ EUR 1.5m after franchise) | Immediate (trend continuation) | medium — based on a real 2-year trend, but projected 4 years out and conflated with "health" | keep, but reframe as momentum, not a growth lever |
| Café franchise (0→25→60→110 cafés, royalties + coffee supply) | EUR 14.0m (management) | EUR 3–14m — wide range because: zero operators signed, no stated royalty rate or per-café revenue, no ramp-curve comparable | Not stated by management | EUR 4.5m (team, brand, flagship) | 2027 onward, but pipeline-dependent | weak — revenue/café (EUR 127k blended, implied, not disclosed) and the ramp schedule are unvalidated assumptions, not evidence | option, not "keep" — needs a signed-pipeline proof point before counting in the base case |

**Sum of kept levers (base case):** EUR 74.8m as management states it, but on a conservative base case that de-rates the franchise lever for zero signed pipeline (say 50% of plan, ≈ EUR 7m) the realistic 2029 total is closer to **EUR 65–68m**, a **remaining gap of EUR 7–10m (9–13% of target)** — before even testing the 8% EBIT floor, which the plan does not address at all.

## Killed options and why

- **"Remaining gap to target: none" as a resting conclusion** — killed by the plan's own arithmetic (74.8 vs 75.0 = EUR 0.17m gap) and by the absence of any EBIT view against the 8% floor, which is a harder constraint than the EUR 0.2m revenue rounding.
- **"Healthy core" as an unqualified label** — killed by the market-share decomposition above; reshaped to "a core growing in line with its recent trend but losing share to a faster-growing market, with no stated response."

## Risks and what would change the answer

1. If **zero franchise agreements are signed by end-2026**, the 25-café opening target for 2027 is not achievable on any normal franchise sales-and-build cycle (site selection, franchisee onboarding, training, fit-out). The EUR 14m lever should be treated as largely a 2028-2029 story at best, not 2027-2029, which would cut several EUR million from the 2029 number and make the EUR 75m target very unlikely without a replacement lever.
2. If **per-café economics are materially below the implied EUR 127k blended average** (plausible if royalty rates are a typical 5-8% of store sales and store sales are modest in a competitive café market), the franchise lever could land nearer EUR 5-8m even at the planned unit count, independent of the signing-pace risk above.
3. If **franchise build costs (team, brand, flagship) and new-store opening costs are margin-dilutive in 2027-2028 before royalty income matures**, group EBIT margin could fall below the 8% floor even if revenue lands close to EUR 75m — a target miss the current plan cannot be checked against because no EBIT figure is given.
4. If the **quoted 9%/yr market growth does not hold to 2029** (it is a single, secondhand-cited figure — a trade yearbook "as quoted in our investor update"), the precise share-loss percentage changes, but the direction (core growing slower than its own market) does not reverse unless market growth falls below roughly 4%/yr, which would need separate verification.

## Next steps

| What | Who | By when |
|---|---|---|
| Produce segment-level EBIT (core and franchise) for 2026-2029 and test against the 8% floor | CFO | Before plan is presented to investors |
| Report signed franchise LOIs/agreements to date; set a kill/rebase gate (e.g., if fewer than ~15 agreements are signed by Q3 2026, rebase the 2027 opening number) | Franchise/BD lead | Immediately, then quarterly |
| Share per-café unit economics: royalty rate, average café revenue, coffee-supply margin, store-level payback period, benchmarked against at least one comparable café-franchise launch | Franchise finance lead | Before the 2027 budget is locked |
| Verify the 9%/yr market-growth figure against a primary source (not a secondhand quote) and state whether it is expected to hold to 2029 | Market research / investor relations | Before next investor update |
| Decide and state the core strategy explicitly: defend share (pricing, named-competitor response, installed-base upsell) or deliberately cede volume for margin — and size whichever is chosen | Commercial lead | Within the current planning cycle |
| Confirm the core's capital needs (roasting capacity, logistics, sales capacity to reach EUR 60.8m) fit inside the EUR 1.5m residual after the EUR 4.5m franchise spend | COO | Before capital is committed |

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Wholesale market keeps growing 9%/yr through 2029 | 9%/yr, 2023-2029 | Trade association yearbook 2025, as quoted in Corvina's own investor update (single, secondhand source) | A primary-source check shows materially different growth (the share-loss direction survives down to ~4%/yr; below that, the "share loss" framing weakens, though the core still wouldn't be growing faster than its market) |
| 2 | Blended 2029 franchise revenue per café (royalty + coffee supply) | ≈ EUR 127k/café, implied from EUR 14m / 110 cafés | Not disclosed by management — derived arithmetically, not a given unit economic | Management discloses an actual royalty rate, average store revenue and coffee-supply margin that differ materially from this implied figure |
| 3 | Group and segment EBIT margin, 2025-2029 | Not available — treated as unknown | Not provided in the brief | Management discloses actual/projected EBIT; this is the single assumption most likely to overturn the "gap: none" conclusion given the 8% floor is a hard investor constraint |
| 4 | Core wholesale needs no material capex/opex beyond the EUR 1.5m residual (EUR 6m cap minus EUR 4.5m franchise spend) to grow from EUR 52m to EUR 60.8m | EUR 1.5m sufficient | Not stated by management; residual arithmetic only | Core requires roasting capacity, logistics or sales headcount investment that exceeds EUR 1.5m, breaching the EUR 6m cap |
| 5 | Franchise ramp (0→25→60→110 cafés, 2026-2029) is achievable starting from zero signed operators | As stated in plan | Management's rollout schedule; no comparable-launch benchmark given | A comparable café-franchise launch (local or international) shows materially slower signing-to-opening cycles, which would push most of the EUR 14m past 2029 |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is projected group and segment EBIT margin for 2026-2029? | The 8% EBIT floor is a hard investor constraint the plan never addresses; revenue hitting EUR 75m could still fail the mandate on margin | CFO | Could independently kill the plan even if both revenue levers land as planned |
| How many franchise agreements (not LOIs) are signed today, and what is the realistic signing-to-opening lead time? | Tests whether 25 openings in 2027 is a real pipeline or a placeholder number | Franchise/BD lead | Directly resizes the EUR 14m lever and its timing |
| What royalty rate, average café revenue and coffee-supply margin underlie the EUR 14m figure? | No unit economics are given; EUR 127k/café is a derived number, not a stated assumption | Franchise finance lead | Could move the franchise base case anywhere from ~EUR 5m to ~EUR 14m |
| Is the 9%/yr market-growth figure confirmed by a source other than the trade association yearbook as quoted in the investor update? | Single secondhand source for a number that drives the entire share-loss finding | Market research / investor relations | Changes the magnitude, not the direction, of the share-loss conclusion down to roughly 4%/yr |
| Does the core wholesale business need investment (capacity, logistics, sales) to sustain even its 4%/yr trend to 2029, and does that fit the EUR 1.5m residual capital? | Investment cap (EUR 6m) is a hard constraint; franchise alone takes EUR 4.5m of it | COO | Could breach the capital constraint even if both revenue levers are otherwise sound |
| Is a deliberate "defend the core" response (pricing, named-competitor share recapture, installed-base upsell) in scope, or is 4%/yr momentum management's considered choice? | The plan proposes zero levers for the core despite clear relative share loss | Commercial lead / board | Could add a third lever and reduce reliance on the unproven franchise bet |

## Trap checks

- [x] **Market growth confused with share growth** — found and fixed: the memo calls 4%/yr core growth "solid" without comparing it to the 9%/yr market it itself quotes; share falls from 8.0% to 6.0% (2023-2029), a 24% relative loss.
- [ ] **Adding up hope** — open/failed: the franchise lever is carried at management's full-pipeline figure (EUR 14m) despite zero signed operators; a base case should de-rate this, which the original plan does not do, and the stated "gap: none" does not survive de-rating.
- [x] **Skipping the core** — not applicable in the usual direction (core is sized first), but inverted: the core is sized and then given no lever at all despite a clearly documented, worsening share problem — the cheapest growth (defend/recapture share, installed-base upsell) is the one branch the plan never examines.
- [ ] **Inside view on new moves** — open/failed: the 0→110-café ramp from zero signed operators has no comparable-launch benchmark anywhere in the plan; this is exactly the trap of forecasting a new business from its own internal logic.
- [x] **Market growth vs share growth separated** — fixed above (8.0% → 7.29% → 6.05%).
- [ ] **Ignoring the constraints** — open: the EBIT margin floor (8%) is never tested against the plan; the capital cap (EUR 6m) is tested only for the franchise lever (EUR 4.5m), leaving the core's capital needs unstated and unverified against the EUR 1.5m residual.
- [x] **Too many initiatives** — not the issue here; the opposite problem — effectively one real lever (franchise, 61% of all new revenue) carries almost the whole plan with no comparable-launch evidence and no signed pipeline, which is a concentration-of-risk problem rather than a sprawl problem.
- [ ] **Revenue without margin** — open/failed, the most material gap: no EBIT or margin figure appears anywhere in the plan despite ≥8% EBIT margin being one of only three constraints the investors set.

