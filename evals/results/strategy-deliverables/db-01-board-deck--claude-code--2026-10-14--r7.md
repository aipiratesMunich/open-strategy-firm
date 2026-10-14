# db-01-board-deck on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (12/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Uses one premium figure throughout, or flags the 1.1 vs 1.2 mismatch to its owner | yes | Assistant message: 'I didn't silently pick one; I kept 1.2 in the total... and called out the EUR 0.1m churn nuance in a visible footnote on the waterfall slide (page 8)'; footnote on page 8: 'net of the 2024-style churn this step is about EUR 1.1m, which would narrow the total by about EUR 0.1m' |
| Writes 06-deck.md in spec format with frontmatter, SCQA opening in four sentences, key line above first slide | yes | Frontmatter block with title/client/audience/date/format/theme; 'Opening (SCQA)' with Situation/Complication/Question/Answer bullets; 'Key line' section with 4 points, all placed before '## 1. Which growth moves...' |
| Page 2 is executive summary with governing thought title, numbered key-line points, EUR 1.3m gap, answer-change condition, EUR 1.9m decision request with COO owner and start date | yes | Page 2 title is the governing thought; body is an <ol> with the four key-line points; ask states 'approve EUR 1.9m... owner COO Lena Marsh, start January 2027... remaining EUR 1.3m gap... accepted... answer changes if off-peak take-up falls below 6,000 members by end of 2027' |
| Every main-page title is a full-sentence finding with a number/comparison; no topic-label titles | yes | e.g. page 3: 'Fernhill gyms run at just 31% utilisation from 10am to 4pm, versus 92% from 6 to 9pm'; page 9: 'The board can approve EUR 1.9m on 10 December 2026...'; no page titled generically like 'Utilisation' or 'Next steps' (those are trackers, not titles) |
| 8-15 main pages, sections follow key line not phases, new-city analysis included as a finding | yes | 9 main pages (title, summary, 2 off-peak pages, corporate, premium, new-city, bridge, next steps) plus 2 appendix pages; page 7 'A new-city gym needs EUR 4.5m and pays back in about seven years — beyond the board's four-year limit' presented as a finding, not hidden |
| Utilisation bar chart with 10am-4pm band highlighted; revenue bridge as waterfall 58.0→64.7 with 66.0 target reference and 1.3 gap visible | yes | Page 3 chart highlight: '10 am-4 pm; 6-9 pm' with 31% bar colored accent; page 8 waterfall rows 58.0→3.1→2.4→1.2→64.7 with reference line 'reference: 66 / Target EUR 66.0m by 2028' and title stating 'EUR 1.3m short of the EUR 66.0m target' |
| Every chart has header (measure, unit, period) and a source line from the synthesis | yes | e.g. page 3 header: 'Average gym utilisation by time band, % of capacity, 34 gyms, Jan to Aug 2026', source: 'Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4' |
| Numbers tie across executive summary, section pages and bridge with no rounding drift | yes | 3.1+2.4+1.2=6.7 consistently used in exec summary title ('add about EUR 6.7m') and bridge page 8 ('three moves add about EUR 6.7m, reaching EUR 64.7m') |
| Titles-only read-through is listed and tells the story in order | yes | '# Titles-only read-through' section: 'the nine main titles alone tell the board what to fund (off-peak, corporate, pricing), what to drop (a new city), what the total adds up to, the remaining gap, and what is being asked of them'; also #overview div in HTML with ordered title list |
| If Python available, runs render_deck.py and reports warnings; otherwise says spec delivered unrendered | yes | 'the renderer's own lint check came back with zero warnings' alongside delivered 06-deck.html and 06-deck.pptx |
| Does not add new analysis, numbers, competitor facts or sources not in the synthesis | yes | All figures (58.0, 3.1, 2.4, 1.2, 64.7, 66.0, 1.3, premium 4x25000x12, off-peak 10800x24x12) match the reference synthesis values given in context; no extraneous figures introduced |
| Does not put agenda, method or background pages before the executive summary | yes | Page 1 is the title/question page, page 2 is immediately the executive summary; no agenda/method page in between |

## Transcript

## Turn 1

**User:** Turn the Fernhill synthesis into the board pre-read deck for 10 December. (Attached in the working directory: db-01-synthesis.md.)

The board pre-read deck is built: `06-deck.md` (spec), `06-deck.html` (open in a browser — arrows to navigate, `t` for titles-only view, print to PDF), and `06-deck.pptx`.

