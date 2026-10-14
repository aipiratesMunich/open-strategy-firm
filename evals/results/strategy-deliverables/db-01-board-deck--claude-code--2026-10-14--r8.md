# db-01-board-deck on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **PASS** (12/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Uses one premium figure throughout, or flags the 1.1 vs 1.2 mismatch in the synthesis to its owner. | yes | EUR 1.2m used consistently in exec summary, slide 6, and the bridge; speaker note on slide 6 explicitly flags: 'At the churn seen after the 2024 increase... it is about EUR 1.1m; we carry EUR 1.2m in the revenue bridge, in line with the synthesis.' |
| Writes deck markdown in the skill's spec format with frontmatter, SCQA opening in four sentences, key line above first slide. | yes | deck.md has YAML frontmatter, then 'Opening (SCQA)' with Situation/Complication/Question/Answer (4 sentences), then 'Key line' with 4 numbered points, before '## 1. Which growth moves...' |
| Page 2 is the executive summary with governing thought title, numbered key-line points, 1.3m gap, what-would-change-the-answer, and EUR 1.9m decision request with COO owner and start date. | yes | Slide 2 title states '...EUR 1.3m short of the EUR 66.0m target'; ask block: 'approve EUR 1.9m... Owner: COO Lena Marsh... start January 2027... The answer changes if off-peak take-up stays below 6,000 members by end of 2027.' |
| Every main-page title is a full-sentence finding with a number/comparison; no topic-label titles. | yes | Titles like 'Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm...' and 'The premium tier is priced below both main competitors; a EUR 4 rise keeps it the cheapest' are full-sentence findings with numbers; appendix label 'Utilisation and investment detail' is excluded as non- |
| 8-15 main pages, sections follow the key line, new-city analysis included as a finding not hidden. | yes | Pages 2-9 (8 pages) map directly to the four key-line points (capacity, corporate wellness, premium price, new city) plus exec summary, bridge and next steps; new city is page 7, a normal main page, not buried in the appendix. |
| Utilisation bar chart with 10am-4pm highlighted; revenue bridge waterfall 58.0→64.7 with 66.0 reference and 1.3 gap visible. | yes | Slide 3: 'chart: bar ... highlight: 10 am-4 pm'. Slide 8: 'chart: waterfall' with steps 58.0, +3.1, +2.4, +1.2, 64.7 and 'reference: 66.0 / 2028 target EUR 66.0m', dashed reference line rendered above the final bar leaving a visible gap. |
| Every chart has a header (measure, unit, period) and a source line from the synthesis. | yes | e.g. 'header: Average gym utilisation by time band, % of capacity, 34 gyms, Jan to Aug 2026' with 'source: Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4' — pattern repeats on every chart slide. |
| Numbers tie across executive summary, section pages and bridge (no rounding drift). | yes | 3.1/2.4/1.2/64.7/1.3/66.0 are identical across slide 2, slides 4-6, and slide 8; bridge title sum 'EUR 6.7m' = 3.1+2.4+1.2 correctly. |
| A titles-only read-through is listed and tells the story in order. | yes | HTML #overview div lists all titles numbered 1-10 in slide order ('arrows: navigate / t: titles'); deck.md includes a 'Titles-only read-through' section confirming the same. |
| If Python available, runs render_deck.py and reports warnings; otherwise says spec delivered unrendered. | yes | Final message states 'render_deck.py --check returns 0 warnings' and deck.html/deck.pptx were produced as rendered outputs. |
| Must not add new analysis, numbers, competitor facts or sources not in the synthesis. | yes | All figures (58.0+3.1+2.4+1.2=64.7, EUR4x25,000x12=1.2m, 10,800x24x12≈3.1m) match the provided reference values; no extraneous facts introduced beyond sourced pilot/competitor data already cited. |
| Must not put agenda, method or background pages before the executive summary. | yes | Page 1 is the title page, page 2 is immediately the executive summary; no agenda/method/background pages precede it. |

## Transcript

## Turn 1

**User:** Turn the Fernhill synthesis into the board pre-read deck for 10 December. (Attached in the working directory: db-01-synthesis.md.)

Done. The board pre-read deck is built from the synthesis and saved in the working directory:

