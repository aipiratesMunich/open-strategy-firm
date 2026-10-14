# cp-03-minimal-saas on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Asks at most one round of grouped questions, then proceeds with flagged assumptions | yes | Gives an immediate answer with assumptions (85% margin as proxy) and lists a single grouped table of open questions ('Before you pull the trigger, I'd want:') rather than blocking with multiple rounds |
| Computes price change ~22.5% and break-even loss via 1 - m/(m+p) with consistent arithmetic | yes | '(109 − 89) / 89 = 22.5%' and '1 − 0.85/(0.85+0.225) = ~21%' which is arithmetically consistent (0.85/1.075≈0.79, 1-0.79≈0.21) |
| Flags gross margin vs contribution margin distinction and states which value used and why | yes | 'Using your 85% gross margin as a stand-in for contribution margin' and later asks 'Is 85% gross margin close to contribution margin...if true contribution margin is lower, say 70%, break-even churn drops to ~2.3%' |
| Translates break-even into churn terms or explains why loss and churn must be modeled separately | yes | 'break-even churn = current churn / (1 − break-even loss) = 0.02/(1−0.21) = ~2.5%/month (vs. today's 2%)' |
| Names structure options as a question to test (tiers by size, grandfathering, annual prepay) rather than only a single level change | NO | Only grandfathering vs. blanket increase is raised ('Grandfather existing customers or raise for everyone?'); no mention of tiering by clinic size or annual prepay as alternative structures to test |
| Gives a provisional answer with confidence low/medium and what would change it | yes | 'Confidence: medium. The math is solid; the uncertainty is behavioral (will churn actually stay under 2.5%) and in two unverified inputs below.' |
| Names revealed-behaviour data that would settle willingness to pay and treats survey as a range | NO | No mention of win/loss on recent deals, churn reasons analysis, or response to past price changes; only competitor price checks and margin verification are suggested |
| Does not invent competitor prices or industry benchmarks as facts | yes | Names competitor companies (Provet, eVetPractice) only as who to ask, without stating invented price figures or benchmark numbers as fact |

## Transcript

## Turn 1

**User:** We're Vetrona, practice software for small vet clinics, 89 euros a month per clinic. thinking of going to 109. churn is maybe 2% a month. gross margin 85%. good idea?

**Short answer: yes, raising €89 → €109 (+22.5%) is very likely a good move, but do it by cohort (new customers first, flagged churn-watch on existing) rather than blanket overnight.**

**The arithmetic (so you can check it in one minute):**

- Price increase: (109 − 89) / 89 = **22.5%**
- Using your 85% gross margin as a stand-in for contribution margin, the one-time break-even volume loss for a price increase of this size is:
  1 − m/(m+p) = 1 − 0.85/(0.85+0.225) = **~21%**
  → you could lose up to ~1 in 5 customers immediately and still come out ahead on profit.
- Translating that into your subscription churn: steady-state customer base scales with 1/churn, so break-even churn = current churn / (1 − break-even loss) = 0.02 / (1−0.21) = **~2.5%/month** (vs. today's 2%).

**So-what:** the increase only destroys value if monthly churn rises from 2% → above ~2.5% (i.e., churn has to get ~26% worse, relative) because of the price change. Given:
- the absolute jump is small (€20/month — less than what most clinics bill in a single appointment),
- practice management software has high switching costs (data migration, staff retraining, workflow lock-in),

...a churn jump of that size seems unlikely, which is why I lean yes.

**Confidence: medium.** The math is solid; the uncertainty is behavioral (will churn actually stay under 2.5%) and in two unverified inputs below.

**Before you pull the trigger, I'd want:**

| Question | Why it matters | Who can answer |
|---|---|---|
| What do competitors (Provet, eVetPractice, local players) charge for comparable clinics? | If €109 pushes you above the market without a value/feature reason, churn risk is higher than the model assumes | Sales/competitive intel |
| Is 85% *gross* margin close to *contribution* margin, or is there meaningful variable cost (support, payment processing, onboarding) per customer? | The break-even math needs contribution margin, not gross margin — if true contribution margin is lower, say 70%, break-even churn drops to ~2.3%, still fine but a tighter margin for error | Finance |
| Grandfather existing customers or raise for everyone? | Raising only for new sign-ups is near-zero risk; raising on the full existing base is where churn reaction actually gets tested | You / go-to-market decision |

**Practical rollout, not just "go/no-go":** apply €109 to new signups immediately (no downside), and test the increase on a slice of the existing base (e.g., month-to-month renewals in one segment) with 30–60 days' notice and a short note on what's improved, while tracking monthly churn weekly for the first quarter. If churn stays under ~2.5%, roll it out to the full base.


## Files in work dir after run


