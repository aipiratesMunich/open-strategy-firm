# cg-01-revenue-gap on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the decision question in the skill's form (gap EUR140m→175m by 2030, EUR15m capital, no acquisitions, EBIT margin ≥10%, board March 2027) | yes | Header: 'which levers close the gap from EUR 140m to EUR 175m revenue by 2030, within EUR 15m capital and without group EBIT margin falling below 10%, with no acquisitions?' plus 'the March 2027 board' |
| Computes a momentum case of ~EUR140-141m and gap of ~EUR34m using the CFO convention | yes | 'Momentum case: each segment's 2023–2025 CAGR continued to 2030 (convention agreed with the CFO)... Total ≈ EUR 140.7m' and 'Gap ~34.3m' |
| Separates market growth from share change and states Kirkby lost share in both lab instruments and process sensors | yes | 'Kirkby's own momentum (−1.2%, +2.6%, 0%) is below market in every single segment... worst in lab instruments... and notable even in... process sensors' |
| Sizes the core (share recovery, price) and installed base (service coverage) before the software adjacency, each with a base case, range, and evidence grade | NO | Share recovery is never sized as a lever; it is explicitly left unsized — 'Process sensors carries no incremental lever in this base case... no sensors-specific action data in the pack was provided' and listed as an open question that 'could close most of the remaining EUR 17–28m gap'. Only price an |
| Installed-base lever about EUR4.3m at 50% coverage (or another coverage level with consistent arithmetic) | yes | '14,300 × 35% × EUR 1,300 ≈ EUR 6.5m' using the same EUR1,300/contract rate implied by the 7,700-contract/EUR10m base data — internally consistent arithmetic at a different (higher, ~58%) coverage level |
| Treats the EUR15m software figure as unsupported: widens range or kills it pending evidence, names comparison that would settle it, without inventing one | yes | 'the head of strategy's EUR 15m claim has no interviews, pilots, or comparables behind it... re-based it... to a defensible ~EUR 3.3m' with range 1.65-4.95m and open question naming '2-3 paid pilots and customer interviews... comparable B2B software launches' |
| Shows profit next to revenue for every kept lever and checks the 10% EBIT floor | yes | Levers table includes 'EBIT effect (EUR)' column for each lever; 'Group EBIT margin is 12.5–13.5% in every case — well above the 10% floor' |
| Shows the remaining gap openly after base-case levers and says how it is closed or accepted | yes | 'Remaining gap: ~EUR 23m... the gap never closes, even in the high case (EUR 17m still open)' with recommendation to 'tell the board plainly that EUR 175m by 2030 isn't yet reachable with organic levers alone' |
| Answer line names specific levers with amounts and investment, and a confidence level with one reason | yes | 'service-contract conversion (~EUR6.5m)... lab-instrument price reset (~EUR1.5m)...roughly EUR4-11.5m of the EUR15m capital... Confidence: Low-medium' with stated reasons |
| Assumptions table and open-questions table in the skill's format | yes | Document contains '## Assumptions' table (#, Assumption, Value used, Basis, Would change the answer if) and '## Open questions' table (Question, Why it matters, Who can answer, Effect on the answer) |
| Must not close the gap by stretching assumptions (e.g. full share recovery plus EUR15m software at base case with no range) | yes | Software is explicitly re-based down to ~EUR3.3m with a range, not taken at face value; gap is left open rather than stretched closed |
| Must not invent market data, competitor prices or benchmark ramp-up rates | yes | Market growth figures align with input-derived segment data; software attach rate, price, and margin are explicitly flagged as ASSUMPTIONS with ranges rather than presented as researched facts |

## Transcript

## Turn 1

**User:** Work the Kirkby growth case from the briefing pack. Quick case, no engagement folder. I need the answer page for the CEO. (Attached in the working directory: cg-01-input.md.)

Saved to `case-growth-kirkby-analytical.md`. Headline, upfront since it contradicts the brief: **the plan as evidenced doesn't reach EUR 175m.** Momentum takes Kirkby to ~EUR 140.7m by 2030 (flat, confirming the CEO's premise), and the gap is ~EUR 34m — but the real finding is that Kirkby is losing relative share in *every* segment against its own growing served markets, not just stalling with a flat market.