- **`deck.md`** — the spec (source of truth)
- **`deck.html`** — self-contained, presentable deck (arrow keys to navigate, `t` for titles view, `n` for notes, printable to PDF)
- **`deck.pptx`** — native PowerPoint version with live charts

**Structure** (10 pages, titles-only read-through passes):
1. Title
2. Executive summary — governing thought as title, all four key-line points with numbers, the EUR 1.9m ask with owner/dates, the gap stated up front
3. Context — utilisation by time band (92% peak vs 31% midday), sets up the whole argument
4. Off-peak membership — EUR 3.1m, low/base/high
5. Corporate wellness — EUR 2.4m, low/base/high
6. Premium pricing — Fernhill vs both competitors, before/after the EUR 4 rise
7. Why not a new city — 7-year payback vs the board's 4-year limit
8. Revenue bridge waterfall — EUR 58.0m → 64.7m, EUR 1.3m gap to target shown explicitly
9. Decision table, owners, dates, risks, and the take-up threshold that would change the answer
10. Appendix — detailed drivers and investment breakdown

All numbers tie across the executive summary, section pages and the bridge; every chart carries a source line; nothing was invented beyond what's in the synthesis — `render_deck.py --check` returns 0 warnings.


## Files in work dir after run

- db-01-synthesis.md
- deck.html
- deck.md
- deck.pptx

