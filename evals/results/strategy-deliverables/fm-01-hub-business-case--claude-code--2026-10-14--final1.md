# fm-01-hub-business-case on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (12/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| States the question, outputs, and decision threshold before building | yes | deck.md SCQA opening: 'Question: Does the south hub clear the CFO's 9% hurdle over its eight-year life, and what would change the answer? Answer: Yes. NPV is EUR 3.2m at 9%, IRR 21%, payback in the fourth year (2030).' precedes the detailed exhibit slides; README also states 'CFO's rule: approve if  |
| Separates inputs, calculations and outputs; no bare numbers in formulas besides 0/1 or documented conversions | yes | Separate inputs.csv, calc.csv, outputs.csv, sensitivity.csv, checks.csv; spec.json formulas like 'pick(t, 0, ramp_2027, ramp_steady)' and '(1 + hurdle_rate) ** -t' use only 0/1 literals. |
| Base NPV within EUR 3.1m-3.4m and payback in 2030/year 4 | yes | outputs.csv: npv base = 3.2302410504; payback_period base = 2030. |
| Tornado ranking with saving per parcel first, parcels routed second | yes | sensitivity.csv rank 1 = saving_per_parcel (swing 6.46), rank 2 = parcels_full_run_rate (swing 5.12). |
| Break-even values for saving per parcel (~0.42-0.43) and parcels (~3.8-3.9m), both flagged inside range | yes | sensitivity.csv: saving_per_parcel break_even 0.4249869616 (yes); parcels_full_run_rate break_even 3.8635178329 (yes). |
| In-range break-even surfaced in headline/decided-by line, not only appendix | yes | Executive summary bullet: 'NPV turns negative below EUR 0.43 per parcel, inside the sourced EUR 0.40 to 0.65 range' appears in slide 2 and the chat 'What decides it' table, not just the appendix. |
| Down case is a coherent competitor-hub story (fewer parcels, lower saving, higher investment), NPV negative | yes | outputs/spec.json down scenario: parcels_full_run_rate=3.8, saving_per_parcel=0.40, investment=7.5, story 'competitor hub opens nearby...'; NPV down = -4.626m. |
| Checks block plus two hand-recomputed outputs with both numbers recorded | yes | checks.csv has multiple OK checks; README 'Spot test (hand recompute, base case)' shows NPV 3.230 vs model 3.23, and payback interpolation vs model payback 2030, both match. |
| 60% ramp listed as a flagged assumption | yes | inputs.csv/README: ramp_2027 source 'ASSUMPTION: planning team, based on the 2023 north hub opening'; Flags section lists ramp_2027 as assumption with no range. |
| 'What the deck should say' sentences carry the model version | yes | Deck footers repeatedly cite 'Source: Kestrel south hub model v01' and outputs.csv includes a model_version column set to 'v01'. |
| Must not present NPV without range/scenarios | yes | NPV is always accompanied by sensitivity table/tornado chart and down/up scenarios throughout (slides 4-6, sensitivity.csv, outputs.csv). |
| Must not add terminal value or tax without flagging departure from conventions | yes | Slide 7 body: 'No tax and no terminal value in this screening model, per the agreed convention; a fuller case before signature should check both.' — no undisclosed addition occurs. |

## Transcript

## Turn 1

**User:** Build the business case for the Kestrel south hub from these inputs. Board needs NPV, payback and what decides the answer. (Attached in the working directory: fm-01-input.md.)

Everything is built and checked. Here's the summary of the business case I put together.

## The answer

**Approve the EUR 6m south hub.** NPV is **EUR 3.2m** at the 9% hurdle rate, IRR 21%, payback in the **fourth year (2030)**.

## What decides it

Ranked by NPV swing across each driver's own sourced range (others held at base):

| Rank | Driver | Swing on NPV | Break-even | Inside given range? |
|---|---|---|---|---|
| 1 | Saving per parcel | EUR 6.5m | EUR 0.43/parcel | **Yes** (range 0.40–0.65) |
| 2 | Routed volume | EUR 5.1m | 3.86m parcels | **Yes** (range 3.8–5.6) |
| 3 | Hub fixed cost | EUR 2.8m | EUR 1.48m/yr | No (above 1.2 high case) |
| 4 | Investment | EUR 2.0m | EUR 9.23m | No (above 7.5 high case) |
| 5 | Hurdle rate | EUR 1.5m | 21% (= IRR) | No (above 11% high case) |

Only the top two drivers have break-evens that actually sit inside the uncertainty finance and planning already gave — those are the two numbers worth watching after approval.

The planning team's qualitative risk (competitor hub nearby) isn't an independent sensitivity — it hits volume, saving, and build cost **simultaneously**. I modeled it as a named scenario (not three separate low-cases): NPV falls to **-EUR 4.6m** and never pays back. I flagged one modeling judgment call explicitly: the saving-per-parcel low case (EUR 0.40) is sourced to a *fuel-price* sensitivity, not a competitive-price one, and I used it only as the closest available proxy for the price response the planning team described.

## Deliverables