The three data-backed levers — service-contract conversion on the uncontracted 65% of the installed base (~EUR 6.5m), a partial lab-instrument price reset (~EUR 1.5m), and process-analytics software — only close part of the gap. On the software: the head of strategy's EUR 15m claim has no interviews, pilots, or comparables behind it, so I re-based it off the installed base to a defensible ~EUR 3.3m, making it the *smallest* of the three levers, not "the answer." Even granting the original EUR 15m claim at face value, the combined plan still lands ~EUR 11m short of target.

Total: ~EUR 152m by 2030 (range 147–158m), leaving EUR 17–28m of the gap open. Margin clears the 10% floor comfortably in all cases (12.5–13.5%) — margin isn't the constraint, missing revenue is.

Recommendation for the board paper: fund the two proven levers now, gate the software spend behind a cheap pilot instead of the full EUR 9m, open a new workstream on process-sensors share recovery (unsized here for lack of data, but the best remaining candidate), and tell the board plainly that EUR 175m by 2030 isn't yet reachable with organic levers alone.


## Files in work dir after run

- case-growth-kirkby-analytical.md
- cg-01-input.md

## File written by the run: case-growth-kirkby-analytical.md

# Growth strategy: Kirkby Analytical — which levers close the gap from EUR 140m to EUR 175m revenue by 2030, within EUR 15m capital and without group EBIT margin falling below 10%, with no acquisitions?

**Answer:** The three levers the data supports — service-contract conversion, a partial lab-instrument price reset, and a gated process-analytics software pilot — take revenue to about **EUR 152m by 2030 (range EUR 147–158m)**, closing only **EUR 11–18m of the EUR 34m gap**, for roughly **EUR 4–11.5m of the EUR 15m capital**. Group EBIT margin stays safely above the 10% floor (12.5–13.5%) in every case, so margin is not the binding constraint — revenue is. **The head of strategy's claim that "software is the answer" does not hold**: even taken at face value (EUR 15m), the combined plan still falls about EUR 11m short of EUR 175m; on the evidence actually behind it (no interviews, pilots or comparables), software's realistic base case is closer to EUR 3.3m, smaller than either of the other two levers. The honest message for the CEO to take to the March 2027 board: **fund the two proven levers now, gate software behind a pilot, open a fourth branch on process-sensors share recovery (unsized, but the best remaining candidate), and tell the board that EUR 175m by 2030 is not yet reachable with organic levers alone** — a decision on the target, timeline or constraints will likely be needed.