**Structure** — 9 main pages + 2-page appendix:
1. Title (the question)
2. Executive summary — governing thought, all four moves with numbers, the EUR 1.3m gap, and the decision ask
3–4. Off-peak membership (31% vs 92% utilisation → EUR 3.1m)
5. Corporate wellness (pilot-proven → EUR 2.4m)
6. Premium price (EUR 5–8 below competitors → EUR 1.2m)
7. Why a new city is ruled out (7-year payback vs 4-year limit)
8. Total effect waterfall (58.0 → 64.7, EUR 1.3m short of the EUR 66.0m target — gap shown, not hidden)
9. Decision requested and next steps, with risks and the answer-changes threshold
A1–A2. Utilisation detail and assumptions/sources

One thing worth flagging: the source document itself has a small internal inconsistency — the premium-price line is "about EUR 1.2m" in the headline total table but "about EUR 1.1m" net of churn in the supporting text. I didn't silently pick one; I kept 1.2 in the total (matching the synthesis's own arithmetic) and called out the EUR 0.1m churn nuance in a visible footnote on the waterfall slide (page 8) rather than burying it.

All numbers tie across the executive summary, section pages, waterfall and appendix, and the renderer's own lint check came back with zero warnings.


## Files in work dir after run

- 06-deck.html
- 06-deck.md
- 06-deck.pptx
- db-01-synthesis.md

## File written by the run: 06-deck.html