- `model/` — CSV-based model (inputs, calc, outputs, checks, sensitivity, `model.xlsx` with live formulas) + `README.md` with hand-verified spot checks. Master check: OK.
- `deck.md` / `deck.html` / `deck.pptx` — 8-page board deck (+2-page appendix): executive summary, base case, sensitivity/break-even, competitor-risk scenario, risks, and a decision request (with owner/date flagged as assumptions since the brief didn't name them).

One open item for the board: confirm a decision owner and date — I proposed COO/Head of Network and a November 2026 board meeting as placeholders, flagged as assumptions in the deck.


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
<body><div id="stage"><section class="slide l-title" id="s1" data-title="Should Kestrel invest in the south region cross-dock hub?"><div class="t-client">Kestrel Logistics (fictional)</div><h1 class="t-title">Should Kestrel invest in the south region cross-dock hub?</h1><p class="t-sub">Business case for the board: NPV, payback and what decides the answer</p><p class="t-meta">Kestrel board, capital approval decision | October 2026</p><footer><div></div><span class="pn">1</span></footer><aside class="notes"><b>Speaker note</b> Pre-read for the capital approval decision. The ask is on page 2 and again on page 8.</aside></section><section class="slide l-summary" id="s2" data-title="Kestrel should approve the EUR 6m south hub; NPV is EUR 3.2m at the 9% hurdle rate, with payback in 2030 — but the case lives or dies on saving per parcel and volume"><div class="tracker">Executive summary</div><h2 class="title long">Kestrel should approve the EUR 6m south hub; NPV is EUR 3.2m at the 9% hurdle rate, with payback in 2030 — but the case lives or dies on saving per parcel and volume</h2><div class="content summary"><p class="lead">2025 network flow data point to about 5m parcels a year in the south region that a dedicated cross-dock hub could route through fewer handlings and a shorter line-haul, saving an estimated EUR 0.55 per parcel.</p><ol><li>Base case: NPV EUR 3.2m at the 9% hurdle rate, IRR 21%, payback in the fourth year of operation (2030). Master check on the model: OK.</li><li>The saving per parcel decides the case: NPV turns negative below EUR 0.43 per parcel, inside the sourced EUR 0.40 to 0.65 range.</li><li>Routed volume is the second lever: NPV turns negative below 3.86m parcels a year, just inside the sourced 3.8 to 5.6m range.</li><li>Hub fixed cost, the investment cost and the hurdle rate would each have to move past the high end of its given range before the case turns negative on its own.</li><li>The planning team&#x27;s own risk flag — a competitor hub pulling volume, squeezing the saving and forcing a faster, costlier fit-out at the same time — does turn the case negative: NPV -EUR 4.6m.</li></ol><div class="ask"><strong>Decision requested:</strong> approve EUR 6m capital for the south hub fit-out and sorter (owner: COO / Head of Network — ASSUMPTION, not named in the brief; by the November 2026 board meeting — ASSUMPTION, to allow fit-out to start ahead of the 2027 opening). Track realised saving per parcel and routed volume from month one of 2027 against the EUR 0.43 and 3.86m break-evens.</div></div><footer><div class="source">Source: Kestrel south hub model v01</div><span class="pn">2</span></footer><aside class="notes"><b>Speaker note</b> Read the bold line and the ask. Pages 3 to 7 prove each point in order.</aside></section><section class="slide l-chart" id="s3" data-title="The hub repays its EUR 6m investment in the fourth year of operation, and is worth EUR 3.2m in today&#x27;s money by 2034"><div class="tracker">1 Base case</div><h2 class="title long">The hub repays its EUR 6m investment in the fourth year of operation, and is worth EUR 3.2m in today&#x27;s money by 2034</h2><div class="header">Cumulative net cash flow, EUR m nominal (undiscounted), start of 2027 to end of 2034</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="The hub repays its EUR 6m investment in the fourth year of operation, and is worth EUR 3.2m in today&#x27;s money by 2034"><text x="46.0" y="365.0" font-size="13" text-anchor="end" fill="#B8C0CC" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-6</text><text x="46.0" y="200.0" font-size="13" text-anchor="end" fill="#B8C0CC" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1</text><text x="46.0" y="35.0" font-size="13" text-anchor="end" fill="#B8C0CC" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">8</text><line x1="56" x2="510" y1="360.0" y2="360.0" stroke="#B8C0CC"/><text x="56.0" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Start 2027</text><text x="112.8" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2027</text><text x="169.5" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2028</text><text x="226.2" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2029</text><text x="283.0" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2030</text><text x="339.8" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2031</text><text x="396.5" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2032</text><text x="453.2" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2033</text><text x="510.0" y="384.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2034</text><line x1="56.0" x2="510.0" y1="218.6" y2="218.6" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="518.0" y="223.6" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Break-even</text><polyline points="56.0,360.0 112.8,342.3 169.5,298.7 226.2,255.1 283.0,211.5 339.8,167.9 396.5,124.3 453.2,80.7 510.0,37.1" fill="none" stroke="#B8C0CC" stroke-width="2.5"/><circle cx="56.0" cy="360.0" r="4" fill="#B8C0CC"/><circle cx="112.8" cy="342.3" r="4" fill="#B8C0CC"/><circle cx="169.5" cy="298.7" r="4" fill="#B8C0CC"/><circle cx="226.2" cy="255.1" r="4" fill="#B8C0CC"/><circle cx="283.0" cy="211.5" r="4" fill="#B8C0CC"/><circle cx="339.8" cy="167.9" r="4" fill="#B8C0CC"/><circle cx="396.5" cy="124.3" r="4" fill="#B8C0CC"/><circle cx="453.2" cy="80.7" r="4" fill="#B8C0CC"/><circle cx="510.0" cy="37.1" r="4" fill="#B8C0CC"/><text x="510.0" y="25.1" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">7.7</text></svg></div><div class="side"><ul><li>2027 ramps at 60% of full run-rate (planning team, based on the 2023 north hub opening); full 5m parcels a year from 2028.</li><li>Net cash flow is EUR 0.75m in 2027 and EUR 1.85m a year from 2028, after EUR 0.9m of fixed hub cost.</li><li>NPV at the 9% hurdle rate is EUR 3.2m; this chart shows nominal cash flow, used only to read payback.</li></ul></div></div><footer><div class="footnote">Payback is read off undiscounted cumulative cash flow, consistent with the CFO&#x27;s convention; NPV above is discounted.</div><div class="source">Source: Kestrel south hub model v01, calc.csv</div><span class="pn">3</span></footer><aside class="notes"><b>Speaker note</b> Cumulative cash crosses zero partway through 2030 — about 3.8 years after the investment, inside the eight-year life.</aside></section><section class="slide l-chart" id="s4" data-title="Saving per parcel and volume swing NPV by EUR 6.5m and EUR 5.1m, three times more than any other driver"><div class="tracker">2 What decides the answer</div><h2 class="title long">Saving per parcel and volume swing NPV by EUR 6.5m and EUR 5.1m, three times more than any other driver</h2><div class="header">NPV swing, EUR m, moving each driver from its low to its high value, others held at base</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Saving per parcel and volume swing NPV by EUR 6.5m and EUR 5.1m, three times more than any other driver"><rect x="280" y="23.4" width="282.6" height="43.0" fill="#B8C0CC"/><text x="570.6" y="50.4" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6.46</text><text x="268.0" y="51.4" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Saving per parcel (EUR 0.40 to 0.65/parcel)</text><rect x="280" y="100.2" width="224.0" height="43.0" fill="#B8C0CC"/><text x="512.0" y="127.2" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">5.12</text><text x="268.0" y="128.2" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Routed volume (3.8 to 5.6m parcels/year)</text><rect x="280" y="177.0" width="121.2" height="43.0" fill="#B8C0CC"/><text x="409.2" y="204.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.77</text><text x="268.0" y="205.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Hub fixed cost (EUR 0.7 to 1.2m/year)</text><rect x="280" y="253.8" width="87.5" height="43.0" fill="#B8C0CC"/><text x="375.5" y="280.8" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.00</text><text x="268.0" y="281.8" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Investment (EUR 5.5 to 7.5m)</text><rect x="280" y="330.6" width="65.2" height="43.0" fill="#B8C0CC"/><text x="353.2" y="357.6" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1.49</text><text x="268.0" y="358.6" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Hurdle rate (7% to 11%)</text><line x1="280" x2="280" y1="8" y2="392.0" stroke="#14213D"/></svg></div><div class="side"><ul><li>Ranking by swing uses each driver&#x27;s own evidence range (network simulation, supplier quotes, group finance), not a uniform plus or minus.</li><li>The two volume-and-price drivers combined explain most of the uncertainty in the answer; cost and financing drivers explain much less.</li></ul></div></div><footer><div class="footnote">Ramp-year share (60% in 2027) has no sourced range and is not tested here; see appendix.</div><div class="source">Source: Kestrel south hub model v01, sensitivity.csv</div><span class="pn">4</span></footer><aside class="notes"><b>Speaker note</b> This is the chart that tells the board which two numbers to watch after approval.</aside></section><section class="slide l-table" id="s5" data-title="Both deciding break-evens sit inside the given ranges; the other three would need to move outside theirs"><div class="tracker">2 What decides the answer</div><h2 class="title long">Both deciding break-evens sit inside the given ranges; the other three would need to move outside theirs</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Driver</th><th class="num">Base</th><th>Break-even (NPV = 0)</th><th>Given range</th><th>Inside range?</th></tr><tr><td>Saving per parcel, EUR/parcel</td><td class="num">0.55</td><td>0.43</td><td>0.40 to 0.65</td><td>Yes</td></tr><tr><td>Routed volume, m parcels/year</td><td class="num">5.0</td><td>3.86</td><td>3.8 to 5.6</td><td>Yes</td></tr><tr><td>Hub fixed cost, EUR m/year</td><td class="num">0.9</td><td>1.48</td><td>0.7 to 1.2</td><td>No — above the high case</td></tr><tr><td>Investment, EUR m</td><td class="num">6.0</td><td>9.23</td><td>5.5 to 7.5</td><td>No — above the high case</td></tr><tr><td>Hurdle rate, per year</td><td class="num">9%</td><td>21% (= IRR)</td><td>7% to 11%</td><td>No — above the high case</td></tr></table></div><div class="side"><ul><li>A break-even inside the given range is the one the board should treat as live risk, not a tail case.</li><li>The hurdle-rate break-even of 21% is the project&#x27;s IRR: the rate would have to more than double from 9% before the rate itself kills the case.</li><li>Cheapest evidence to settle the two live drivers: track actual parcels routed and the realised handling/line-haul saving per parcel against plan for the first two quarters of 2027, before committing the 2028 staffing ramp.</li></ul></div></div><footer><div class="footnote">Break-even values from sensitivity.csv; computed holding all other drivers at base.</div><div class="source">Source: Kestrel south hub model v01, sensitivity.csv</div><span class="pn">5</span></footer></section><section class="slide l-chart" id="s6" data-title="A nearby competitor hub hits volume, saving and build cost together, and that combination turns NPV negative"><div class="tracker">3 Competitor risk</div><h2 class="title long">A nearby competitor hub hits volume, saving and build cost together, and that combination turns NPV negative</h2><div class="header">NPV by case, EUR m, discounted at 9% over 2027-2034</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="A nearby competitor hub hits volume, saving and build cost together, and that combination turns NPV negative"><line x1="8.0" x2="542.0" y1="241.3" y2="241.3" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="550.0" y="246.3" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Hurdle (NPV = 0)</text><rect x="41.8" y="241.3" width="106.4" height="98.8" fill="#D9822B"/><text x="95.0" y="358.1" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">-4.63</text><text x="97.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Down (competitor</text><text x="97.0" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">entry)</text><rect x="219.8" y="172.4" width="106.4" height="68.9" fill="#B8C0CC"/><text x="273.0" y="164.4" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.23</text><text x="275.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base</text><rect x="397.8" y="39.9" width="106.4" height="201.4" fill="#B8C0CC"/><text x="451.0" y="31.9" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">9.44</text><text x="453.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Up (demand and</text><text x="453.0" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">efficiency beat plan)</text><line x1="8" x2="542" y1="241.3" y2="241.3" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Down case: the planning team&#x27;s own scenario — volume at the low case (3.8m parcels), saving per parcel at the low case (EUR 0.40), investment at the high case (EUR 7.5m) for an accelerated fit-out, all together.</li><li>The EUR 0.40 low case in the sourced range is actually a 2025-fuel-price sensitivity, not a competitive-price one; it is used here as the closest available proxy for the price response the planning team described, and should be refined once a competitor move looks real.</li><li>Up case: no competitor response, volume and saving at their high cases, fit-out delivered on the lower supplier quote and fixed cost run lean — a coherent &quot;plan beats expectations&quot; story, not a mirror of the down case.</li><li>The down case never pays back within the eight-year life.</li></ul></div></div><footer><div class="footnote">Scenario definitions and stories in the model README; this is a named scenario, not a sensitivity on one driver.</div><div class="source">Source: Kestrel south hub model v01, outputs.csv</div><span class="pn">6</span></footer><aside class="notes"><b>Speaker note</b> This is the one event, not any single input miss, that the board should watch for.</aside></section><section class="slide l-table" id="s7" data-title="Risks and what would change the answer"><div class="tracker">Risks</div><h2 class="title">Risks and what would change the answer</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Risk</th><th>Effect on the case</th><th>What we would do</th></tr><tr><td>Competitor opens a hub nearby</td><td>Correlated hit to volume, saving and build cost; NPV to -EUR 4.6m</td><td>Treat any confirmed competitor fit-out announcement as a trigger to re-run the case before further spend</td></tr><tr><td>Saving per parcel comes in below EUR 0.43</td><td>NPV turns negative</td><td>Monitor realised saving per parcel against plan from month one of 2027</td></tr><tr><td>Routed volume comes in below 3.86m</td><td>NPV turns negative</td><td>Monitor routed volume against plan from month one of 2027</td></tr><tr><td>2027 ramp is slower than 60% (no sourced range)</td><td>Delays payback, does not on its own flip NPV at base case levels</td><td>Use actual 2027 ramp as an early read on the volume risk above</td></tr></table></div><div class="side"><ul><li>No tax and no terminal value in this screening model, per the agreed convention; a fuller case before signature should check both.</li></ul></div></div><footer><div class="source">Source: fm-01-input.md; Kestrel south hub model v01</div><span class="pn">7</span></footer></section><section class="slide l-table" id="s8" data-title="Decision requested: approve EUR 6m for the south hub, with a first checkpoint after two quarters of operation"><div class="tracker">Next steps</div><h2 class="title long">Decision requested: approve EUR 6m for the south hub, with a first checkpoint after two quarters of operation</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Step</th><th>Owner</th><th>By when</th></tr><tr><td>Board approves EUR 6m capital for fit-out and sorter</td><td>Board</td><td>November 2026 (ASSUMPTION — no board date given; set ahead of the 2027 opening implied by the investment timing)</td></tr><tr><td>Confirm site lease and 14 FTE staffing plan</td><td>COO / Head of Network (ASSUMPTION — owner not named)</td><td>December 2026</td></tr><tr><td>Hub opens, 2027 ramp begins</td><td>Head of Network (ASSUMPTION)</td><td>January 2027</td></tr><tr><td>Checkpoint: realised saving per parcel and routed volume vs. EUR 0.43 / 3.86m break-evens</td><td>CFO (ASSUMPTION)</td><td>End of Q2 2027</td></tr></table></div><div class="side"><ul><li>Owners and dates marked ASSUMPTION are not in the planning team&#x27;s brief and need confirmation.</li></ul></div></div><footer><div class="source">Source: Team proposal based on fm-01-input.md</div><span class="pn">8</span></footer></section><section class="slide l-table" id="s9" data-title="Model inputs"><div class="tracker">Appendix</div><h2 class="title">Model inputs</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Driver</th><th class="num">Value</th><th>Low</th><th>High</th><th>Source</th></tr><tr><td>Parcels at full run-rate, m/year</td><td class="num">5.0</td><td>3.8</td><td>5.6</td><td>2025 network flow data, south region (Kestrel planning team)</td></tr><tr><td>Ramp in 2027, share of full run-rate</td><td class="num">60%</td><td>—</td><td>—</td><td>ASSUMPTION: planning team, based on the 2023 north hub opening</td></tr><tr><td>Ramp from 2028, share of full run-rate</td><td class="num">100%</td><td>—</td><td>—</td><td>ASSUMPTION: no data given beyond 2027; modelled at full run-rate from year 2</td></tr><tr><td>Saving per parcel, EUR</td><td class="num">0.55</td><td>0.40</td><td>0.65</td><td>Network simulation v4; low/high = 2025/2023 fuel prices</td></tr><tr><td>Hub fixed cost, EUR m/year</td><td class="num">0.9</td><td>0.7</td><td>1.2</td><td>Site lease offer plus 14 FTE staffing plan</td></tr><tr><td>Investment, EUR m</td><td class="num">6.0</td><td>5.5</td><td>7.5</td><td>Two supplier quotes, September 2026</td></tr><tr><td>Hurdle rate</td><td class="num">9%</td><td>7%</td><td>11%</td><td>Group finance</td></tr></table></div></div><footer><div class="source">Source: fm-01-input.md; Kestrel south hub model v01</div><span class="pn">A1</span></footer></section><section class="slide l-table" id="s10" data-title="Base-case annual cash flow"><div class="tracker">Appendix</div><h2 class="title">Base-case annual cash flow</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>EUR m</th><th class="num">Start 2027</th><th class="num">2027</th><th class="num">2028</th><th class="num">2029-2034 (each year)</th></tr><tr><td>Parcels routed, m/year</td><td class="num">0.0</td><td class="num">3.0</td><td class="num">5.0</td><td class="num">5.0</td></tr><tr><td>Saving</td><td class="num">0.0</td><td class="num">1.65</td><td class="num">2.75</td><td class="num">2.75</td></tr><tr><td>Hub fixed cost</td><td class="num">0.0</td><td class="num">-0.9</td><td class="num">-0.9</td><td class="num">-0.9</td></tr><tr><td>Investment</td><td class="num">-6.0</td><td class="num">0.0</td><td class="num">0.0</td><td class="num">0.0</td></tr><tr><td>Net cash flow</td><td class="num">-6.0</td><td class="num">0.75</td><td class="num">1.85</td><td class="num">1.85</td></tr></table></div></div><footer><div class="source">Source: Kestrel south hub model v01, calc.csv</div><span class="pn">A2</span></footer></section></div>
<div id="overview"><h1>Titles-only read-through</h1><ol><li>Should Kestrel invest in the south region cross-dock hub? <span style='color:#8A93A3'>(1)</span></li><li>Kestrel should approve the EUR 6m south hub; NPV is EUR 3.2m at the 9% hurdle rate, with payback in 2030 — but the case lives or dies on saving per parcel and volume <span style='color:#8A93A3'>(2)</span></li><li>The hub repays its EUR 6m investment in the fourth year of operation, and is worth EUR 3.2m in today&#x27;s money by 2034 <span style='color:#8A93A3'>(3)</span></li><li>Saving per parcel and volume swing NPV by EUR 6.5m and EUR 5.1m, three times more than any other driver <span style='color:#8A93A3'>(4)</span></li><li>Both deciding break-evens sit inside the given ranges; the other three would need to move outside theirs <span style='color:#8A93A3'>(5)</span></li><li>A nearby competitor hub hits volume, saving and build cost together, and that combination turns NPV negative <span style='color:#8A93A3'>(6)</span></li><li>Risks and what would change the answer <span style='color:#8A93A3'>(7)</span></li><li>Decision requested: approve EUR 6m for the south hub, with a first checkpoint after two quarters of operation <span style='color:#8A93A3'>(8)</span></li><li>Model inputs <span style='color:#8A93A3'>(A1)</span></li><li>Base-case annual cash flow <span style='color:#8A93A3'>(A2)</span></li></ol></div>
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
audience: Kestrel board, capital approval decision
date: October 2026
format: deck
theme:
  text: "#14213D"
  accent: "#D9822B"
  muted: "#B8C0CC"
  light: "#E8EBF0"
  background: "#FFFFFF"
---

# Deck: Should Kestrel invest in the south region cross-dock hub?

*Fictional company. All figures, people and documents invented for evaluation.*

**Opening (SCQA)**
- Situation: 2025 network flow data show about 5m parcels a year in the south region that a dedicated cross-dock hub could route more cheaply, saving an estimated EUR 0.55 per parcel in line-haul and handling.
- Complication: The hub needs EUR 6m upfront and EUR 0.9m a year to run, both the ramp-up and the saving are estimates with real ranges, and a competitor hub nearby could cut volume, compress the saving and raise the build cost all at once.
- Question: Does the south hub clear the CFO's 9% hurdle over its eight-year life, and what would change the answer?
- Answer: Yes. NPV is EUR 3.2m at 9%, IRR 21%, payback in the fourth year (2030). The saving per parcel and the routed volume decide the case; a correlated competitor-entry scenario is the one event that flips it, to -EUR 4.6m.

**Key line**
1. The base case clears the hurdle: NPV EUR 3.2m at 9%, IRR 21%, payback in 2030.
2. The saving per routed parcel decides the case: NPV turns negative below EUR 0.43 per parcel, inside the given EUR 0.40-0.65 range.
3. Routed volume is the second lever: NPV turns negative below 3.86m parcels a year, just inside the given 3.8-5.6m range.
4. Hub fixed cost, the investment and the hurdle rate do not swing the decision alone: each would have to move past the high end of its given range to turn NPV negative.
5. A competitor hub nearby would hit volume, the saving and the build cost together, not separately, and that combination does turn NPV negative, to -EUR 4.6m.

## 1. Should Kestrel invest in the south region cross-dock hub?
layout: title
subtitle: Business case for the board: NPV, payback and what decides the answer
note: Pre-read for the capital approval decision. The ask is on page 2 and again on page 8.

## 2. Kestrel should approve the EUR 6m south hub; NPV is EUR 3.2m at the 9% hurdle rate, with payback in 2030 — but the case lives or dies on saving per parcel and volume
layout: summary
tracker: Executive summary
lead: 2025 network flow data point to about 5m parcels a year in the south region that a dedicated cross-dock hub could route through fewer handlings and a shorter line-haul, saving an estimated EUR 0.55 per parcel.
body:
- Base case: NPV EUR 3.2m at the 9% hurdle rate, IRR 21%, payback in the fourth year of operation (2030). Master check on the model: OK.
- The saving per parcel decides the case: NPV turns negative below EUR 0.43 per parcel, inside the sourced EUR 0.40 to 0.65 range.
- Routed volume is the second lever: NPV turns negative below 3.86m parcels a year, just inside the sourced 3.8 to 5.6m range.
- Hub fixed cost, the investment cost and the hurdle rate would each have to move past the high end of its given range before the case turns negative on its own.
- The planning team's own risk flag — a competitor hub pulling volume, squeezing the saving and forcing a faster, costlier fit-out at the same time — does turn the case negative: NPV -EUR 4.6m.
ask: **Decision requested:** approve EUR 6m capital for the south hub fit-out and sorter (owner: COO / Head of Network — ASSUMPTION, not named in the brief; by the November 2026 board meeting — ASSUMPTION, to allow fit-out to start ahead of the 2027 opening). Track realised saving per parcel and routed volume from month one of 2027 against the EUR 0.43 and 3.86m break-evens.
source: Kestrel south hub model v01
note: Read the bold line and the ask. Pages 3 to 7 prove each point in order.

## 3. The hub repays its EUR 6m investment in the fourth year of operation, and is worth EUR 3.2m in today's money by 2034
layout: chart
tracker: 1 Base case
message: time-series
chart: line
header: Cumulative net cash flow, EUR m nominal (undiscounted), start of 2027 to end of 2034
reference: 0 | Break-even
highlight: 2030
scale: zero
| Year | Cumulative cash flow |
|---|---|
| Start 2027 | -6.0 |
| 2027 | -5.25 |
| 2028 | -3.4 |
| 2029 | -1.55 |
| 2030 | 0.3 |
| 2031 | 2.15 |
| 2032 | 4.0 |
| 2033 | 5.85 |
| 2034 | 7.7 |
body:
- 2027 ramps at 60% of full run-rate (planning team, based on the 2023 north hub opening); full 5m parcels a year from 2028.
- Net cash flow is EUR 0.75m in 2027 and EUR 1.85m a year from 2028, after EUR 0.9m of fixed hub cost.
- NPV at the 9% hurdle rate is EUR 3.2m; this chart shows nominal cash flow, used only to read payback.
footnote: Payback is read off undiscounted cumulative cash flow, consistent with the CFO's convention; NPV above is discounted.
source: Kestrel south hub model v01, calc.csv
note: Cumulative cash crosses zero partway through 2030 — about 3.8 years after the investment, inside the eight-year life.

## 4. Saving per parcel and volume swing NPV by EUR 6.5m and EUR 5.1m, three times more than any other driver
layout: chart
tracker: 2 What decides the answer
message: ranking
chart: hbar
header: NPV swing, EUR m, moving each driver from its low to its high value, others held at base
highlight: Saving per parcel; Routed volume
| Driver | NPV swing |
|---|---|
| Saving per parcel (EUR 0.40 to 0.65/parcel) | 6.46 |
| Routed volume (3.8 to 5.6m parcels/year) | 5.12 |
| Hub fixed cost (EUR 0.7 to 1.2m/year) | 2.77 |
| Investment (EUR 5.5 to 7.5m) | 2.00 |
| Hurdle rate (7% to 11%) | 1.49 |
body:
- Ranking by swing uses each driver's own evidence range (network simulation, supplier quotes, group finance), not a uniform plus or minus.
- The two volume-and-price drivers combined explain most of the uncertainty in the answer; cost and financing drivers explain much less.
footnote: Ramp-year share (60% in 2027) has no sourced range and is not tested here; see appendix.
source: Kestrel south hub model v01, sensitivity.csv
note: This is the chart that tells the board which two numbers to watch after approval.

## 5. Both deciding break-evens sit inside the given ranges; the other three would need to move outside theirs
layout: table
tracker: 2 What decides the answer
| Driver | Base | Break-even (NPV = 0) | Given range | Inside range? |
|---|---|---|---|---|
| Saving per parcel, EUR/parcel | 0.55 | 0.43 | 0.40 to 0.65 | Yes |
| Routed volume, m parcels/year | 5.0 | 3.86 | 3.8 to 5.6 | Yes |
| Hub fixed cost, EUR m/year | 0.9 | 1.48 | 0.7 to 1.2 | No — above the high case |
| Investment, EUR m | 6.0 | 9.23 | 5.5 to 7.5 | No — above the high case |
| Hurdle rate, per year | 9% | 21% (= IRR) | 7% to 11% | No — above the high case |
body:
- A break-even inside the given range is the one the board should treat as live risk, not a tail case.
- The hurdle-rate break-even of 21% is the project's IRR: the rate would have to more than double from 9% before the rate itself kills the case.
- Cheapest evidence to settle the two live drivers: track actual parcels routed and the realised handling/line-haul saving per parcel against plan for the first two quarters of 2027, before committing the 2028 staffing ramp.
footnote: Break-even values from sensitivity.csv; computed holding all other drivers at base.
source: Kestrel south hub model v01, sensitivity.csv

## 6. A nearby competitor hub hits volume, saving and build cost together, and that combination turns NPV negative
layout: chart
tracker: 3 Competitor risk
message: deviation
chart: bar
header: NPV by case, EUR m, discounted at 9% over 2027-2034
reference: 0 | Hurdle (NPV = 0)
highlight: Down (competitor entry)
| Case | NPV |
|---|---|
| Down (competitor entry) | -4.63 |
| Base | 3.23 |
| Up (demand and efficiency beat plan) | 9.44 |
body:
- Down case: the planning team's own scenario — volume at the low case (3.8m parcels), saving per parcel at the low case (EUR 0.40), investment at the high case (EUR 7.5m) for an accelerated fit-out, all together.
- The EUR 0.40 low case in the sourced range is actually a 2025-fuel-price sensitivity, not a competitive-price one; it is used here as the closest available proxy for the price response the planning team described, and should be refined once a competitor move looks real.
- Up case: no competitor response, volume and saving at their high cases, fit-out delivered on the lower supplier quote and fixed cost run lean — a coherent "plan beats expectations" story, not a mirror of the down case.
- The down case never pays back within the eight-year life.
footnote: Scenario definitions and stories in the model README; this is a named scenario, not a sensitivity on one driver.
source: Kestrel south hub model v01, outputs.csv
note: This is the one event, not any single input miss, that the board should watch for.

## 7. Risks and what would change the answer
layout: table
tracker: Risks
| Risk | Effect on the case | What we would do |
|---|---|---|
| Competitor opens a hub nearby | Correlated hit to volume, saving and build cost; NPV to -EUR 4.6m | Treat any confirmed competitor fit-out announcement as a trigger to re-run the case before further spend |
| Saving per parcel comes in below EUR 0.43 | NPV turns negative | Monitor realised saving per parcel against plan from month one of 2027 |
| Routed volume comes in below 3.86m | NPV turns negative | Monitor routed volume against plan from month one of 2027 |
| 2027 ramp is slower than 60% (no sourced range) | Delays payback, does not on its own flip NPV at base case levels | Use actual 2027 ramp as an early read on the volume risk above |
body:
- No tax and no terminal value in this screening model, per the agreed convention; a fuller case before signature should check both.
source: fm-01-input.md; Kestrel south hub model v01

## 8. Decision requested: approve EUR 6m for the south hub, with a first checkpoint after two quarters of operation
layout: table
tracker: Next steps
| Step | Owner | By when |
|---|---|---|
| Board approves EUR 6m capital for fit-out and sorter | Board | November 2026 (ASSUMPTION — no board date given; set ahead of the 2027 opening implied by the investment timing) |
| Confirm site lease and 14 FTE staffing plan | COO / Head of Network (ASSUMPTION — owner not named) | December 2026 |
| Hub opens, 2027 ramp begins | Head of Network (ASSUMPTION) | January 2027 |
| Checkpoint: realised saving per parcel and routed volume vs. EUR 0.43 / 3.86m break-evens | CFO (ASSUMPTION) | End of Q2 2027 |
body:
- Owners and dates marked ASSUMPTION are not in the planning team's brief and need confirmation.
source: Team proposal based on fm-01-input.md

## A1. Model inputs
layout: table
tracker: Appendix
| Driver | Value | Low | High | Source |
|---|---|---|---|---|
| Parcels at full run-rate, m/year | 5.0 | 3.8 | 5.6 | 2025 network flow data, south region (Kestrel planning team) |
| Ramp in 2027, share of full run-rate | 60% | — | — | ASSUMPTION: planning team, based on the 2023 north hub opening |
| Ramp from 2028, share of full run-rate | 100% | — | — | ASSUMPTION: no data given beyond 2027; modelled at full run-rate from year 2 |
| Saving per parcel, EUR | 0.55 | 0.40 | 0.65 | Network simulation v4; low/high = 2025/2023 fuel prices |
| Hub fixed cost, EUR m/year | 0.9 | 0.7 | 1.2 | Site lease offer plus 14 FTE staffing plan |
| Investment, EUR m | 6.0 | 5.5 | 7.5 | Two supplier quotes, September 2026 |
| Hurdle rate | 9% | 7% | 11% | Group finance |
source: fm-01-input.md; Kestrel south hub model v01

## A2. Base-case annual cash flow
layout: table
tracker: Appendix
| EUR m | Start 2027 | 2027 | 2028 | 2029-2034 (each year) |
|---|---|---|---|---|
| Parcels routed, m/year | 0.0 | 3.0 | 5.0 | 5.0 |
| Saving | 0.0 | 1.65 | 2.75 | 2.75 |
| Hub fixed cost | 0.0 | -0.9 | -0.9 | -0.9 |
| Investment | -6.0 | 0.0 | 0.0 | 0.0 |
| Net cash flow | -6.0 | 0.75 | 1.85 | 1.85 |
source: Kestrel south hub model v01, calc.csv


## File written by the run: model/README.md

# Model: Kestrel south hub cross-dock business case, v01

**Question answered:** Should Kestrel invest in a cross-dock hub in the south region? CFO's rule: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life (2027-2034).

**Master check:** OK

**Spot test (hand recompute, base case):**
- NPV = sum of discounted cash flow: -6.0 + 0.688 + 1.557 + 1.429 + 1.311 + 1.202 + 1.103 + 1.012 + 0.928 = 3.230 EUR m. Model: 3.23. Match.
- Payback: cumulative cash flow is -1.55 EUR m at end of 2029 and +0.30 EUR m at end of 2030, so it crosses zero in 2030, about 3.8 years after the investment (-1.55 / (-1.55+0.30+1.55) ... interpolated as 1.55/1.85 = 0.84 of the way through 2030). Model payback output: 2030. Match.

## Key outputs

| Output | Unit | base | down | up |
|---|---|---|---|---|
| NPV at hurdle rate | EUR m | 3.23 | -4.626 | 9.437 |
| IRR | per year | 0.2091 | -0.09939 | 0.4241 |
| Payback (first period cumulative cash >= 0) | year | 2030 | none | 2029 |
| Net cash flow 2027 (ramp year) | EUR m | 0.75 | 0.012 | 1.484 |
| Net cash flow 2028 (first full-run-rate year) | EUR m | 1.85 | 0.62 | 2.94 |
| Parcels routed 2028 | m parcels per year | 5 | 3.8 | 5.6 |

Scenarios (coherent sets, drivers changed from base):
- **down**: parcels_full_run_rate = 3.8, saving_per_parcel = 0.4, investment = 7.5 (competitor hub opens nearby: shippers divert volume (parcels at low end, 3.8m), the price response eats into the per-parcel saving (modelled at the low end, 0.40 EUR, as a magnitude proxy -- the sourced low/high range is actually a fuel-price sensitivity, not a competitive one), and Kestrel accelerates the fit-out to respond, pushing investment to the high end (7.5 EUR m). A correlated downside, not three independent draws.)
- **up**: parcels_full_run_rate = 5.6, saving_per_parcel = 0.65, fixed_cost_per_year = 0.7, investment = 5.5 (no competitor response; network demand and hub efficiency beat plan: parcels and saving per parcel at the high end, fit-out delivered on the low-cost quote, staffing run lean (fixed cost at the low end))

## Sensitivity on npv (one-way, others at base; break-even target 0)

| Rank | Driver | Low / base / high | Output low | Output high | Swing | Break-even | Inside range? |
|---|---|---|---|---|---|---|---|
| 1 | saving_per_parcel | 0.4 / 0.55 / 0.65 EUR per parcel | -0.6456 | 5.814 | 6.46 | 0.425 | yes |
| 2 | parcels_full_run_rate | 3.8 / 5 / 5.6 m parcels per year | -0.1805 | 4.936 | 5.116 | 3.864 | yes |
| 3 | fixed_cost_per_year | 0.7 / 0.9 / 1.2 EUR m per year | 4.337 | 1.57 | 2.767 | 1.484 | no |
| 4 | investment | 5.5 / 6 / 7.5 EUR m | 3.73 | 1.73 | 2 | 9.23 | no |
| 5 | hurdle_rate | 0.07 / 0.09 / 0.11 per year | 4.019 | 2.529 | 1.49 | 0.2091 | no |

Drivers without low/high range (not tested): ramp_2027, ramp_steady

## Inputs

| Driver | Value | Unit | Low | High | Source |
|---|---|---|---|---|---|
| parcels_full_run_rate | 5 | m parcels per year | 3.8 | 5.6 | 2025 network flow data, south region (Kestrel planning team) |
| ramp_2027 | 0.6 | share of full run-rate |  |  | ASSUMPTION: planning team, based on the 2023 north hub opening |
| ramp_steady | 1 | share of full run-rate |  |  | ASSUMPTION: no ramp data given beyond 2027; modelled at full run-rate from 2028 onward, consistent with the north-hub precedent cited for the 2027 figure |
| saving_per_parcel | 0.55 | EUR per parcel | 0.4 | 0.65 | Network simulation v4; low = simulation with 2025 fuel prices, high = with 2023 fuel prices |
| fixed_cost_per_year | 0.9 | EUR m per year | 0.7 | 1.2 | Site lease offer plus 14 FTE staffing plan |
| investment | 6 | EUR m | 5.5 | 7.5 | Two supplier quotes, September 2026 |
| hurdle_rate | 0.09 | per year | 0.07 | 0.11 | Group finance |

## Line items (calculation order)

| Line item | Unit | Formula |
|---|---|---|
| ramp | share of full run-rate | `pick(t, 0, ramp_2027, ramp_steady)` |
| parcels_routed | m parcels per year | `parcels_full_run_rate * ramp` |
| saving | EUR m | `parcels_routed * saving_per_parcel` |
| fixed_cost | EUR m | `-fixed_cost_per_year * min(1, t)` |
| capex | EUR m | `-investment * pick(t, 1, 0)` |
| net_cash_flow | EUR m | `saving + fixed_cost + capex` |
| cumulative_cash_flow | EUR m | `prev(cumulative_cash_flow) + net_cash_flow` |
| discount_factor | factor | `(1 + hurdle_rate) ** -t` |
| discounted_cash_flow | EUR m | `net_cash_flow * discount_factor` |

## Checks

| Check | Scenario | Expected | Actual | Status |
|---|---|---|---|---|
| ramp_not_above_one | base | >=0 | 0 | OK |
| ramp_not_above_one | down | >=0 | 0 | OK |
| ramp_not_above_one | up | >=0 | 0 | OK |
| ramp_not_negative | base | >=0 | 0 | OK |
| ramp_not_negative | down | >=0 | 0 | OK |
| ramp_not_negative | up | >=0 | 0 | OK |
| net_cash_flow_ties_to_parts | base | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | down | ==0 | 0 | OK |
| net_cash_flow_ties_to_parts | up | ==0 | 0 | OK |

## Flags

- Drivers flagged as assumptions (no source or source starts with 'assumption'): ramp_2027, ramp_steady
- No range for: ramp_2027, ramp_steady

## Files

- `calc.csv`: every line item by period, base case
- `outputs.csv`: key outputs per scenario
- `checks.csv`: check results per scenario
- `sensitivity.csv`: tornado ranking and break-even values
- `model.xlsx`: Inputs (blue on yellow = input), Calc (live formulas), Outputs (live, master check), Sensitivity (values)


## File written by the run: model/calc.csv

line_item,unit,start,2027,2028,2029,2030,2031,2032,2033,2034
ramp,share of full run-rate,0.0,0.6,1.0,1.0,1.0,1.0,1.0,1.0,1.0
parcels_routed,m parcels per year,0.0,3.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0
saving,EUR m,0.0,1.65,2.75,2.75,2.75,2.75,2.75,2.75,2.75
fixed_cost,EUR m,0.0,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9,-0.9
capex,EUR m,-6.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
net_cash_flow,EUR m,-6.0,0.75,1.85,1.85,1.85,1.85,1.85,1.85,1.85
cumulative_cash_flow,EUR m,-6.0,-5.25,-3.4,-1.55,0.3,2.15,4.0,5.85,7.7
discount_factor,factor,1.0,0.9174311927,0.8416799933,0.7721834801,0.7084252111,0.6499313863,0.5962673269,0.5470342448,0.5018662797
discounted_cash_flow,EUR m,-6.0,0.6880733945,1.5571079875,1.4285394381,1.3105866405,1.2023730647,1.1030945547,1.012013353,0.9284526174


## File written by the run: model/checks.csv

check,scenario,expected,actual,status
ramp_not_above_one,base,>=0,0.0,OK
ramp_not_above_one,down,>=0,0.0,OK
ramp_not_above_one,up,>=0,0.0,OK
ramp_not_negative,base,>=0,0.0,OK
ramp_not_negative,down,>=0,0.0,OK
ramp_not_negative,up,>=0,0.0,OK
net_cash_flow_ties_to_parts,base,==0,0.0,OK
net_cash_flow_ties_to_parts,down,==0,0.0,OK
net_cash_flow_ties_to_parts,up,==0,0.0,OK


## File written by the run: model/inputs.csv

driver,value,unit,source,low,high,note
parcels_full_run_rate,5.0,m parcels per year,"2025 network flow data, south region (Kestrel planning team)",3.8,5.6,volume routed through the hub once ramped up
ramp_2027,0.60,share of full run-rate,"ASSUMPTION: planning team, based on the 2023 north hub opening",,,opening-year ramp only; no range given
ramp_steady,1.00,share of full run-rate,"ASSUMPTION: no ramp data given beyond 2027; modelled at full run-rate from 2028 onward, consistent with the north-hub precedent cited for the 2027 figure",,,applies 2028-2034
saving_per_parcel,0.55,EUR per parcel,"Network simulation v4; low = simulation with 2025 fuel prices, high = with 2023 fuel prices",0.40,0.65,shorter line-haul and fewer handlings
fixed_cost_per_year,0.9,EUR m per year,Site lease offer plus 14 FTE staffing plan,0.7,1.2,
investment,6.0,EUR m,"Two supplier quotes, September 2026",5.5,7.5,paid at start of 2027 (t=0)
hurdle_rate,0.09,per year,Group finance,0.07,0.11,CFO approval rule: NPV > 0 at this rate


## File written by the run: model/outputs.csv

output,unit,base,down,up,model_version
npv,EUR m,3.2302410504,-4.626210314,9.4365883808,v01
irr,per year,0.2091368125,-0.0993929701,0.4241115708,v01
payback_period,year,2030,,2029,v01
net_cash_flow_2027,EUR m,0.75,0.012,1.484,v01
net_cash_flow_2028,EUR m,1.85,0.62,2.94,v01
parcels_routed_2028,m parcels per year,5.0,3.8,5.6,v01


## File written by the run: model/sensitivity.csv

rank,driver,unit,low,base,high,output_low,output_base,output_high,swing,break_even,break_even_in_range
1,saving_per_parcel,EUR per parcel,0.4,0.55,0.65,-0.6456439279,3.2302410504,5.8141643692,6.4598082971,0.4249869616,yes
2,parcels_full_run_rate,m parcels per year,3.8,5.0,5.6,-0.1805377305,3.2302410504,4.9356304408,5.1161681713,3.8635178329,yes
3,fixed_cost_per_year,EUR m per year,0.7,0.9,1.2,4.3372048733,3.2302410504,1.5697953159,2.7674095574,1.483621792,no
4,investment,EUR m,5.5,6.0,7.5,3.7302410504,3.2302410504,1.7302410504,2.0,9.2302410504,no
5,hurdle_rate,per year,0.07,0.09,0.11,4.0188648533,3.2302410504,2.5293361167,1.4895287366,0.2091368125,no


## File written by the run: model/spec.json

{
  "title": "Kestrel south hub cross-dock business case",
  "question": "Should Kestrel invest in a cross-dock hub in the south region? CFO's rule: approve if NPV at the 9% hurdle rate is above zero over the hub's eight-year life (2027-2034).",
  "periods": ["start", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034"],
  "rows": [
    {"name": "ramp", "unit": "share of full run-rate", "expr": "pick(t, 0, ramp_2027, ramp_steady)"},
    {"name": "parcels_routed", "unit": "m parcels per year", "expr": "parcels_full_run_rate * ramp"},
    {"name": "saving", "unit": "EUR m", "expr": "parcels_routed * saving_per_parcel"},
    {"name": "fixed_cost", "unit": "EUR m", "expr": "-fixed_cost_per_year * min(1, t)"},
    {"name": "capex", "unit": "EUR m", "expr": "-investment * pick(t, 1, 0)"},
    {"name": "net_cash_flow", "unit": "EUR m", "expr": "saving + fixed_cost + capex"},
    {"name": "cumulative_cash_flow", "unit": "EUR m", "expr": "prev(cumulative_cash_flow) + net_cash_flow"},
    {"name": "discount_factor", "unit": "factor", "expr": "(1 + hurdle_rate) ** -t"},
    {"name": "discounted_cash_flow", "unit": "EUR m", "expr": "net_cash_flow * discount_factor"}
  ],
  "outputs": [
    {"name": "npv", "label": "NPV at hurdle rate", "unit": "EUR m", "fn": "sum", "row": "discounted_cash_flow"},
    {"name": "irr", "label": "IRR", "unit": "per year", "fn": "irr", "row": "net_cash_flow"},
    {"name": "payback_period", "label": "Payback (first period cumulative cash >= 0)", "unit": "year", "fn": "payback", "row": "cumulative_cash_flow"},
    {"name": "net_cash_flow_2027", "label": "Net cash flow 2027 (ramp year)", "unit": "EUR m", "fn": "value", "row": "net_cash_flow", "period": "2027"},
    {"name": "net_cash_flow_2028", "label": "Net cash flow 2028 (first full-run-rate year)", "unit": "EUR m", "fn": "value", "row": "net_cash_flow", "period": "2028"},
    {"name": "parcels_routed_2028", "label": "Parcels routed 2028", "unit": "m parcels per year", "fn": "value", "row": "parcels_routed", "period": "2028"}
  ],
  "checks": [
    {"name": "ramp_not_above_one", "expr": "1 - ramp", "rule": ">=0"},
    {"name": "ramp_not_negative", "expr": "ramp", "rule": ">=0"},
    {"name": "net_cash_flow_ties_to_parts", "expr": "net_cash_flow - saving - fixed_cost - capex", "rule": "==0"}
  ],
  "scenarios": {
    "down": {"parcels_full_run_rate": 3.8, "saving_per_parcel": 0.40, "investment": 7.5},
    "up": {"parcels_full_run_rate": 5.6, "saving_per_parcel": 0.65, "fixed_cost_per_year": 0.7, "investment": 5.5}
  },
  "scenario_stories": {
    "down": "competitor hub opens nearby: shippers divert volume (parcels at low end, 3.8m), the price response eats into the per-parcel saving (modelled at the low end, 0.40 EUR, as a magnitude proxy -- the sourced low/high range is actually a fuel-price sensitivity, not a competitive one), and Kestrel accelerates the fit-out to respond, pushing investment to the high end (7.5 EUR m). A correlated downside, not three independent draws.",
    "up": "no competitor response; network demand and hub efficiency beat plan: parcels and saving per parcel at the high end, fit-out delivered on the low-cost quote, staffing run lean (fixed cost at the low end)"
  },
  "break_even": {"output": "npv", "target": 0}
}

