# fm-01-hub-business-case on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (12/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the question, outputs, and decision threshold before building | yes | README.md opens with 'Question: Should Kestrel invest EUR 6.0m in a cross-dock hub in the south region? Threshold: NPV at the 9% hurdle rate above zero...' before any build/calc detail; deck.md SCQA states Question/Answer up front. |
| Separates inputs, calculations and outputs; no stray numbers in formulas | yes | inputs.csv, calc.csv, outputs.csv are separate files; spec.json formulas only use 0/1 literals, e.g. 'pick(t, 0, ramp_2027, 1, 1, 1, 1, 1, 1, 1)' and '(1 + discount_rate) ** -t'. |
| Base NPV within EUR 3.1m–3.4m and payback in 2030/year 4 | yes | outputs.csv: npv base = 3.2302410504; payback_undiscounted base = 2030. |
| Tornado ranking with saving per parcel first and parcels routed second | yes | sensitivity.csv rank 1 = saving_per_parcel, rank 2 = volume_full_run_rate; deck slide 4 tornado shows same order. |
| Break-even values given for saving per parcel (~0.42–0.43) and parcels (~3.8–3.9m), both flagged inside range | yes | sensitivity.csv: saving_per_parcel break_even=0.4249869616 (yes); volume_full_run_rate break_even=3.8635178329 (yes); README states both 'inside'. |
| Because break-even is inside range, it's placed in the headline/decided-by line, not only an appendix | yes | Answer headline: 'both with break-evens *inside* their evidenced ranges — meaning the base case isn't a safe margin'; deck slide 2 title: 'the margin rests on two drivers whose break-evens sit inside the plausible range'. |
| Down case is a coherent story (competitor hub: fewer parcels, lower saving, higher investment), NPV reported negative | yes | spec.json scenario_stories.down: 'a competitor opens a hub nearby: fewer shippers route through Kestrel, the price response... eats much of the per-parcel saving, and the accelerated fit-out costs more'; outputs.csv npv down = -4.626210314. |
| Checks block and two outputs recomputed by hand, both numbers recorded | yes | README.md 'Spot test: NPV: model EUR 3.2302m, by hand EUR 3.2302m...; payback (undiscounted): model 2030 (t=4), by hand 2030...'; checks.csv present with 12 OK checks. |
| Lists the 60% ramp as a flagged assumption | yes | README.md Flags section: 'Drivers flagged as assumptions... ramp_2027'; inputs.csv source 'ASSUMPTION: planning team; based on the 2023 north hub opening'. |
| 'What the deck should say' sentences carry the model version | yes | README.md: '**What the deck should say:** ... (Kestrel south hub model v01.)' |
| Must not present NPV without range or scenarios | yes | Every NPV mention (answer message, deck, README) is accompanied by down/up scenario values, e.g. '+EUR 3.2m (base) — down case -EUR 4.6m, up case +EUR 8.3m'. |
| Must not add terminal value or tax without flagging departure from conventions | yes | Model explicitly follows agreed conventions: 'no terminal value taken beyond 2034; no tax in this screening model' — no terminal value or tax was added. |

## Transcript

## Turn 1

**User:** Build the business case for the Kestrel south hub from these inputs. Board needs NPV, payback and what decides the answer. (Attached in the working directory: fm-01-input.md.)

All built and checked. Here's the business case for the board:

**Answer: approve, but the margin is thin.**

- **NPV at 9%:** +EUR 3.2m (base) — down case -EUR 4.6m, up case +EUR 8.3m
- **Payback:** 2030 undiscounted (year 4 of 8), 2031 discounted (year 5 of 8) — well inside the 8-year life
- **IRR:** 21% (vs. the 9% hurdle)

**What decides it:** two drivers, ranked by NPV swing, both with break-evens *inside* their evidenced ranges — meaning the base case isn't a safe margin, not a settled answer:
1. **Saving per parcel** — break-even EUR 0.43, evidenced range EUR 0.40–0.65
2. **Full run-rate volume** — break-even 3.9m parcels, evidenced range 3.8–5.6m

Opex, investment cost and the discount rate are *not* deciding — their break-evens sit outside the given ranges. The planning team's own named risk (a competitor hub opening nearby, which hits volume, saving *and* fit-out cost together) reproduces almost exactly as the down case: NPV -EUR 4.6m.

**Files delivered** (in the working directory):
- `model/` — inputs.csv, spec.json, calc.csv, outputs.csv, checks.csv, sensitivity.csv, `model.xlsx` (live formulas), and README.md with the hand-off summary, spot-test (hand-checked against the model), and flagged assumptions
- `deck.md` / `deck.html` / `deck.pptx` — 6-page board deck plus appendix, same numbers as the model