<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fernhill Fitness growth moves 2027-2028</title><style>
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
<body><div id="stage"><section class="slide l-title" id="s1" data-title="Which growth moves should Fernhill approve on 10 December 2026 to reach EUR 66.0m by 2028?"><div class="t-client">Fernhill Fitness (fictional)</div><h1 class="t-title">Which growth moves should Fernhill approve on 10 December 2026 to reach EUR 66.0m by 2028?</h1><p class="t-sub">Pre-read on off-peak membership, corporate wellness and premium pricing</p><p class="t-meta">Board of directors, pre-read for the 10 December 2026 meeting | December 2026</p><footer><div></div><span class="pn">1</span></footer><aside class="notes"><b>Speaker note</b> Pre-read for the 10 December 2026 board meeting. The decision requested is on page 2 and again on page 9.</aside></section><section class="slide l-summary" id="s2" data-title="Fernhill should fill its empty daytime capacity, sell corporate wellness and raise the premium price by EUR 4; together they add about EUR 6.7m by 2028, reaching EUR 64.7m against the EUR 66.0m target"><div class="tracker">Executive summary</div><h2 class="title long">Fernhill should fill its empty daytime capacity, sell corporate wellness and raise the premium price by EUR 4; together they add about EUR 6.7m by 2028, reaching EUR 64.7m against the EUR 66.0m target</h2><div class="content summary"><p class="lead">Fernhill operates 34 gyms with revenue flat at EUR 58.0m since 2023, while the board targets EUR 66.0m by 2028 without opening gyms in new cities and with at most EUR 2m of investment.</p><ol><li>Daytime utilisation averages just 31% from 10am to 4pm versus 92% from 6 to 9pm across 34 gyms; an off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028 (range EUR 2.0m to 3.8m) at roughly 10,800 members.</li><li>Corporate wellness contracts, proven with six employers in a 2026 pilot (1,150 employees), add about EUR 2.4m a year by 2028 at 40 contracts (range EUR 1.4m to 3.0m), with two corporate sales hires needed.</li><li>The premium tier is priced EUR 5 to 8 below both main competitors; a EUR 4 increase adds about EUR 1.2m a year before churn (about EUR 1.1m net of the churn seen after the 2024 increase).</li><li>A new-city gym needs EUR 4.5m and pays back in about seven years at the ramp of the last three openings — beyond the board&#x27;s four-year limit, so we do not recommend one before 2029.</li></ol><div class="ask"><strong>Decision requested on 10 December 2026:</strong> approve EUR 1.9m (off-peak launch marketing EUR 0.8m; two corporate sales hires and pilot extension EUR 0.6m; booking-app changes EUR 0.5m), owner COO Lena Marsh, start January 2027; premium price change from 1 March 2027. The remaining EUR 1.3m gap to the EUR 66.0m target is accepted rather than funding a new city. The answer changes if off-peak take-up falls below 6,000 members by end of 2027.</div></div><footer><div class="source">Source: Fernhill growth model v4; off-peak and corporate pilots 2026; competitor price lists, September 2026; opening P&amp;Ls 2019-2023</div><span class="pn">2</span></footer><aside class="notes"><b>Speaker note</b> Read the bold line and the ask. Pages 3 to 7 prove each of the four points; page 8 shows the total against target.</aside></section><section class="slide l-chart" id="s3" data-title="Fernhill gyms run at just 31% utilisation from 10am to 4pm, versus 92% from 6 to 9pm"><div class="tracker">1 Off-peak membership</div><h2 class="title">Fernhill gyms run at just 31% utilisation from 10am to 4pm, versus 92% from 6 to 9pm</h2><div class="header">Average gym utilisation by time band, % of capacity, 34 gyms, Jan to Aug 2026</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Fernhill gyms run at just 31% utilisation from 10am to 4pm, versus 92% from 6 to 9pm"><rect x="61.4" y="145.6" width="116.0" height="162.4" fill="#B8C0CC"/><text x="119.4" y="137.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58%</text><text x="121.4" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-10 am</text><rect x="288.2" y="221.2" width="116.0" height="86.8" fill="#D9822B"/><text x="346.2" y="213.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">31%</text><text x="348.2" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">10 am-4 pm</text><rect x="515.0" y="128.8" width="116.0" height="179.2" fill="#B8C0CC"/><text x="573.0" y="120.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64%</text><text x="575.0" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">4-6 pm</text><rect x="741.8" y="50.4" width="116.0" height="257.6" fill="#D9822B"/><text x="799.8" y="42.4" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">92%</text><text x="801.8" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-9 pm</text><rect x="968.6" y="196.0" width="116.0" height="112.0" fill="#B8C0CC"/><text x="1026.6" y="188.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">40%</text><text x="1028.6" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">9-11 pm</text><line x1="8" x2="1142" y1="308.0" y2="308.0" stroke="#14213D" stroke-width="1"/></svg></div></div><div class="takeaway">The 10am-4pm band is the single largest block of unused capacity across all 34 gyms — the target for the new off-peak membership.</div><footer><div class="source">Source: Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4</div><span class="pn">3</span></footer><aside class="notes"><b>Speaker note</b> This is the evidence behind key-line point 1. The off-peak pilot (next page) tests whether members will actually buy into this capacity.</aside></section><section class="slide l-chart" id="s4" data-title="An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028, reaching roughly 10,800 members"><div class="tracker">1 Off-peak membership</div><h2 class="title long">An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028, reaching roughly 10,800 members</h2><div class="header">Off-peak membership revenue by scenario, EUR m per year, 2028</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028, reaching roughly 10,800 members"><rect x="62.0" y="188.0" width="116.0" height="160.0" fill="#B8C0CC"/><text x="120.0" y="180.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.0</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Low</text><rect x="290.0" y="100.0" width="116.0" height="248.0" fill="#D9822B"/><text x="348.0" y="92.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.1</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base (2028 plan)</text><rect x="518.0" y="44.0" width="116.0" height="304.0" fill="#B8C0CC"/><text x="576.0" y="36.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.8</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">High</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Priced at EUR 24 a month, below the EUR 39 standard rate</li><li>Pilot: 4 gyms, May to Aug 2026, 420 sign-ups, 6% of sign-ups were existing members downgrading</li><li>Risk: if downgrading exceeds 15% of new sign-ups, this step adds less than EUR 2.0m</li></ul></div></div><footer><div class="source">Source: Off-peak pilot, 4 gyms, May-Aug 2026; gate-entry data; Fernhill growth model v4</div><span class="pn">4</span></footer><aside class="notes"><b>Speaker note</b> 6% downgrading in the pilot is well inside the 15% threshold that would cut this below EUR 2.0m, but the board should know it is the single biggest swing factor in the plan.</aside></section><section class="slide l-chart" id="s5" data-title="Corporate wellness, proven with six employers in pilot, adds about EUR 2.4m a year by 2028 at 40 contracts"><div class="tracker">2 Corporate wellness</div><h2 class="title long">Corporate wellness, proven with six employers in pilot, adds about EUR 2.4m a year by 2028 at 40 contracts</h2><div class="header">Corporate wellness revenue by scenario, EUR m per year, 2028</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Corporate wellness, proven with six employers in pilot, adds about EUR 2.4m a year by 2028 at 40 contracts"><rect x="62.0" y="198.7" width="116.0" height="149.3" fill="#B8C0CC"/><text x="120.0" y="190.7" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1.4</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Low</text><rect x="290.0" y="92.0" width="116.0" height="256.0" fill="#D9822B"/><text x="348.0" y="84.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.4</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base (40 contracts)</text><rect x="518.0" y="28.0" width="116.0" height="320.0" fill="#B8C0CC"/><text x="576.0" y="20.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.0</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">High</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Pilot: six employers signed, 1,150 employees enrolled, 2026</li><li>Average contract value about EUR 60k a year</li><li>Needs two corporate sales hires starting by February 2027</li></ul></div></div><footer><div class="source">Source: Corporate pilot contracts, 2026; Fernhill growth model v4</div><span class="pn">5</span></footer><aside class="notes"><b>Speaker note</b> This is the most proven of the three moves — it is already signed revenue in pilot, not a projection from a benchmark.</aside></section><section class="slide l-chart" id="s6" data-title="Fernhill&#x27;s premium tier is priced EUR 5 to 8 below both competitors; a EUR 4 rise adds about EUR 1.2m a year"><div class="tracker">3 Premium price</div><h2 class="title long">Fernhill&#x27;s premium tier is priced EUR 5 to 8 below both competitors; a EUR 4 rise adds about EUR 1.2m a year</h2><div class="header">Premium membership price, EUR per month, comparable offer (pool, classes, sauna), September 2026</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Fernhill&#x27;s premium tier is priced EUR 5 to 8 below both competitors; a EUR 4 rise adds about EUR 1.2m a year"><rect x="160" y="42.3" width="770.5" height="43.0" fill="#B8C0CC"/><text x="938.5" y="69.3" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">67</text><text x="148.0" y="70.3" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor B</text><rect x="160" y="157.0" width="736.0" height="43.0" fill="#B8C0CC"/><text x="904.0" y="184.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="148.0" y="185.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor A</text><rect x="160" y="271.7" width="678.5" height="43.0" fill="#D9822B"/><text x="846.5" y="298.7" font-size="15" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">59</text><text x="148.0" y="299.7" font-size="15" text-anchor="end" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Fernhill (current)</text><line x1="160" x2="160" y1="8" y2="352.0" stroke="#14213D"/></svg></div></div><div class="takeaway">After the EUR 4 increase Fernhill would charge EUR 63 a month, still below both competitors; net of the churn seen after the 2024 increase, this step adds about EUR 1.1m a year.</div><footer><div class="source">Source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026; Fernhill growth model v4</div><span class="pn">6</span></footer><aside class="notes"><b>Speaker note</b> 25,000 premium members x EUR 4 x 12 months = EUR 1.2m before churn. The 1.1m net figure uses the extra 1.5 points of churn for three months seen after the 2024 increase.</aside></section><section class="slide l-table" id="s7" data-title="A new-city gym needs EUR 4.5m and pays back in about seven years — beyond the board&#x27;s four-year limit"><div class="tracker">4 New city (not recommended)</div><h2 class="title long">A new-city gym needs EUR 4.5m and pays back in about seven years — beyond the board&#x27;s four-year limit</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Metric</th><th>New-city gym</th></tr><tr><td>Investment required</td><td>EUR 4.5m</td></tr><tr><td>Payback period, at the ramp of the last 3 openings</td><td>about 7 years</td></tr><tr><td>Board&#x27;s payback limit</td><td>4 years</td></tr></table></div><div class="side"><ul><li>Based on the ramp of the three most recent openings, 2019 to 2023</li><li>Not recommended before the three approved moves have run and the 2028 target is reassessed; earliest 2029</li></ul></div></div><footer><div class="source">Source: Opening P&amp;Ls 2019-2023; Fernhill growth model v4</div><span class="pn">7</span></footer><aside class="notes"><b>Speaker note</b> This closes off the fourth key-line point: a new city was considered and ruled out, not simply left off the list.</aside></section><section class="slide l-chart" id="s8" data-title="The three moves add about EUR 6.7m, reaching EUR 64.7m — EUR 1.3m short of the EUR 66.0m target by 2028"><div class="tracker">Total effect</div><h2 class="title long">The three moves add about EUR 6.7m, reaching EUR 64.7m — EUR 1.3m short of the EUR 66.0m target by 2028</h2><div class="header">Revenue bridge, 2026 actual to 2028 with the three moves, EUR m per year</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="The three moves add about EUR 6.7m, reaching EUR 64.7m — EUR 1.3m short of the EUR 66.0m target by 2028"><rect x="46.4" y="116.0" width="120.0" height="232.0" fill="#14213D"/><line x1="8.0" x2="992.0" y1="84.0" y2="84.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="1000.0" y="89.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Target EUR 66.0m by 2028</text><text x="106.4" y="108.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58.0</text><text x="106.4" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2026</text><rect x="243.2" y="103.6" width="120.0" height="12.4" fill="#D9822B"/><text x="303.2" y="95.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+3.1</text><line x1="166.4" x2="243.2" y1="116.0" y2="116.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="303.2" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Off-peak membership</text><rect x="440.0" y="94.0" width="120.0" height="9.6" fill="#B8C0CC"/><text x="500.0" y="86.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+2.4</text><line x1="363.2" x2="440.0" y1="103.6" y2="103.6" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="500.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Corporate wellness</text><rect x="636.8" y="89.2" width="120.0" height="4.8" fill="#B8C0CC"/><text x="696.8" y="81.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+1.2</text><line x1="560.0" x2="636.8" y1="94.0" y2="94.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="696.8" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Premium price</text><rect x="833.6" y="89.2" width="120.0" height="258.8" fill="#14213D"/><text x="893.6" y="81.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64.7</text><line x1="756.8" x2="833.6" y1="89.2" y2="89.2" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="893.6" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2028 with the</text><text x="893.6" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">three moves</text><line x1="8" x2="992" y1="348.0" y2="348.0" stroke="#14213D"/></svg></div></div><footer><div class="footnote">Premium price step shown before churn (EUR 1.2m), consistent with the growth model total; net of the 2024-style churn this step is about EUR 1.1m, which would narrow the total by about EUR 0.1m. Core revenue is assumed flat at EUR 58.0m without the three moves (membership numbers flat 2023-2026).</div><div class="source">Source: Fernhill growth model v4</div><span class="pn">8</span></footer><aside class="notes"><b>Speaker note</b> The gap is shown, not hidden. The board is being asked to accept EUR 1.3m of shortfall rather than fund a new city to close it, because a new city does not pay back within the four-year limit (page 7).</aside></section><section class="slide l-table" id="s9" data-title="The board can approve EUR 1.9m on 10 December 2026, with execution starting in January 2027"><div class="tracker">Next steps</div><h2 class="title">The board can approve EUR 1.9m on 10 December 2026, with execution starting in January 2027</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Step</th><th>Owner</th><th>By when</th></tr><tr><td>Board approval of EUR 1.9m and the EUR 4 premium price rise</td><td>Board</td><td>10 December 2026</td></tr><tr><td>Off-peak membership launch and marketing</td><td>COO Lena Marsh</td><td>January 2027</td></tr><tr><td>Two corporate sales hires start</td><td>COO Lena Marsh</td><td>February 2027</td></tr><tr><td>Booking-app changes live</td><td>COO Lena Marsh</td><td>January 2027</td></tr><tr><td>Premium price change in force</td><td>COO Lena Marsh</td><td>1 March 2027</td></tr><tr><td>Review off-peak take-up against the 6,000-member threshold</td><td>COO Lena Marsh</td><td>December 2027</td></tr></table></div><div class="side"><ul><li>Risk: if more than 15% of new off-peak members are downgrading standard members, the off-peak move adds less than EUR 2.0m</li><li>Risk: the corporate sales ramp depends on both hires starting by February 2027</li><li>What would change the answer: off-peak take-up below 6,000 members by end of 2027</li></ul></div></div><div class="takeaway">The plan holds only if off-peak downgrading stays under 15% of new sign-ups and both corporate hires start by February 2027.</div><footer><div class="source">Source: Fernhill growth model v4; decision request, Fernhill growth synthesis, December 2026</div><span class="pn">9</span></footer><aside class="notes"><b>Speaker note</b> Ask for the decision explicitly. Offer the December 2027 review as the checkpoint against the 6,000-member threshold.</aside></section><section class="slide l-table" id="s10" data-title="Utilisation by time band, average of 34 gyms, January to August 2026"><div class="tracker">Appendix</div><h2 class="title">Utilisation by time band, average of 34 gyms, January to August 2026</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Time band</th><th class="num">Utilisation</th></tr><tr><td>6-10 am</td><td class="num">58%</td></tr><tr><td>10 am-4 pm</td><td class="num">31%</td></tr><tr><td>4-6 pm</td><td class="num">64%</td></tr><tr><td>6-9 pm</td><td class="num">92%</td></tr><tr><td>9-11 pm</td><td class="num">40%</td></tr></table></div></div><footer><div class="source">Source: Gate-entry data, 34 gyms, Jan to Aug 2026</div><span class="pn">A1</span></footer></section><section class="slide l-table" id="s11" data-title="Key assumptions and sources behind the EUR 6.7m of growth moves"><div class="tracker">Appendix</div><h2 class="title">Key assumptions and sources behind the EUR 6.7m of growth moves</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Driver</th><th>Value</th><th>Basis</th></tr><tr><td>Off-peak members by 2028</td><td>about 10,800</td><td>Fernhill growth model v4</td></tr><tr><td>Off-peak price</td><td>EUR 24/month (vs EUR 39 standard)</td><td>Pilot pricing, 2026</td></tr><tr><td>Off-peak pilot downgrading</td><td>6% of sign-ups</td><td>Pilot, 4 gyms, May-Aug 2026, 420 sign-ups</td></tr><tr><td>Corporate contracts by 2028</td><td>40 (avg EUR 60k/year)</td><td>Fernhill growth model v4</td></tr><tr><td>Corporate pilot</td><td>6 employers, 1,150 employees</td><td>Corporate pilot contracts, 2026</td></tr><tr><td>Premium price increase</td><td>EUR 4/month on 25,000 members</td><td>Fernhill membership data 2024-2026</td></tr><tr><td>Premium churn after increase</td><td>1.5 points extra for 3 months (2024 precedent)</td><td>Fernhill membership data 2024-2026</td></tr><tr><td>New-city investment</td><td>EUR 4.5m</td><td>Opening P&amp;Ls 2019-2023</td></tr><tr><td>New-city payback</td><td>about 7 years</td><td>Opening P&amp;Ls 2019-2023, ramp of last 3 openings</td></tr></table></div></div><footer><div class="source">Source: Fernhill growth model v4; Fernhill growth synthesis, December 2026</div><span class="pn">A2</span></footer></section></div>
<div id="overview"><h1>Titles-only read-through</h1><ol><li>Which growth moves should Fernhill approve on 10 December 2026 to reach EUR 66.0m by 2028? <span style='color:#8A93A3'>(1)</span></li><li>Fernhill should fill its empty daytime capacity, sell corporate wellness and raise the premium price by EUR 4; together they add about EUR 6.7m by 2028, reaching EUR 64.7m against the EUR 66.0m target <span style='color:#8A93A3'>(2)</span></li><li>Fernhill gyms run at just 31% utilisation from 10am to 4pm, versus 92% from 6 to 9pm <span style='color:#8A93A3'>(3)</span></li><li>An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028, reaching roughly 10,800 members <span style='color:#8A93A3'>(4)</span></li><li>Corporate wellness, proven with six employers in pilot, adds about EUR 2.4m a year by 2028 at 40 contracts <span style='color:#8A93A3'>(5)</span></li><li>Fernhill&#x27;s premium tier is priced EUR 5 to 8 below both competitors; a EUR 4 rise adds about EUR 1.2m a year <span style='color:#8A93A3'>(6)</span></li><li>A new-city gym needs EUR 4.5m and pays back in about seven years — beyond the board&#x27;s four-year limit <span style='co

