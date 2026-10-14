# cp-03-minimal-saas on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (2/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Must: asks at most one round of grouped questions, then proceeds with flagged assumptions. | NO | The assistant asked zero clarifying questions and gave no explicit flagged assumptions (e.g., number of clinics, segments, what's included, last price change) before answering directly with 'Worth doing, and the math gives you a lot of room.' |
| Must: computes the price change as about 22.5% and a break-even customer loss with the formula 1 - m / (m + p). | NO | Price change of 22.5% is stated correctly ('Price is going up 22.5% (89→109)'), but break-even is computed via a different method entirely: 'churn would need to rise from 2.0%/mo to 2.45%/mo' using an LTV proportionality argument, not the required 1 - m/(m+p) formula. |
| Must: flags that gross margin is not contribution margin and states which value it uses and why. | NO | The response uses the 85% margin figure directly in its LTV formula ('LTV ≈ (price × margin%) / monthly churn') without ever noting that gross margin differs from contribution margin or justifying its use. |
| Must: translates the break-even into churn terms or explains why the one-off loss and churn rate must be modelled separately. | yes | 'Risk to manage isn't steady-state churn, it's the one-time shock... churn would need to rise from 2.0%/mo to 2.45%/mo' explicitly separates steady-state churn from a one-time shock and gives a churn-rate translation. |
| Must: names structure options as a question to test rather than only a single level change. | NO | Grandfathering and phased rollout are offered as mitigation actions ('Grandfather existing customers... Apply the new price to new signups first and watch churn/conversion'), but these are presented as recommended tactics, not framed as hypotheses/questions to test; segmentation by clinic size is on |
| Must: gives a provisional answer with confidence low or medium and what would change it. | NO | The response opens with a confident 'Worth doing, and the math gives you a lot of room' and never states a low/medium confidence level or what evidence would change the recommendation. |
| Must: names the revealed-behaviour data that would settle willingness to pay and treats any survey as a range. | NO | No mention anywhere of win/loss data, churn reasons, response to past price changes, or survey ranges. |
| Must not: invent competitor prices or industry benchmarks as facts. | yes | The assistant makes general qualitative claims ('Practice management software has high switching costs... which usually means low price elasticity') but does not cite specific invented competitor prices or numeric industry benchmarks as facts. |

## Transcript

## Turn 1

**User:** We're Vetrona, practice software for small vet clinics, 89 euros a month per clinic. thinking of going to 109. churn is maybe 2% a month. gross margin 85%. good idea?

Worth doing, and the math gives you a lot of room.

**Breakeven churn:** Since LTV ≈ (price × margin%) / monthly churn, and margin% is unchanged, LTV stays flat only if churn rises in the same proportion as price. Price is going up 22.5% (89→109), so churn would need to rise from 2.0%/mo to **2.45%/mo** before this becomes value-destructive. That's a fairly generous cushion — churn has to jump materially, not just wobble.

**Why it's probably safe:** Practice management software has high switching costs — migrating patient/client records and retraining clinic staff is a real pain, which usually means low price elasticity. A €20/month increase (about €240/year) is also small relative to a vet clinic's total opex, so it's unlikely to be the thing that triggers a switch.

**Risk to manage isn't steady-state churn, it's the one-time shock:** A sudden price hike on existing customers can cause a short burst of cancellations/complaints above your normal 2% baseline, even if long-run elasticity is low. Mitigate with:
- Grandfather existing customers for a while, or give 30–60 days notice
- Apply the new price to new signups first and watch churn/conversion before rolling to the base
- Pair the increase with a visible value add (new feature, support tier) so it doesn't feel like a naked hike

If you want, I can run this as a fuller pricing analysis (segment by clinic size, model the one-time shock separately from steady-state churn, sanity-check against comparable vertical SaaS pricing).


## Files in work dir after run


