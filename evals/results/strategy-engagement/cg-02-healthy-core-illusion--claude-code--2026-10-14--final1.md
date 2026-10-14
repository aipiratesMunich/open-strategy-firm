# cg-02-healthy-core-illusion on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (8/9 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Computes Corvina's market share and shows it fell (8.0% to ~7.3%), states 4% growth in a 9% market is share loss not healthy core | yes | "Corvina's market share: 8.00% (2023) → 7.29% (2025) — a real and continuing share loss" and "The core is not 'healthy' — it is losing share in a growing market" |
| Sizes what holding share would be worth (~EUR73m/~EUR12-13m above plan's core) and makes the cause of share loss the first question to answer | NO | Holding-share value is sized ('~EUR 73.4m by 2029'), but the cause-of-share-loss question is NOT placed first: Next Steps row 1 is 'Build an EBIT margin P&L...' and row 2 is 'Diagnose why core grew ~4%/yr...'; Open Questions table likewise lists the EBIT-margin question first and the share-loss-caus |
| Shows franchise carries almost the whole gap, treats 0-110 café ramp as unproven (widened range, names/compares to comparable launches, notes no operator signed) | yes | "responsible for ~99% of that gap"; "zero operators signed, no comparable launch cited"; range listed as "wide, effectively unbounded downside"; open question "What comparable franchise launches inform the 0→25→60→110 ramp..." |
| Flags the 9% market growth as a trade-association figure quoted second-hand, to be checked at source | yes | "Roasters' trade association yearbook 2025, as quoted in the investor update — a single, secondhand-quoted source"; next step "Triangulate the 9%/yr market-growth figure against a second, independent source" |
| Concludes plan as drafted is not right (or not yet), reordered answer: fix core share loss first, franchise as option/later lever with proof point | yes | "No, not as drafted"; "keep the franchise as one option, add a priced 'defend/recover core share' lever"; "Secure at least one signed franchise operator and one open pilot café before committing capital to the 2027 ramp" |
| Shows profit next to revenue or flags its absence, checks the 8% EBIT floor or names it unknown | yes | "The investors' 8% EBIT margin floor is never addressed anywhere in the plan"; lever table marks EBIT effect "not sized — no margin data given" for every lever |
| Shows the remaining gap openly under its own levers | yes | "Sum if the franchise lever is treated skeptically (base case = core only): EUR 60.8m; remaining gap: EUR 14.2m" |
| Must not accept 'our core is healthy' or the EUR14m franchise figure at face value | yes | "The section titled 'Our core is healthy' is describing a business that is quietly ceding ground"; franchise figure called "option, not a 'keep' that can safely carry 99% of the gap" |
| Must not invent reasons for share loss as facts (only as hypotheses) | yes | Share-loss cause is posed as an open question ('which competitors or channels captured the share Corvina didn't') rather than asserted as fact; no competitor names, prices, or quotes invented. |

## Transcript

## Turn 1

**User:** The Corvina management team has drafted their growth plan. Pressure-test it and give me the answer page: is this the right plan to reach EUR 75m by 2029? (Attached in the working directory: cg-02-input.md.)

Saved to `case-growth-strategy-corvina.md`. Headline finding:

**No, not as drafted.** Management's own numbers show the "healthy core" is actually losing market share — it grew ~4%/yr while the market grew 9%/yr, so Corvina's share slid from 8.0% (2023) to 7.3% (2025) and, on the plan's own 4%/yr assumption, would keep sliding to ~6.0% by 2029. That reframes the whole plan:

- The core-only momentum case reaches EUR 60.8m, leaving a EUR 14.2m gap.
- The café franchise — zero operators signed, no comparable launch cited, revenue not starting before 2027 — is asked to supply EUR 14.0m, i.e. ~99% of that gap. That's the entire target resting on the single least-proven lever.
- A lever management never priced: simply **holding 2025 share** (7.29%) in a market still growing 9%/yr would get core revenue alone to ~EUR 73.4m by 2029 — 92% of the target, with none of the franchise's execution risk.
- The investors' 8% EBIT margin floor is never addressed anywhere in the plan — it's a revenue-only plan measured against a revenue-and-margin target.

The full answer page has the gap math, a reality-checked levers table, downside scenarios (e.g., slipped franchise ramp + continued share loss → ~EUR 67.8m, a ~10% miss), and concrete next steps (margin P&L by line, diagnose the share loss, require a signed franchise operator before committing to the 2027 ramp, triangulate the market-growth figure).


## Files in work dir after run

- case-growth-strategy-corvina.md
- cg-02-input.md

## File written by the run: case-growth-strategy-corvina.md

# Growth strategy: Corvina Coffee Roasters, does management's 2026-2029 plan reliably reach EUR 75m revenue at ≥8% EBIT margin within EUR 6m of investment?

**Answer:** No, not as drafted. The plan's own numbers show the core is **losing market share, not "healthy"** (grew ~4%/yr while the market grew 9%/yr), and then makes a single unlaunched café-franchise business — zero operators signed, no comparable launch cited — responsible for ~99% of the remaining EUR 14.2m gap to target. The plan also never addresses the investors' binding 8% EBIT margin floor at all. Management should keep the franchise as one option, add a priced "defend/recover core share" lever (which, at the market's own growth rate, closes almost the whole gap by itself), and not call the gap "none" until a margin P&L exists.

**Confidence:** Medium — high confidence in the share-loss finding (it follows directly from management's own cited figures); medium-to-low confidence in the overall verdict because the two numbers that would decide it — group EBIT margin and franchise unit economics — are not in the plan at all.

**Specialists and review:** None legal/regulatory-specific from the data given; before sign-off, get Finance to produce a margin P&L by business line, and have the franchise/commercial lead stress-test the rollout ramp against a comparable franchise launch.

## The gap

| EUR m | 2025 | 2029 |
|---|---|---|
| Revenue, momentum case (core only, continuing its own 2023-25 trend, no franchise) | 52.0 | 60.8 |
| Revenue, target | 52.0 | 75.0 |
| **Gap** | – | **14.2** |
| Constraints | EBIT margin ≥ 8% (not addressed anywhere in the plan); capital ≤ EUR 6.0m (EUR 4.5m already allocated to the franchise); nothing stated as ruled out |

## The core is not "healthy" — it is losing share in a growing market

This is the finding that reframes the whole plan. Using management's own numbers:

- Core wholesale: EUR 48.0m (2023) → EUR 52.0m (2025) = **+4.1%/yr**.
- National wholesale market: EUR 600m (2023), growing **9%/yr** (roasters' trade association yearbook 2025, as quoted in the investor update — a single, secondhand-quoted source; flagged as weak evidence below) → **EUR 713.1m in 2025**.
- Corvina's market share: **8.00% (2023) → 7.29% (2025)** — a real and continuing share loss, even though absolute revenue rose.
- Carrying the plan's own "+4%/yr" assumption to 2029 (EUR 60.8m) against a market still compounding at 9%/yr (EUR 1,007m in 2029) implies share falling further to **~6.0%** — a quarter of the company's 2023 share gone by 2029.

So-what: the section titled "Our core is healthy" is describing a business that is quietly ceding ground to competitors every year. Labelling that "healthy" and leaving it on autopilot, while betting the entire incremental gap on a brand-new, unsigned business line, is the core error in this plan.

**The lever management didn't size:** if Corvina merely *held its 2025 share* (7.29%) as the market keeps growing at 9%/yr, core revenue alone reaches **~EUR 73.4m by 2029** (52.0 × 1.09⁴) — 92% of the EUR 75m target, with none of the execution risk of launching a franchise system from zero. Even partial share recovery/defence would close most of the gap more cheaply and reliably than the franchise bet.

## Levers, reality-checked

| Lever | Revenue, base case 2029 | Range | EBIT effect | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Core wholesale, management's plan (+4%/yr, continued share loss) | EUR 60.8m | EUR 58.5-62m | **not sized — no margin data given** | not separately budgeted | ongoing | weak (trend-continuation; ignores that the trend itself is share loss) | keep, but reframe — see below |
| *(missing from the plan)* Defend/recover core share to market growth rate | up to EUR 73.4m if share merely held flat | EUR 61-73m depending on how much share is recovered | not sized | not budgeted (plan allocates nothing to this) | 12-24 months to show in share data | weak — not yet investigated by management | **should be added as a priced option before the franchise is treated as the only path to target** |
| Café franchise (0→25→60→110 cafés, 2026-2029) | EUR 14.0m | wide, effectively unbounded downside — no comparable launch cited, 0 operators signed today | **not sized — no margin data given** | EUR 4.5m | first revenue not before 2027, full ramp assumed by 2029 | weak (unlaunched concept, no signed partner, no outside-view benchmark for the ramp or the ~EUR 127k revenue/café average) | option, not a "keep" that can safely carry 99% of the gap |

**Sum if the franchise lever is treated skeptically (base case = core only):** EUR 60.8m; **remaining gap: EUR 14.2m, currently resting entirely on one unlaunched, unsigned business.** Management's claim of "no remaining gap" is only true if the franchise delivers essentially 100% of its unproven plan on schedule.

## Killed options and why

None killed outright from the data given. The material gap is an option *never put on the table*: a priced core-share-defence/recovery lever. It should be sized before the franchise is relied on for the whole gap.

## Risks and what would change the answer

1. If no franchise operator is signed by, say, mid-2027 — plausible, since none is signed as of today and the plan still assumes 25 open cafés that year — the ramp slips a year; a one-year delay alone removes roughly one cohort of unit-openings from 2029, pulling total revenue toward **EUR 68-70m**, below target even with the core on plan.
2. If core share loss continues at its embedded rate *and* the franchise delivers only half its plan (EUR 7.0m, plausible given zero signed operators today), total lands near **EUR 67.8m** — a ~10% miss with no visible buffer, because the plan already assumed the full base case of both levers to "just" reach EUR 74.8m.
3. If franchise-business EBIT margin is lower than core wholesale in the ramp years (likely: new franchise-team overhead, a loss-making flagship store, royalties that ramp slower than unit count) — plausible but unverified — group EBIT margin could land under 8% even if revenue hits EUR 75m, meaning the plan fails the investor brief despite "hitting the number."
4. If the 9%/yr market-growth figure is wrong (it is single-sourced, trade-association data quoted secondhand), the size of the share-loss problem changes, but even a materially lower market growth rate (e.g. 6%) would still exceed the core's own 4%/yr plan, so the share-loss finding is fairly robust to this uncertainty.

## Next steps

| What | Who | By when |
|---|---|---|
| Build an EBIT margin P&L by business line (core, franchise) against the 8% floor — currently entirely absent | CFO/Finance | Before the plan is approved |
| Diagnose why core grew ~4%/yr against a 9%/yr market: which competitors or channels captured the share Corvina didn't | Commercial/strategy lead | Next quarter |
| Size a "defend/recover core share" lever explicitly, with its own investment ask, as an alternative or complement to the franchise | Commercial lead | Next quarter |
| Secure at least one signed franchise operator and one open pilot café before committing capital to the 2027 ramp of 25 cafés | Franchise lead | Before the 2027 budget is locked |
| Get an outside view: how comparable food/beverage franchise launches actually ramped in years 1-3, and what revenue per unit they achieved, to test the 0→25→60→110 schedule and the ~EUR 127k/café average | Franchise lead + external benchmarking | Before the 2027 budget is locked |
| Triangulate the 9%/yr market-growth figure against a second, independent source | Strategy/market research | Next quarter |

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Core continues its 2023-25 trend | +4%/yr | Management draft; matches the actual 48→52m move | Share-loss cause is fixable — core could grow faster, reducing or removing reliance on the franchise |
| 2 | Market growth is accurately measured | +9%/yr since 2023 | Roasters' trade association yearbook 2025, quoted in the investor update (single, secondhand source) | True market growth is materially different — changes the size of the share-loss finding, though not its direction at any plausible value |
| 3 | Franchise 2029 revenue is achievable on the planned ramp | EUR 14.0m from 110 cafés | Management draft; no operator signed, no comparable launch cited | Ramp slips or per-unit revenue undershoots — 2029 revenue falls materially short |
| 4 | EUR 4.5m is sufficient to build and launch the franchise system | EUR 4.5m | Management draft | More corporate-owned flagship stores are needed in the absence of a signed franchisee, pushing spend toward or past the EUR 6m cap |
| 5 | Group EBIT margin reaches the 8% floor | Not stated anywhere in the plan | No data given — this is a flagged gap, not an assumption management made explicit | Franchise or core margin in 2029 is thin — revenue could hit EUR 75m while the plan still fails the investor brief |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| What is the projected 2029 EBIT margin for core and franchise separately? | 8% is a hard investor floor; the plan is silent on margin entirely | CFO | Could invalidate the plan even if revenue hits EUR 75m |
| Why did core grow at less than half the market's rate in 2023-25? | Determines whether share loss is structural (losing to named competitors/channels) or incidental | Commercial/sales leadership | If fixable, a priced share-defence lever could replace most of the franchise's risk |
| Has any franchise operator signed, or given a letter of intent? | The plan needs 25 open cafés within ~18 months of a zero-operator start today | Franchise lead | If none, the 2027 ramp needs to slip, cutting 2029 revenue |
| What comparable franchise launches inform the 0→25→60→110 ramp and the ~EUR 127k/café average? | No outside view is given; both the ramp and the per-unit revenue are unverified | Franchise lead / external benchmarking | Could substantially widen or narrow the credible revenue range |
| Is there a second, independent source for the 9%/yr market-growth figure? | Currently single-sourced via a trade association, quoted secondhand | Strategy/market research | Confirms or revises the size of the share-loss finding |