## File written by the run: 06-deck.md

---
title: Fernhill Fitness growth moves 2027-2028
client: Fernhill Fitness (fictional)
audience: Board of directors, pre-read for the 10 December 2026 meeting
date: December 2026
format: deck
theme:
  text: "#14213D"
  accent: "#D9822B"
  muted: "#B8C0CC"
  light: "#E8EBF0"
  background: "#FFFFFF"
  font: "Helvetica Neue, Helvetica, Arial, sans-serif"
---

# Deck: Which growth moves should Fernhill approve on 10 December 2026?

*Fictional company. All figures, people and documents invented for evaluation.*

**Opening (SCQA)**
- Situation: Fernhill operates 34 gyms with revenue of EUR 58.0m in 2026.
- Complication: The board targets EUR 66.0m by 2028, without opening gyms in new cities and with at most EUR 2m of investment.
- Question: Which growth moves should the board approve on 10 December 2026?
- Answer: Approve an off-peak membership, corporate wellness contracts and a EUR 4 premium price rise; together they add about EUR 6.7m, leaving a EUR 1.3m gap the board should accept rather than fund a new city.

**Key line**
1. Daytime capacity is the largest unused asset; an off-peak membership fills it.
2. Corporate wellness contracts are proven in the pilot.
3. The premium tier is priced below both main competitors.
4. A new city does not pay back within the board's four-year limit.

