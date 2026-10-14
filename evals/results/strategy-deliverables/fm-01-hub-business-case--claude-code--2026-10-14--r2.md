# fm-01-hub-business-case on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the question, outputs, and decision threshold before building | yes | Deck slide 1: 'Should Kestrel invest in a cross-dock hub in the south region?' with speaker note 'Decision rule from the CFO: approve if NPV at the 9% hurdle rate is above zero...'; opening answer gives NPV, IRR, payback up front. |
| Separates inputs, calculations and outputs; no number typed inside formula other than 0/1 or documented unit conversion | yes | spec.json formulas e.g. 'parcels_routed = parcels_full_run_rate * ramp', 'capex = -investment * pick(t,1,0,0,0,0,0,0,0,0)' reference named inputs only, literals limited to 0/1; inputs.csv, calc.csv, outputs.csv, checks.csv, sensitivity.csv kept separate. |
| Base NPV within EUR 3.1m-3.4m and payback in 2030/year 4 | yes | outputs.csv: npv base = 3.2302410504; payback_period base = 2030. |
| Tornado ranking with saving per parcel first, parcels routed second | yes | sensitivity.csv: rank 1 saving_per_parcel (swing 6.46), rank 2 parcels_full_run_rate (swing 5.12). |
| Break-even values given for saving per parcel (~0.42-0.43) and parcels (~3.8-3.9m), both flagged inside range | yes | sensitivity.csv: saving_per_parcel break_even=0.4249869616 'yes'; parcels_full_run_rate break_even=3.8635178329 'yes'. |
| Because break-even lies inside range, it's in the headline/decided-by line, not just an appendix | yes | Slide 2 headline: 'Approve the EUR 6m south hub: base-case NPV is EUR 3.2m with payback by 2030, but the answer rests on two drivers that break even close to their low-end range'. |
| Down case is a coherent story (not a uniform cut) and reports negative NPV | yes | spec.json scenario_stories: 'down': 'south volumes land at the bottom of the quoted flow range and the lease/staffing cost comes in at the top of its range'; outputs.csv npv down = -1.8409834649 (and competitor_response, an even closer match to the fewer-parcels/lower-saving/higher-investment story, |
| A checks block and two outputs recomputed by hand with both numbers recorded | NO | checks.csv/README 'Checks' only contain structural consistency checks (parcels_within_capacity, ramp_not_negative, ramp_not_above_one, net_cash_flow_ties_to_parts) — no independent hand recomputation of NPV/payback with both the hand value and model value recorded anywhere in the deliverables; the o |
| Lists the 60% ramp as a flagged assumption | yes | README 'Flags: Drivers flagged as assumptions (no source or source starts with 'assumption'): ramp_2027'; deck appendix footnote '*No range was quoted for the 2027 ramp...' |
| 'What the deck should say' sentences carrying the model version | yes | Every slide footer: 'Source: Kestrel south hub business case model v01...'; slide 1 note: 'Model version v01.' |
| Must not present NPV without range or scenarios | yes | Headline and summary always pair base NPV 3.2m with the -1.8m/+8.9m range and the -4.6m competitor scenario. |
| Must not add terminal value or tax without flagging departure from conventions | yes | Appendix conventions line: 'no terminal value; no tax in this screening model' — none added. |

## Transcript

## Turn 1

**User:** Build the business case for the Kestrel south hub from these inputs. Board needs NPV, payback and what decides the answer. (Attached in the working directory: fm-01-input.md.)

**The answer:** approve the EUR 6m south hub — base-case NPV is **EUR 3.2m** at the 9% hurdle, IRR 21%, payback by **2030** (year 4). But the margin is thin: NPV ranges from -EUR 1.8m to +EUR 8.9m across the quoted low/high inputs, and **-EUR 4.6m** if a competitor opens a rival hub.

**What decides the answer:** of the six uncertain drivers, two actually matter — saving per parcel (break-even EUR 0.43, vs. quoted range 0.40–0.65) and parcels routed (break-even 3.86m, vs. quoted range 3.8–5.6m). Both break-evens sit just inside the low end of the evidence already on file, which is the real risk. Fixed cost, investment and the discount rate would all have to move past their quoted ranges alone to flip the decision — they're not decisive. The planning team's competitor-response note (volume loss + price erosion + accelerated fit-out cost) hits both decisive drivers plus investment at once, which is why it's the one scenario that fails the hurdle outright.

Delivered:
- `model/` — transparent CSV model (inputs/calc/outputs/checks/sensitivity separated, one formula per row) plus a live-formula `model.xlsx` with scenario switch, and `README.md` with the full write-up. All checks pass; hand-verified NPV and payback tie to the model.
- `deck.md` / `deck.html` / `deck.pptx` — an 8-page board deck: title, executive summary, payback chart, scenario comparison, the break-even sensitivity table, a waterfall decomposing the competitor-response case, recommendation with a monitoring checkpoint, and an appendix of inputs/sources. Titles-only read-through tells the whole story; renderer flagged zero warnings.

One flagged gap: no range was quoted for the 2027 ramp assumption (60%), so I added my own illustrative 40–80% spread to test it — it turns out not to matter (NPV only moves EUR 2.7m–3.7m), but that range is mine, not evidence, and is called out as such in both the model and the deck appendix.


## Files in work dir after run

- deck.html
- deck.md
- deck.pptx
- fm-01-input.md
- model/README.md
- model/calc.csv
- model/checks.csv
- model/inputs.csv
- model/model.xlsx
- model/outputs.csv
- model/sensitivity.csv
- model/spec.json

## File written by the run: deck.html

<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kestrel south hub business case</title><style>
:root{--text:#14213D;--accent:#D9822B;--muted:#B8C0CC;--light:#E8EBF0;--bg:#FFFFFF}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:#2B2F36;font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;color:var(--text)}
#stage{position:absolute;left:0;top:0;width:1280px;height:720px;transform-origin:0 0}
.slide{display:none;position:absolute;inset:0;width:1280px;height:720px;background:var(--bg);padding:44px 64px 30px;flex-direction:column}
.slide.active{display:flex}
.tracker{font-size:14px;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);font-weight:700;min-height:18px;margin-bottom:10px}
.title{font-size:30px;line-height:1.22;font-weight:700;max-width:1120px}
.title.long{font-size:26px}
.header{font-size:16px;color:#5B6475;margin-top:12px}
.content{flex:1;display:flex;gap:40px;margin-top:22px;min-height:0}
.exhibit{flex:1;min-width:0;display:flex;align-items:center;justify-content:center}
.exhibit.tbl{align-items:flex-start}
.chart{width:100%;height:100%}
.side{width:380px;font-size:19px;line-height:1.45;padding-top:8px}
.side li,.text li{margin:0 0 14px 20px}
.text{flex-direction:column;font-size:22px;line-height:1.45;max-width:1040px}
.lead{font-size:20px;line-height:1.5;color:#3B4458;margin-bottom:18px;max-width:1080px}
.summary{flex-direction:column;gap:0}
.summary ol{font-size:19px;line-height:1.45;margin-left:24px}
.summary li{margin-bottom:10px;padding-left:6px}
.ask{margin-top:auto;border-left:5px solid var(--accent);background:var(--light);padding:14px 18px;font-size:18px;line-height:1.4}
.takeaway{margin-top:14px;padding:10px 16px;border-top:2px solid var(--text);font-size:18px;font-weight:600}
footer{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;margin-top:14px;font-size:13px;color:#5B6475;line-height:1.35}
footer .pn{font-weight:700;color:var(--text)}
.footnote{margin-bottom:2px}
table.data{border-collapse:collapse;font-size:17px;width:100%}
table.data th{text-align:left;border-bottom:2px solid var(--text);padding:8px 12px;font-weight:700}
table.data td{border-bottom:1px solid var(--light);padding:8px 12px;vertical-align:top}
table.data th.num{text-align:right}
table.data td.num{text-align:right;font-variant-numeric:tabular-nums}
table.data tr.hl td{background:var(--light);font-weight:700}
.slide.l-title{justify-content:center;padding-left:96px}
.t-client{font-size:18px;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);font-weight:700;margin-bottom:24px}
.t-title{font-size:48px;line-height:1.15;max-width:980px;font-weight:700}
.t-sub{font-size:22px;margin-top:24px;color:#3B4458;max-width:900px}
.t-meta{font-size:16px;margin-top:40px;color:#5B6475}
.slide.l-title footer,.slide.l-section footer{margin-top:auto}
.slide.l-section{justify-content:center;padding-left:96px}
.s-title{font-size:40px;line-height:1.2;max-width:1000px;margin-top:12px}
.notes{display:none;position:absolute;left:0;right:0;bottom:0;background:#FFF8E8;border-top:2px solid var(--accent);padding:12px 64px;font-size:16px;line-height:1.4}
body.shownotes .slide.active .notes{display:block}
#overview{display:none;position:fixed;inset:0;overflow:auto;background:var(--bg);padding:40px 56px;font-size:18px;line-height:1.5}
body.overview #overview{display:block}
#overview h1{font-size:22px;margin-bottom:16px}
#overview li{margin:0 0 8px 28px;cursor:pointer}
#hint{position:fixed;right:12px;bottom:8px;font-size:12px;color:#C9CED8}
.warn{color:#B00020}
@media print{
  @page{size:1280px 720px;margin:0}
  html,body{background:#fff}
  #stage{position:static;transform:none!important;width:auto;height:auto}
  .slide{display:flex!important;position:relative;page-break-after:always;break-after:page}
  .notes,#hint,#overview{display:none!important}
}
</style></head>
<body><div id="stage"><section class="slide l-title" id="s1" data-title="Should Kestrel invest in a cross-dock hub in the south region?"><div class="t-client">Kestrel Logistics (fictional)</div><h1 class="t-title">Should Kestrel invest in a cross-dock hub in the south region?</h1><p class="t-sub">Business case for the board, EUR 6m investment decision</p><p class="t-meta">Board, investment decision | October 2026</p><footer><div></div><span class="pn">1</span></footer><aside class="notes"><b>Speaker note</b> Model version v01. Decision rule from the CFO: approve if NPV at the 9% hurdle rate is above zero over the hub&#x27;s eight-year life, 2027 to 2034.</aside></section><section class="slide l-summary" id="s2" data-title="Approve the EUR 6m south hub: base-case NPV is EUR 3.2m with payback by 2030, but the answer rests on two drivers that break even close to their low-end range"><div class="tracker">Executive summary</div><h2 class="title long">Approve the EUR 6m south hub: base-case NPV is EUR 3.2m with payback by 2030, but the answer rests on two drivers that break even close to their low-end range</h2><div class="content summary"><p class="lead">2025 network-flow data and a network simulation show a south-region cross-dock hub would cut handling and line-haul cost per routed parcel. The question for the board is whether the EUR 6m investment clears the CFO&#x27;s 9% hurdle rate once the uncertainty in volume, saving and competitor response is taken into account.</p><ol><li>Base case: NPV EUR 3.2m at the 9% hurdle rate, IRR 21%, payback by 2030 (year 4 of operation). Range across the quoted low/high inputs: -EUR 1.8m to +EUR 8.9m.</li><li>Saving per parcel (base EUR 0.55) breaks even at EUR 0.43, inside its quoted EUR 0.40-0.65 range and close to the low end.</li><li>Parcels routed at full run-rate (base 5.0m) break even at 3.86m, inside its quoted 3.8-5.6m range and close to the low end.</li><li>If a rival opens its own south hub, lower volume, an eroded saving and a more expensive accelerated fit-out together would push NPV to about -EUR 4.6m, failing the hurdle.</li></ol><div class="ask"><strong>Decision requested:</strong> approve EUR 6m for the south hub, paid at the start of 2027 (owner: head of network planning). Set a checkpoint at the end of 2027 against actual routed volume and saving per parcel; treat a confirmed rival hub announcement as a trigger to re-underwrite the case before further capital commitment.</div></div><footer><div class="source">Source: Kestrel south hub business case model v01</div><span class="pn">2</span></footer><aside class="notes"><b>Speaker note</b> Read the bold line and the ask. Pages 3 to 6 prove each point in turn.</aside></section><section class="slide l-chart" id="s3" data-title="The EUR 6m hub pays back within four years of opening, turning cash-positive in 2030"><div class="tracker">1 Base case</div><h2 class="title">The EUR 6m hub pays back within four years of opening, turning cash-positive in 2030</h2><div class="header">Cumulative net cash flow, EUR m, base case, 2027 to 2034</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="The EUR 6m hub pays back within four years of opening, turning cash-positive in 2030"><text x="46.0" y="365.0" font-size="13" text-anchor="end" fill="#B8C0CC" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-6</text><text x="46.0" y="200.0" font-size="13" text-anchor="end" fill="#B8C0CC" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1</text><text x="46.0" y="35.0" font-size="13" text-anchor="end" fill="#B8C0CC" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">8</text><line x1="56" x2="510" y1="360.0" y2="360.0" stroke="#B8C0CC"/><text x="56.0" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2027 (investment)</text><text x="112.8" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2027</text><text x="169.5" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2028</text><text x="226.2" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2029</text><text x="283.0" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2030</text><text x="339.8" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2031</text><text x="396.5" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2032</text><text x="453.2" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2033</text><text x="510.0" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2034</text><line x1="56.0" x2="510.0" y1="218.6" y2="218.6" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="518.0" y="223.6" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Cumulative cash = 0 (payback)</text><polyline points="56.0,360.0 112.8,342.3 169.5,298.7 226.2,255.1 283.0,211.5 339.8,167.9 396.5,124.3 453.2,80.7 510.0,37.1" fill="none" stroke="#B8C0CC" stroke-width="2.5"/><circle cx="56.0" cy="360.0" r="4" fill="#B8C0CC"/><circle cx="112.8" cy="342.3" r="4" fill="#B8C0CC"/><circle cx="169.5" cy="298.7" r="4" fill="#B8C0CC"/><circle cx="226.2" cy="255.1" r="4" fill="#B8C0CC"/><circle cx="283.0" cy="211.5" r="4" fill="#B8C0CC"/><circle cx="339.8" cy="167.9" r="4" fill="#B8C0CC"/><circle cx="396.5" cy="124.3" r="4" fill="#B8C0CC"/><circle cx="453.2" cy="80.7" r="4" fill="#B8C0CC"/><circle cx="510.0" cy="37.1" r="4" fill="#B8C0CC"/><text x="510.0" y="25.1" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">7.7</text></svg></div><div class="side"><ul><li>EUR 6m paid at the start of 2027; operating cash flows at year-end 2027-2034, discounted 1 to 8 years at 9%, no terminal value.</li><li>2027 is the ramp year (60% of full run-rate parcels, per the planning team&#x27;s assumption from the 2023 north hub opening); full run-rate from 2028.</li><li>Discounted at 9%, the same cash flows give NPV EUR 3.2m and IRR 21%, both above the hurdle.</li></ul></div></div><footer><div class="footnote">&quot;2027 (investment)&quot; is the EUR 6m outflow at the start of the year; &quot;2027&quot; is the first year of operating cash flow, at year-end.</div><div class="source">Source: Kestrel south hub business case model v01, base case</div><span class="pn">3</span></footer><aside class="notes"><b>Speaker note</b> Payback lands in year 4 of operation. The board&#x27;s rule is NPV, not payback, but payback is the liquidity read members usually ask for first.</aside></section><section class="slide l-chart" id="s4" data-title="NPV swings from +EUR 8.9m to -EUR 4.6m across scenarios; only the base and up cases clear the 9% hurdle"><div class="tracker">1 Base case</div><h2 class="title long">NPV swings from +EUR 8.9m to -EUR 4.6m across scenarios; only the base and up cases clear the 9% hurdle</h2><div class="header">NPV by scenario at the 9% hurdle rate, EUR m</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="NPV swings from +EUR 8.9m to -EUR 4.6m across scenarios; only the base and up cases clear the 9% hurdle"><rect x="168" y="33.0" width="411.2" height="43.0" fill="#B8C0CC"/><text x="587.2" y="60.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">8.9</text><text x="156.0" y="61.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Up</text><rect x="168" y="129.0" width="147.8" height="43.0" fill="#B8C0CC"/><text x="323.8" y="156.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.2</text><text x="156.0" y="157.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base</text><rect x="168" y="225.0" width="0.5" height="43.0" fill="#B8C0CC"/><text x="176.0" y="252.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-1.8</text><text x="156.0" y="253.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Down</text><rect x="168" y="321.0" width="0.5" height="43.0" fill="#D9822B"/><text x="176.0" y="348.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-4.6</text><text x="156.0" y="349.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor response</text><line x1="168" x2="168" y1="8" y2="392.0" stroke="#14213D"/><line x1="168.0" x2="168.0" y1="8" y2="392.0" stroke="#14213D" stroke-dasharray="6 5"/><text x="168.0" y="398.0" font-size="13" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Approval threshold: NPV = 0</text></svg></div><div class="side"><ul><li>Up: volume and saving at the top of their quoted ranges, fixed cost at the bottom (strong flow capture, high-fuel-cost environment, lean site).</li><li>Down: volume at the bottom of its range, fixed cost at the top (weak flow capture, lease/staffing cost overruns); saving and investment unchanged.</li><li>Competitor response: the planning team&#x27;s qualitative risk, quantified (detail on page 6).</li></ul></div></div><footer><div class="source">Source: Kestrel south hub business case model v01, scenarios down / up / competitor_response</div><span class="pn">4</span></footer><aside class="notes"><b>Speaker note</b> Down alone does not fail the hurdle as badly as competitor response, because competitor response hits three drivers at once.</aside></section><section class="slide l-table" id="s5" data-title="Saving per parcel and parcels routed decide the answer; both break even just inside their quoted ranges"><div class="tracker">2 What decides the answer</div><h2 class="title long">Saving per parcel and parcels routed decide the answer; both break even just inside their quoted ranges</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Driver</th><th class="num">Base</th><th>Quoted range</th><th class="num">NPV at low</th><th class="num">NPV at high</th><th class="num">Break-even</th><th>Inside quoted range?</th></tr><tr><td>Saving per parcel, EUR/parcel</td><td class="num">0.55</td><td>0.40 - 0.65</td><td class="num">-0.6</td><td class="num">5.8</td><td class="num">0.43</td><td>Yes, just above the low end</td></tr><tr><td>Parcels at full run-rate, m/year</td><td class="num">5.0</td><td>3.8 - 5.6</td><td class="num">-0.2</td><td class="num">4.9</td><td class="num">3.86</td><td>Yes, just above the low end</td></tr><tr><td>Hub fixed cost, EUR m/year</td><td class="num">0.9</td><td>0.7 - 1.2</td><td class="num">4.3</td><td class="num">1.6</td><td class="num">1.48</td><td>No, above the high end</td></tr><tr><td>Investment, EUR m</td><td class="num">6.0</td><td>5.5 - 7.5</td><td class="num">3.7</td><td class="num">1.7</td><td class="num">9.2</td><td>No, above the high end</td></tr><tr><td>Discount rate, per year</td><td class="num">9%</td><td>7% - 11%</td><td class="num">4.0</td><td class="num">2.5</td><td class="num">21%</td><td>No, far above the high end</td></tr></table></div><div class="side"><ul><li>One-way sensitivity, each driver tested at its quoted low and high with the others held at base; ranked by swing in NPV.</li><li>Ramp in 2027 (base 60%) was also tested at an illustrative 40-80% range, since no range was quoted for it; NPV only moves EUR 2.7m to EUR 3.7m, so it is not decisive.</li><li>Hub fixed cost, investment and the discount rate cannot flip the decision on their own: each would have to move past its quoted range to push NPV to zero.</li></ul></div></div><div class="takeaway">Saving per parcel and parcels routed are the only drivers whose break-even sits inside the evidence range already on file; they are what the board&#x27;s approval actually rests on.</div><footer><div class="source">Source: Kestrel south hub business case model v01, sensitivity table</div><span class="pn">5</span></footer><aside class="notes"><b>Speaker note</b> This is the page that answers &quot;what decides the answer.&quot; The break-even discount rate of 21% is the same number as the base-case IRR, which is a useful cross-check.</aside></section><section class="slide l-chart" id="s6" data-title="A rival hub nearby would push NPV to about -EUR 4.6m by hitting volume, saving and cost at once"><div class="tracker">2 What decides the answer</div><h2 class="title">A rival hub nearby would push NPV to about -EUR 4.6m by hitting volume, saving and cost at once</h2><div class="header">NPV bridge from base case to the competitor-response case, EUR m</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="A rival hub nearby would push NPV to about -EUR 4.6m by hitting volume, saving and cost at once"><rect x="28.3" y="57.8" width="66.2" height="119.1" fill="#14213D"/><line x1="8.0" x2="542.0" y1="176.8" y2="176.8" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="550.0" y="181.8" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Approval threshold: NPV = 0</text><text x="61.4" y="49.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.2</text><text x="61.4" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base case</text><text x="61.4" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">NPV</text><rect x="135.1" y="57.8" width="66.2" height="126.5" fill="#B8C0CC"/><text x="168.2" y="49.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-3.4</text><line x1="94.5" x2="135.1" y1="57.8" y2="57.8" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="168.2" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Lower volume</text><text x="168.2" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">(parcels to</text><text x="168.2" y="404.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">low end,</text><rect x="241.9" y="184.3" width="66.2" height="107.9" fill="#B8C0CC"/><text x="275.0" y="176.3" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-2.9</text><line x1="201.3" x2="241.9" y1="184.3" y2="184.3" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="275.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Lower saving</text><text x="275.0" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">per parcel</text><text x="275.0" y="404.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">(price</text><rect x="348.7" y="292.2" width="66.2" height="55.8" fill="#B8C0CC"/><text x="381.8" y="284.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-1.5</text><line x1="308.1" x2="348.7" y1="292.2" y2="292.2" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="381.8" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Higher</text><text x="381.8" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">investment</text><text x="381.8" y="404.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">(accelerated</text><rect x="455.5" y="176.8" width="66.2" height="171.2" fill="#D9822B"/><text x="488.6" y="168.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-4.6</text><line x1="414.9" x2="455.5" y1="348.0" y2="348.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="488.6" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor-response</text><text x="488.6" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">NPV</text><line x1="8" x2="542" y1="176.8" y2="176.8" stroke="#14213D"/></svg></div><div class="side"><ul><li>The planning team&#x27;s note was qualitative, not quantified: &quot;some shippers move... they would also force a price response... the fit-out would cost more because we would accelerate it.&quot;</li><li>No distinct figures exist for this case. We proxy it with the already-quoted low end of volume and saving and the already-quoted high end of investment, since each moves in the direction the note describes; this mapping is itself an assumption, separate from the ranges behind it.</li><li>Each step is applied on top of the last, so the three deltas add up exactly to the gap between the base and competitor-response NPV.</li></ul></div></div><footer><div class="footnote">If the board wants a firmer number here, the cheapest next step is a short commercial read on how much volume a rival hub would likely divert in year one, rather than more financial modelling.</div><div class="source">Source: Kestrel south hub business case model v01, scenario competitor_response</div><span class="pn">6</span></footer><aside class="notes"><b>Speaker note</b> This is the one scenario that fails the hurdle outright. It is a reason to set a checkpoint, not a reason to decline the investment today.</aside></section><section class="slide l-table" id="s7" data-title="Recommend approval, with a 2027 checkpoint against the two decisive drivers"><div class="tracker">Recommendation and next steps</div><h2 class="title">Recommend approval, with a 2027 checkpoint against the two decisive drivers</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Step</th><th>Owner</th><th>By when</th></tr><tr><td>Board approval of EUR 6m, paid at the start of 2027</td><td>Board</td><td>Q4 2026</td></tr><tr><td>Lock supplier quote and fit-out schedule</td><td>Head of network planning</td><td>Q4 2026</td></tr><tr><td>Track actual routed volume and realised saving per parcel against break-even (3.86m parcels; EUR 0.43 per parcel)</td><td>Head of network planning</td><td>Monthly from Q1 2027</td></tr><tr><td>Re-underwrite the case if a rival south hub is confirmed</td><td>CFO</td><td>On announcement</td></tr><tr><td>Checkpoint review of year-1 ramp and run-rate volume</td><td>CFO and board</td><td>End of 2027</td></tr></table></div><div class="side"><ul><li>Risk: the 60% 2027 ramp assumption has no quoted range; year-1 cash flow is not what decides the approval, but a materially slower ramp would delay payback beyond 2030.</li><li>Risk: the EUR 6m investment itself has a quoted range of EUR 5.5-7.5m from two supplier quotes; investment alone would have to reach about EUR 9.2m to fail the hurdle, well outside that range.</li><li>The decision does not need to wait on a firmer competitor-response estimate; it needs a checkpoint that would catch the risk early.</li></ul></div></div><footer><div class="source">Source: Kestrel south hub business case model v01</div><span class="pn">7</span></footer><aside class="notes"><b>Speaker note</b> Close on the ask. The board can approve today and still manage the risk named on page 6.</aside></section><section class="slide l-table" id="s8" data-title="Inputs and sources behind the model"><div class="tracker">Appendix</div><h2 class="title">Inputs and sources behind the model</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Driver</th><th class="num">Base</th><th>Low</th><th>High</th><th>Unit</th><th>Source</th></tr><tr><td>Parcels at full run-rate</td><td class="num">5.0</td><td>3.8</td><td>5.6</td><td>m parcels/year</td><td>2025 network flow data, south region (Kestrel planning team)</td></tr><tr><td>Ramp in 2027</td><td class="num">60%</td><td>40%*</td><td>80%*</td><td>share of full run-rate</td><td>ASSUMPTION: planning team, based on the 2023 north hub opening</td></tr><tr><td>Saving per routed parcel</td><td class="num">0.55</td><td>0.40</td><td>0.65</td><td>EUR/parcel</td><td>Network simulation v4; low = 2025 fuel prices, high = 2023 fuel prices</td></tr><tr><td>Hub operating fixed cost</td><td class="num">0.9</td><td>0.7</td><td>1.2</td><td>EUR m/year</td><td>Site lease offer plus 14 FTE staffing plan</td></tr><tr><td>Investment (fit-out, sorter)</td><td class="num">6.0</td><td>5.5</td><td>7.5</td><td>EUR m</td><td>Two supplier quotes, September 2026</td></tr><tr><td>Hurdle rate</td><td class="num">9%</td><td>7%</td><td>11%</td><td>per year</td><td>Group finance</td></tr></table></div><div class="side"><ul><li>*No range was quoted for the 2027 ramp; 40%-80% is our own illustrative spread for the sensitivity test on page 5, not evidence. Replace it if planning can point to the actual north-hub ramp curve.</li><li>Conventions: EUR m; investment paid at the start of 2027 (t=0); operating cash flows at year-end 2027-2034, discounted 1 to 8 years; no terminal value; no tax in this screening model.</li><li>Full model (CSV and Excel, with live formulas, checks and the scenario switch): model/ folder, version v01.</li></ul></div></div><footer><div class="source">Source: fm-01-input.md; Kestrel south hub business case model v01</div><span class="pn">A1</span></footer></section></div>
<div id="overview"><h1>Titles-only read-through</h1><ol><li>Should Kestrel invest in a cross-dock hub in the south region? <span style='color:#8A93A3'>(1)</span></li><li>Approve the EUR 6m south hub: base-case NPV is EUR 3.2m with payback by 2030, but the answer rests on two drivers that break even close to their low-end range <span style='color:#8A93A3'>(2)</span></li><li>The EUR 6m hub pays back within four years of opening, turning cash-positive in 2030 <span style='color:#8A93A3'>(3)</span></li><li>NPV swings from +EUR 8.9m to -EUR 4.6m across scenarios; only the base and up cases clear the 9% hurdle <span style='color:#8A93A3'>(4)</span></li><li>Saving per parcel and parcels routed decide the answer; both break even just inside their quoted ranges <span style='color:#8A93A3'>(5)</span></li><li>A rival hub nearby would push NPV to about -EUR 4.6m by hitting volume, saving and cost at once <span style='color:#8A93A3'>(6)</span></li><li>Recommend approval, with a 2027 checkpoint against the two decisive drivers <span style='color:#8A93A3'>(7)</span></li><li>Inputs and sources behind the model <span style='color:#8A93A3'>(A1)</span></li></ol></div>
<div id="hint">arrows: navigate | t: titles | n: notes | print: PDF</div>
<script>
(function(){
var slides=[].slice.call(document.querySelectorAll('.slide')),i=0,stage=document.getElementById('stage');
function fit(){var s=Math.min(innerWidth/1280,innerHeight/720);stage.style.transform='translate('+((innerWidth-1280*s)/2)+'px,'+((innerHeight-720*s)/2)+'px) scale('+s+')';}
function show(n){i=Math.max(0,Math.min(slides.length-1,n));slides.forEach(function(el,k){el.classList.toggle('active',k===i);});history.replaceState(null,'','#'+(i+1));}
addEventListener('resize

## File written by the run: deck.md

---
title: Kestrel south hub business case
client: Kestrel Logistics (fictional)
audience: Board, investment decision
date: October 2026
format: deck
theme:
  text: "#14213D"
  accent: "#D9822B"
  muted: "#B8C0CC"
  light: "#E8EBF0"
  background: "#FFFFFF"
---

# Deck: Should Kestrel invest in a cross-dock hub in the south region?

*Fictional company. All figures, people and documents invented for evaluation.*

**Opening (SCQA)**
- Situation: 2025 network-flow data shows a south-region cross-dock hub could cut EUR 0.55 per routed parcel through shorter line-haul and fewer handlings.
- Complication: the EUR 6m investment only clears the CFO's 9% hurdle rate if volume and saving land near the base case; both of the drivers that decide the answer break even just inside the low end of their quoted ranges, and a rival hub opening nearby could push the case negative.
- Question: Should Kestrel approve the EUR 6m south hub investment now?
- Answer: Yes, approve it — base-case NPV is EUR 3.2m with payback by 2030 — but track routed volume and saving per parcel against their break-even levels from day one, and treat a rival hub opening as a trigger to re-underwrite the case.

**Key line**
1. Base case: NPV EUR 3.2m at the 9% hurdle rate, IRR 21%, payback by 2030 (year 4 of operation).
2. Saving per parcel and parcels routed decide the answer; both break even just inside the low end of their quoted ranges, so the cushion is thin.
3. If a rival hub opens nearby, the combined hit to volume, saving and fit-out cost would push NPV to about -EUR 4.6m, failing the hurdle.

## 1. Should Kestrel invest in a cross-dock hub in the south region?
layout: title
subtitle: Business case for the board, EUR 6m investment decision
note: Model version v01. Decision rule from the CFO: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life, 2027 to 2034.

## 2. Approve the EUR 6m south hub: base-case NPV is EUR 3.2m with payback by 2030, but the answer rests on two drivers that break even close to their low-end range
layout: summary
tracker: Executive summary
lead: 2025 network-flow data and a network simulation show a south-region cross-dock hub would cut handling and line-haul cost per routed parcel. The question for the board is whether the EUR 6m investment clears the CFO's 9% hurdle rate once the uncertainty in volume, saving and competitor response is taken into account.
body:
- Base case: NPV EUR 3.2m at the 9% hurdle rate, IRR 21%, payback by 2030 (year 4 of operation). Range across the quoted low/high inputs: -EUR 1.8m to +EUR 8.9m.
- Saving per parcel (base EUR 0.55) breaks even at EUR 0.43, inside its quoted EUR 0.40-0.65 range and close to the low end.
- Parcels routed at full run-rate (base 5.0m) break even at 3.86m, inside its quoted 3.8-5.6m range and close to the low end.
- If a rival opens its own south hub, lower volume, an eroded saving and a more expensive accelerated fit-out together would push NPV to about -EUR 4.6m, failing the hurdle.
ask: **Decision requested:** approve EUR 6m for the south hub, paid at the start of 2027 (owner: head of network planning). Set a checkpoint at the end of 2027 against actual routed volume and saving per parcel; treat a confirmed rival hub announcement as a trigger to re-underwrite the case before further capital commitment.
source: Kestrel south hub business case model v01
note: Read the bold line and the ask. Pages 3 to 6 prove each point in turn.

## 3. The EUR 6m hub pays back within four years of opening, turning cash-positive in 2030
layout: chart
tracker: 1 Base case
message: time-series
chart: line
header: Cumulative net cash flow, EUR m, base case, 2027 to 2034
reference: 0 | Cumulative cash = 0 (payback)
highlight: 2030
| Year | Cumulative cash flow |
|---|---|
| 2027 (investment) | -6.0 |
| 2027 | -5.25 |
| 2028 | -3.4 |
| 2029 | -1.55 |
| 2030 | 0.3 |
| 2031 | 2.15 |
| 2032 | 4.0 |
| 2033 | 5.85 |
| 2034 | 7.7 |
body:
- EUR 6m paid at the start of 2027; operating cash flows at year-end 2027-2034, discounted 1 to 8 years at 9%, no terminal value.
- 2027 is the ramp year (60% of full run-rate parcels, per the planning team's assumption from the 2023 north hub opening); full run-rate from 2028.
- Discounted at 9%, the same cash flows give NPV EUR 3.2m and IRR 21%, both above the hurdle.
footnote: "2027 (investment)" is the EUR 6m outflow at the start of the year; "2027" is the first year of operating cash flow, at year-end.
source: Kestrel south hub business case model v01, base case
note: Payback lands in year 4 of operation. The board's rule is NPV, not payback, but payback is the liquidity read members usually ask for first.

## 4. NPV swings from +EUR 8.9m to -EUR 4.6m across scenarios; only the base and up cases clear the 9% hurdle
layout: chart
tracker: 1 Base case
message: deviation
chart: hbar
header: NPV by scenario at the 9% hurdle rate, EUR m
reference: 0 | Approval threshold: NPV = 0
highlight: Competitor response
| Scenario | NPV |
|---|---|
| Up | 8.9 |
| Base | 3.2 |
| Down | -1.8 |
| Competitor response | -4.6 |
body:
- Up: volume and saving at the top of their quoted ranges, fixed cost at the bottom (strong flow capture, high-fuel-cost environment, lean site).
- Down: volume at the bottom of its range, fixed cost at the top (weak flow capture, lease/staffing cost overruns); saving and investment unchanged.
- Competitor response: the planning team's qualitative risk, quantified (detail on page 6).
source: Kestrel south hub business case model v01, scenarios down / up / competitor_response
note: Down alone does not fail the hurdle as badly as competitor response, because competitor response hits three drivers at once.

## 5. Saving per parcel and parcels routed decide the answer; both break even just inside their quoted ranges
layout: table
tracker: 2 What decides the answer
| Driver | Base | Quoted range | NPV at low | NPV at high | Break-even | Inside quoted range? |
|---|---|---|---|---|---|---|
| Saving per parcel, EUR/parcel | 0.55 | 0.40 - 0.65 | -0.6 | 5.8 | 0.43 | Yes, just above the low end |
| Parcels at full run-rate, m/year | 5.0 | 3.8 - 5.6 | -0.2 | 4.9 | 3.86 | Yes, just above the low end |
| Hub fixed cost, EUR m/year | 0.9 | 0.7 - 1.2 | 4.3 | 1.6 | 1.48 | No, above the high end |
| Investment, EUR m | 6.0 | 5.5 - 7.5 | 3.7 | 1.7 | 9.2 | No, above the high end |
| Discount rate, per year | 9% | 7% - 11% | 4.0 | 2.5 | 21% | No, far above the high end |
body:
- One-way sensitivity, each driver tested at its quoted low and high with the others held at base; ranked by swing in NPV.
- Ramp in 2027 (base 60%) was also tested at an illustrative 40-80% range, since no range was quoted for it; NPV only moves EUR 2.7m to EUR 3.7m, so it is not decisive.
- Hub fixed cost, investment and the discount rate cannot flip the decision on their own: each would have to move past its quoted range to push NPV to zero.
takeaway: Saving per parcel and parcels routed are the only drivers whose break-even sits inside the evidence range already on file; they are what the board's approval actually rests on.
source: Kestrel south hub business case model v01, sensitivity table
note: This is the page that answers "what decides the answer." The break-even discount rate of 21% is the same number as the base-case IRR, which is a useful cross-check.

## 6. A rival hub nearby would push NPV to about -EUR 4.6m by hitting volume, saving and cost at once
layout: chart
tracker: 2 What decides the answer
message: flow
chart: waterfall
header: NPV bridge from base case to the competitor-response case, EUR m
reference: 0 | Approval threshold: NPV = 0
highlight: Competitor-response NPV
| Step | EUR m | Type |
|---|---|---|
| Base case NPV | 3.2 | total |
| Lower volume (parcels to low end, 3.8m) | -3.4 | delta |
| Lower saving per parcel (price response, to EUR 0.40) | -2.9 | delta |
| Higher investment (accelerated fit-out, to EUR 7.5m) | -1.5 | delta |
| Competitor-response NPV | -4.6 | total |
body:
- The planning team's note was qualitative, not quantified: "some shippers move... they would also force a price response... the fit-out would cost more because we would accelerate it."
- No distinct figures exist for this case. We proxy it with the already-quoted low end of volume and saving and the already-quoted high end of investment, since each moves in the direction the note describes; this mapping is itself an assumption, separate from the ranges behind it.
- Each step is applied on top of the last, so the three deltas add up exactly to the gap between the base and competitor-response NPV.
footnote: If the board wants a firmer number here, the cheapest next step is a short commercial read on how much volume a rival hub would likely divert in year one, rather than more financial modelling.
source: Kestrel south hub business case model v01, scenario competitor_response
note: This is the one scenario that fails the hurdle outright. It is a reason to set a checkpoint, not a reason to decline the investment today.

## 7. Recommend approval, with a 2027 checkpoint against the two decisive drivers
layout: table
tracker: Recommendation and next steps
| Step | Owner | By when |
|---|---|---|
| Board approval of EUR 6m, paid at the start of 2027 | Board | Q4 2026 |
| Lock supplier quote and fit-out schedule | Head of network planning | Q4 2026 |
| Track actual routed volume and realised saving per parcel against break-even (3.86m parcels; EUR 0.43 per parcel) | Head of network planning | Monthly from Q1 2027 |
| Re-underwrite the case if a rival south hub is confirmed | CFO | On announcement |
| Checkpoint review of year-1 ramp and run-rate volume | CFO and board | End of 2027 |
body:
- Risk: the 60% 2027 ramp assumption has no quoted range; year-1 cash flow is not what decides the approval, but a materially slower ramp would delay payback beyond 2030.
- Risk: the EUR 6m investment itself has a quoted range of EUR 5.5-7.5m from two supplier quotes; investment alone would have to reach about EUR 9.2m to fail the hurdle, well outside that range.
- The decision does not need to wait on a firmer competitor-response estimate; it needs a checkpoint that would catch the risk early.
ask: **Decision requested:** approve EUR 6m for the south hub now; adopt the monthly volume/saving checkpoint and the re-underwrite trigger above as a condition of approval.
source: Kestrel south hub business case model v01
note: Close on the ask. The board can approve today and still manage the risk named on page 6.

## A1. Inputs and sources behind the model
layout: table
tracker: Appendix
| Driver | Base | Low | High | Unit | Source |
|---|---|---|---|---|---|
| Parcels at full run-rate | 5.0 | 3.8 | 5.6 | m parcels/year | 2025 network flow data, south region (Kestrel planning team) |
| Ramp in 2027 | 60% | 40%* | 80%* | share of full run-rate | ASSUMPTION: planning team, based on the 2023 north hub opening |
| Saving per routed parcel | 0.55 | 0.40 | 0.65 | EUR/parcel | Network simulation v4; low = 2025 fuel prices, high = 2023 fuel prices |
| Hub operating fixed cost | 0.9 | 0.7 | 1.2 | EUR m/year | Site lease offer plus 14 FTE staffing plan |
| Investment (fit-out, sorter) | 6.0 | 5.5 | 7.5 | EUR m | Two supplier quotes, September 2026 |
| Hurdle rate | 9% | 7% | 11% | per year | Group finance |
body:
- *No range was quoted for the 2027 ramp; 40%-80% is our own illustrative spread for the sensitivity test on page 5, not evidence. Replace it if planning can point to the actual north-hub ramp curve.
- Conventions: EUR m; investment paid at the start of 2027 (t=0); operating cash flows at year-end 2027-2034, discounted 1 to 8 years; no terminal value; no tax in this screening model.
- Full model (CSV and Excel, with live formulas, checks and the scenario switch): model/ folder, version v01.
source: fm-01-input.md; Kestrel south hub business case model v01


## File written by the run: model/README.md

# Model: Kestrel south hub cross-dock business case (fictional), v01

**Question answered:** Should Kestrel invest in a cross-dock hub in the south region? Decision rule: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life (2027-2034); investment paid at the start of 2027 (t=0), operating cash flows at year-end 2027-2034, no terminal value, no tax.

**Master check:** OK

## Key outputs

| Output | Unit | base | down | up | competitor_response |
|---|---|---|---|---|---|
| NPV at hurdle rate | EUR m | 3.23 | -1.841 | 8.937 | -4.626 |
| IRR | per year | 0.2091 | 0.009393 | 0.3865 | -0.09939 |
| Payback (first year cumulative cash >= 0) | year | 2030 | 2034 | 2029 | none |
| Parcels routed, 2027 (ramp year) | m parcels | 3 | 2.28 | 3.36 | 2.28 |
| Parcels routed, 2028 (full run-rate) | m parcels | 5 | 3.8 | 5.6 | 3.8 |

Scenarios (coherent sets, drivers changed from base):
- **down**: parcels_full_run_rate = 3.8, hub_operating_fixed_cost = 1.2 (generic downside: south volumes land at the bottom of the quoted flow range and the lease/staffing cost comes in at the top of its range; saving per parcel and investment unchanged)
- **up**: parcels_full_run_rate = 5.6, saving_per_parcel = 0.65, hub_operating_fixed_cost = 0.7 (generic upside: south volumes land at the top of the flow range, a high-fuel-cost environment raises the value of consolidation, and the site is run lean)
- **competitor_response**: parcels_full_run_rate = 3.8, saving_per_parcel = 0.4, investment = 7.5 (planning team's note, quantified: a rival hub opens nearby, shippers partially defect (volume at the low end of the range), the price response that follows erodes the saving per parcel (also to the low end of its range), and Kestrel accelerates the fit-out to respond, pushing investment to the top of the two quotes. No distinct figures were supplied for this case; it reuses the already-quoted low/high ends of the three affected drivers, which is itself an assumption about the mapping, flagged separately)

## Sensitivity on npv (one-way, others at base; break-even target 0)

| Rank | Driver | Low / base / high | Output low | Output high | Swing | Break-even | Inside range? |
|---|---|---|---|---|---|---|---|
| 1 | saving_per_parcel | 0.4 / 0.55 / 0.65 EUR per parcel | -0.6456 | 5.814 | 6.46 | 0.425 | yes |
| 2 | parcels_full_run_rate | 3.8 / 5 / 5.6 m parcels per year | -0.1805 | 4.936 | 5.116 | 3.864 | yes |
| 3 | hub_operating_fixed_cost | 0.7 / 0.9 / 1.2 EUR m per year | 4.337 | 1.57 | 2.767 | 1.484 | no |
| 4 | investment | 5.5 / 6 / 7.5 EUR m | 3.73 | 1.73 | 2 | 9.23 | no |
| 5 | discount_rate | 0.07 / 0.09 / 0.11 per year | 4.019 | 2.529 | 1.49 | 0.2091 | no |
| 6 | ramp_2027 | 0.4 / 0.6 / 0.8 share of full run-rate | 2.726 | 3.735 | 1.009 | -0.6804 | no |

## Inputs

| Driver | Value | Unit | Low | High | Source |
|---|---|---|---|---|---|
| parcels_full_run_rate | 5 | m parcels per year | 3.8 | 5.6 | 2025 network flow data, south region (Kestrel planning team) |
| ramp_2027 | 0.6 | share of full run-rate | 0.4 | 0.8 | ASSUMPTION: planning team, based on the 2023 north hub opening |
| saving_per_parcel | 0.55 | EUR per parcel | 0.4 | 0.65 | Network simulation v4; low = simulation with 2025 fuel prices, high = with 2023 fuel prices |
| hub_operating_fixed_cost | 0.9 | EUR m per year | 0.7 | 1.2 | Site lease offer plus 14 FTE staffing plan |
| investment | 6 | EUR m | 5.5 | 7.5 | Two supplier quotes, September 2026 |
| discount_rate | 0.09 | per year | 0.07 | 0.11 | Group finance |

## Line items (calculation order)

| Line item | Unit | Formula |
|---|---|---|
| ramp | share of full run-rate | `pick(t, 0, ramp_2027, 1, 1, 1, 1, 1, 1, 1)` |
| parcels_routed | m parcels | `parcels_full_run_rate * ramp` |
| saving_cash | EUR m | `parcels_routed * saving_per_parcel` |
| fixed_cost | EUR m | `-hub_operating_fixed_cost * min(1, t)` |
| capex | EUR m | `-investment * pick(t, 1, 0, 0, 0, 0, 0, 0, 0, 0)` |
| net_cash_flow | EUR m | `saving_cash + fixed_cost + capex` |
| cumulative_cash_flow | EUR m | `prev(cumulative_cash_flow) + net_cash_flow` |
| discount_factor | factor | `(1 + discount_rate) ** -t` |
| discounted_cash_flow | EUR m | `net_cash_flow * discount_factor` |

## Checks

| Check | Scenario | Expected | Actual | Status |
|---|---|---|---|---|
| parcels_within_capacity | base | >=0 | 0 | OK |
| parcels_within_capacity | down | >=0 | 0 | OK |
| parcels_within_capacity | up | >=0 | 0 | OK |
| parcels_within_capacity | competitor_response | >=0 | 0 | OK |
| ramp_not_negative | base | >=0 | 0 | OK |
| ramp_not_negative | down | >=0 | 0 | OK |
| ramp_not_negative | up | >=0 | 0 | OK |
| ramp_not_negative | competitor_response | >=0 | 0 | OK |
| ramp_not_above_one | base | >=0 | 0 | OK |
| ramp_not_above_one | down | >=0 | 0 | OK |
| ramp_not_above_one | up | >=0 | 0 | OK |
| ramp_not_above_one | competitor_response | >=0 | 0 | OK |
| net_cash_flow_ties_to_parts | base | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | down | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | up | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | competitor_response | ==0 | 0 | OK |

## Flags

- Drivers flagged as assumptions (no source or source starts with 'assumption'): ramp_2027

## Files

- `calc.csv`: every line item by period, base case
- `outputs.csv`: key outputs per scenario
- `checks.csv`: check results per scenario
- `sensitivity.csv`: tornado ranking and break-even values
- `model.xlsx`: Inputs (blue on yellow = input), Calc (live formulas), Outputs (live, master check), Sensitivity (values)


## File written by the run: model/calc.csv

line_item,unit,start,2027,2028,2029,2030,2031,2032,2033,2034
ramp,share of full run-rate,0.0,0.6,1.0,1.0,1.0,1.0,1.0,1.0,1.0
parcels_routed,m parcels,0.0,3.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0
saving_cash,EUR m,0.0,1.65,2.75,2.75,2.75,2.75,2.75,2.75,2.75
fixed_cost,EUR m,0.0,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9
capex,EUR m,-6.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
net_cash_flow,EUR m,-6.0,0.75,1.85,1.85,1.85,1.85,1.85,1.85,1.85
cumulative_cash_flow,EUR m,-6.0,-5.25,-3.4,-1.55,0.3,2.15,4.0,5.85,7.7
discount_factor,factor,1.0,0.9174311927,0.8416799933,0.7721834801,0.7084252111,0.6499313863,0.5962673269,0.5470342448,0.5018662797
discounted_cash_flow,EUR m,-6.0,0.6880733945,1.5571079875,1.4285394381,1.3105866405,1.2023730647,1.1030945547,1.012013353,0.9284526174


## File written by the run: model/checks.csv

check,scenario,expected,actual,status
parcels_within_capacity,base,>=0,0.0,OK
parcels_within_capacity,down,>=0,0.0,OK
parcels_within_capacity,up,>=0,0.0,OK
parcels_within_capacity,competitor_response,>=0,0.0,OK
ramp_not_negative,base,>=0,0.0,OK
ramp_not_negative,down,>=0,0.0,OK
ramp_not_negative,up,>=0,0.0,OK
ramp_not_negative,competitor_response,>=0,0.0,OK
ramp_not_above_one,base,>=0,0.0,OK
ramp_not_above_one,down,>=0,0.0,OK
ramp_not_above_one,up,>=0,0.0,OK
ramp_not_above_one,competitor_response,>=0,0.0,OK
net_cash_flow_ties_to_parts,base,==0,0.0,OK
net_cash_flow_ties_to_parts,down,==0,0.0,OK
net_cash_flow_ties_to_parts,up,==0,0.0,OK
net_cash_flow_ties_to_parts,competitor_response,==0,0.0,OK


## File written by the run: model/inputs.csv

driver,value,unit,source,low,high,note
parcels_full_run_rate,5.0,m parcels per year,"2025 network flow data, south region (Kestrel planning team)",3.8,5.6,full run-rate volume once ramp is complete
ramp_2027,0.60,share of full run-rate,"ASSUMPTION: planning team, based on the 2023 north hub opening",0.40,0.80,"value is sourced; the 0.40-0.80 range is our own illustrative spread since no range was quoted - ask planning for the actual north-hub ramp curve to replace it"
saving_per_parcel,0.55,EUR per parcel,"Network simulation v4; low = simulation with 2025 fuel prices, high = with 2023 fuel prices",0.40,0.65,shorter line-haul and fewer handlings
hub_operating_fixed_cost,0.9,EUR m per year,Site lease offer plus 14 FTE staffing plan,0.7,1.2,charged every operating year 2027-2034 in full (not ramped)
investment,6.0,EUR m,"Two supplier quotes, September 2026",5.5,7.5,paid at the start of 2027 (t=0)
discount_rate,0.09,per year,Group finance,0.07,0.11,CFO hurdle rate


## File written by the run: model/outputs.csv

output,unit,base,down,up,competitor_response,model_version
npv,EUR m,3.2302410504,-1.8409834649,8.9365883808,-4.626210314,v01
irr,per year,0.2091368125,0.0093934279,0.3864734957,-0.0993929701,v01
payback_period,year,2030,2034,2029,,v01
parcels_routed_2027,m parcels,3.0,2.28,3.36,2.28,v01
parcels_routed_2028,m parcels,5.0,3.8,5.6,3.8,v01


## File written by the run: model/sensitivity.csv

rank,driver,unit,low,base,high,output_low,output_base,output_high,swing,break_even,break_even_in_range
1,saving_per_parcel,EUR per parcel,0.4,0.55,0.65,-0.6456439279,3.2302410504,5.8141643692,6.4598082971,0.4249869616,yes
2,parcels_full_run_rate,m parcels per year,3.8,5.0,5.6,-0.1805377305,3.2302410504,4.9356304408,5.1161681713,3.8635178329,yes
3,hub_operating_fixed_cost,EUR m per year,0.7,0.9,1.2,4.3372048733,3.2302410504,1.5697953159,2.7674095574,1.483621792,no
4,investment,EUR m,5.5,6.0,7.5,3.7302410504,3.2302410504,1.7302410504,2.0,9.2302410504,no
5,discount_rate,per year,0.07,0.09,0.11,4.0188648533,3.2302410504,2.5293361167,1.4895287366,0.2091368125,no
6,ramp_2027,share of full run-rate,0.4,0.6,0.8,2.7256538944,3.2302410504,3.7348282063,1.0091743119,-0.680350089,no


## File written by the run: model/spec.json

{
  "title": "Kestrel south hub cross-dock business case (fictional)",
  "question": "Should Kestrel invest in a cross-dock hub in the south region? Decision rule: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life (2027-2034); investment paid at the start of 2027 (t=0), operating cash flows at year-end 2027-2034, no terminal value, no tax.",
  "periods": ["start", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034"],
  "rows": [
    {"name": "ramp", "unit": "share of full run-rate", "expr": "pick(t, 0, ramp_2027, 1, 1, 1, 1, 1, 1, 1)"},
    {"name": "parcels_routed", "unit": "m parcels", "expr": "parcels_full_run_rate * ramp"},
    {"name": "saving_cash", "unit": "EUR m", "expr": "parcels_routed * saving_per_parcel"},
    {"name": "fixed_cost", "unit": "EUR m", "expr": "-hub_operating_fixed_cost * min(1, t)"},
    {"name": "capex", "unit": "EUR m", "expr": "-investment * pick(t, 1, 0, 0, 0, 0, 0, 0, 0, 0)"},
    {"name": "net_cash_flow", "unit": "EUR m", "expr": "saving_cash + fixed_cost + capex"},
    {"name": "cumulative_cash_flow", "unit": "EUR m", "expr": "prev(cumulative_cash_flow) + net_cash_flow"},
    {"name": "discount_factor", "unit": "factor", "expr": "(1 + discount_rate) ** -t"},
    {"name": "discounted_cash_flow", "unit": "EUR m", "expr": "net_cash_flow * discount_factor"}
  ],
  "outputs": [
    {"name": "npv", "label": "NPV at hurdle rate", "unit": "EUR m", "fn": "sum", "row": "discounted_cash_flow"},
    {"name": "irr", "label": "IRR", "unit": "per year", "fn": "irr", "row": "net_cash_flow"},
    {"name": "payback_period", "label": "Payback (first year cumulative cash >= 0)", "unit": "year", "fn": "payback", "row": "cumulative_cash_flow"},
    {"name": "parcels_routed_2027", "label": "Parcels routed, 2027 (ramp year)", "unit": "m parcels", "fn": "value", "row": "parcels_routed", "period": "2027"},
    {"name": "parcels_routed_2028", "label": "Parcels routed, 2028 (full run-rate)", "unit": "m parcels", "fn": "value", "row": "parcels_routed", "period": "2028"}
  ],
  "checks": [
    {"name": "parcels_within_capacity", "expr": "parcels_full_run_rate - parcels_routed", "rule": ">=0"},
    {"name": "ramp_not_negative", "expr": "ramp", "rule": ">=0"},
    {"name": "ramp_not_above_one", "expr": "1 - ramp", "rule": ">=0"},
    {"name": "net_cash_flow_ties_to_parts", "expr": "net_cash_flow - saving_cash - fixed_cost - capex", "rule": "==0"}
  ],
  "scenarios": {
    "down": {"parcels_full_run_rate": 3.8, "hub_operating_fixed_cost": 1.2},
    "up": {"parcels_full_run_rate": 5.6, "saving_per_parcel": 0.65, "hub_operating_fixed_cost": 0.7},
    "competitor_response": {"parcels_full_run_rate": 3.8, "saving_per_parcel": 0.40, "investment": 7.5}
  },
  "scenario_stories": {
    "down": "generic downside: south volumes land at the bottom of the quoted flow range and the lease/staffing cost comes in at the top of its range; saving per parcel and investment unchanged",
    "up": "generic upside: south volumes land at the top of the flow range, a high-fuel-cost environment raises the value of consolidation, and the site is run lean",
    "competitor_response": "planning team's note, quantified: a rival hub opens nearby, shippers partially defect (volume at the low end of the range), the price response that follows erodes the saving per parcel (also to the low end of its range), and Kestrel accelerates the fit-out to respond, pushing investment to the top of the two quotes. No distinct figures were supplied for this case; it reuses the already-quoted low/high ends of the three affected drivers, which is itself an assumption about the mapping, flagged separately"
  },
  "break_even": {"output": "npv", "target": 0}
}

