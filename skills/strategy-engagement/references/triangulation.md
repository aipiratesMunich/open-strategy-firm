# Triangulation

## What it is

Checking a key claim or number with two or more approaches that could have failed independently: different data, different methods, different people. Agreement raises confidence; disagreement is a finding that needs an explanation. It answers: "Would we still believe this if our main source turned out to be wrong?"

## When to use

- Every number on the executive summary and every key-line claim ([Weak Evidence](weak-evidence.md), check 4).
- Market sizes, take-up rates, willingness to pay, cost savings: any estimate the recommendation depends on.
- Interview findings before they are generalised.
- Client-supplied figures that drive the answer.

## When NOT to use

- **Supporting details that cannot change the answer.** Triangulating every number wastes days. Apply it to the claims a [Sensitivity Analysis](sensitivity-analysis.md) shows to be decisive.
- **Audited or official figures used as stated** (reported revenue, statutory headcount). One primary source is enough; record it.
- **When only one honest source exists.** Manufacturing a second, weaker source to tick the box adds false comfort. State the single source, widen the range, and flag it.
- **Qualitative "why" questions answered well by interviews.** Why customers left can rest on interviews alone; how many left needs data.

## Step by step

1. **Pick the claims.** Input: draft storyline or model. Output: the five to ten claims or inputs the answer depends on most.
2. **Write each as a number or testable statement** with unit, scope and period.
3. **Choose at least two approaches from different families:**
   - Data: client systems, official statistics, transactions.
   - People: customer, expert or employee interviews ([Interview Guide](interview-guide.md)).
   - Benchmarks: comparable companies, markets or past projects (the outside view).
   - Method: top-down (from a total, cut down) versus bottom-up (from units, built up) ([Market Sizing](market-sizing.md)).
   - Revealed versus stated: what people paid or did versus what they say they would do.
4. **Check independence.** For each pair, ask: could both be wrong for the same reason? Do they trace back to the same original figure, the same interviewee, the same client estimate? Shared origin counts as one source.
5. **Compare.** Output: each approach's result side by side, on the same unit and scope.
6. **Interpret.** Within a reasonable band (the claim's own uncertainty): confidence rises, use a range covering the results. Outside it: explain the gap before using the number. The explanation is often the most useful insight.
7. **Record** the result and its strength label for the evidence review.

## Inputs needed

- The list of decisive claims.
- Access to at least two independent kinds of evidence per claim.

## Output produced

- Per claim: approaches used, results, independence check, gap explanation, final range and strength rating.

## Common mistakes

- **Counting citations, not origins.** Three press articles quoting one industry association are one source. A partner traces it back in a minute.
- **Same method twice.** Two bottom-up builds by the same analyst from the same assumptions are not triangulation.
- **Averaging away a gap.** A top-down of EUR 30m and a bottom-up of EUR 12m averaged to EUR 21m hides that one of them is wrong.
- **Triangulating with the client's belief.** Management's estimate is a hypothesis, not a second source ([Weak Evidence](weak-evidence.md), check 7).
- **Only confirming.** Looking for the second source that agrees, never for the one that would disagree.

## Worked example

*Fictional example. Company, figures and people are invented.*

Claim: "Alder Pumps customers will pay about EUR 1,000 per pump per year for a service contract with 48-hour response."

- **Interviews (stated):** 12 plant managers name EUR 900 to EUR 1,200.
- **Revealed spend:** plant managers report unplanned failures cost EUR 4,000 to EUR 40,000 each. Alder's own repair records show uncontracted pumps older than eight years fail about once every three years. Expected failure cost is therefore at least EUR 1,300 per pump per year, above the contract price.
- **Benchmark:** a distributor quotes competitor contracts at EUR 1,100 to EUR 1,300.
- **Independence check:** the distributor also arranged four of the twelve interviews. The benchmark and one third of the interviews share a channel and may share a bias. The team adds two interviews with customers sourced from Alder's own service records.
- **Result:** three approaches overlap around EUR 1,000 to EUR 1,200. Use EUR 1,000 as the base case, rated strong.

Take-up rate, triangulated the same way, does not converge: interviews suggest 55%, comparable offers reached 30% to 45% after three years. The team keeps 40% as base case with a 25% to 50% range and names take-up as the weakest input.

## Output template

```markdown
# Triangulation: <claim, with unit, scope, period>

| Approach | Family | Source (origin) | Result | Notes |
|---|---|---|---|---|
| 1 | data / people / benchmark / top-down / bottom-up / revealed | | | |
| 2 | | | | |
| 3 | | | | |

**Independence check:** <shared origins or shared biases found, and fix>
**Convergence:** converges within <band> / gap of <size>
**Gap explanation:** <why the approaches differ>
**Final value:** base <value>, range <low> to <high>
**Strength:** strong / medium / weak
```

## Related

- [Weak Evidence](weak-evidence.md), [Interview Guide](interview-guide.md), [Market Sizing](market-sizing.md), [Sensitivity Analysis](sensitivity-analysis.md), [Hypothesis-Driven Approach](hypothesis-driven-approach.md), [Synthesis](synthesis.md)