## 1. Which growth moves should Fernhill approve on 10 December 2026 to reach EUR 66.0m by 2028?
layout: title
subtitle: Pre-read on off-peak membership, corporate wellness and premium pricing
note: Pre-read for the 10 December 2026 board meeting. The decision requested is on page 2 and again on page 9.

## 2. Fernhill should fill its empty daytime capacity, sell corporate wellness and raise the premium price by EUR 4; together they add about EUR 6.7m by 2028, reaching EUR 64.7m against the EUR 66.0m target
layout: summary
tracker: Executive summary
lead: Fernhill operates 34 gyms with revenue flat at EUR 58.0m since 2023, while the board targets EUR 66.0m by 2028 without opening gyms in new cities and with at most EUR 2m of investment.
body:
- Daytime utilisation averages just 31% from 10am to 4pm versus 92% from 6 to 9pm across 34 gyms; an off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028 (range EUR 2.0m to 3.8m) at roughly 10,800 members.
- Corporate wellness contracts, proven with six employers in a 2026 pilot (1,150 employees), add about EUR 2.4m a year by 2028 at 40 contracts (range EUR 1.4m to 3.0m), with two corporate sales hires needed.
- The premium tier is priced EUR 5 to 8 below both main competitors; a EUR 4 increase adds about EUR 1.2m a year before churn (about EUR 1.1m net of the churn seen after the 2024 increase).
- A new-city gym needs EUR 4.5m and pays back in about seven years at the ramp of the last three openings — beyond the board's four-year limit, so we do not recommend one before 2029.
ask: **Decision requested on 10 December 2026:** approve EUR 1.9m (off-peak launch marketing EUR 0.8m; two corporate sales hires and pilot extension EUR 0.6m; booking-app changes EUR 0.5m), owner COO Lena Marsh, start January 2027; premium price change from 1 March 2027. The remaining EUR 1.3m gap to the EUR 66.0m target is accepted rather than funding a new city. The answer changes if off-peak take-up falls below 6,000 members by end of 2027.
source: Fernhill growth model v4; off-peak and corporate pilots 2026; competitor price lists, September 2026; opening P&Ls 2019-2023
note: Read the bold line and the ask. Pages 3 to 7 prove each of the four points; page 8 shows the total against target.

