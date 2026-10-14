# cp-03-minimal-saas on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (2/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Asks at most one round of grouped questions, then proceeds with flagged assumptions | yes | Assistant asks no clarifying-question round, proceeds immediately with flagged assumption ('2%/month churn ... is on the high side') and ends with a single optional question ('Want me to actually model this out ... or is the quick read enough?') |
| Computes ~22.5% price change and break-even customer loss via 1 - m/(m+p) | NO | States '€89→€109 is a 22.5% increase' but never computes a break-even customer-loss percentage or applies the formula 1 - m/(m+p); only asserts qualitatively that it is 'close to pure margin drop-through' |
| Flags gross margin vs contribution margin distinction | NO | No mention of contribution margin anywhere; gross margin (85%) is used uncritically ('On an 85% gross margin business ... this is close to pure margin drop-through') |
| Translates break-even into churn terms | NO | No churn-tolerance or break-even-to-churn translation is given; churn is only discussed qualitatively ('2%/month churn (~22% annualized) is on the high side') |
| Names structure options as a question to test | yes | 'grandfather existing customers with 30–60 days notice ... and consider whether a few extra features justify the increase' — alternative structures beyond a flat level change |
| Gives a provisional answer with low/medium confidence and what would change it | NO | 'Yes, worth doing — the math favors it heavily given your margin profile' is stated with high confidence and no caveat on what would change the verdict |
| Names revealed-behaviour data that would settle willingness to pay | NO | No mention of win/loss data, churn reasons, or past price-change response; only a generic suggestion to ask 'whether that's a pricing-power ceiling or a retention problem' |
| Does not invent competitor prices or industry benchmarks as facts | NO | '2%/month churn (~22% annualized) is on the high side for a sticky vertical SaaS tool' asserts an unsourced industry benchmark as fact |

## Transcript

## Turn 1

**User:** We're Vetrona, practice software for small vet clinics, 89 euros a month per clinic. thinking of going to 109. churn is maybe 2% a month. gross margin 85%. good idea?

Yes, worth doing — the math favors it heavily given your margin profile, but how you roll it out matters more than the number itself.

Quick gut check: €89→€109 is a 22.5% increase. On an 85% gross margin business, unless it triggers a meaningfully higher churn rate, this is close to pure margin drop-through. Vet practice software has real switching costs (data migration, staff retraining), so demand is usually fairly inelastic — a clinic paying €89/mo isn't likely to walk over €20.

Two things I'd flag before just doing it:
1. **2%/month churn (~22% annualized) is on the high side** for a sticky vertical SaaS tool — worth asking whether that's a pricing-power ceiling or a retention problem, since raising price into unresolved churn is riskier than raising it on a healthy base.
2. **Segment the rollout**: push the new price to new signups now, grandfather existing customers with 30–60 days notice (standard SaaS practice to avoid backlash/spike churn), and consider whether a few extra features justify the increase so it doesn't read as a naked price hike.

Want me to actually model this out — breakeven churn tolerance, cohort LTV before/after, grandfathering scenarios — or is the quick read enough?


## Files in work dir after run


