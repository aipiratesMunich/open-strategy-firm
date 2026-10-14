# cg-02-healthy-core-illusion on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (9/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes Corvina's market share and shows it fell (8.0% to about 7.3%), and states that 4% growth in a 9% market is share loss, not a healthy core. | yes | "Share: 8.00% → 7.29%"... "This is a share-losing core, not a healthy one." |
| Sizes what holding share would be worth (about EUR 73m in 2029, or about EUR 12 to 13m above the plan's core) and makes the cause of share loss the first question to answer. | yes | "holding share flat gets core to ~EUR 73.4m by 2029"; answer lead: "redirect most of the effort toward diagnosing and arresting core share loss (worth up to ~EUR 12.6m by 2029...) ... de-risk the franchise ... and produce the EBIT bridge" — diagnosis listed first. |
| Shows the franchise carries almost the whole gap and treats the 0 to 110 cafés ramp as unproven: widens the range, compares with comparable franchise launches or names that comparison as missing, and notes no operator is signed. | yes | "franchise lever is sized at EUR 14.0m — within EUR 0.2m of exactly plugging this gap"; "zero signed operators and no comparable cited"; Range column shows 7-14m. |
| Flags that the 9% market growth comes from a trade association figure quoted second-hand and should be checked at the source. | yes | "Trade association yearbook 2025, as quoted in the company's own investor update — single source, interested party, not independently triangulated"; open question asks if it's "verifiable outside the trade association's own yearbook". |
| Concludes the plan as drafted is not the right plan (or not yet), and gives a reordered answer: fix the core share loss first, franchise as an option or later lever with a proof point. | yes | "Answer: No. Treat this as not yet a plan..."; Decision column: core "Add — highest-value, lowest-risk lever on the table", franchise "Option — stage it, don't bet the plan on it". |
| Shows profit next to revenue or flags that the plan lacks it, and checks the 8% EBIT floor or names it as unknown. | yes | "No EBIT figures anywhere in the plan"; "Cannot be evaluated — critical data gap"; open question on EBIT margin "Could kill the plan independently of revenue". |
| Shows the remaining gap openly under its own levers. | yes | Stress test table: "Management base case ... 74.8 ... -0.2m (management's own table does not actually reach 75m)". |
| Must not accept "our core is healthy" or the EUR 14m franchise figure at face value. | yes | "'Our core is healthy' / 'solid growth' framing: killed by management's own numbers"; franchise evidence grade "Weak", "ramp is asserted, not evidenced". |
| Must not invent reasons for the share loss (competitor names, price levels, customer quotes) as facts; may list them as hypotheses to test. | yes | Open question phrased as a question, not an assertion: "Why is the core losing share — pricing, distribution coverage, product range, a specific competitor?" with no specific name/figure asserted as fact. |

## Transcript

## Turn 1

**User:** The Corvina management team has drafted their growth plan. Pressure-test it and give me the answer page: is this the right plan to reach EUR 75m by 2029? (Attached in the working directory: cg-02-input.md.)

I pressure-tested the plan against management's own numbers. Short version: **no, this is not a plan that reliably reaches EUR 75m** — the full workings are saved to `case-growth-strategy-corvina.md`; the answer page is below.

---

# Growth strategy: Corvina Coffee Roasters — does the 2026-2029 plan reach EUR 75m by 2029?

**Answer:** No. Treat this as not yet a plan: redirect most of the effort toward diagnosing and arresting core share loss (worth up to ~EUR 12.6m by 2029 at zero incremental capital — bigger than the whole franchise bet), de-risk the franchise to a staged pilot before committing EUR 4.5m of a EUR 6m budget to an unsigned concept, and produce the EBIT bridge the investors actually asked for before claiming the plan "closes the gap."

**Confidence:** High on the diagnosis (the share-loss and margin-silence findings come straight from management's own figures), medium on the fix (lever sizes for "defend the core" and "right-size the franchise" are directionally solid but not yet built from root-cause or pipeline data).

**Specialists and review:** None legal/regulatory at this stage; a franchise-law/contracts review is needed before any franchise agreements are signed, and this should go back to the investors with the EBIT question before being presented as final.

## The gap

| EUR m | 2025 | 2029 |
|---|---|---|
| Revenue, momentum case (core only) | 52.0 | 60.8 |
| Revenue, target | 52.0 | 75.0 |
| Gap | — | 14.2 |
| Constraints | capital ≤6.0m, margin floor ≥8% EBIT, ruled out: n/a (not stated) |

## Levers

| Lever | Revenue base case 2029 | Range | EBIT effect | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Core, momentum (4%/yr) | 60.8m | — | Not stated anywhere in the plan | 0 (none disclosed) | Ongoing | Medium | Keep, but mislabelled "healthy" |
| **Core, defend the share** (hold 7.3% share as market grows 9%/yr — not currently in management's plan) | **73.4m** | 61-73m | Not sized — needs diagnosis | Unknown, likely well under EUR 1.5m headroom | 1-2 years to show effect | Hypothesis, untested | **Add — highest-value, lowest-risk lever on the table** |
| Café franchise | 14.0m | 7-14m | Not stated anywhere in the plan | 4.5m | 2027-2029 | **Weak** (zero signed operators, no comparable cited) | Option — stage it, don't bet the plan on it |

**Sum of kept levers (base case, as management presents it):** 74.8m; **remaining gap:** 0.2m even in management's own best case — not "none." **How we close or accept it:** the plan as drafted does not show how; it simply stacks two single-point best-case numbers.

## Killed options and why

- "Our core is healthy" / "solid growth" framing: killed by management's own numbers. Core share of the wholesale market fell from **8.00% (2023) to 7.29% (2025)** against a market growing 9%/yr while the core grew only 4%/yr; projected forward, share keeps falling to **6.05% by 2029** under the stated plan. This is a share-losing core, not a healthy one.
- "Remaining gap: none": killed. Management's own table sums to EUR 74.8m against a EUR 75m target (a EUR 0.2m shortfall even before any risk is applied), and the franchise figure (EUR 14.0m) sits within EUR 0.2m of exactly the momentum gap (EUR 14.2m) — consistent with a number sized to plug the gap rather than built up from signed units or per-café economics.

## Risks and what would change the answer

1. If the franchise delivers only 50% of plan (plausible with zero operators signed today and no comparable rollout cited), total revenue is ~EUR 67.8m — a 9.6% miss, before any margin effect from ramp losses on the franchise team and flagship.
2. If core share loss is diagnosed and merely arrested (not reversed), core alone reaches ~EUR 73.4m — nearly the full target — at zero incremental capital, which would flip the entire strategy from "build a new franchise" to "fix the core and treat franchise as upside."
3. The investors' 8% EBIT margin floor is not addressed anywhere in the plan; since new-unit franchise rollouts typically run at a loss during ramp, this constraint — not the revenue target — may be the one that actually fails first. This alone should stop the plan from being presented as final.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Market CAGR 9%/yr | 9%/yr, 2023-2029 | Trade association yearbook, quoted in the company's own investor update — single, interested-party source | Independent verification showed a materially lower market growth rate (direction of finding — share loss — would likely survive; magnitude would shrink) |
| 2 | Franchise revenue scales roughly with unit count in stress scenarios | Linear | No per-unit maturity curve given; only the 110-unit/EUR 14.0m endpoint was supplied | Real per-café ramp data would resize the downside cases |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is Corvina's EBIT margin today, and projected for 2029? | The 8% floor is an investor hard constraint the plan never addresses | Corvina CFO | Could kill the plan independently of revenue |
| Why exactly is the core losing share? | The largest unpriced lever on the table (~EUR 12.6m) depends on this being fixable | Corvina commercial leadership | Could justify reallocating capital from franchise to core |
| Is there any signed or near-signed franchise pipeline, and what do comparable launches achieve? | The 0/25/60/110 ramp has zero evidentiary support today | Franchise development lead / industry benchmarks | Could materially cut the EUR 14.0m figure |
| What capex does the core need for ~17% volume growth to 2029? | EUR 4.5m of the EUR 6m cap is already committed to franchise | Corvina operations/finance | Could force a trade-off between funding core and franchise |

## Trap checks

- [x] Lever sized on base case, gap shown openly? **Failed** — franchise number reads as reverse-engineered to plug the gap; "remaining gap: none" contradicts management's own arithmetic (74.8 vs 75.0).
- [x] Core and installed base sized before adjacency? **Failed** — no wallet/installed-base analysis; plan jumps straight to an unproven new concept.
- [x] Ramp-up benchmarked against comparable launches? **Failed** — no comparable cited for 0→110 units in 3 years with zero signed operators.
- [x] Market growth vs. share change separated? **Passed in this review** — not in management's narrative.
- [x] No lever breaches the capital limit? **At risk** — no core capex disclosed; could push the plan over EUR 6m.
- [x] Two or three large levers, not many small bets? **Technically yes, but all new growth concentrated in one unproven lever.**
- [x] EBIT shown per lever, margin checked against the floor? **Failed** — no cost or margin data anywhere in the plan.


## Files in work dir after run

- case-growth-strategy-corvina.md
- cg-02-input.md

## File written by the run: case-growth-strategy-corvina.md

# Growth strategy — quick case: Corvina Coffee Roasters

Source: `cg-02-input.md` (management draft growth plan, 2026-2029). Fictional company; all figures invented for evaluation.

## Step 1: Sharpen the question

Given directly in the brief: target EUR 75m revenue by 2029, EBIT margin ≥8%, investment ≤EUR 6m, set by investors. Decision maker: investors / board, timing not stated.

Sharpened question: *"Does management's two-lever plan (core wholesale at 4%/yr + Corvina café franchise) plausibly close the gap from EUR 52m to EUR 75m by 2029, within EUR 6m investment and an 8% EBIT floor — or does it understate the core's real problem and overstate the franchise's real risk?"*

Not asked of a user in this pass (no interactive counterpart) — proceeding on the data given and flagging gaps as Open questions rather than halting, per the brief's own request for a pressure-test and answer page.

## Step 2: Issue tree

| Branch | Hypothesis | Kill criterion | Status |
|---|---|---|---|
| Gap and momentum | Momentum case (core only, no new action) misses the EUR 75m target by a material amount | Gap under ~EUR 2-3m: question becomes "defend the core," not "find a new growth engine" | **Confirmed** — gap is EUR 14.2m, core alone reaches only EUR 60.8m |
| Core: market vs share | The wholesale market is growing strongly; Corvina's core is losing share, not merely growing slower than a flat market | Share stable or rising 2023-2025: reframe "core is healthy" stands | **Confirmed killed (for management)** — share fell from 8.0% to 7.3% in two years against a 9%/yr-growing market |
| Core: defend-the-core lever | Arresting the share loss (not even reversing it) closes most of the gap on its own, at zero incremental capital | Flat-share scenario adds under EUR 5m by 2029: not worth prioritising over franchise | **Confirmed false — lever is large**: holding share flat gets core to ~EUR 73.4m by 2029, within EUR 1.6m of the full target |
| Franchise: ramp realism | The 0/25/60/110-unit ramp and EUR 14m 2029 revenue are supported by a pipeline or comparable launch | No signed operators and no comparable cited: ramp is asserted, not evidenced | **Killed as stated** — zero operators signed, no benchmark given; evidence weak |
| Franchise: right to win | Corvina has retail/franchise execution capability transferable from B2B wholesale roasting | No franchise, retail or consumer-brand experience evidenced anywhere in the plan | **Open / unproven** |
| Portfolio and margin | The combined plan clears the EUR 75m target with an EBIT margin ≥8% within EUR 6m investment | No EBIT figures anywhere in the plan | **Cannot be evaluated — critical data gap** |

## Step 3: Deciding analyses

**a. Gap and momentum case.** Core at its own stated momentum (4%/yr, consistent with the 2023-2025 CAGR of 4.08%) reaches EUR 52m × 1.04⁴ ≈ **EUR 60.8m** by 2029 with no new action. Against the EUR 75m target, the **momentum gap is EUR 14.2m**. The franchise lever is sized at EUR 14.0m — within EUR 0.2m of exactly plugging this gap. That closeness is itself a flag: it reads as a number reverse-engineered to close the gap, not one built up from signed franchisees or per-unit economics. *Hypothesis "gap is material" — confirmed.*

**b. Market and share split.** Market: EUR 600m (2023), growing 9%/yr per the trade yearbook ⇒ EUR 712.9m (2025) ⇒ EUR 1,006.3m (2029). Corvina core: EUR 48m (2023) ⇒ EUR 52m (2025). **Share: 8.00% → 7.29%**, a loss of 0.7pp in two years (≈ 9% of its own share, relative). Projected forward on management's own 4%/yr plan while the market keeps compounding at 9%/yr, share keeps falling to **6.05% by 2029** — the plan's "healthy core" is a core that keeps losing relative ground every year of the plan. *Hypothesis "core is losing share, not just growing slower than a slow market" — confirmed; "core is healthy" framing is not supported by management's own market data.*

**c. Installed base and wallet.** No data given on what existing wholesale customers (cafés, restaurants, offices) buy elsewhere (equipment, other beverage lines, consumables) or on account-level penetration. **Not sized — missing lever.** This is normally the cheapest growth available and the plan does not mention testing it.

**d. Lever sizing.**
| Lever | 2029 base case | Evidence grade | Basis |
|---|---|---|---|
| Core, momentum (4%/yr) | EUR 60.8m | Medium | Straight-line extrapolation of a 2-year trend; internally consistent with continuing to lose the same relative share, but untested against competitor moves |
| Core, share held flat (9%/yr, matching market) | EUR 73.4m | Hypothesis, not in management's plan | Mechanical consequence of the market data management itself cites; no diagnosis offered of *why* share is being lost or whether it's fixable |
| Franchise | EUR 14.0m | Weak | Zero signed operators; ramp 0/25/60/110 units in 3 years asserted without a comparable launch; implied blended revenue per unit (~EUR 127k) not benchmarked |

**e. Adjacency attractiveness (franchise).** Size: addressable café/franchise market size not given. Structure: competitive, fragmented café market (assumed — not evidenced). Right to win: Corvina's core competence is B2B wholesale roasting and supply logistics; running a consumer-facing retail franchise network (site selection, franchisee recruitment, training, retail marketing) is a different capability set, and the plan cites no prior experience in it. **Right to win unproven.**

**f. Portfolio and timing (Three Horizons).** Core = Horizon 1, defend/extend — yet receives **zero** incremental investment despite being the branch with the single largest identified, unpriced lever (arresting share loss, worth up to ~EUR 12.6m by 2029, i.e. 73.4 − 60.8). Franchise = Horizon 2/3, new and unproven — yet receives **100% of new investment (EUR 4.5m of EUR 6m) and is expected to deliver 100% of the plan's growth above momentum.** The portfolio is not diversified: it is one large, unevidenced bet dressed as a two-line plan, with no smaller options and no fallback if the bet underperforms.

**g. Stress test.**
| Scenario | Core | Franchise | Total | vs EUR 75m target |
|---|---|---|---|---|
| Management base case | 60.8 | 14.0 | 74.8 | **−0.2m** (management's own table does not actually reach 75m) |
| Franchise delivers 50% of plan (plausible given zero operators signed today) | 60.8 | 7.0 | 67.8 | **−7.2m (−9.6%)** |
| Franchise rollout slips ~1 year (0/0/25/60 vs 0/25/60/110) | 60.8 | ~7-8 | ~68-69 | **−6 to −7m** |
| Core defends share instead (flat share, +franchise base case) | 73.4 | 14.0 | 87.4 | **+12.4m** — shows the defend-the-core lever is bigger than the franchise bet |

## Step 4: Trap checks

- [ ] **Each lever sized on base case, remaining gap shown openly** — **No.** Franchise revenue (EUR 14.0m) sits within EUR 0.2m of exactly the momentum gap (EUR 14.2m) with no bottom-up buildup from signed units or per-café economics; "remaining gap: none" is stated even though management's own table sums to EUR 74.8m, not EUR 75m.
- [ ] **Core and installed base sized before any adjacency** — **No.** No wallet-share or installed-base analysis is offered. The plan moves straight to a brand-new franchise concept while the core's actual, quantified problem (share loss) is not diagnosed or addressed with any investment.
- [ ] **Ramp-up of new moves compared with comparable launches** — **No.** No comparable café-franchise rollout is cited anywhere to support 0→110 units in three years from a zero-operator start.
- [ ] **Market growth and share change separated** — **Yes, in this pressure test** (not in management's narrative, which calls the share-losing core "healthy" and its growth "solid").
- [ ] **No lever needs capital above the limit** — **Unknown/at risk.** EUR 4.5m of the EUR 6m ceiling goes to the franchise; no capex is stated for the core's own ~17% volume growth to 2029. Any material core capex pushes the plan over the EUR 6m cap.
- [ ] **Two or three large levers carry the plan, not many small ones** — **Technically yes (two), but concentrated to the point of fragility**: all growth above flat momentum rides on one unproven, unresourced-for-risk lever.
- [ ] **EBIT effect in euros shown per lever, margin checked against the floor** — **No.** The plan contains no EBIT or cost figures. The investors' 8% margin floor — arguably the binding constraint, given that new-unit franchise rollouts typically run at a loss during ramp (franchise team, flagship costs) — is never addressed.

## Step 5: Answer page

See below — delivered as the final answer page to the user.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Market CAGR 9%/yr 2023-2029 | 9%/yr | Trade association yearbook 2025, as quoted in the company's own investor update — single source, interested party, not independently triangulated | A lower independently-verified market growth rate (e.g. 5-6%/yr) would shrink the measured share loss, though a loss would likely still exist (recomputed at 5%/yr: share still falls from 8.0% to 7.9%) |
| 2 | Franchise revenue scales roughly in proportion to unit count for stress-test purposes | Linear scaling | No per-unit ramp curve (maturity curve) was given; used management's own 14.0m/110-unit endpoint as the only anchor | Actual per-unit ramp data (royalty take-up curve, time-to-breakeven per café) would change the downside-scenario sizing materially |
| 3 | No EBIT/cost data exists to check the 8% margin floor | Treated as a blocking gap, not estimated | Nothing in the source document states costs, SG&A or current margin | Management's EBIT bridge, if provided, would let this be assessed properly — currently it cannot be |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is Corvina's current EBIT margin, and what does the plan project for 2029? | Investors set an 8% margin floor as a hard constraint; the plan is silent on it entirely | Corvina CFO/management | Could independently kill the plan even if revenue hits EUR 75m |
| Why is the core losing share — pricing, distribution coverage, product range, a specific competitor? | This is the largest unpriced lever (~EUR 12.6m by 2029 just from holding share flat); fixing it is likely cheaper and lower-risk than the franchise bet | Corvina sales/commercial leadership | Could justify reallocating investment from franchise to core-defense, or at minimum rebalancing the two |
| Is there a signed or near-signed franchise operator pipeline, and what do comparable café-franchise launches achieve in years 1-3? | The 0/25/60/110 ramp has zero evidentiary support; outside-view benchmarks would set a realistic range | Corvina franchise development lead / franchise industry data | Could cut the EUR 14.0m 2029 figure substantially, reopening the gap |
| What capex, if any, does the core need to support ~17% volume growth to 2029? | EUR 4.5m of the EUR 6m investment ceiling is already committed to franchise; any core capex risks breaching the cap | Corvina operations/finance | Could force a choice between funding the core and funding the franchise at the stated scale |
| Is the independent market-growth figure (9%/yr) verifiable outside the trade association's own yearbook? | The entire "losing share" finding is scaled by this number; direction is robust, magnitude is not | Independent market research, national statistics office | Would sharpen (not reverse) the share-loss finding |

## Trap checks

See Step 4 above — repeated at the end of the answer page per format.