## 3. Fernhill gyms run at just 31% utilisation from 10am to 4pm, versus 92% from 6 to 9pm
layout: chart
tracker: 1 Off-peak membership
message: time-series
chart: bar
header: Average gym utilisation by time band, % of capacity, 34 gyms, Jan to Aug 2026
highlight: 10 am-4 pm; 6-9 pm
| Time band | Utilisation |
|---|---|
| 6-10 am | 58% |
| 10 am-4 pm | 31% |
| 4-6 pm | 64% |
| 6-9 pm | 92% |
| 9-11 pm | 40% |
takeaway: The 10am-4pm band is the single largest block of unused capacity across all 34 gyms — the target for the new off-peak membership.
source: Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4
note: This is the evidence behind key-line point 1. The off-peak pilot (next page) tests whether members will actually buy into this capacity.

## 4. An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028, reaching roughly 10,800 members
layout: chart
tracker: 1 Off-peak membership
message: ranking
chart: bar
header: Off-peak membership revenue by scenario, EUR m per year, 2028
highlight: Base (2028 plan)
| Scenario | Revenue |
|---|---|
| Low | 2.0 |
| Base (2028 plan) | 3.1 |
| High | 3.8 |
body:
- Priced at EUR 24 a month, below the EUR 39 standard rate
- Pilot: 4 gyms, May to Aug 2026, 420 sign-ups, 6% of sign-ups were existing members downgrading
- Risk: if downgrading exceeds 15% of new sign-ups, this step adds less than EUR 2.0m
source: Off-peak pilot, 4 gyms, May-Aug 2026; gate-entry data; Fernhill growth model v4
note: 6% downgrading in the pilot is well inside the 15% threshold that would cut this below EUR 2.0m, but the board should know it is the single biggest swing factor in the plan.

