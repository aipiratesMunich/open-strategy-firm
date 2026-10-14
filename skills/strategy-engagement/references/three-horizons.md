# Three Horizons

## What it is

A way to sort growth initiatives by maturity: horizon 1 defends and extends the core business, horizon 2 builds emerging businesses that already have customers, horizon 3 creates options that may become businesses later. Each horizon needs its own goals, metrics and funding logic, and all three run at once. It informs how to split money and management attention across a growth portfolio. It cannot tell you which initiatives are worth funding or how large they become.

## When to use

- A growth plan that mixes core improvements with new businesses, and the board needs to see the balance.
- A core business that still earns well but is flat, with nothing behind it.
- Setting different targets and governance for new ventures than for the core.

## When NOT to use

- **Choosing between options.** The horizons classify, they do not rank. Use [Business Case](business-case.md) and [Sensitivity Analysis](sensitivity-analysis.md).
- **Turnarounds.** When the core is losing money, horizon 3 spending is a distraction. Fix the core with [Profit Tree](profit-tree.md) and [Cost Benchmarking](cost-benchmarking.md).
- **Allocation across existing mature units.** Use [Growth-Share Matrix](growth-share-matrix.md).
- **As a timeline.** Horizons describe maturity, not years. Treating them as "year 1, 3, 5" produces wrong targets.

## Step by step

1. **List all growth initiatives.** Input: strategy documents, budget, project lists. Output: one row per initiative with spend and expected revenue.
2. **Assign a horizon by maturity.** Test: H1 has a proven model and existing customers; H2 has paying customers and an unproven scale model; H3 has neither yet. Output: horizon per initiative.
3. **Set metrics per horizon.** H1: profit, cash, margin. H2: revenue growth, customer acquisition, unit economics. H3: milestones and option value, with a stop rule. Output: metric set per initiative.
4. **Check the balance.** Input: spend and expected contribution per horizon. Output: whether H2 can replace H1 growth when the core flattens, and whether H3 feeds H2.
5. **Set funding and governance.** Output: budget per horizon, decision owner and review cycle; stop rules for H3.

## Inputs needed

- Initiative list with spend, revenue plans and status.
- Core business forecast.
- Capital limits and the board's risk appetite.

## Output produced

- Initiative portfolio by horizon with metrics and funding.
- A statement whether the portfolio closes the growth gap over time.

## Common mistakes

- **Everything is H3.** Labelling weak core projects as "future bets" to shield them from scrutiny.
- **Same metrics everywhere.** Judging an H3 pilot on margin kills it; judging an H2 business only on milestones lets it drift.
- **No stop rules.** H3 options without kill criteria become permanent cost.
- **Empty H2.** Many bets and a core, with nothing ready to scale, means a growth gap in a few years.

## Worked example

*Fictional example. Company, figures and people are invented.*

Alder Pumps, revenue EUR 180m flat, target EUR 200m by 2030, capital limit EUR 20m.

| Horizon | Initiative | Spend | 2030 revenue | Metric | Stop rule |
|---|---|---|---|---|---|
| H1 | 4% list-price increase | Minimal | About EUR 7m | Price realisation, volume loss | Volume loss above 3% |
| H2 | Service contracts | EUR 6m | About EUR 12.5m | Contracts signed, response time, contract margin | Take-up below 25% after two years |
| H3 | Remote condition monitoring pilot | EUR 1.5m | None planned | Pilot customers, failure prediction accuracy | No paying pilot by end of 2028 |

Total spend EUR 7.5m, within the EUR 20m limit. H1 and H2 give about EUR 19.5m of the EUR 20m gap. The board sees that the target is met only if service scales as planned, with almost no cushion, and that H3 cannot be counted on by 2030.

## Output template

```markdown
# Growth portfolio by horizon: <company>

| Horizon | Initiative | Maturity evidence | Spend | Revenue by <year> | Metrics | Stop rule | Owner |
|---|---|---|---|---|---|---|---|
| H1 | | | | | | | |
| H2 | | | | | | | |
| H3 | | | | | | | |

**Spend by horizon:** H1 <x>, H2 <y>, H3 <z> (limit <amount>)
**Gap closed by <year>:** <amount> of <gap>; open: <amount>
```

## Related

- [Ansoff Matrix](ansoff-matrix.md), [Growth-Share Matrix](growth-share-matrix.md), [Growth Strategy](growth-strategy.md), [Business Case](business-case.md), [Seven-S Framework](seven-s.md)