Two things worth flagging before this goes to the board: I assumed the hub reaches 100% of full run-rate from 2028 onward (the input only states the 2027 ramp at 60%) — if that takes longer, NPV and payback both slip. And I proposed a board date, owner, and next-step owners since the input didn't name any — those need confirming, not rubber-stamping.


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
html,body{height:100%;background:#2B2F36;font-family:Helvetica Neue, Helvetica, Arial, sans-serif;color:var(--text)}
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
<body><div id="stage"><section class="slide l-title" id="s1" data-title="Should Kestrel invest EUR 6.0m in the south region cross-dock hub?"><div class="t-client">Kestrel Logistics (fictional)</div><h1 class="t-title">Should Kestrel invest EUR 6.0m in the south region cross-dock hub?</h1><p class="t-sub">NPV, payback and the two drivers that decide the answer</p><p class="t-meta">Board of directors, pre-read for the December 2026 board meeting (date proposed) | October 2026</p><footer><div></div><span class="pn">1</span></footer><aside class="notes"><b>Speaker note</b> Pre-read for the December 2026 board meeting (date proposed; confirm with the board secretary).</aside></section><section class="slide l-summary" id="s2" data-title="Approve the EUR 6.0m south hub: NPV of EUR 3.2m at the 9% hurdle, but the margin rests on two drivers whose break-evens sit inside the plausible range"><div class="tracker">Executive summary</div><h2 class="title long">Approve the EUR 6.0m south hub: NPV of EUR 3.2m at the 9% hurdle, but the margin rests on two drivers whose break-evens sit inside the plausible range</h2><div class="content summary"><p class="lead">The south hub earns back the EUR 6.0m investment and clears the CFO&#x27;s 9% hurdle rate in the base case over its eight-year life (2027-2034), but the margin is thin enough that the two most uncertain drivers can flip the answer within their own evidenced ranges.</p><ol><li>Base case clears the hurdle: NPV +EUR 3.2m at 9%, IRR 21%; cumulative cash flow turns positive by 2030 (undiscounted) and 2031 (discounted) — within the eight-year life.</li><li>The answer is decided by two drivers: saving per routed parcel (break-even EUR 0.43, inside the EUR 0.40 to 0.65 evidenced range) and full run-rate volume (break-even 3.9m parcels, inside the 3.8m to 5.6m evidenced range).</li><li>The one risk the planning team names explicitly — a competitor hub opening nearby — moves both drivers down together and raises the investment cost; combined, NPV turns negative at -EUR 4.6m.</li><li>Cost and financing risk are secondary: operating cost, investment cost and the discount rate would each have to move past the high end of their estimated range to erase the NPV.</li></ol><div class="ask">Decision requested at the December 2026 board meeting (date proposed): approve EUR 6.0m for the south hub (owner: VP Network Operations, proposed; start 1 January 2027). The answer changes if evidence firms up below EUR 0.43 saving per parcel or 3.9m parcels of full run-rate volume.</div></div><footer><div class="source">Source: Kestrel south hub model v01 (this case), built from fm-01-input.md</div><span class="pn">2</span></footer><aside class="notes"><b>Speaker note</b> Read the bold line and the ask. Pages 3 to 6 prove each point.</aside></section><section class="slide l-chart" id="s3" data-title="Cumulative discounted cash flow turns positive in 2031, three years before the hub&#x27;s eight-year life ends in 2034"><div class="tracker">1 Base case</div><h2 class="title long">Cumulative discounted cash flow turns positive in 2031, three years before the hub&#x27;s eight-year life ends in 2034</h2><div class="header">Cumulative discounted cash flow, EUR m, start of 2027 to end of 2034, discounted at the 9% hurdle rate</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Cumulative discounted cash flow turns positive in 2031, three years before the hub&#x27;s eight-year life ends in 2034"><text x="46.0" y="365.0" font-size="13" text-anchor="end" fill="#B8C0CC" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-6</text><text x="46.0" y="200.0" font-size="13" text-anchor="end" fill="#B8C0CC" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-1</text><text x="46.0" y="35.0" font-size="13" text-anchor="end" fill="#B8C0CC" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">4</text><line x1="56" x2="510" y1="360.0" y2="360.0" stroke="#B8C0CC"/><text x="56.0" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Start 2027</text><text x="112.8" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2027</text><text x="169.5" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2028</text><text x="226.2" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2029</text><text x="283.0" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2030</text><text x="339.8" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2031</text><text x="396.5" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2032</text><text x="453.2" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2033</text><text x="510.0" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">End 2034</text><line x1="56.0" x2="510.0" y1="162.0" y2="162.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="518.0" y="167.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Break-even (NPV = 0)</text><polyline points="56.0,360.0 112.8,336.9 169.5,287.4 226.2,237.9 283.0,195.0 339.8,155.4 396.5,119.1 453.2,86.1 510.0,56.4" fill="none" stroke="#D9822B" stroke-width="3.5"/><circle cx="56.0" cy="360.0" r="4" fill="#D9822B"/><text x="56.0" y="348.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-6.0</text><circle cx="112.8" cy="336.9" r="4" fill="#D9822B"/><text x="112.8" y="324.9" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-5.3</text><circle cx="169.5" cy="287.4" r="4" fill="#D9822B"/><text x="169.5" y="275.4" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-3.8</text><circle cx="226.2" cy="237.9" r="4" fill="#D9822B"/><text x="226.2" y="225.9" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-2.3</text><circle cx="283.0" cy="195.0" r="4" fill="#D9822B"/><text x="283.0" y="183.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-1.0</text><circle cx="339.8" cy="155.4" r="4" fill="#D9822B"/><text x="339.8" y="143.4" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">0.2</text><circle cx="396.5" cy="119.1" r="4" fill="#D9822B"/><text x="396.5" y="107.1" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1.3</text><circle cx="453.2" cy="86.1" r="4" fill="#D9822B"/><text x="453.2" y="74.1" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.3</text><circle cx="510.0" cy="56.4" r="4" fill="#D9822B"/><text x="510.0" y="44.4" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.2</text></svg></div><div class="side"><ul><li>Undiscounted payback: 2030 (year 4 of 8); discounted payback at 9%: 2031 (year 5 of 8)</li><li>NPV at end of 2034, discounted at 9%: EUR +3.2m; IRR 21%</li><li>EUR 6.0m investment (two supplier quotes, September 2026) paid at the start of 2027; no terminal value taken beyond 2034; no tax in this screening model</li></ul></div></div><footer><div class="source">Source: Kestrel south hub model v01, cumulative_discounted_cash_flow row</div><span class="pn">3</span></footer><aside class="notes"><b>Speaker note</b> The curve reflects the agreed 60% ramp in 2027 reaching full run-rate from 2028 (ramp path beyond 2027 is not stated in the input; flagged in the appendix).</aside></section><section class="slide l-chart" id="s4" data-title="Saving per parcel and full run-rate volume decide the answer: both break-evens sit inside the evidenced range"><div class="tracker">2 What decides the answer</div><h2 class="title long">Saving per parcel and full run-rate volume decide the answer: both break-evens sit inside the evidenced range</h2><div class="header">NPV swing from each driver&#x27;s low to high value, EUR m, base case NPV = EUR 3.2m</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Saving per parcel and full run-rate volume decide the answer: both break-evens sit inside the evidenced range"><rect x="208" y="23.4" width="342.9" height="43.0" fill="#D9822B"/><text x="558.9" y="50.4" font-size="15" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6.5</text><text x="196.0" y="51.4" font-size="15" text-anchor="end" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Saving per parcel</text><rect x="208" y="100.2" width="269.0" height="43.0" fill="#B8C0CC"/><text x="485.0" y="127.2" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">5.1</text><text x="196.0" y="128.2" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Full run-rate volume</text><rect x="208" y="177.0" width="147.7" height="43.0" fill="#B8C0CC"/><text x="363.7" y="204.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.8</text><text x="196.0" y="205.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Hub operating fixed cost</text><rect x="208" y="253.8" width="105.5" height="43.0" fill="#B8C0CC"/><text x="321.5" y="280.8" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.0</text><text x="196.0" y="281.8" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Investment cost</text><rect x="208" y="330.6" width="79.1" height="43.0" fill="#B8C0CC"/><text x="295.1" y="357.6" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1.5</text><text x="196.0" y="358.6" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Discount rate</text><line x1="208" x2="208" y1="8" y2="392.0" stroke="#14213D"/></svg></div><div class="side"><ul><li>Saving per parcel: NPV ranges from -EUR 0.6m (at EUR 0.40) to +EUR 5.8m (at EUR 0.65); break-even EUR 0.43 per parcel — inside the EUR 0.40 to 0.65 evidenced range</li><li>Full run-rate volume: NPV ranges from -EUR 0.2m (at 3.8m parcels) to +EUR 4.9m (at 5.6m parcels); break-even 3.9m parcels — inside the 3.8m to 5.6m evidenced range</li><li>Hub operating cost, investment cost and the discount rate would each have to move past the high end of their estimated range to erase the NPV (break-evens of EUR 1.5m a year, EUR 9.2m and 21% respectively)</li><li>Cheapest evidence to settle this before commitment: re-run the saving-per-parcel simulation on the current fuel price curve rather than the 2023-2025 spread, and check 2026 year-to-date network flow data or firm shipper volume commitments for the south region</li></ul></div></div><footer><div class="source">Source: Kestrel south hub model v01, sensitivity.csv (one-way on NPV, other drivers held at base)</div><span class="pn">4</span></footer><aside class="notes"><b>Speaker note</b> Ramp in 2027 (60%) has no low/high range in the input and is not tested here; it is flagged in the appendix.</aside></section><section class="slide l-chart" id="s5" data-title="If a nearby competitor opens its own hub, as the planning team warns, NPV turns negative at -EUR 4.6m"><div class="tracker">3 Downside risk</div><h2 class="title long">If a nearby competitor opens its own hub, as the planning team warns, NPV turns negative at -EUR 4.6m</h2><div class="header">NPV by scenario, EUR m, versus the zero break-even</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="If a nearby competitor opens its own hub, as the planning team warns, NPV turns negative at -EUR 4.6m"><line x1="8.0" x2="542.0" y1="241.3" y2="241.3" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="550.0" y="246.3" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Break-even</text><rect x="41.8" y="241.3" width="106.4" height="98.1" fill="#D9822B"/><text x="95.0" y="357.5" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-4.6</text><text x="97.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Down (competitor hub)</text><rect x="219.8" y="173.1" width="106.4" height="68.3" fill="#B8C0CC"/><text x="273.0" y="165.1" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.2</text><text x="275.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base case</text><rect x="397.8" y="64.3" width="106.4" height="177.1" fill="#B8C0CC"/><text x="451.0" y="56.3" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">8.3</text><text x="453.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Up (no competitor</text><text x="453.0" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">move)</text><line x1="8" x2="542" y1="241.3" y2="241.3" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Down case: full run-rate volume falls to 3.8m parcels, saving per parcel falls to EUR 0.40 as the competitor&#x27;s price response bites, and the accelerated fit-out costs EUR 7.5m — three moves with one cause, not three independent worst cases</li><li>Up case: volume reaches 5.6m parcels, saving per parcel holds at EUR 0.65 (2023 fuel-price level), and fit-out comes in at the lower EUR 5.5m supplier quote</li><li>The down case is the scenario to monitor for an early warning, not a remote tail risk</li></ul></div></div><footer><div class="source">Source: Kestrel south hub model v01, outputs.csv (scenarios: down, up); planning team note on competitor response</div><span class="pn">5</span></footer><aside class="notes"><b>Speaker note</b> The planning team&#x27;s own words: &quot;If a competitor opens its own hub nearby, some shippers move and we would route fewer parcels; they would also force a price response that eats part of the saving, and the fit-out would cost more because we would accelerate it.&quot;</aside></section><section class="slide l-table" id="s6" data-title="Approve now, with a checkpoint to confirm volume and saving-per-parcel evidence before the larger spend"><div class="tracker">Decision and next steps</div><h2 class="title long">Approve now, with a checkpoint to confirm volume and saving-per-parcel evidence before the larger spend</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Step</th><th>Owner (proposed)</th><th>By when</th></tr><tr><td>Board approves the EUR 6.0m investment</td><td>Board</td><td>December 2026 (date proposed)</td></tr><tr><td>Confirm south region volume against 2026 flow data and firm shipper commitments</td><td>VP Network Operations (proposed)</td><td>Q1 2027, before fit-out starts</td></tr><tr><td>Re-run the saving-per-parcel simulation on the current fuel price curve</td><td>Network simulation team (proposed)</td><td>Q1 2027, before fit-out starts</td></tr><tr><td>Go/no-go checkpoint against updated volume and saving evidence</td><td>CFO (proposed)</td><td>Q1 2027, before fit-out spend is committed</td></tr></table></div><div class="side"><ul><li>Risk: a competitor opens a hub in the south region, moving volume, saving and investment cost together (page 5)</li><li>Risk: the 2027 ramp (60%) is a planning-team assumption based on the 2023 north hub opening, with no tested range; a slower ramp or a lower post-launch run-rate pushes payback later than 2030/2031</li><li>Owners and dates above are proposed by this case; the input named neither and they need confirmation</li></ul></div></div><footer><div class="source">Source: Team plan; thresholds from Kestrel south hub model v01 sensitivities</div><span class="pn">6</span></footer><aside class="notes"><b>Speaker note</b> Ask for the decision explicitly; offer the Q1 2027 checkpoint as the point to walk away before the larger fit-out spend is committed.</aside></section><section class="slide l-table" id="s7" data-title="Inputs and flagged assumptions"><div class="tracker">Appendix</div><h2 class="title">Inputs and flagged assumptions</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Driver</th><th>Value</th><th>Low</th><th>High</th><th>Source</th></tr><tr><td>Full run-rate volume</td><td>5.0m parcels/year</td><td>3.8</td><td>5.6</td><td>2025 network flow data, south region (Kestrel planning team)</td></tr><tr><td>Ramp in 2027</td><td>60% of full run-rate</td><td>-</td><td>-</td><td>ASSUMPTION: planning team, based on the 2023 north hub opening</td></tr><tr><td>Saving per routed parcel</td><td>EUR 0.55/parcel</td><td>0.40</td><td>0.65</td><td>Network simulation v4; low/high = 2025/2023 fuel price scenarios</td></tr><tr><td>Hub operating fixed cost</td><td>EUR 0.9m/year</td><td>0.7</td><td>1.2</td><td>Site lease offer plus 14 FTE staffing plan</td></tr><tr><td>Investment</td><td>EUR 6.0m</td><td>5.5</td><td>7.5</td><td>Two supplier quotes, September 2026</td></tr><tr><td>Hurdle rate</td><td>9%/year</td><td>7%</td><td>11%</td><td>Group finance</td></tr></table></div><div class="side"><ul><li>ASSUMPTION, not stated in the input: full run-rate (100%) is reached from 2028 onward. The input gives only the 2027 ramp (60%); if full run-rate is reached later, both NPV and payback move out.</li><li>Ramp in 2027 has no low/high range in the input and is not tested in the sensitivity ranking on page 4.</li><li>Audience, the December 2026 board meeting date, and the task owners on page 6 are proposed by this case, not stated in the input.</li><li>Conventions agreed with finance and used throughout: EUR m; investment at the start of 2027 (t=0); operating cash flows at the end of each year 2027-2034, discounted 1 to 8 years; no terminal value; no tax.</li></ul></div></div><footer><div class="source">Source: fm-01-input.md; Kestrel south hub model v01</div><span class="pn">A1</span></footer></section></div>
<div id="overview"><h1>Titles-only read-through</h1><ol><li>Should Kestrel invest EUR 6.0m in the south region cross-dock hub? <span style='color:#8A93A3'>(1)</span></li><li>Approve the EUR 6.0m south hub: NPV of EUR 3.2m at the 9% hurdle, but the margin rests on two drivers whose break-evens sit inside the plausible range <span style='color:#8A93A3'>(2)</span></li><li>Cumulative discounted cash flow turns positive in 2031, three years before the hub&#x27;s eight-year life ends in 2034 <span style='color:#8A93A3'>(3)</span></li><li>Saving per parcel and full run-rate volume decide the answer: both break-evens sit inside the evidenced range <span style='color:#8A93A3'>(4)</span></li><li>If a nearby competitor opens its own hub, as the planning team warns, NPV turns negative at -EUR 4.6m <span style='color:#8A93A3'>(5)</span></li><li>Approve now, with a checkpoint to confirm volume and saving-per-parcel evidence before the larger spend <span style='color:#8A93A3'>(6)</span></li><li>Inputs and flagged assumptions <span style='color:#8A93A3'>(A1)</span></li></ol></div>
<div id="hint">arrows: navigate | t: titles | n: notes | print: PDF</div>
<script>
(function(){
var slides=[].slice.call(document.querySelectorAll('.slide')),i=0,stage=document.getElementById('stage');
function fit(){var s=Math.min(innerWidth/1280,innerHeight/720);stage.style.transform='translate('+((innerWidth-1280*s)/2)+'px,'+((innerHeight-720*s)/2)+'px) scale('+s+')';}
function show(n){i=Math.max(0,Math.min(slides.length-1,n));slides.forEach(function(el,k){el.classList.toggle('active',k===i);});history.replaceState(null,'','#'+(i+1));}
addEventListener('resize',fit);
addEventListener('keydown',function(e){
 var k=e.key;
 if(k==='ArrowRight'||k==='PageDown'||k===' '||k==='Enter'){show(i+1);e.preventDefault();}
 else if(k==='ArrowLeft'||k==='PageUp'||k==='Backspace'){show(i-1);e.preventDefault();}
 else if(k==='Home'){show(0);}else if(k==='End'){show(slides.length-1);}
 else if(k==='t'){document.body.classList.toggle('overview');}
 else if(k==='n'){document.body.classList.toggle('shownotes');}
 else if(k==='Escape'){document.body.classList.remove('overview');}
});
[].slice.call(document.querySelectorAll('#overview li')).forEach(function(li,k){li.addEventListener('click',function(){document.body.classList.remove('overview');show(k);});});
fit();show((parseInt(location.hash.slice(1),10)||1)-1);
})();
</script></body></html>


## File written by the run: deck.md

---
title: Kestrel south hub business case
client: Kestrel Logistics (fictional)
audience: Board of directors, pre-read for the December 2026 board meeting (date proposed)
date: October 2026
format: deck
theme:
  text: "#14213D"
  accent: "#D9822B"
  muted: "#B8C0CC"
  light: "#E8EBF0"
  background: "#FFFFFF"
  font: "Helvetica Neue, Helvetica, Arial, sans-serif"
---

# Deck: Should Kestrel invest in the south region cross-dock hub?

*Fictional company; all figures, people and documents invented for evaluation (per fm-01-input.md).*

**Opening (SCQA)**
- Situation: Kestrel routes south-region parcels without a dedicated cross-dock hub, carrying longer line-hauls and more handlings than a hub would allow.
- Complication: A south hub would cost EUR 6.0m to build and EUR 0.9m a year to run; the CFO will only approve it if NPV at the 9% hurdle rate is positive over the hub's eight-year life (2027-2034).
- Question: Should Kestrel invest in the south region cross-dock hub?
- Answer: Yes in the base case (NPV +EUR 3.2m), but the answer is decided by two drivers — saving per parcel and full run-rate volume — whose break-evens sit inside the plausible range.

**Key line**
1. The base case clears the hurdle: NPV +EUR 3.2m at 9%, IRR 21%, payback within the eight-year life.
2. Saving per routed parcel and full run-rate volume decide the answer; both break-evens sit inside their evidenced ranges.
3. The one risk the planning team names explicitly — a nearby competitor hub — would turn the answer negative (NPV -EUR 4.6m) if it happens.

## 1. Should Kestrel invest EUR 6.0m in the south region cross-dock hub?
layout: title
subtitle: NPV, payback and the two drivers that decide the answer
note: Pre-read for the December 2026 board meeting (date proposed; confirm with the board secretary).

## 2. Approve the EUR 6.0m south hub: NPV of EUR 3.2m at the 9% hurdle, but the margin rests on two drivers whose break-evens sit inside the plausible range
layout: summary
tracker: Executive summary
lead: The south hub earns back the EUR 6.0m investment and clears the CFO's 9% hurdle rate in the base case over its eight-year life (2027-2034), but the margin is thin enough that the two most uncertain drivers can flip the answer within their own evidenced ranges.
body:
- Base case clears the hurdle: NPV +EUR 3.2m at 9%, IRR 21%; cumulative cash flow turns positive by 2030 (undiscounted) and 2031 (discounted) — within the eight-year life.
- The answer is decided by two drivers: saving per routed parcel (break-even EUR 0.43, inside the EUR 0.40 to 0.65 evidenced range) and full run-rate volume (break-even 3.9m parcels, inside the 3.8m to 5.6m evidenced range).
- The one risk the planning team names explicitly — a competitor hub opening nearby — moves both drivers down together and raises the investment cost; combined, NPV turns negative at -EUR 4.6m.
- Cost and financing risk are secondary: operating cost, investment cost and the discount rate would each have to move past the high end of their estimated range to erase the NPV.
ask: Decision requested at the December 2026 board meeting (date proposed): approve EUR 6.0m for the south hub (owner: VP Network Operations, proposed; start 1 January 2027). The answer changes if evidence firms up below EUR 0.43 saving per parcel or 3.9m parcels of full run-rate volume.
source: Kestrel south hub model v01 (this case), built from fm-01-input.md
note: Read the bold line and the ask. Pages 3 to 6 prove each point.

## 3. Cumulative discounted cash flow turns positive in 2031, three years before the hub's eight-year life ends in 2034
layout: chart
tracker: 1 Base case
message: time-series
chart: line
header: Cumulative discounted cash flow, EUR m, start of 2027 to end of 2034, discounted at the 9% hurdle rate
reference: 0 | Break-even (NPV = 0)
highlight: Cumulative discounted cash flow
| Period | Cumulative discounted cash flow |
|---|---|
| Start 2027 | -6.0 |
| End 2027 | -5.3 |
| End 2028 | -3.8 |
| End 2029 | -2.3 |
| End 2030 | -1.0 |
| End 2031 | 0.2 |
| End 2032 | 1.3 |
| End 2033 | 2.3 |
| End 2034 | 3.2 |
body:
- Undiscounted payback: 2030 (year 4 of 8); discounted payback at 9%: 2031 (year 5 of 8)
- NPV at end of 2034, discounted at 9%: EUR +3.2m; IRR 21%
- EUR 6.0m investment (two supplier quotes, September 2026) paid at the start of 2027; no terminal value taken beyond 2034; no tax in this screening model
source: Kestrel south hub model v01, cumulative_discounted_cash_flow row
note: The curve reflects the agreed 60% ramp in 2027 reaching full run-rate from 2028 (ramp path beyond 2027 is not stated in the input; flagged in the appendix).

## 4. Saving per parcel and full run-rate volume decide the answer: both break-evens sit inside the evidenced range
layout: chart
tracker: 2 What decides the answer
message: ranking
chart: hbar
header: NPV swing from each driver's low to high value, EUR m, base case NPV = EUR 3.2m
highlight: Saving per parcel
| Driver | NPV swing (high minus low) |
|---|---|
| Saving per parcel | 6.5 |
| Full run-rate volume | 5.1 |
| Hub operating fixed cost | 2.8 |
| Investment cost | 2.0 |
| Discount rate | 1.5 |
body:
- Saving per parcel: NPV ranges from -EUR 0.6m (at EUR 0.40) to +EUR 5.8m (at EUR 0.65); break-even EUR 0.43 per parcel — inside the EUR 0.40 to 0.65 evidenced range
- Full run-rate volume: NPV ranges from -EUR 0.2m (at 3.8m parcels) to +EUR 4.9m (at 5.6m parcels); break-even 3.9m parcels — inside the 3.8m to 5.6m evidenced range
- Hub operating cost, investment cost and the discount rate would each have to move past the high end of their estimated range to erase the NPV (break-evens of EUR 1.5m a year, EUR 9.2m and 21% respectively)
- Cheapest evidence to settle this before commitment: re-run the saving-per-parcel simulation on the current fuel price curve rather than the 2023-2025 spread, and check 2026 year-to-date network flow data or firm shipper volume commitments for the south region
source: Kestrel south hub model v01, sensitivity.csv (one-way on NPV, other drivers held at base)
note: Ramp in 2027 (60%) has no low/high range in the input and is not tested here; it is flagged in the appendix.

## 5. If a nearby competitor opens its own hub, as the planning team warns, NPV turns negative at -EUR 4.6m
layout: chart
tracker: 3 Downside risk
message: deviation
chart: bar
header: NPV by scenario, EUR m, versus the zero break-even
reference: 0 | Break-even
highlight: Down (competitor hub)
| Scenario | NPV |
|---|---|
| Down (competitor hub) | -4.6 |
| Base case | 3.2 |
| Up (no competitor move) | 8.3 |
body:
- Down case: full run-rate volume falls to 3.8m parcels, saving per parcel falls to EUR 0.40 as the competitor's price response bites, and the accelerated fit-out costs EUR 7.5m — three moves with one cause, not three independent worst cases
- Up case: volume reaches 5.6m parcels, saving per parcel holds at EUR 0.65 (2023 fuel-price level), and fit-out comes in at the lower EUR 5.5m supplier quote
- The down case is the scenario to monitor for an early warning, not a remote tail risk
source: Kestrel south hub model v01, outputs.csv (scenarios: down, up); planning team note on competitor response
note: The planning team's own words: "If a competitor opens its own hub nearby, some shippers move and we would route fewer parcels; they would also force a price response that eats part of the saving, and the fit-out would cost more because we would accelerate it."

## 6. Approve now, with a checkpoint to confirm volume and saving-per-parcel evidence before the larger spend
layout: table
tracker: Decision and next steps
| Step | Owner (proposed) | By when |
|---|---|---|
| Board approves the EUR 6.0m investment | Board | December 2026 (date proposed) |
| Confirm south region volume against 2026 flow data and firm shipper commitments | VP Network Operations (proposed) | Q1 2027, before fit-out starts |
| Re-run the saving-per-parcel simulation on the current fuel price curve | Network simulation team (proposed) | Q1 2027, before fit-out starts |
| Go/no-go checkpoint against updated volume and saving evidence | CFO (proposed) | Q1 2027, before fit-out spend is committed |
body:
- Risk: a competitor opens a hub in the south region, moving volume, saving and investment cost together (page 5)
- Risk: the 2027 ramp (60%) is a planning-team assumption based on the 2023 north hub opening, with no tested range; a slower ramp or a lower post-launch run-rate pushes payback later than 2030/2031
- Owners and dates above are proposed by this case; the input named neither and they need confirmation
source: Team plan; thresholds from Kestrel south hub model v01 sensitivities
note: Ask for the decision explicitly; offer the Q1 2027 checkpoint as the point to walk away before the larger fit-out spend is committed.

## A1. Inputs and flagged assumptions
layout: table
tracker: Appendix
| Driver | Value | Low | High | Source |
|---|---|---|---|---|
| Full run-rate volume | 5.0m parcels/year | 3.8 | 5.6 | 2025 network flow data, south region (Kestrel planning team) |
| Ramp in 2027 | 60% of full run-rate | - | - | ASSUMPTION: planning team, based on the 2023 north hub opening |
| Saving per routed parcel | EUR 0.55/parcel | 0.40 | 0.65 | Network simulation v4; low/high = 2025/2023 fuel price scenarios |
| Hub operating fixed cost | EUR 0.9m/year | 0.7 | 1.2 | Site lease offer plus 14 FTE staffing plan |
| Investment | EUR 6.0m | 5.5 | 7.5 | Two supplier quotes, September 2026 |
| Hurdle rate | 9%/year | 7% | 11% | Group finance |
body:
- ASSUMPTION, not stated in the input: full run-rate (100%) is reached from 2028 onward. The input gives only the 2027 ramp (60%); if full run-rate is reached later, both NPV and payback move out.
- Ramp in 2027 has no low/high range in the input and is not tested in the sensitivity ranking on page 4.
- Audience, the December 2026 board meeting date, and the task owners on page 6 are proposed by this case, not stated in the input.
- Conventions agreed with finance and used throughout: EUR m; investment at the start of 2027 (t=0); operating cash flows at the end of each year 2027-2034, discounted 1 to 8 years; no terminal value; no tax.
source: fm-01-input.md; Kestrel south hub model v01


## File written by the run: model/README.md

# Model: Kestrel Logistics south hub, v01, 2026-10-14

**Question:** Should Kestrel invest EUR 6.0m in a cross-dock hub in the south region? Threshold: NPV at the 9% hurdle rate above zero over the hub's eight-year operating life (2027-2034).

**Answer in numbers:** NPV base EUR +3.23m (down -4.63m, up +8.33m); IRR base 21% (down -10%, up 39%); payback within the eight-year life in both the base and up cases, no payback within the life in the down case.

**Decided by:** saving per routed parcel (break-even EUR 0.425/parcel, range EUR 0.40 to 0.65 — inside) and full run-rate volume (break-even 3.86m parcels, range 3.8m to 5.6m — inside). Operating cost, investment cost and the discount rate are not deciding: their break-evens (EUR 1.48m/year, EUR 9.23m, 21%) lie outside the given ranges.

**Master check:** OK

**Spot test:** NPV: model EUR 3.2302m, by hand EUR 3.2302m (-6.0 + 0.75/1.09 + Σ 1.85/1.09^t for t=2..8); payback (undiscounted): model 2030 (t=4), by hand 2030 (cumulative turns from -1.55 at t=3 to +0.30 at t=4).

**Known weaknesses:** ramp in 2027 (60%) is an assumption with no tested range; this model additionally assumes (not stated in the input) that the hub reaches 100% of full run-rate from 2028 onward — if that takes longer, NPV and payback both move out. The down/up scenarios move volume, saving per parcel and investment together on the planning team's competitor story; they are not statistical confidence bounds.

**What the deck should say:** The south hub clears the CFO's hurdle (NPV +EUR 3.2m, IRR 21%, payback inside the eight-year life), but the margin is thin: saving per parcel and full run-rate volume both have break-evens inside their evidenced ranges, and the planning team's own competitor-hub risk would flip the answer to -EUR 4.6m. (Kestrel south hub model v01.)

**Question answered:** Should Kestrel invest in a cross-dock hub in the south region? CFO's rule: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year operating life (2027-2034).

## Key outputs

| Output | Unit | base | down | up |
|---|---|---|---|---|
| NPV at 9% hurdle rate | EUR m | 3.23 | -4.626 | 8.33 |
| IRR | per year | 0.2091 | -0.09939 | 0.388 |
| Payback, undiscounted | year (period) | 2030 | none | 2029 |
| Payback, discounted at 9% | year (period) | 2031 | none | 2029 |
| Annual saving at full run-rate (2028) | EUR m | 2.75 | 1.52 | 3.64 |

Scenarios (coherent sets, drivers changed from base):
- **down**: volume_full_run_rate = 3.8, saving_per_parcel = 0.4, investment = 7.5 (a competitor opens a hub nearby: fewer shippers route through Kestrel, the price response it forces eats much of the per-parcel saving, and the accelerated fit-out costs more)
- **up**: volume_full_run_rate = 5.6, saving_per_parcel = 0.65, investment = 5.5 (no competitor move materialises: shipper volume reaches the top of the range, the saving per parcel holds at the high (2023 fuel price) end, and fit-out comes in at the lower of the two supplier quotes)

## Sensitivity on npv (one-way, others at base; break-even target 0)

| Rank | Driver | Low / base / high | Output low | Output high | Swing | Break-even | Inside range? |
|---|---|---|---|---|---|---|---|
| 1 | saving_per_parcel | 0.4 / 0.55 / 0.65 EUR per parcel | -0.6456 | 5.814 | 6.46 | 0.425 | yes |
| 2 | volume_full_run_rate | 3.8 / 5 / 5.6 m parcels per year | -0.1805 | 4.936 | 5.116 | 3.864 | yes |
| 3 | opex_fixed | 0.7 / 0.9 / 1.2 EUR m per year | 4.337 | 1.57 | 2.767 | 1.484 | no |
| 4 | investment | 5.5 / 6 / 7.5 EUR m | 3.73 | 1.73 | 2 | 9.23 | no |
| 5 | discount_rate | 0.07 / 0.09 / 0.11 per year | 4.019 | 2.529 | 1.49 | 0.2091 | no |

Drivers without low/high range (not tested): ramp_2027

## Inputs

| Driver | Value | Unit | Low | High | Source |
|---|---|---|---|---|---|
| volume_full_run_rate | 5 | m parcels per year | 3.8 | 5.6 | 2025 network flow data; south region (Kestrel planning team) |
| ramp_2027 | 0.6 | share of full run-rate |  |  | ASSUMPTION: planning team; based on the 2023 north hub opening |
| saving_per_parcel | 0.55 | EUR per parcel | 0.4 | 0.65 | Network simulation v4; low = simulation with 2025 fuel prices; high = with 2023 fuel prices |
| opex_fixed | 0.9 | EUR m per year | 0.7 | 1.2 | Site lease offer plus 14 FTE staffing plan |
| investment | 6 | EUR m | 5.5 | 7.5 | Two supplier quotes; September 2026 |
| discount_rate | 0.09 | per year | 0.07 | 0.11 | Group finance (CFO hurdle rate) |

## Line items (calculation order)

| Line item | Unit | Formula |
|---|---|---|
| ramp | share of full run-rate | `pick(t, 0, ramp_2027, 1, 1, 1, 1, 1, 1, 1)` |
| volume | m parcels per year | `volume_full_run_rate * ramp` |
| saving | EUR m | `volume * saving_per_parcel` |
| fixed_cost | EUR m | `-opex_fixed * min(1, t)` |
| capex | EUR m | `-investment * pick(t, 1, 0, 0, 0, 0, 0, 0, 0, 0)` |
| net_cash_flow | EUR m | `saving + fixed_cost + capex` |
| cumulative_cash_flow | EUR m | `prev(cumulative_cash_flow) + net_cash_flow` |
| discount_factor | factor | `(1 + discount_rate) ** -t` |
| discounted_cash_flow | EUR m | `net_cash_flow * discount_factor` |
| cumulative_discounted_cash_flow | EUR m | `prev(cumulative_discounted_cash_flow) + discounted_cash_flow` |

## Checks

| Check | Scenario | Expected | Actual | Status |
|---|---|---|---|---|
| net_cash_flow_ties_to_parts | base | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | down | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | up | ==0 | 0 | OK |
| volume_within_full_run_rate | base | >=0 | 0 | OK |
| volume_within_full_run_rate | down | >=0 | 0 | OK |
| volume_within_full_run_rate | up | >=0 | 0 | OK |
| ramp_within_bounds | base | >=0 | 0 | OK |
| ramp_within_bounds | down | >=0 | 0 | OK |
| ramp_within_bounds | up | >=0 | 0 | OK |
| discounted_cash_flow_ties | base | ==0 | 0 | OK |
| discounted_cash_flow_ties | down | ==0 | 0 | OK |
| discounted_cash_flow_ties | up | ==0 | 0 | OK |

## Flags

- Drivers flagged as assumptions (no source or source starts with 'assumption'): ramp_2027
- No range for: ramp_2027

## Files

- `calc.csv`: every line item by period, base case
- `outputs.csv`: key outputs per scenario
- `checks.csv`: check results per scenario
- `sensitivity.csv`: tornado ranking and break-even values
- `model.xlsx`: Inputs (blue on yellow = input), Calc (live formulas), Outputs (live, master check), Sensitivity (values)


## File written by the run: model/calc.csv

line_item,unit,t0,2027,2028,2029,2030,2031,2032,2033,2034
ramp,share of full run-rate,0.0,0.6,1.0,1.0,1.0,1.0,1.0,1.0,1.0
volume,m parcels per year,0.0,3.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0
saving,EUR m,0.0,1.65,2.75,2.75,2.75,2.75,2.75,2.75,2.75
fixed_cost,EUR m,0.0,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9
capex,EUR m,-6.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
net_cash_flow,EUR m,-6.0,0.75,1.85,1.85,1.85,1.85,1.85,1.85,1.85
cumulative_cash_flow,EUR m,-6.0,-5.25,-3.4,-1.55,0.3,2.15,4.0,5.85,7.7
discount_factor,factor,1.0,0.9174311927,0.8416799933,0.7721834801,0.7084252111,0.6499313863,0.5962673269,0.5470342448,0.5018662797
discounted_cash_flow,EUR m,-6.0,0.6880733945,1.5571079875,1.4285394381,1.3105866405,1.2023730647,1.1030945547,1.012013353,0.9284526174
cumulative_discounted_cash_flow,EUR m,-6.0,-5.3119266055,-3.754818618,-2.3262791798,-1.0156925394,0.1866805253,1.28977508,2.301788433,3.2302410504


## File written by the run: model/checks.csv

check,scenario,expected,actual,status
net_cash_flow_ties_to_parts,base,==0,0.0,OK
net_cash_flow_ties_to_parts,down,==0,0.0,OK
net_cash_flow_ties_to_parts,up,==0,0.0,OK
volume_within_full_run_rate,base,>=0,0.0,OK
volume_within_full_run_rate,down,>=0,0.0,OK
volume_within_full_run_rate,up,>=0,0.0,OK
ramp_within_bounds,base,>=0,0.0,OK
ramp_within_bounds,down,>=0,0.0,OK
ramp_within_bounds,up,>=0,0.0,OK
discounted_cash_flow_ties,base,==0,0.0,OK
discounted_cash_flow_ties,down,==0,0.0,OK
discounted_cash_flow_ties,up,==0,0.0,OK


## File written by the run: model/inputs.csv

driver,value,unit,source,low,high,note
volume_full_run_rate,5.0,m parcels per year,2025 network flow data; south region (Kestrel planning team),3.8,5.6,
ramp_2027,0.60,share of full run-rate,ASSUMPTION: planning team; based on the 2023 north hub opening,,,100% run-rate assumed 2028-2034 onward: not stated in input; flagged
saving_per_parcel,0.55,EUR per parcel,Network simulation v4; low = simulation with 2025 fuel prices; high = with 2023 fuel prices,0.40,0.65,
opex_fixed,0.9,EUR m per year,Site lease offer plus 14 FTE staffing plan,0.7,1.2,
investment,6.0,EUR m,Two supplier quotes; September 2026,5.5,7.5,paid at start of 2027 (t=0); no terminal value; no tax in this screening model
discount_rate,0.09,per year,Group finance (CFO hurdle rate),0.07,0.11,


## File written by the run: model/outputs.csv

output,unit,base,down,up,model_version
npv,EUR m,3.2302410504,-4.626210314,8.3296245579,v01
irr,per year,0.2091368125,-0.0993929701,0.3880178751,v01
payback_undiscounted,year (period),2030,,2029,v01
payback_discounted,year (period),2031,,2029,v01
saving_full_run_rate,EUR m,2.75,1.52,3.64,v01


## File written by the run: model/sensitivity.csv

rank,driver,unit,low,base,high,output_low,output_base,output_high,swing,break_even,break_even_in_range
1,saving_per_parcel,EUR per parcel,0.4,0.55,0.65,-0.6456439279,3.2302410504,5.8141643692,6.4598082971,0.4249869616,yes
2,volume_full_run_rate,m parcels per year,3.8,5.0,5.6,-0.1805377305,3.2302410504,4.9356304408,5.1161681713,3.8635178329,yes
3,opex_fixed,EUR m per year,0.7,0.9,1.2,4.3372048733,3.2302410504,1.5697953159,2.7674095574,1.483621792,no
4,investment,EUR m,5.5,6.0,7.5,3.7302410504,3.2302410504,1.7302410504,2.0,9.2302410504,no
5,discount_rate,per year,0.07,0.09,0.11,4.0188648533,3.2302410504,2.5293361167,1.4895287366,0.2091368125,no


## File written by the run: model/spec.json

{
  "title": "Kestrel Logistics: south region cross-dock hub business case (fictional)",
  "question": "Should Kestrel invest in a cross-dock hub in the south region? CFO's rule: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year operating life (2027-2034).",
  "periods": ["t0", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034"],
  "rows": [
    {"name": "ramp", "unit": "share of full run-rate", "expr": "pick(t, 0, ramp_2027, 1, 1, 1, 1, 1, 1, 1)"},
    {"name": "volume", "unit": "m parcels per year", "expr": "volume_full_run_rate * ramp"},
    {"name": "saving", "unit": "EUR m", "expr": "volume * saving_per_parcel"},
    {"name": "fixed_cost", "unit": "EUR m", "expr": "-opex_fixed * min(1, t)"},
    {"name": "capex", "unit": "EUR m", "expr": "-investment * pick(t, 1, 0, 0, 0, 0, 0, 0, 0, 0)"},
    {"name": "net_cash_flow", "unit": "EUR m", "expr": "saving + fixed_cost + capex"},
    {"name": "cumulative_cash_flow", "unit": "EUR m", "expr": "prev(cumulative_cash_flow) + net_cash_flow"},
    {"name": "discount_factor", "unit": "factor", "expr": "(1 + discount_rate) ** -t"},
    {"name": "discounted_cash_flow", "unit": "EUR m", "expr": "net_cash_flow * discount_factor"},
    {"name": "cumulative_discounted_cash_flow", "unit": "EUR m", "expr": "prev(cumulative_discounted_cash_flow) + discounted_cash_flow"}
  ],
  "outputs": [
    {"name": "npv", "label": "NPV at 9% hurdle rate", "unit": "EUR m", "fn": "sum", "row": "discounted_cash_flow"},
    {"name": "irr", "label": "IRR", "unit": "per year", "fn": "irr", "row": "net_cash_flow"},
    {"name": "payback_undiscounted", "label": "Payback, undiscounted", "unit": "year (period)", "fn": "payback", "row": "cumulative_cash_flow"},
    {"name": "payback_discounted", "label": "Payback, discounted at 9%", "unit": "year (period)", "fn": "payback", "row": "cumulative_discounted_cash_flow"},
    {"name": "saving_full_run_rate", "label": "Annual saving at full run-rate (2028)", "unit": "EUR m", "fn": "value", "row": "saving", "period": "2028"}
  ],
  "checks": [
    {"name": "net_cash_flow_ties_to_parts", "expr": "net_cash_flow - saving - fixed_cost - capex", "rule": "==0"},
    {"name": "volume_within_full_run_rate", "expr": "volume_full_run_rate - volume", "rule": ">=0"},
    {"name": "ramp_within_bounds", "expr": "1 - ramp", "rule": ">=0"},
    {"name": "discounted_cash_flow_ties", "expr": "discounted_cash_flow - net_cash_flow * discount_factor", "rule": "==0"}
  ],
  "scenarios": {
    "down": {"volume_full_run_rate": 3.8, "saving_per_parcel": 0.40, "investment": 7.5},
    "up": {"volume_full_run_rate": 5.6, "saving_per_parcel": 0.65, "investment": 5.5}
  },
  "scenario_stories": {
    "down": "a competitor opens a hub nearby: fewer shippers route through Kestrel, the price response it forces eats much of the per-parcel saving, and the accelerated fit-out costs more",
    "up": "no competitor move materialises: shipper volume reaches the top of the range, the saving per parcel holds at the high (2023 fuel price) end, and fit-out comes in at the lower of the two supplier quotes"
  },
  "break_even": {"output": "npv", "target": 0}
}

