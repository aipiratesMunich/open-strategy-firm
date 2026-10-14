# cp-03-minimal-saas on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (6/8 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Asks at most one round of grouped questions, then proceeds with flagged assumptions | yes | No clarifying questions were asked at all (0 rounds, within the 'at most one' bound), and the assistant explicitly flagged assumptions in a table ('Why I'm not at high confidence without more': competitor benchmark, value-to-customer read, new vs existing customers, segment sensitivity). |
| Computes price change ~22.5% and break-even customer loss with 1 - m/(m+p), arithmetic consistent with margin used | yes | 'Price increase: p = (109−89)/89 = 22.5%' and 'Break-even volume loss ... 1 − m/(m+p) = 1 − 0.85/1.075 = ~21%' — consistent with m=0.85. |
| Flags gross margin is not contribution margin and states which value used and why | yes | 'Contribution margin: m = 85% (using gross margin as a stand-in for contribution margin — assumption, see below)' |
| Translates break-even into churn terms or explains why loss and churn must be modelled separately | yes | 'break-even churn = current churn / (1 − break-even loss) = 0.02 / 0.79 = ~2.53%/month ... the increase pays for itself unless monthly churn rises from 2% to above ~2.53%' |
| Names structure options as a question to test rather than only a single level change | yes | Recommends 'grandfather a 2–4 week legacy-price window or staging the increase (e.g., €89 → €99 → €109)' and flags 'A uniform 22% hike for everyone is probably not optimal even if it's safe on average' (segmentation). |
| Gives a provisional answer with confidence low or medium and what would change it | yes | 'Confidence: medium — the breakeven math is solid and favorable, but it's a margin-affordability check, not a value-based pricing case. Would raise to high with a competitor benchmark and a churn reaction from a staged/segmented rollout.' |
| Names revealed-behaviour data that would settle willingness to pay and treats any survey as a range | NO | Only suggests 'get a quick read on competitor pricing and what clinics actually value most' and 'watch monthly churn for 2-3 months post-increase' — no mention of win/loss on recent deals, stated churn reasons, or response to past price changes, and no treatment of any survey/read as a range of valu |
| Must not invent competitor prices or industry benchmarks as facts | NO | 'churn reactions to price increases in that kind of product are usually much smaller than that' is stated as a general industry fact with no source or data provided. |

## Transcript

## Turn 1

**User:** We're Vetrona, practice software for small vet clinics, 89 euros a month per clinic. thinking of going to 109. churn is maybe 2% a month. gross margin 85%. good idea?

## Answer: Yes — the math gives you a wide safety margin, raise the price

**Bottom line:** At 85% gross margin, a move from €89 to €109 (+22.5%) only needs to stay profit-positive versus a **break-even monthly churn of ~2.53%** (vs. your current ~2%). You have roughly **+0.5 percentage points (≈26% relative) of churn tolerance** before the increase stops paying for itself. That's a comfortable cushion for a B2B vertical SaaS with switching costs (data migration, staff retraining) — churn reactions to price increases in that kind of product are usually much smaller than that.

### The arithmetic (so you can check it in a minute)

- Price increase: p = (109−89)/89 = **22.5%**
- Contribution margin: m = 85% (using gross margin as a stand-in for contribution margin — **assumption**, see below)
- Break-even volume loss for a price increase: `1 − m/(m+p)` = 1 − 0.85/1.075 = **~21%** (you could lose a one-off 21% of the affected customers and still be no worse off on profit)
- Translating a one-off volume-loss tolerance into a churn tolerance (steady-state base scales as 1/churn): break-even churn = current churn / (1 − break-even loss) = 0.02 / 0.79 = **~2.53%/month**
- So the increase pays for itself unless monthly churn rises from 2% to above ~2.53% and stays there.

Per customer: variable cost stays fixed in euros (~€13.35/customer, implied by 85% margin on €89), so the extra €20/month from the price rise is almost pure incremental contribution — that's why the tolerance is so wide.

### Why I'm not at "high confidence" without more

| Gap | Why it matters | Effect on the answer |
|---|---|---|
| No competitor price benchmark | If you're already priced above comparable vet-practice software, 22% more could overshoot willingness to pay badly | Could flip from "safe" to "risky" |
| No value-to-customer read | Price should be anchored on what the software saves/earns the clinic (staff time, no-show reduction, billing), not just on margin headroom | Right now this is a cost/margin justification, not a value one — fine as a sanity check, not sufficient as the full case |
| New vs. existing customers | Raising list price for new sign-ups is nearly risk-free; raising it on your existing base is where churn risk actually lives | Recommend splitting the rollout |
| One-off announcement shock vs. steady-state drift | The break-even math above is a steady-state view. A price-increase announcement can trigger a short-term cancellation spike concentrated among your most price-sensitive clinics (adverse selection), which looks different from a smooth +0.5pp churn | Worth a grandfather period / staged increase to de-risk |
| Segment sensitivity | Solo-vet vs. multi-vet clinics likely differ in price sensitivity | A uniform 22% hike for everyone is probably not optimal even if it's safe on average |

### Recommendation

1. Apply **€109 to all new customers now** — no churn risk, immediate margin benefit.
2. For the existing base, **give 30–60 days' notice** (standard practice, also likely required by your ToS/local consumer law — check), and consider **grandfathering a 2–4 week legacy-price window** or staging the increase (e.g., €89 → €99 → €109) to blunt the cancellation-spike risk.
3. Watch monthly churn for 2–3 months post-increase; **2.53% is your kill number** — if churn clearly trends above that and stays there, the increase is destroying value and you should pull back or re-segment.
4. Before going further than this single move, get a quick read on competitor pricing and what clinics actually value most (time saved, fewer no-shows, billing accuracy) — that tells you whether 22% is leaving money on the table or pushing your luck, rather than just "is it affordable."

**Confidence: medium** — the breakeven math is solid and favorable, but it's a margin-affordability check, not a value-based pricing case. Would raise to high with a competitor benchmark and a churn reaction from a staged/segmented rollout.


## Files in work dir after run


