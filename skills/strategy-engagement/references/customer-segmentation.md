# Customer Segmentation

## What it is

A split of customers into groups that need different things and therefore respond differently to the client's offer, price or channel. Good segments are built on needs and behaviour, then described with firmographics or demographics so sales can find them. It answers "which customers should we serve, with what, and how many are there?"

## When to use

- One offer or price is applied to all customers and results vary widely.
- A new offer needs a target group and a realistic take-up per group.
- Market sizing needs take-up rates that differ by customer type.

## When NOT to use

- **The customer base is small and known by name.** Thirty key accounts need an account plan each, not segments.
- **No data on needs or behaviour, and no time for interviews.** A demographic split alone will look tidy and predict nothing. Say so, run five to ten interviews first ([Interview Guide](interview-guide.md)), or use the existing sales categories as a placeholder and flag it.
- **The decision is the same for every segment.** If all segments get the same offer and price, segmentation adds slides, not insight.
- **The question is why customers buy at all.** Start with [Jobs to Be Done](jobs-to-be-done.md), then segment by job.

## Step by step

1. **State the decision** the segmentation serves: target choice, offer design, pricing, channel. Output: one sentence.
2. **List candidate variables.**
   - *Needs and behaviour:* the job the customer hires the product for, cost of failure, buying process, switching behaviour, usage intensity.
   - *Descriptors:* industry, size, region, age of equipment, ownership.
   Needs variables form the segments; descriptors make them findable. Output: variable list.
3. **Collect evidence.** Ask the user for CRM, sales and service data. Add interviews focused on past behaviour, not opinions about the future. Output: data set per customer, gaps flagged.
4. **Form segments.** Start from two or three needs variables that the decision depends on. Combine into four to six segments. Use clustering only if the data supports it; a judgement-based grid that survives the test below is fine. Output: segment definitions.
5. **Size and describe each segment** with counts, revenue and the descriptors sales can use. Output: segment table.
6. **Run the actionability test.** Each segment must be:
   - *Distinct:* responds differently to the offer or price.
   - *Identifiable:* sales can tell from available data which segment a customer is in.
   - *Sizeable:* worth a separate approach.
   - *Reachable:* a channel exists to serve it.
   - *Stable:* will still exist in the decision horizon.
   Drop or merge segments that fail. Output: test table.
7. **Prioritise** by size, expected response and fit with the client's capabilities. Output: target segments with offer and expected take-up.

## Inputs needed

- The decision the segmentation serves.
- Customer data: CRM, sales history, service records (user-supplied).
- Interview notes or survey data on needs and behaviour.

## Output produced

- Segment definitions, sizing, actionability test, priority and expected response per segment.

## Common mistakes

- **Demographic segments presented as insight.** "Large, medium, small customers" predicts little about who buys a service contract.
- **Too many segments.** Twelve segments cannot each get a different offer. Four to six is usually the limit of what sales can act on.
- **Segments sales cannot find.** A needs-based segment with no descriptor stays on the slide.
- **Opinions as evidence.** "Would you buy this?" answers overstate demand. Ask what customers did the last time the problem occurred.
- **Segments that do not sum to the total.** Every customer belongs to exactly one segment ([MECE](mece.md)).

## Worked example

*Fictional example. Company, figures and people are invented.*

Decision: which Alder Pumps customers to target first with a service contract (48-hour response, about EUR 1,000 per pump per year). Population: 31,200 pumps older than eight years without contract.

Needs variables from 12 plant-manager interviews and service records: cost of a failure (reported from EUR 4,000 to EUR 40,000) and in-house maintenance capacity. Descriptor: industry, from the ERP.

| Segment | Need | Share of pumps | Expected take-up |
|---|---|---|---|
| A. Uptime-critical, thin maintenance team (food, pharma) | Fast response, no own technicians | 38% | 65% |
| B. Uptime-critical, strong in-house team (chemicals) | Parts and remote diagnosis | 22% | 25% |
| C. Low failure cost (general industry) | Lowest price, repair on demand | 27% | 20% |
| D. Public utilities | Tendered framework contracts | 13% | 30% |

Weighted take-up: 0.38 × 65% + 0.22 × 25% + 0.27 × 20% + 0.13 × 30% = 39.5%, consistent with the 40% base case. Actionability: all four are identifiable from industry and service history. D fails "reachable" for the standard offer because it requires tenders; it gets a separate bid approach. Priority: A first, B with a lighter remote-only contract.

## Output template

```markdown
# Segmentation: <population> for <decision>

**Answer:** Target <segments> first with <offer>; expected take-up <x%>.

## Segments
| Segment | Needs / behaviour | Descriptors (how sales finds them) | Count | Revenue or units | Expected response | Evidence |
|---|---|---|---|---|---|---|

## Actionability test
| Segment | Distinct | Identifiable | Sizeable | Reachable | Stable | Keep / merge / drop |
|---|---|---|---|---|---|---|

## Priority
1. <segment>: <offer, channel, why>

**Assumptions flagged:**
-
```

## Related

- [Jobs to Be Done](jobs-to-be-done.md), [Market Sizing](market-sizing.md), [Pricing Analysis](pricing-analysis.md), [Interview Guide](interview-guide.md), [MECE](mece.md), [Weak Evidence](weak-evidence.md)
