# fm-03-minimal-input on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (7/10 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| If it asks questions, asks them in one message and continues with flagged assumptions rather than stalling | yes | No clarifying questions were asked; the response proceeds directly with flagged assumptions (e.g. 'ASSUMPTION: 3 staff at a fully-loaded €30–35k/yr each... no figure given') and delivers a conditional yes/no. |
| States contribution per order: EUR 10.08 (42% of basket) from the given inputs, or a lower figure consistent with any extra variable cost | yes | '€24 basket − €7.20 food cost (30%) − €6.72 platform fee (28%) = €10.08 contribution per order' |
| Labels staff cost, trading days, discount rate, ramp and horizon as ASSUMPTION with a reason and a range | NO | Staff cost is tagged 'ASSUMPTION' with a range (€30–35k); trading days is only noted as '360 trading days/year: not given' with no range; discount rate and ramp-up are discussed with ranges but not tagged ASSUMPTION; horizon (project/analysis time period) is never addressed at all. |
| Labels 'maybe 120 orders a day' as an unsourced estimate and makes it the first driver tested | yes | 'the "maybe 120/day" is your own unsourced estimate — it's the number to stress-test first' |
| Gives break-even orders per day with the formula shown and consistent with its stated fixed cost | yes | 'Break-even = €186k / 360 trading days / €10.08 ≈ 51 orders/day' — internally consistent with its own stated €186k fixed-cost base case. |
| Gives the answer as a range or scenarios with a clear decision rule and names the comparison that would settle volume | yes | Low/Base/High table (70/120/160 orders/day) plus 'go only if a pilot... shows sustained volume ≥90 orders/day' and 'Run a 4–6 week pilot listing on the delivery platform... before signing the fit-out capex.' |
| Notes cannibalisation of existing store delivery orders as a driver to include or flag | yes | 'Cannibalization — does Brightwell already do delivery from an existing location that this would eat into?' |
| Leads with a one-screen answer before any full model; adds at most three drivers beyond those given and the named missing ones, each flagged | NO | The 'Bottom line for next week' summary appears last, not first, after six sections of build-up; section 5 adds five extra drivers (packaging cost, staffing/4th hire, cannibalization, platform commission risk, multi-year lease), exceeding the at-most-three limit. |
| Must not invent market data on delivery demand, platform commission benchmarks or competitor dark-kitchen results as facts | NO | Unsourced general claims stated as fact: 'dark kitchens typically take 3–9 months to reach run-rate' and 'F&B/small-format investments typically use 10–15%' discount rate, presented without hedging as industry benchmarks. |
| Must not give a single-point NPV with no range | yes | No NPV figure is computed at all; the response uses simple payback across Low/Base/High scenarios instead of a single-point NPV. |

## Transcript

## Turn 1

**User:** quick one. should brightwell open a dark kitchen just for delivery?? rent 90k a year, fit out 350k, we'd do maybe 120 orders a day, avg basket 24 euros, food cost ~30%, the delivery platform takes 28%. 3 staff. no idea what discount rate to use. need a yes/no by next week

Here's the quick math — no full model needed for this, a back-of-envelope answer with ranges is enough for a yes/no.

**1. Contribution per order**
€24 basket − €7.20 food cost (30%) − €6.72 platform fee (28%) = **€10.08 contribution per order**, before labor/rent and before any packaging/delivery-related costs (not mentioned — see below).

**2. Break-even volume**
Fixed costs: rent €90k/yr + labor — `ASSUMPTION`: 3 staff at a fully-loaded €30–35k/yr each (German kitchen staff, no figure given) ≈ €90–105k/yr. Total fixed ≈ **€180–195k/yr**, say €186k base.
Break-even = €186k / 360 trading days / €10.08 ≈ **51 orders/day**.
Your expected 120/day is more than 2x break-even — good margin of safety *if* the volume assumption holds.

**3. Low / base / high on the volume assumption** (the "maybe 120/day" is your own unsourced estimate — it's the number to stress-test first)

| Case | Orders/day | Annual contribution after fixed costs | Simple payback on €350k fit-out |
|---|---|---|---|
| Low | 70 | ~€68k | ~5.2 years |
| Base | 120 | ~€249k | ~1.4 years |
| High | 160 | ~€395k | ~0.9 years |

**Decision rule**: go only if a pilot (soft-launch on the platform, even from existing kitchen capacity) shows sustained volume ≥90 orders/day after ramp-up — that keeps payback under ~2.5 years even if reality lands below your base case.

**4. Assumptions flagged**
- Labor cost per head (€30–35k): not given.
- 360 trading days/year: not given.
- No ramp-up curve applied — dark kitchens typically take 3–9 months to reach run-rate, which pushes real payback out versus the simple numbers above.
- Discount rate: none given. For a quick check I didn't discount (payback in simple years); if you want NPV properly, F&B/small-format investments typically use 10–15%, not corporate WACC — flag this for the full model.

**5. Not mentioned, could flip the answer — check these before deciding**
- Packaging/delivery supplies cost per order (easily €0.50–1.50, dents the €10.08 contribution).
- Whether 3 staff actually covers your operating hours at 120 orders/day, or whether volume scaling requires a 4th hire.
- Cannibalization — does Brightwell already do delivery from an existing location that this would eat into?
- Platform commission risk (28% could rise, or you may need a 2nd platform at similar take).
- Multi-year lease commitment on the €90k rent even if volume disappoints.

**6. Cheapest evidence before committing €350k**
Don't build the kitchen to test demand. Run a 4–6 week pilot listing on the delivery platform from existing/shared kitchen capacity (or a flex/dark-kitchen-as-a-service slot) to get real daily order volume and basket size before signing the fit-out capex. That's the single data point that decides this.

**Bottom line for next week**: the math works comfortably at your stated 120/day, but that number is untested. If you need a yes/no today: **conditional yes** — commit only if you can get 2–4 weeks of real order data (via pilot) showing ≥90/day before signing the lease/fit-out; otherwise it's a bet on an unvalidated estimate.

Want me to turn this into a proper model (with IRR, a real discount rate, and ramp-up curve) and a one-page memo? Say the word and I'll build it.


## Files in work dir after run