## 5. Corporate wellness, proven with six employers in pilot, adds about EUR 2.4m a year by 2028 at 40 contracts
layout: chart
tracker: 2 Corporate wellness
message: ranking
chart: bar
header: Corporate wellness revenue by scenario, EUR m per year, 2028
highlight: Base (40 contracts)
| Scenario | Revenue |
|---|---|
| Low | 1.4 |
| Base (40 contracts) | 2.4 |
| High | 3.0 |
body:
- Pilot: six employers signed, 1,150 employees enrolled, 2026
- Average contract value about EUR 60k a year
- Needs two corporate sales hires starting by February 2027
source: Corporate pilot contracts, 2026; Fernhill growth model v4
note: This is the most proven of the three moves — it is already signed revenue in pilot, not a projection from a benchmark.

## 6. Fernhill's premium tier is priced EUR 5 to 8 below both competitors; a EUR 4 rise adds about EUR 1.2m a year
layout: chart
tracker: 3 Premium price
message: ranking
chart: hbar
header: Premium membership price, EUR per month, comparable offer (pool, classes, sauna), September 2026
highlight: Fernhill (current)
| Supplier | Price |
|---|---|
| Competitor B | 67 |
| Competitor A | 64 |
| Fernhill (current) | 59 |
takeaway: After the EUR 4 increase Fernhill would charge EUR 63 a month, still below both competitors; net of the churn seen after the 2024 increase, this step adds about EUR 1.1m a year.
source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026; Fernhill growth model v4
note: 25,000 premium members x EUR 4 x 12 months = EUR 1.2m before churn. The 1.1m net figure uses the extra 1.5 points of churn for three months seen after the 2024 increase.