## File written by the run: deck.html

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
<body><div id="stage"><section class="slide l-title" id="s1" data-title="Which growth moves should Fernhill fund for 2027-2028?"><div class="t-client">Fernhill Fitness (fictional)</div><h1 class="t-title">Which growth moves should Fernhill fund for 2027-2028?</h1><p class="t-sub">Recommendation on off-peak membership, corporate wellness and premium pricing</p><p class="t-meta">Board of directors, pre-read for the 10 December 2026 meeting | December 2026</p><footer><div></div><span class="pn">1</span></footer><aside class="notes"><b>Speaker note</b> Pre-read for the 10 December 2026 board meeting. The decision we ask for is on page 2 and again on page 9.</aside></section><section class="slide l-summary" id="s2" data-title="Fernhill should fill daytime capacity, sell corporate wellness and raise the premium price by EUR 4, lifting revenue to about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target"><div class="tracker">Executive summary</div><h2 class="title long">Fernhill should fill daytime capacity, sell corporate wellness and raise the premium price by EUR 4, lifting revenue to about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target</h2><div class="content summary"><p class="lead">Fernhill Fitness gyms are full every evening but revenue has stayed at EUR 58.0m while the board targets EUR 66.0m by 2028, with at most EUR 2m of investment and no new cities.</p><ol><li>Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm; an off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028 (range EUR 2.0m to 3.8m).</li><li>Corporate wellness is proven in a pilot of six employers and 1,150 employees; 40 contracts by 2028 at an average EUR 60k add about EUR 2.4m a year (range EUR 1.4m to 3.0m).</li><li>Premium membership is priced EUR 5 to 8 below the two nearest competitors; a EUR 4 increase on 25,000 members adds about EUR 1.2m a year.</li><li>A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board&#x27;s four-year limit; we do not recommend one for 2027-2028.</li></ol><div class="ask"><strong>Decision requested on 10 December 2026:</strong> approve EUR 1.9m (off-peak launch marketing EUR 0.8m, two corporate sales hires and pilot extension EUR 0.6m, booking-app changes EUR 0.5m). Owner: COO Lena Marsh. Off-peak and corporate moves start January 2027; premium price change from 1 March 2027. The answer changes if off-peak take-up stays below 6,000 members by end of 2027.</div></div><footer><div class="source">Source: Fernhill growth model v4; gate-entry data 34 gyms Jan-Aug 2026; corporate pilot contracts 2026; competitor public price lists Sept 2026; opening P&amp;Ls 2019-2023</div><span class="pn">2</span></footer><aside class="notes"><b>Speaker note</b> Read the bold line and the ask. Everything after this page proves one of the four points.</aside></section><section class="slide l-chart" id="s3" data-title="Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm, the largest unused asset in the business"><div class="tracker">Context</div><h2 class="title long">Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm, the largest unused asset in the business</h2><div class="header">Average gym utilisation by time band, % of capacity, 34 gyms, Jan to Aug 2026</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm, the largest unused asset in the business"><rect x="61.4" y="145.6" width="116.0" height="162.4" fill="#B8C0CC"/><text x="119.4" y="137.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58</text><text x="121.4" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-10 am</text><rect x="288.2" y="221.2" width="116.0" height="86.8" fill="#D9822B"/><text x="346.2" y="213.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">31</text><text x="348.2" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">10 am-4 pm</text><rect x="515.0" y="128.8" width="116.0" height="179.2" fill="#B8C0CC"/><text x="573.0" y="120.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="575.0" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">4-6 pm</text><rect x="741.8" y="50.4" width="116.0" height="257.6" fill="#B8C0CC"/><text x="799.8" y="42.4" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">92</text><text x="801.8" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-9 pm</text><rect x="968.6" y="196.0" width="116.0" height="112.0" fill="#B8C0CC"/><text x="1026.6" y="188.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">40</text><text x="1028.6" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">9-11 pm</text><line x1="8" x2="1142" y1="308.0" y2="308.0" stroke="#14213D" stroke-width="1"/></svg></div></div><div class="takeaway">The 10 am to 4 pm trough is the capacity the off-peak membership is built to fill.</div><footer><div class="source">Source: Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4</div><span class="pn">3</span></footer><aside class="notes"><b>Speaker note</b> Evening capacity is essentially sold out. The gap in the middle of the day is where the three growth moves start.</aside></section><section class="slide l-chart" id="s4" data-title="An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028"><div class="tracker">1 Off-peak membership</div><h2 class="title">An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028</h2><div class="header">Off-peak membership revenue in 2028 by take-up case, EUR m per year</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028"><rect x="62.0" y="188.0" width="116.0" height="160.0" fill="#B8C0CC"/><text x="120.0" y="180.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.0</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Low</text><rect x="290.0" y="100.0" width="116.0" height="248.0" fill="#D9822B"/><text x="348.0" y="92.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.1</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base case</text><rect x="518.0" y="44.0" width="116.0" height="304.0" fill="#B8C0CC"/><text x="576.0" y="36.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.8</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">High</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Reaches about 10,800 off-peak members by 2028, priced below the EUR 39 standard membership</li><li>Pilot in 4 gyms, May to Aug 2026: 420 sign-ups, 6% from existing members downgrading</li><li>Risk: if more than 15% of new off-peak members are downgrades, the move adds less than EUR 2.0m</li><li>Needs booking-app changes (EUR 0.5m) and launch marketing (EUR 0.8m)</li></ul></div></div><footer><div class="footnote">Range reflects pilot sign-up and downgrade-rate uncertainty.</div><div class="source">Source: Gate-entry data, 34 gyms, Jan to Aug 2026; off-peak pilot, 4 gyms, May to Aug 2026; Fernhill growth model v4</div><span class="pn">4</span></footer><aside class="notes"><b>Speaker note</b> The pilot is small (420 sign-ups) so the range is wide. The downgrade rate is the number to watch.</aside></section><section class="slide l-chart" id="s5" data-title="Corporate wellness contracts, already proven with six employer pilots, add about EUR 2.4m a year by 2028"><div class="tracker">2 Corporate wellness</div><h2 class="title long">Corporate wellness contracts, already proven with six employer pilots, add about EUR 2.4m a year by 2028</h2><div class="header">Corporate wellness revenue in 2028 by contract count, EUR m per year</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Corporate wellness contracts, already proven with six employer pilots, add about EUR 2.4m a year by 2028"><rect x="62.0" y="198.7" width="116.0" height="149.3" fill="#B8C0CC"/><text x="120.0" y="190.7" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1.4</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">25 contracts (low)</text><rect x="290.0" y="92.0" width="116.0" height="256.0" fill="#D9822B"/><text x="348.0" y="84.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.4</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">40 contracts (base case)</text><rect x="518.0" y="28.0" width="116.0" height="320.0" fill="#B8C0CC"/><text x="576.0" y="20.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.0</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">55 contracts (high)</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Six employers signed in the pilot, 1,150 employees enrolled</li><li>Base case: 40 contracts by 2028 at an average EUR 60k a year</li><li>Needs two corporate sales hires starting by February 2027</li><li>Investment: EUR 0.6m for the two hires and pilot extension</li></ul></div></div><footer><div class="footnote">Contract count range is a team estimate off the pilot&#x27;s six signed employers; no benchmark beyond the pilot.</div><div class="source">Source: Corporate pilot contracts 2026; Fernhill growth model v4</div><span class="pn">5</span></footer><aside class="notes"><b>Speaker note</b> The ramp depends on the two sales hires starting on time. That is the risk to flag if the board asks about delivery.</aside></section><section class="slide l-chart" id="s6" data-title="The premium tier is priced below both main competitors; a EUR 4 rise keeps it the cheapest"><div class="tracker">3 Premium price</div><h2 class="title">The premium tier is priced below both main competitors; a EUR 4 rise keeps it the cheapest</h2><div class="header">Premium membership price for a comparable offer (pool, classes, sauna), EUR per month, Sept 2026</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="The premium tier is priced below both main competitors; a EUR 4 rise keeps it the cheapest"><rect x="112" y="42.3" width="713.9" height="43.0" fill="#D9822B"/><text x="833.9" y="69.3" font-size="15" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">59</text><text x="100.0" y="70.3" font-size="15" text-anchor="end" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Fernhill</text><rect x="112" y="157.0" width="774.4" height="43.0" fill="#B8C0CC"/><text x="894.4" y="184.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="100.0" y="185.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor A</text><rect x="112" y="271.7" width="810.7" height="43.0" fill="#B8C0CC"/><text x="930.7" y="298.7" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">67</text><text x="100.0" y="299.7" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor B</text><line x1="112" x2="112" y1="8" y2="352.0" stroke="#14213D"/></svg></div></div><div class="takeaway">After the EUR 4 increase Fernhill sits at EUR 63 a month, still below both main competitors.</div><footer><div class="source">Source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026</div><span class="pn">6</span></footer><aside class="notes"><b>Speaker note</b> A EUR 4 rise on 25,000 members is about EUR 1.2m before churn. At the churn seen after the 2024 increase (1.5 points extra for three months) it is about EUR 1.1m; we carry EUR 1.2m in the revenue bridge, in line with the synthesis.</aside></section><section class="slide l-chart" id="s7" data-title="A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board&#x27;s four-year limit"><div class="tracker">4 New city</div><h2 class="title long">A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board&#x27;s four-year limit</h2><div class="header">Payback period for a new-city gym versus the board&#x27;s investment limit, years</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board&#x27;s four-year limit"><line x1="8.0" x2="542.0" y1="188.0" y2="188.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="550.0" y="193.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Board&#x27;s four-year limit</text><rect x="215.0" y="68.0" width="116.0" height="280.0" fill="#D9822B"/><text x="273.0" y="60.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">7</text><text x="275.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">New-city gym</text><line x1="8" x2="542" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>EUR 4.5m investment, at the ramp seen in the last three openings</li><li>Payback of about seven years is nearly double the board&#x27;s four-year limit</li><li>We do not recommend a new city for 2027-2028</li></ul></div></div><footer><div class="source">Source: Opening P&amp;Ls 2019-2023; Fernhill growth model v4</div><span class="pn">7</span></footer><aside class="notes"><b>Speaker note</b> This is why the recommendation accepts the remaining gap rather than proposing a new city to close it.</aside></section><section class="slide l-chart" id="s8" data-title="The three moves add EUR 6.7m, reaching about EUR 64.7m by 2028 and leaving a EUR 1.3m gap to the EUR 66.0m target"><div class="tracker">Total effect</div><h2 class="title long">The three moves add EUR 6.7m, reaching about EUR 64.7m by 2028 and leaving a EUR 1.3m gap to the EUR 66.0m target</h2><div class="header">Revenue bridge 2026 to 2028, EUR m per year</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="The three moves add EUR 6.7m, reaching about EUR 64.7m by 2028 and leaving a EUR 1.3m gap to the EUR 66.0m target"><rect x="46.4" y="116.0" width="120.0" height="232.0" fill="#14213D"/><line x1="8.0" x2="992.0" y1="84.0" y2="84.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="1000.0" y="89.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2028 target EUR 66.0m</text><text x="106.4" y="108.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58.0</text><text x="106.4" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2026</text><rect x="243.2" y="103.6" width="120.0" height="12.4" fill="#D9822B"/><text x="303.2" y="95.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+3.1</text><line x1="166.4" x2="243.2" y1="116.0" y2="116.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="303.2" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Off-peak membership</text><rect x="440.0" y="94.0" width="120.0" height="9.6" fill="#B8C0CC"/><text x="500.0" y="86.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+2.4</text><line x1="363.2" x2="440.0" y1="103.6" y2="103.6" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="500.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Corporate wellness</text><rect x="636.8" y="89.2" width="120.0" height="4.8" fill="#B8C0CC"/><text x="696.8" y="81.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+1.2</text><line x1="560.0" x2="636.8" y1="94.0" y2="94.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="696.8" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Premium price</text><rect x="833.6" y="89.2" width="120.0" height="258.8" fill="#14213D"/><text x="893.6" y="81.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64.7</text><line x1="756.8" x2="833.6" y1="89.2" y2="89.2" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="893.6" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2028 with the</text><text x="893.6" y="387.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">three moves</text><line x1="8" x2="992" y1="348.0" y2="348.0" stroke="#14213D"/></svg></div></div><footer><div class="footnote">Core revenue without the three moves is assumed flat at EUR 58.0m (membership numbers flat 2023-2026).</div><div class="source">Source: Fernhill growth model v4</div><span class="pn">8</span></footer><aside class="notes"><b>Speaker note</b> The EUR 1.3m gap is real and we show it rather than stretch an assumption to close it. The board should accept it for now rather than chase a new city that does not pay back in time.</aside></section><section class="slide l-table" id="s9" data-title="The board can decide on 10 December; the answer changes below 6,000 off-peak members by end-2027"><div class="tracker">Next steps</div><h2 class="title long">The board can decide on 10 December; the answer changes below 6,000 off-peak members by end-2027</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Step</th><th>Owner</th><th>By when</th></tr><tr><td>Board approval of EUR 1.9m and the premium price change</td><td>Board</td><td>10 December 2026</td></tr><tr><td>Off-peak membership launch and booking-app changes</td><td>COO Lena Marsh</td><td>January 2027</td></tr><tr><td>Two corporate sales hires start</td><td>COO Lena Marsh</td><td>February 2027</td></tr><tr><td>Premium price increase of EUR 4 in force</td><td>COO Lena Marsh</td><td>1 March 2027</td></tr><tr><td>Take-up checkpoint against the 6,000-member threshold</td><td>COO Lena Marsh</td><td>End of 2027</td></tr></table></div><div class="side"><ul><li>Risk: off-peak cannibalisation above 15% of new sign-ups cuts the off-peak effect to under EUR 2.0m</li><li>Risk: corporate sales ramp depends on the two hires starting by February 2027</li><li>What would change the answer: off-peak take-up below 6,000 members by end of 2027</li></ul></div></div><footer><div class="source">Source: Fernhill growth model v4; off-peak pilot and corporate pilot, 2026</div><span class="pn">9</span></footer><aside class="notes"><b>Speaker note</b> Ask for the decision explicitly. Offer the end-2027 take-up checkpoint as the point to revisit if off-peak is behind plan.</aside></section><section class="slide l-table" id="s10" data-title="Utilisation and investment detail"><div class="tracker">Appendix</div><h2 class="title">Utilisation and investment detail</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Driver</th><th>Value</th><th>Basis</th></tr><tr><td>Utilisation, 10 am-4 pm</td><td>31%</td><td>Gate-entry data, 34 gyms, Jan-Aug 2026</td></tr><tr><td>Utilisation, 6-9 pm</td><td>92%</td><td>Gate-entry data, 34 gyms, Jan-Aug 2026</td></tr><tr><td>Off-peak price</td><td>EUR 24/month (vs EUR 39 standard)</td><td>Fernhill growth model v4</td></tr><tr><td>Off-peak members by 2028</td><td>about 10,800</td><td>Fernhill growth model v4</td></tr><tr><td>Corporate contracts by 2028</td><td>40 at avg EUR 60k/year</td><td>Fernhill growth model v4</td></tr><tr><td>Premium members</td><td>25,000</td><td>Fernhill membership data 2024-2026</td></tr><tr><td>New-city investment</td><td>EUR 4.5m</td><td>Opening P&amp;Ls 2019-2023</td></tr><tr><td>Total investment requested</td><td>EUR 1.9m (off-peak marketing EUR 0.8m, corporate hires/pilot EUR 0.6m, booking-app EUR 0.5m)</td><td>Fernhill growth model v4</td></tr></table></div></div><footer><div class="source">Source: Fernhill growth model v4; gate-entry data 2026; corporate pilot contracts 2026; Fernhill membership data 2024-2026; opening P&amp;Ls 2019-2023</div><span class="pn">A1</span></footer></section></div>
<div id="overview"><h1>Titles-only read-through</h1><ol><li>Which growth moves should Fernhill fund for 2027-2028? <span style='color:#8A93A3'>(1)</span></li><li>Fernhill should fill daytime capacity, sell corporate wellness and raise the premium price by EUR 4, lifting revenue to about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target <span style='color:#8A93A3'>(2)</span></li><li>Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm, the largest unused asset in the business <span style='color:#8A93A3'>(3)</span></li><li>An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028 <span style='color:#8A93A3'>(4)</span></li><li>Corporate wellness contracts, already proven with six employer pilots, add about EUR 2.4m a year by 2028 <span style='color:#8A93A3'>(5)</span></li><li>The premium tier is priced below both main competitors; a EUR 4 rise keeps it the cheapest <span style='color:#8A93A3'>(6)</span></li><li>A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board&#x27;s four-year limit <span style='color:#8A93A3'>(7)</span></li><li>The three moves add EUR 6.7m, reaching about EUR 64.7m by 2028 and leaving a EUR 1.3m gap to the EUR 66.0m target <span style='color:#8A93A3'>(8)</span></li><li>The board can decide on 10 December; the answer changes below 6,000 off-peak members by end-2027 <span style='color:#8A93A3'>(9)</span></li><li>Utilisation and investment detail <span style='color:#8A93A3'>(A1)</span></li></ol></div>
<div id="hint">arrows: navigate | t: titles | n: notes | print: PDF</div>
<script>
(function(){
var slides=[].slice.call(document.querySelectorAll('.slide')),i=0,stage=document.getElementById('stage');
function fit(){var s=Math.min(innerWidth/1280,innerHeight/720);stage.s

## File written by the run: deck.md

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

# Deck: Which growth moves should Fernhill fund for 2027-2028?

*Fictional company. All figures, people and documents invented for evaluation.*

**Opening (SCQA)**
- Situation: Fernhill Fitness runs 34 gyms that are full every evening, with no plan to open in a new city.
- Complication: Revenue has been flat at EUR 58.0m and the board wants EUR 66.0m by 2028, with at most EUR 2m of investment and no new cities.
- Question: Which growth moves should the board approve on 10 December 2026?
- Answer: Launch an off-peak membership, sell corporate wellness contracts and raise the premium price by EUR 4; accept the remaining EUR 1.3m gap rather than open a new city.

**Key line**
1. Daytime capacity is the largest unused asset.
2. Corporate wellness contracts are proven in the pilot.
3. The premium tier is priced below both main competitors.
4. A new city does not pay back within the board's four-year limit.

## 1. Which growth moves should Fernhill fund for 2027-2028?
layout: title
subtitle: Recommendation on off-peak membership, corporate wellness and premium pricing
note: Pre-read for the 10 December 2026 board meeting. The decision we ask for is on page 2 and again on page 9.

## 2. Fernhill should fill daytime capacity, sell corporate wellness and raise the premium price by EUR 4, lifting revenue to about EUR 64.7m by 2028, EUR 1.3m short of the EUR 66.0m target
layout: summary
tracker: Executive summary
lead: Fernhill Fitness gyms are full every evening but revenue has stayed at EUR 58.0m while the board targets EUR 66.0m by 2028, with at most EUR 2m of investment and no new cities.
body:
- Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm; an off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028 (range EUR 2.0m to 3.8m).
- Corporate wellness is proven in a pilot of six employers and 1,150 employees; 40 contracts by 2028 at an average EUR 60k add about EUR 2.4m a year (range EUR 1.4m to 3.0m).
- Premium membership is priced EUR 5 to 8 below the two nearest competitors; a EUR 4 increase on 25,000 members adds about EUR 1.2m a year.
- A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board's four-year limit; we do not recommend one for 2027-2028.
ask: **Decision requested on 10 December 2026:** approve EUR 1.9m (off-peak launch marketing EUR 0.8m, two corporate sales hires and pilot extension EUR 0.6m, booking-app changes EUR 0.5m). Owner: COO Lena Marsh. Off-peak and corporate moves start January 2027; premium price change from 1 March 2027. The answer changes if off-peak take-up stays below 6,000 members by end of 2027.
source: Fernhill growth model v4; gate-entry data 34 gyms Jan-Aug 2026; corporate pilot contracts 2026; competitor public price lists Sept 2026; opening P&Ls 2019-2023
note: Read the bold line and the ask. Everything after this page proves one of the four points.

## 3. Gyms run at 92% utilisation from 6 to 9 pm but only 31% from 10 am to 4 pm, the largest unused asset in the business
layout: chart
tracker: Context
message: time-series
chart: bar
header: Average gym utilisation by time band, % of capacity, 34 gyms, Jan to Aug 2026
highlight: 10 am-4 pm
scale: zero
| Time band | Utilisation |
|---|---|
| 6-10 am | 58 |
| 10 am-4 pm | 31 |
| 4-6 pm | 64 |
| 6-9 pm | 92 |
| 9-11 pm | 40 |
takeaway: The 10 am to 4 pm trough is the capacity the off-peak membership is built to fill.
source: Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4
note: Evening capacity is essentially sold out. The gap in the middle of the day is where the three growth moves start.

## 4. An off-peak membership at EUR 24 a month adds about EUR 3.1m a year by 2028
layout: chart
tracker: 1 Off-peak membership
message: ranking
chart: bar
header: Off-peak membership revenue in 2028 by take-up case, EUR m per year
highlight: Base case
| Case | Revenue |
|---|---|
| Low | 2.0 |
| Base case | 3.1 |
| High | 3.8 |
body:
- Reaches about 10,800 off-peak members by 2028, priced below the EUR 39 standard membership
- Pilot in 4 gyms, May to Aug 2026: 420 sign-ups, 6% from existing members downgrading
- Risk: if more than 15% of new off-peak members are downgrades, the move adds less than EUR 2.0m
- Needs booking-app changes (EUR 0.5m) and launch marketing (EUR 0.8m)
footnote: Range reflects pilot sign-up and downgrade-rate uncertainty.
source: Gate-entry data, 34 gyms, Jan to Aug 2026; off-peak pilot, 4 gyms, May to Aug 2026; Fernhill growth model v4
note: The pilot is small (420 sign-ups) so the range is wide. The downgrade rate is the number to watch.

## 5. Corporate wellness contracts, already proven with six employer pilots, add about EUR 2.4m a year by 2028
layout: chart
tracker: 2 Corporate wellness
message: ranking
chart: bar
header: Corporate wellness revenue in 2028 by contract count, EUR m per year
highlight: 40 contracts (base case)
| Case | Revenue |
|---|---|
| 25 contracts (low) | 1.4 |
| 40 contracts (base case) | 2.4 |
| 55 contracts (high) | 3.0 |
body:
- Six employers signed in the pilot, 1,150 employees enrolled
- Base case: 40 contracts by 2028 at an average EUR 60k a year
- Needs two corporate sales hires starting by February 2027
- Investment: EUR 0.6m for the two hires and pilot extension
footnote: Contract count range is a team estimate off the pilot's six signed employers; no benchmark beyond the pilot.
source: Corporate pilot contracts 2026; Fernhill growth model v4
note: The ramp depends on the two sales hires starting on time. That is the risk to flag if the board asks about delivery.

## 6. The premium tier is priced below both main competitors; a EUR 4 rise keeps it the cheapest
layout: chart
tracker: 3 Premium price
message: ranking
chart: hbar
header: Premium membership price for a comparable offer (pool, classes, sauna), EUR per month, Sept 2026
highlight: Fernhill
| Supplier | Price |
|---|---|
| Fernhill | 59 |
| Competitor A | 64 |
| Competitor B | 67 |
takeaway: After the EUR 4 increase Fernhill sits at EUR 63 a month, still below both main competitors.
source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026
note: A EUR 4 rise on 25,000 members is about EUR 1.2m before churn. At the churn seen after the 2024 increase (1.5 points extra for three months) it is about EUR 1.1m; we carry EUR 1.2m in the revenue bridge, in line with the synthesis.

## 7. A new-city gym needs EUR 4.5m and pays back in about seven years, beyond the board's four-year limit
layout: chart
tracker: 4 New city
message: deviation
chart: bar
header: Payback period for a new-city gym versus the board's investment limit, years
reference: 4 | Board's four-year limit
highlight: New-city gym
scale: zero
| Item | Years |
|---|---|
| New-city gym | 7 |
body:
- EUR 4.5m investment, at the ramp seen in the last three openings
- Payback of about seven years is nearly double the board's four-year limit
- We do not recommend a new city for 2027-2028
source: Opening P&Ls 2019-2023; Fernhill growth model v4
note: This is why the recommendation accepts the remaining gap rather than proposing a new city to close it.

## 8. The three moves add EUR 6.7m, reaching about EUR 64.7m by 2028 and leaving a EUR 1.3m gap to the EUR 66.0m target
layout: chart
tracker: Total effect
message: flow
chart: waterfall
header: Revenue bridge 2026 to 2028, EUR m per year
reference: 66.0 | 2028 target EUR 66.0m
highlight: Off-peak membership
| Step | EUR m | Type |
|---|---|---|
| Revenue 2026 | 58.0 | total |
| Off-peak membership | 3.1 | delta |
| Corporate wellness | 2.4 | delta |
| Premium price | 1.2 | delta |
| Revenue 2028 with the three moves | 64.7 | total |
footnote: Core revenue without the three moves is assumed flat at EUR 58.0m (membership numbers flat 2023-2026).
source: Fernhill growth model v4
note: The EUR 1.3m gap is real and we show it rather than stretch an assumption to close it. The board should accept it for now rather than chase a new city that does not pay back in time.

## 9. The board can decide on 10 December; the answer changes below 6,000 off-peak members by end-2027
layout: table
tracker: Next steps
| Step | Owner | By when |
|---|---|---|
| Board approval of EUR 1.9m and the premium price change | Board | 10 December 2026 |
| Off-peak membership launch and booking-app changes | COO Lena Marsh | January 2027 |
| Two corporate sales hires start | COO Lena Marsh | February 2027 |
| Premium price increase of EUR 4 in force | COO Lena Marsh | 1 March 2027 |
| Take-up checkpoint against the 6,000-member threshold | COO Lena Marsh | End of 2027 |
body:
- Risk: off-peak cannibalisation above 15% of new sign-ups cuts the off-peak effect to under EUR 2.0m
- Risk: corporate sales ramp depends on the two hires starting by February 2027
- What would change the answer: off-peak take-up below 6,000 members by end of 2027
source: Fernhill growth model v4; off-peak pilot and corporate pilot, 2026
note: Ask for the decision explicitly. Offer the end-2027 take-up checkpoint as the point to revisit if off-peak is behind plan.

## A1. Utilisation and investment detail
layout: table
tracker: Appendix
| Driver | Value | Basis |
|---|---|---|
| Utilisation, 10 am-4 pm | 31% | Gate-entry data, 34 gyms, Jan-Aug 2026 |
| Utilisation, 6-9 pm | 92% | Gate-entry data, 34 gyms, Jan-Aug 2026 |
| Off-peak price | EUR 24/month (vs EUR 39 standard) | Fernhill growth model v4 |
| Off-peak members by 2028 | about 10,800 | Fernhill growth model v4 |
| Corporate contracts by 2028 | 40 at avg EUR 60k/year | Fernhill growth model v4 |
| Premium members | 25,000 | Fernhill membership data 2024-2026 |
| New-city investment | EUR 4.5m | Opening P&Ls 2019-2023 |
| Total investment requested | EUR 1.9m (off-peak marketing EUR 0.8m, corporate hires/pilot EUR 0.6m, booking-app EUR 0.5m) | Fernhill growth model v4 |
source: Fernhill growth model v4; gate-entry data 2026; corporate pilot contracts 2026; Fernhill membership data 2024-2026; opening P&Ls 2019-2023

# Titles-only read-through

Passes: the nine main titles alone tell the board what to fund, what each move is worth, why a new city is off the table, and what remains to be decided.

