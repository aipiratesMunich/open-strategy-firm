# cp-03: Minimal input, subscription price change

## Prompt

> We're Vetrona, practice software for small vet clinics, 89 euros a month per clinic. thinking of going to 109. churn is maybe 2% a month. gross margin 85%. good idea?

*Fictional company. All figures invented for evaluation.*

## What this case tests

Robustness. One line of data, a subscription model where volume loss shows up as churn over time, gross margin given instead of contribution margin, no segments, no competitor prices. The skill should ask a short set of answerable questions or proceed with flagged assumptions, compute the break-even, translate it into churn terms, and not invent competitor prices.

## Reference values

- Price change: 20 / 89 = about +22.5%.
- Break-even customer loss with m = 0.85 (gross margin used as a proxy for contribution margin): 1 - 0.85 / (0.85 + 0.225) = about 20.9%.
- With m = 0.70: 1 - 0.70 / 0.925 = about 24.3%. A lower contribution margin tolerates a larger loss for a price increase. Accept any m the run states, if the formula and arithmetic are consistent.
- Annual revenue per clinic: EUR 1,068 at 89, EUR 1,308 at 109.

## Pass criteria

- Must: asks at most one round of grouped questions (e.g. number of clinics, segments by clinic size, competitor or alternative prices the user knows, last price change and churn after it, what is included at each price), then proceeds with flagged assumptions.
- Must: computes the price change as about 22.5% and a break-even customer loss with the formula 1 - m / (m + p), with the arithmetic consistent with the margin it uses.
- Must: flags that gross margin is not contribution margin and states which value it uses and why.
- Must: translates the break-even into churn terms (e.g. how much extra churn over 12 months the increase can absorb against the 2% monthly baseline) or explains why the one-off loss and the churn rate must be modelled separately.
- Must: names structure options as a question to test (e.g. tiers by clinic size, grandfathering existing clinics, annual prepay) rather than only a single level change.
- Must: gives a provisional answer with confidence low or medium and what would change it.
- Must: names the revealed-behaviour data that would settle willingness to pay (e.g. win/loss on recent deals, churn reasons, response to past changes) and treats any survey as a range.
- Must not: invent competitor prices or industry benchmarks (churn, typical price-increase size, conversion) as facts.