## 7. A new-city gym needs EUR 4.5m and pays back in about seven years — beyond the board's four-year limit
layout: table
tracker: 4 New city (not recommended)
| Metric | New-city gym |
|---|---|
| Investment required | EUR 4.5m |
| Payback period, at the ramp of the last 3 openings | about 7 years |
| Board's payback limit | 4 years |
body:
- Based on the ramp of the three most recent openings, 2019 to 2023
- Not recommended before the three approved moves have run and the 2028 target is reassessed; earliest 2029
source: Opening P&Ls 2019-2023; Fernhill growth model v4
note: This closes off the fourth key-line point: a new city was considered and ruled out, not simply left off the list.

## 8. The three moves add about EUR 6.7m, reaching EUR 64.7m — EUR 1.3m short of the EUR 66.0m target by 2028
layout: chart
tracker: Total effect
message: flow
chart: waterfall
header: Revenue bridge, 2026 actual to 2028 with the three moves, EUR m per year
reference: 66 | Target EUR 66.0m by 2028
highlight: Off-peak membership
| Step | EUR m | Type |
|---|---|---|
| Revenue 2026 | 58.0 | total |
| Off-peak membership | 3.1 | delta |
| Corporate wellness | 2.4 | delta |
| Premium price | 1.2 | delta |
| Revenue 2028 with the three moves | 64.7 | total |
footnote: Premium price step shown before churn (EUR 1.2m), consistent with the growth model total; net of the 2024-style churn this step is about EUR 1.1m, which would narrow the total by about EUR 0.1m. Core revenue is assumed flat at EUR 58.0m without the three moves (membership numbers flat 2023-2026).
source: Fernhill growth model v4
note: The gap is shown, not hidden. The board is being asked to accept EUR 1.3m of shortfall rather than fund a new city to close it, because a new city does not pay back within the four-year limit (page 7).

## 9. The board can approve EUR 1.9m on 10 December 2026, with execution starting in January 2027
layout: table
tracker: Next steps
takeaway: The plan holds only if off-peak downgrading stays under 15% of new sign-ups and both corporate hires start by February 2027.
| Step | Owner | By when |
|---|---|---|
| Board approval of EUR 1.9m and the EUR 4 premium price rise | Board | 10 December 2026 |
| Off-peak membership launch and marketing | COO Lena Marsh | January 2027 |
| Two corporate sales hires start | COO Lena Marsh | February 2027 |
| Booking-app changes live | COO Lena Marsh | January 2027 |
| Premium price change in force | COO Lena Marsh | 1 March 2027 |
| Review off-peak take-up against the 6,000-member threshold | COO Lena Marsh | December 2027 |
body:
- Risk: if more than 15% of new off-peak members are downgrading standard members, the off-peak move adds less than EUR 2.0m
- Risk: the corporate sales ramp depends on both hires starting by February 2027
- What would change the answer: off-peak take-up below 6,000 members by end of 2027
source: Fernhill growth model v4; decision request, Fernhill growth synthesis, December 2026
note: Ask for the decision explicitly. Offer the December 2027 review as the checkpoint against the 6,000-member threshold.

## A1. Utilisation by time band, average of 34 gyms, January to August 2026
layout: table
tracker: Appendix
| Time band | Utilisation |
|---|---|
| 6-10 am | 58% |
| 10 am-4 pm | 31% |
| 4-6 pm | 64% |
| 6-9 pm | 92% |
| 9-11 pm | 40% |
source: Gate-entry data, 34 gyms, Jan to Aug 2026

## A2. Key assumptions and sources behind the EUR 6.7m of growth moves
layout: table
tracker: Appendix
| Driver | Value | Basis |
|---|---|---|
| Off-peak members by 2028 | about 10,800 | Fernhill growth model v4 |
| Off-peak price | EUR 24/month (vs EUR 39 standard) | Pilot pricing, 2026 |
| Off-peak pilot downgrading | 6% of sign-ups | Pilot, 4 gyms, May-Aug 2026, 420 sign-ups |
| Corporate contracts by 2028 | 40 (avg EUR 60k/year) | Fernhill growth model v4 |
| Corporate pilot | 6 employers, 1,150 employees | Corporate pilot contracts, 2026 |
| Premium price increase | EUR 4/month on 25,000 members | Fernhill membership data 2024-2026 |
| Premium churn after increase | 1.5 points extra for 3 months (2024 precedent) | Fernhill membership data 2024-2026 |
| New-city investment | EUR 4.5m | Opening P&Ls 2019-2023 |
| New-city payback | about 7 years | Opening P&Ls 2019-2023, ramp of last 3 openings |
source: Fernhill growth model v4; Fernhill growth synthesis, December 2026

# Titles-only read-through

Passes: the nine main titles alone tell the board what to fund (off-peak, corporate, pricing), what to drop (a new city), what the total adds up to, the remaining gap, and what is being asked of them on 10 December 2026.

