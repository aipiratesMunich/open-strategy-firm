# cg-02-healthy-core-illusion on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes Corvina's market share fall (8.0% to ~7.3%) and states 4% growth in a 9% market is share loss, not healthy core | yes | 'Corvina share 8.0% / 7.3%' table; '4%/year against a 9%/year market is share loss, not health (8.0% → 7.3% share, 2023-25)' |
| Sizes what holding share would be worth (~EUR 73m in 2029, ~12-13m above plan's core) and makes cause of share loss the first question to answer | NO | Run computes held-share value using the 2023 share (8.0%) rather than the current 2025 share (7.3%), getting '~EUR 80.5m' and 'about EUR 20m' gap instead of the correct ~73.4m/~12.6m; also the cause-of-share-loss question is ranked 3rd in Open Questions and 4th in Next Steps, not first |
| Shows franchise carries almost the whole gap and treats 0-110 café ramp as unproven (widens range, names/compares missing comparable launches, notes no operator signed) | yes | 'Remaining gap if franchise delivers nothing in 2029: EUR 14.2m' alongside franchise=14.0 shows franchise ~ the whole gap; 'Wide — no operator signed, no pilot, no comparable cited'; 'No comparable franchise launch is cited to show this ramp is achievable from a standing start' |
| Flags that the 9% market growth figure is second-hand (trade association) and should be checked at source | yes | 'The 9%/year market-growth figure is a single source (one trade association yearbook, relayed through the company's own investor update)...worth independently checking'; next step: 'Independently verify the 9%/year market-growth figure against a second source' |
| Concludes plan as drafted is not the right plan (or not yet), with reordered answer: fix core share loss first, franchise as option/later lever with proof point | yes | 'Answer: No, not as drafted'; 'do not book the franchise revenue into the investor-facing plan until a signed operator and a working pilot exist; keep it as upside, and separately fund a core-defence initiative' |
| Shows profit next to revenue or flags plan lacks it; checks 8% EBIT floor or names as unknown | yes | 'The plan also never shows the 8% EBIT margin the investors actually require; it is a revenue bridge only'; open question 'does the combined plan clear the 8% floor the investors set?' |
| Shows the remaining gap openly under its own levers | yes | 'Sum of kept levers (base case, core only...): EUR 60.8m. Remaining gap if franchise delivers nothing in 2029: EUR 14.2m (19% of target)' |
| Must not accept 'our core is healthy' or EUR 14m franchise figure at face value | yes | 'Hypothesis: "the core is healthy..." — killed'; franchise treated as 'Option, not a committed lever' with wide uncertainty range |
| Must not invent reasons for share loss as facts (may list as hypotheses) | yes | 'whatever is taking share (the document never says who or why)'; open question lists 'price, distribution, a specific competitor, channel shift' as things to investigate, not asserted facts |

## Transcript

## Turn 1

**User:** The Corvina management team has drafted their growth plan. Pressure-test it and give me the answer page: is this the right plan to reach EUR 75m by 2029? (Attached in the working directory: cg-02-input.md.)

**Short answer: no.** The plan hits EUR 74.8m, not 75.0m, and it gets there by calling a share-losing core "healthy" and betting 61% of the needed growth on a franchise network with no signed operator and ~10 weeks of runway before its first milestone.

The two things that actually break it:

1. **"Healthy core" doesn't survive the company's own data.** Core grew 4%/year while the market (per management's own cited source) grew 9%/year — share fell from 8.0% (2023) to 7.3% (2025). Projecting flat 4%/year to 2029 just continues that share loss to ~6.0%. Had Corvina simply held its 2023 share, the core alone would be worth ~EUR 80.5m by 2029 — more than the whole target, no franchise required. Zero of the EUR 6m investment budget is pointed at fixing this.
2. **The franchise lever is a straight-line hope, not a plan.** 0→25→60→110 cafés with no operator signed, no unit economics shown, and no comparable launch cited — and today is 14 Oct 2026, meaning the "25 cafés in 2027" milestone is roughly 14 months out with nothing yet in motion.

Minor but telling: 60.8 + 14.0 = 74.8, not 75.0 — the plan's "remaining gap: none" is simply wrong by EUR 0.2m, and the investors' 8% EBIT margin condition isn't addressed anywhere in the draft.

Full pressure-test with the gap bridge, lever table, killed hypotheses, assumptions and open questions is written to `case-growth-corvina.md` in the working directory.


## Files in work dir after run

- case-growth-corvina.md
- cg-02-input.md

## File written by the run: case-growth-corvina.md

# Growth strategy: Corvina Coffee Roasters, does the 2026-2029 plan reach EUR 75m revenue at ≥8% EBIT margin within EUR 6m investment?

**Answer: No, not as drafted.** The plan reaches EUR 74.8m (not EUR 75.0m — the "no gap" claim is itself a EUR 0.2m rounding error) by (1) mislabelling a core business that is **losing share in a fast-growing market** as "healthy," and (2) putting 61% of the required growth (EUR 14.0m of EUR 23.0m) on a franchise network that does not exist yet, has no signed operator, no unit economics, and — as of today (14 Oct 2026) — about ten weeks of runway left before the plan needs 25 cafés trading. The plan also never shows the 8% EBIT margin the investors actually require; it is a revenue bridge only.

**Confidence:** Low, because the two numbers that carry the whole plan (core "health" and franchise ramp) do not survive a first check against the company's own market data, and margin — one of the three investor conditions — is not addressed anywhere in the document.

## The gap

| EUR m | 2025 | 2029 (plan) |
|---|---|---|
| Core wholesale | 52.0 | 60.8 |
| Café franchise | 0 | 14.0 |
| **Total (plan)** | **52.0** | **74.8** |
| **Target** | | **75.0** |
| **Gap (plan vs. target)** | | **0.2** |
| Constraints | capital ≤ EUR 6m (EUR 4.5m already committed to franchise), EBIT margin ≥ 8%, no margin shown for either lever |

## What the market data the plan itself quotes actually says

Management cites the roasters' trade association yearbook: the wholesale market was EUR 600m in 2023 and has grown 9%/year since. Applying that:

| | 2023 | 2025 | 2029 (if 9%/yr continues) |
|---|---|---|---|
| Market | 600.0 | 712.9 | 1,006.3 |
| Corvina core wholesale | 48.0 | 52.0 | 60.8 (plan) |
| **Corvina share** | **8.0%** | **7.3%** | **6.0%** |

Core revenue grew ~4%/year 2023-25 (48 → 52), which management calls "solid growth in a competitive market." Against a market growing 9%/year, that same number means Corvina's share fell from 8.0% to 7.3% in two years — the core is **losing share, not holding its own**, and the plan's own forward assumption (flat 4%/year to 2029) extends that loss to an implied 6.0% share by 2029. If Corvina had merely held its 2023 share of 8.0% through the market's growth, the core alone would be worth ~EUR 80.5m in 2029 — more than the entire EUR 75m target, with no franchise needed at all. That gap between "held share" (80.5m) and "plan" (60.8m), about EUR 20m, is the real size of the core problem the plan calls healthy and does not address with a single euro of the EUR 6m investment budget.

**Hypothesis: "the core is healthy, 4%/year is a safe floor" — killed.** Reshaped to: the core is on a share-losing trajectory; 4%/year is a plausible trend-continuation estimate, not a conservative one, and it is not stress-tested against the possibility that whatever is taking share (the document never says who or why) keeps accelerating in a market still growing at 9%/year.

## Levers

| Lever | Revenue base case 2029 | Range | EBIT effect | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Core wholesale, flat 4%/yr | EUR 60.8m | EUR 55-61m if share loss persists or worsens; upside only with a funded defend-share plan | Not shown | EUR 0 allocated | Immediate (in motion) | Medium — extrapolates a 2-year trend, no causal diagnosis of share loss, single market-size source | **Keep base case, but reopen**: size what it costs to defend share instead of accepting further loss |
| Café franchise (0→25→60→110 cafés) | EUR 14.0m | Wide — no operator signed, no pilot, no comparable cited; could be a fraction of 14.0m if signing or ramp slips | Not shown | EUR 4.5m | First revenue not before 2027; full ramp assumes signing + scale-up inside ~14 months from today | Weak — single straight-line management estimate, implied EUR 130-165k revenue/café-year to Corvina not benchmarked against any comparable franchise system | **Option, not a committed lever** until an operator is signed and a pilot (5-10 units) validates unit economics |

**Sum of kept levers (base case, core only, franchise treated as unproven option):** EUR 60.8m. **Remaining gap if franchise delivers nothing in 2029:** EUR 14.2m (19% of target). **How we close or accept it:** do not book the franchise revenue into the investor-facing plan until a signed operator and a working pilot exist; keep it as upside, and separately fund a core-defence initiative sized against the ~EUR 20m "held-share" benchmark above.

## Killed options and why

- "Core is healthy at 4%/year, no action needed": killed by the company's own cited market data — 4%/year against a 9%/year market is share loss, not health (8.0% → 7.3% share, 2023-25).
- "Remaining gap to target: none": false — 60.8 + 14.0 = 74.8, EUR 0.2m short of EUR 75.0m.

## Risks and what would change the answer

1. If the franchise operator is not signed soon, the 2027 "25 cafés" milestone is already at risk: today is 14 October 2026, the plan shows zero cafés opening in 2026, and no operator has been signed — leaving roughly ten weeks to sign an operator, build the flagship and franchise team (EUR 4.5m), and still open 25 units in 2027. No comparable franchise launch is cited to show this ramp is achievable from a standing start.
2. If the franchise delivers even half its 2029 target (EUR 7m instead of EUR 14m), total revenue falls to ~EUR 67.8m, a EUR 7.2m miss — and the core, the larger and more certain part of the plan, has no funded response to its own share loss to help close that.
3. The plan has no EBIT margin line for either lever. Franchise build-out (new team, brand, flagship) front-loads cost before royalty and supply revenue ramp, which pressures margin in exactly the years the investors' 8% floor applies. Revenue could land at or near EUR 75m and the plan could still fail the mandate on margin.
4. The 9%/year market-growth figure is a single source (one trade association yearbook, relayed through the company's own investor update) — if the true rate is lower, the core's relative share loss is smaller than calculated above, but the core's absolute growth (4%/year) would then be closer to market and "healthy" would be a fairer label. This number is worth independently checking before the share-loss finding is presented to investors as fact.

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Market growth of 9%/year holds for 2023-2029, applied as a constant annual rate | 9%/year, 6 years (2023→2029) | Company-cited trade association yearbook, single source | Actual rate is materially lower (e.g. 4-5%/year) — core share loss would be much smaller or absent, and the "healthy core" framing would be largely vindicated |
| 2 | "110 cafés in 2029" is a cumulative count opened by year-end 2029 (25 in 2027, +35 in 2028, +50 in 2029) | Cumulative, straight-line additions | Only reading consistent with the stated figures; not confirmed in the document | Figures mean something else (e.g. gross openings including closures) — franchise revenue per unit would need rework |
| 3 | EUR 14.0m franchise revenue is evenly distributable across store-years for a rough per-unit sanity check | ~EUR 130-165k revenue to Corvina per café-year (royalty + coffee supply) | Back-calculated from the plan's own total; not a disclosed or sourced unit economic | A disclosed royalty rate and per-café sales assumption shows this is in line with comparable coffee-franchise systems |
| 4 | No overlap/cannibalisation between core wholesale customers (cafés, restaurants, offices) and new Corvina-branded franchised cafés | Treated as fully incremental | Not addressed in the document | Franchised cafés replace sites that were, or would have become, wholesale accounts — some of the EUR 14.0m is not incremental to the group |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What EBIT margin does each lever carry, and does the combined plan clear the 8% floor the investors set? | This is one of three explicit investor conditions and is completely unaddressed in the draft | CFO / FP&A | Could invalidate the plan even if the EUR 75m revenue figure is hit |
| Has a franchise operator been identified or is one in negotiation, and on what timeline? | The 2027 ramp (25 cafés) is ~14 months away from today (14 Oct 2026) with "no operator signed yet" stated as fact | Head of franchise / CEO | If no operator is close to signing, the entire EUR 14.0m lever should be downgraded to a low-probability option for 2029 reporting purposes |
| What is driving the core's share loss against a 9%/year market (price, distribution, a specific competitor, channel shift to direct roasting)? | Without a cause, the 4%/year forward assumption cannot be judged as conservative, realistic, or optimistic | Commercial/sales leadership | Identifies whether a funded core-defence initiative could close a meaningful part of the EUR 20m "held-share" gap more cheaply and with less risk than the franchise bet |
| What per-café royalty rate and coffee-supply margin underlie the EUR 14.0m figure, and against what comparable franchise system were they benchmarked? | No unit economics are shown; the implied EUR 130-165k/café-year is unverified | Franchise development lead | Confirms or revises the single largest lever in the plan |
| Is any of the EUR 6m investment budget earmarked to defend or accelerate the core, beyond the EUR 4.5m already committed to the franchise? | Currently EUR 0 is allocated to the part of the business shown above to be losing the most ground | CFO | A funded core-defence lever could replace some of the risk currently concentrated in the unsigned franchise bet |

## Next steps

| What | Who | By when |
|---|---|---|
| Independently verify the 9%/year market-growth figure against a second source | Strategy/FP&A | Before the plan goes to investors |
| Get a signed franchise operator (or letter of intent) and a costed pilot plan for 5-10 units before booking any 2027 franchise revenue in the investor plan | Head of franchise | Immediately — the 2027 milestone is ~14 months out and currently unstaffed |
| Build the EBIT margin bridge for both core and franchise levers against the 8% floor | CFO | Before the plan is finalised |
| Diagnose the cause of core share loss and cost a defend-share initiative, funded from the EUR 6m budget | Commercial leadership | Next planning cycle |
| Correct the EUR 74.8m vs. EUR 75.0m arithmetic and remove the "remaining gap: none" claim | Whoever owns the deck | Immediately |