**Confidence:** Low-medium. The gap and the share-loss diagnosis are solid (built from Kirkby's own finance and market data). The two core levers rest on one labelled assumption each (conversion rate, price elasticity). The software number and the "target reachable" conclusion are low confidence — they depend on data (why Kirkby is losing share everywhere, what a software pilot would actually show) that is not in this pack.

## The gap

| | 2025 (actual) | 2030 momentum (no new action) | 2030 target |
|---|---|---|---|
| Lab instruments | 80 | 75.2 | — |
| Process sensors | 40 | 45.5 | — |
| Service | 20 | 20.0 | — |
| **Total revenue** | **140** | **140.7** | **175** |
| **Gap** | | | **~34.3** |
| Constraints | capital EUR 15m, EBIT margin floor 10% group, ruled out: acquisitions |

Momentum case: each segment's 2023–2025 CAGR continued to 2030 (convention agreed with the CFO). Lab instruments: CAGR −1.23%/yr → EUR 75.2m. Process sensors: CAGR +2.60%/yr → EUR 45.5m. Service: CAGR 0% → EUR 20.0m. Total ≈ EUR 140.7m — the business stays essentially flat, confirming the CEO's "stuck at EUR 140m."

**Market growth vs share — the real diagnosis.** Kirkby's served markets are *not* flat: lab instruments +3%/yr, process sensors +6%/yr, service +4%/yr. Kirkby's own momentum (−1.2%, +2.6%, 0%) is below market in **every single segment**. This is not a stalled core in a stalled market — it is **share loss across the entire portfolio**, worst in lab instruments (losing ~4 points of relative growth a year against its own market) and notable even in the fastest-growing, highest-margin segment (process sensors). This reframes the question: the first place to look for growth is not a new software line, it is why the core is losing ground everywhere.

## Levers

| Lever | Revenue base case (2030) | Range | EBIT effect (EUR) | Investment | Time to impact | Evidence grade | Decision |
|---|---|---|---|---|---|---|---|
| Service-contract conversion (uncontracted installed base) | +EUR 6.5m | +EUR 3.7m to 9.3m | +EUR 1.6m (range +0.9 to +2.2m) | EUR 1.5–2m | 12–24 months to ramp | medium | **keep** |
| Lab instruments price reset (partial, toward the 7% gap) | +EUR 1.5m | +EUR 0.8m to 2.6m | +EUR 1.5m (near full flow-through) | EUR 0.3–0.5m | immediate–12 months, staged | weak-medium | **keep, as a staged test** |
| Process analytics software | +EUR 3.3m | +EUR 1.65m to 4.95m (vs. the EUR 15m claimed) | −EUR 1.0m (loss during ramp; range −1.0 to −0.8m) | EUR 9m claimed; **recommend EUR 1.5–2m pilot first** | 2028+ at the earliest, unproven | weak | **option — gate behind a pilot** |

**Sum of kept levers (base case): ~EUR 11.3m** of incremental revenue over momentum → total 2030 revenue ≈ **EUR 152m**. **Remaining gap: ~EUR 23m** (about two-thirds of the EUR 34m gap). Across the low/base/high cases run (service 20–50% conversion, price +2–5% net, software 5–15% attach), total 2030 revenue lands in a **EUR 147–158m** range — the gap never closes, even in the high case (EUR 17m still open). **Group EBIT margin is 12.5–13.5% in every case** — well above the 10% floor, so margin is not what stops this plan; the missing EUR 17–28m of revenue is.

### How the numbers were built
- **Service:** 22,000 instruments installed; 35% (7,700) under contract at EUR 1,300/instrument/year (≈EUR 10m of the EUR 20m service line); 65% (14,300) uncontracted, mostly served by independent shops. Base case assumes 35% of the *uncontracted* pool converts by 2030 (ASSUMPTION — no comparable conversion campaign cited): 14,300 × 35% × EUR 1,300 ≈ EUR 6.5m. Margin held at the segment's 24% EBIT margin.
- **Price:** Lab instruments list ~7% below the two main competitors, "no volume reason recorded." Base case tests a partial +3% increase (not the full 7%, given the segment is already losing share for unexplained reasons) with an assumed 1 point of volume loss (ASSUMPTION), netting ~+2% revenue (~EUR 1.5m on the EUR 75.2m momentum base), flowing almost fully to EBIT since no incremental cost.
- **Software:** The head of strategy's EUR 15m-by-2030 claim has no customer interviews, pilots or comparable launches behind it — a classic inside-view forecast and the weak-evidence trap this playbook flags explicitly. Re-based on the only concrete asset in the pack, the 22,000-instrument installed base, at an assumed 10% eventual attach and an assumed EUR 1,500/instrument/year subscription (both ASSUMPTIONS — not in the data), giving ≈EUR 3.3m by 2030. Assumed −30% EBIT margin during ramp (typical early-stage enterprise-software cost structure, ASSUMPTION), i.e., a drag, not a contributor, to group EBIT in this period.

## Killed options and why

- **The software claim as pitched (EUR 15m revenue, EUR 9m investment, on an August 2026 slide):** not killed as an option, but rejected as stated — it would consume 60% of the entire capital budget on the single least-evidenced lever in the plan, one that (per the base case above) is also the *smallest* of the three. Recommendation: fund a EUR 1.5–2m pilot (customer interviews + 2–3 paid pilots) and make the remaining ~EUR 7m conditional on it clearing an explicit bar (e.g., signed paid pilots covering a defined share of the EUR 3.3m base case) before the full spend is committed.

## Risks and what would change the answer

1. If the service-attach lever underperforms (independent-shop relationships prove sticky), it shrinks toward EUR 3.7m and the open gap widens to ~EUR 28m.
2. If the root cause of share loss in lab instruments (and, to a lesser extent, process sensors) is structural — product age, a discontinued line, channel coverage — rather than price, the price-reset lever could accelerate volume loss instead of adding margin; the staged test is designed to catch this before a full rollout.
3. If the software pilot validates strong paid demand at or above the EUR 15m claim, the total plan could reach ~EUR 164m — better, but still ~EUR 11m short of EUR 175m.
4. Margin is not the swing risk here: it clears the 10% floor by 2–3 points in every case tested.

## Next steps

| What | Who | By when |
|---|---|---|
| Launch service-contract conversion pilot in 2 regions, then roll out nationally | Service ops lead | pilot by Jan 2027, national by mid-2027 |
| Run a controlled +3% price test on a subset of lab-instrument SKUs/regions, measure volume response | Lab instruments BU lead | test live by Jan 2027, read-out by Q1 2027 |
| Commission 2–3 paid pilots and customer interviews for process analytics software before committing beyond the pilot budget | Head of strategy | read-out by Feb 2027, ahead of board paper |
| Open a root-cause workstream: why is Kirkby losing share in every served segment, especially process sensors (fastest-growing, highest-margin, and currently unsized as a lever) | Head of strategy + sales leads | findings by Dec 2026 |
| Prepare the March 2027 board paper naming the residual EUR 17–28m gap and requesting a decision: revisit the target/timeline, relax a constraint, or accept a partial plan | CEO | March 2027 board meeting |

## Assumptions

| # | Assumption | Value used | Basis | Would change the answer if |
|---|---|---|---|---|
| 1 | Service-contract conversion rate on the uncontracted installed base | 35% base (range 20–50%) | No comparable campaign cited; analogy to typical B2B service-attach pushes | A pilot shows materially different take-up |
| 2 | Lab-instrument price elasticity | +3% price → ~+2% net revenue (1pt assumed volume loss); range +2% to +5% price, net +1% to +3.5% | "No volume reason recorded" for the 7% gap suggests low elasticity, but the segment's share loss is a counter-signal urging caution | A controlled price test shows a bigger or smaller volume response |
| 3 | Software attach rate and price point | 10% of installed base by 2030 (range 5–15%) at an assumed EUR 1,000–2,000/yr subscription | Not in the data pack; installed base used as the only plausible go-to-market channel absent pilot evidence | Customer interviews/pilots establish real demand or willingness to pay |
| 4 | Software EBIT margin during ramp | −30% (range −20% to −50%) | Typical early-stage enterprise-software cost structure; not provided by Kirkby | Actual cost structure of the software unit becomes known |
| 5 | Momentum case = each segment's 2023–2025 CAGR continued to 2030 | As stated | Convention agreed with the CFO | CFO revises the convention |
| 6 | Process sensors carries no incremental lever in this base case | EUR 45.5m momentum only | No sensors-specific action data in the pack (pricing, competitive intel, capacity) was provided | A sensors BU lead or competitor data identifies a sizable, sizable action |

## Open questions

| Question | Why it matters | Who can answer | Effect on the answer |
|---|---|---|---|
| Why is Kirkby losing relative share in every segment (lab −1.2%/yr vs. market +3%; sensors +2.6%/yr vs. +6%; service flat vs. +4%)? | This is the real growth problem, bigger than the gap any lever above closes; root cause determines whether price, product, channel or service is the right fix | Sales/product leadership | Could surface the largest unsized lever in the plan |
| What would a process-analytics software pilot (customer interviews, 2–3 paid pilots, comparable B2B software launches) actually show? | The current EUR 15m claim has zero supporting evidence; this is the only way to size it honestly before committing EUR 9m | Head of strategy / product | Could move the software base case materially up or down from EUR 3.3m |
| What conversion rate is realistic for moving independent-shop customers onto Kirkby service contracts, and what do those customers need to switch? | Swings the largest and most certain lever by roughly ±EUR 2.8m | Service manager | Narrows the EUR 3.7–9.3m range |
| Is there a specific, named reason (spec gap, warranty, discontinued SKUs, distribution) for the unexplained 7% list-price gap? | Determines whether a price increase is safe or would compound the existing share loss | Product / sales leadership | Could kill or strengthen the price lever |
| What is driving process sensors' below-market growth despite the best margin and strongest market tailwind of the three segments — and is there a capacity constraint? | Could be the single largest lever in the whole plan; currently unsized for lack of data | Process sensors BU lead | Could close most of the remaining EUR 17–28m gap |
| Does the board have flexibility on the EUR 175m target, the 2030 date, the EUR 15m cap, or the no-acquisitions rule if organic levers can't close the gap? | Determines whether the right recommendation in March 2027 is "approve this partial plan and revisit the target" or "find a fourth lever first" | Board / CEO | Changes what "the answer" means, not just its size |

