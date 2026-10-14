# db-01-board-deck on Claude Code

- Run model: sonnet; judge model: sonnet
- Result: **FAIL** (11/12 criteria)

| Criterion | Pass | Evidence |
|---|---|---|
| Uses one premium figure throughout, or flags the 1.1 vs 1.2 mismatch to its owner | yes | "We carried the synthesis's own EUR 1.2m in the bridge... but made the EUR 1.1m net figure visible everywhere it matters — exec summary, the premium slide, a bridge footnote, and a dedicated risk row" |
| Writes 06-deck.md in spec format with frontmatter, SCQA opening (four sentences), key line above first slide | yes | Frontmatter block present; 'Opening (SCQA)' has Situation/Complication/Question/Answer (4 sentences); 'Key line' with 4 numbered points sits above '## 1. Which growth moves...' |
| Page 2 is executive summary with governing thought title, numbered key-line points, EUR 1.3m gap, what-would-change-the-answer, decision request (EUR 1.9m, COO, start date) | yes | Page 2 title states gap; body has 4 bullets matching key-line (rendered as <ol>); ask block: 'approve EUR 1.9m... Owner: COO Lena Marsh... The answer changes if off-peak take-up stays below 6,000 members by the end of 2027.' |
| Every main-page title is a full-sentence finding with a number/comparison; no topic-label titles | yes | Pages 2-10 titles all contain numbers/comparisons, e.g. 'adds about EUR 6.7m by 2028, leaving a EUR 1.3m gap' and 'needs EUR 4.5m and pays back in about seven years' |
| 8-15 main pages, sections follow key line, new-city analysis included as a finding | yes | Pages 2-10 (9 main pages) ordered as off-peak(1), corporate(2), premium(3), new-city(4) matching key line; page 7 is 'A new-city gym needs EUR 4.5m and pays back in about seven years' |
| Utilisation bar chart with 10am-4pm highlighted; revenue bridge as waterfall 58.0→64.7 with 66.0 reference and 1.3 gap visible | yes | Page 3 'chart: bar... highlight: 10 am-4 pm'; page 8 'chart: waterfall... reference: 66 / Target EUR 66m by 2028' with steps 58.0→64.7 and takeaway 'remaining EUR 1.3m gap' |
| Every chart has header (measure, unit, period) and source line from synthesis | yes | e.g. header 'Utilisation by time band, % of capacity, average of 34 gyms, Jan to Aug 2026' with source 'Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4' |
| Numbers tie across executive summary, section pages and bridge with no rounding drift | yes | 3.1+2.4+1.2=6.7 consistent in exec summary, section titles, and bridge table (58.0+3.1+2.4+1.2=64.7, gap 1.3) throughout |
| Titles-only read-through is listed and tells the story in order | yes | '<div id="overview"><h1>Titles-only read-through</h1><ol>...' lists slide titles in sequence; chat confirms 'Titles-only read-through... pass clean' |
| Runs render_deck.py and reports warnings if Python available, otherwise states spec delivered unrendered | NO | Response only says 'the renderer's quality checks both pass clean (no warnings)' without naming render_deck.py, confirming Python availability, or stating the spec was delivered unrendered |
| Does not add new analysis, numbers, competitor facts or sources not in the synthesis | yes | No figures or sources appear beyond those attributed to 'Fernhill growth model v4', pilot data, and competitor price lists already used consistently across pages |
| No agenda, method or background pages before the executive summary | yes | Page 1 is the title page and page 2 is immediately the executive summary; no intervening agenda/method page |

## Transcript

## Turn 1

**User:** Turn the Fernhill synthesis into the board pre-read deck for 10 December. (Attached in the working directory: db-01-synthesis.md.)

Done. The board pre-read deck is built from the Fernhill synthesis:

- **`06-deck.md`** — the spec (source of truth)
- **`06-deck.html`** — self-contained render (arrow keys to navigate, `t` for titles-only view, `n` for notes; print to PDF for one slide per page)
- **`06-deck.pptx`** — native PowerPoint with live charts

**Structure (10 main pages + 2-page appendix):** title → executive summary (governing thought, all three moves, the EUR 1.3m gap, the decision ask) → context (the 92% vs 31% utilisation gap) → off-peak membership → corporate wellness → premium price → new-city rejected → revenue bridge (waterfall, EUR 58.0m → EUR 64.7m vs EUR 66m target) → risks → next steps/decision request → appendix (full utilisation table, assumptions).

One thing worth flagging: the synthesis gives the premium price move as **EUR 1.2m before churn** in the bridge table but **EUR 1.1m net of the churn seen after the 2024 increase** in the supporting text — these don't reconcile to one number. I carried the synthesis's own EUR 1.2m in the bridge (since that's what its total/gap arithmetic uses) but made the EUR 1.1m net figure visible everywhere it matters — exec summary, the premium slide, a bridge footnote, and a dedicated risk row — rather than hiding it. If the churn pattern repeats, the real gap is closer to EUR 1.4m, not EUR 1.3m; worth deciding before 10 December whether the board sees the gross or net number as the headline.

Titles-only read-through and the renderer's quality checks both pass clean (no warnings).


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
<body><div id="stage"><section class="slide l-title" id="s1" data-title="Which growth moves should Fernhill approve for 2027-2028?"><div class="t-client">Fernhill Fitness (fictional)</div><h1 class="t-title">Which growth moves should Fernhill approve for 2027-2028?</h1><p class="t-sub">Recommendation on off-peak membership, corporate wellness and premium pricing — and why a new city should wait</p><p class="t-meta">Board of directors, pre-read for the 10 December 2026 meeting | December 2026</p><footer><div></div><span class="pn">1</span></footer><aside class="notes"><b>Speaker note</b> Pre-read for the 10 December 2026 board meeting. The decision we ask for is on page 2 and again on page 10.</aside></section><section class="slide l-summary" id="s2" data-title="Off-peak membership, corporate contracts and a EUR 4 premium rise add about EUR 6.7m by 2028, leaving a EUR 1.3m gap we recommend accepting"><div class="tracker">Executive summary</div><h2 class="title long">Off-peak membership, corporate contracts and a EUR 4 premium rise add about EUR 6.7m by 2028, leaving a EUR 1.3m gap we recommend accepting</h2><div class="content summary"><p class="lead">Fernhill generated EUR 58.0m in 2026. The board&#x27;s target is EUR 66.0m by 2028, without opening gyms in new cities and with at most EUR 2m of investment.</p><ol><li>Off-peak membership at EUR 24 a month (against the EUR 39 standard membership) reaches about 10,800 members by 2028 and adds about EUR 3.1m a year (range EUR 2.0m to 3.8m), filling gyms that run at only 31% utilisation from 10am to 4pm against 92% in the evening peak.</li><li>Corporate wellness contracts, proven in a six-employer pilot (1,150 employees enrolled), reach 40 contracts by 2028 at an average EUR 60k a year, adding about EUR 2.4m a year (range EUR 1.4m to 3.0m); needs two corporate sales hires.</li><li>The premium tier, priced EUR 59 against EUR 64 and EUR 67 at the two nearest competitors, can rise EUR 4 a month on 25,000 members, adding about EUR 1.2m a year before churn (about EUR 1.1m net of the churn pattern seen after the 2024 increase).</li><li>A new-city gym needs EUR 4.5m and pays back in about seven years at the ramp of the last three openings — outside the board&#x27;s four-year limit; we recommend not pursuing one now.</li></ol><div class="ask"><strong>Decision requested 10 December 2026:</strong> approve EUR 1.9m (off-peak launch marketing EUR 0.8m; two corporate sales hires and pilot extension EUR 0.6m; booking-app changes EUR 0.5m). Owner: COO Lena Marsh. Off-peak and corporate hiring start January 2027; premium price change from 1 March 2027. The answer changes if off-peak take-up stays below 6,000 members by the end of 2027.</div></div><footer><div class="source">Source: Fernhill growth model v4; gate-entry data, 34 gyms, Jan to Aug 2026; corporate pilot contracts 2026; competitor price lists, September 2026; opening P&amp;Ls 2019-2023</div><span class="pn">2</span></footer><aside class="notes"><b>Speaker note</b> Read the bold line and the ask. Everything after this page proves one of the four points.</aside></section><section class="slide l-chart" id="s3" data-title="Gyms run at 92% utilisation in the evening peak but only 31% from 10am to 4pm, the largest unused asset Fernhill has"><div class="tracker">Context</div><h2 class="title long">Gyms run at 92% utilisation in the evening peak but only 31% from 10am to 4pm, the largest unused asset Fernhill has</h2><div class="header">Utilisation by time band, % of capacity, average of 34 gyms, Jan to Aug 2026</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Gyms run at 92% utilisation in the evening peak but only 31% from 10am to 4pm, the largest unused asset Fernhill has"><rect x="61.4" y="145.6" width="116.0" height="162.4" fill="#B8C0CC"/><text x="119.4" y="137.6" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58</text><text x="121.4" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-10 am</text><rect x="288.2" y="221.2" width="116.0" height="86.8" fill="#D9822B"/><text x="346.2" y="213.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">31</text><text x="348.2" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">10 am-4 pm</text><rect x="515.0" y="128.8" width="116.0" height="179.2" fill="#B8C0CC"/><text x="573.0" y="120.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="575.0" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">4-6 pm</text><rect x="741.8" y="50.4" width="116.0" height="257.6" fill="#B8C0CC"/><text x="799.8" y="42.4" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">92</text><text x="801.8" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">6-9 pm</text><rect x="968.6" y="196.0" width="116.0" height="112.0" fill="#B8C0CC"/><text x="1026.6" y="188.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">40</text><text x="1028.6" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">9-11 pm</text><line x1="8" x2="1142" y1="308.0" y2="308.0" stroke="#14213D" stroke-width="1"/></svg></div></div><div class="takeaway">The 10am-4pm trough runs six hours a day, every day, across all 34 gyms.</div><footer><div class="source">Source: Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4</div><span class="pn">3</span></footer><aside class="notes"><b>Speaker note</b> This is the gap the off-peak membership is built to fill.</aside></section><section class="slide l-chart" id="s4" data-title="An off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year"><div class="tracker">1 Off-peak membership</div><h2 class="title long">An off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year</h2><div class="header">Off-peak membership revenue by 2028, EUR m per year, by scenario</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="An off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year"><rect x="62.0" y="188.0" width="116.0" height="160.0" fill="#B8C0CC"/><text x="120.0" y="180.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.0</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Low</text><rect x="290.0" y="100.0" width="116.0" height="248.0" fill="#D9822B"/><text x="348.0" y="92.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.1</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base case (10,800 members)</text><rect x="518.0" y="44.0" width="116.0" height="304.0" fill="#B8C0CC"/><text x="576.0" y="36.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.8</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">High</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Priced at EUR 24 a month against the EUR 39 standard membership, targeting the 31% daytime trough.</li><li>Pilot in 4 gyms, May to Aug 2026: 420 sign-ups; 6% were existing members downgrading from standard.</li><li>Risk: if more than 15% of sign-ups are downgrades rather than new members, the move adds less than EUR 2.0m (see page 9).</li></ul></div></div><footer><div class="footnote">Member count and revenue range from Fernhill growth model v4; pilot cannibalisation rate measured over 4 months and may not hold at scale.</div><div class="source">Source: Gate-entry data, 34 gyms, Jan to Aug 2026; off-peak pilot, 4 gyms, May to Aug 2026; Fernhill growth model v4</div><span class="pn">4</span></footer><aside class="notes"><b>Speaker note</b> 10,800 members x EUR 24 x 12 months is about EUR 3.1m, which ties to the base case.</aside></section><section class="slide l-chart" id="s5" data-title="Corporate wellness contracts are proven in the pilot; 40 contracts by 2028 add about EUR 2.4m a year"><div class="tracker">2 Corporate wellness</div><h2 class="title long">Corporate wellness contracts are proven in the pilot; 40 contracts by 2028 add about EUR 2.4m a year</h2><div class="header">Corporate wellness revenue by 2028, EUR m per year, by scenario</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Corporate wellness contracts are proven in the pilot; 40 contracts by 2028 add about EUR 2.4m a year"><rect x="62.0" y="198.7" width="116.0" height="149.3" fill="#B8C0CC"/><text x="120.0" y="190.7" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">1.4</text><text x="122.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Low</text><rect x="290.0" y="92.0" width="116.0" height="256.0" fill="#D9822B"/><text x="348.0" y="84.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">2.4</text><text x="350.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Base case (40 contracts)</text><rect x="518.0" y="28.0" width="116.0" height="320.0" fill="#B8C0CC"/><text x="576.0" y="20.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">3.0</text><text x="578.0" y="370.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">High</text><line x1="8" x2="692" y1="348.0" y2="348.0" stroke="#14213D" stroke-width="1"/></svg></div><div class="side"><ul><li>Pilot: six employers signed, 1,150 employees enrolled, 2026.</li><li>Average contract value EUR 60k a year; needs two corporate sales hires starting by February 2027.</li><li>Risk: the ramp to 40 contracts depends on both hires starting on time (see page 9).</li></ul></div></div><footer><div class="source">Source: Corporate pilot contracts 2026; Fernhill growth model v4</div><span class="pn">5</span></footer><aside class="notes"><b>Speaker note</b> 40 contracts x EUR 60k is EUR 2.4m, the base case.</aside></section><section class="slide l-chart" id="s6" data-title="Fernhill&#x27;s premium tier is priced below both main competitors; a EUR 4 rise adds about EUR 1.1m to 1.2m a year"><div class="tracker">3 Premium price</div><h2 class="title long">Fernhill&#x27;s premium tier is priced below both main competitors; a EUR 4 rise adds about EUR 1.1m to 1.2m a year</h2><div class="header">Premium tier monthly price, EUR, comparable offer with pool, classes and sauna, September 2026</div><div class="content two"><div class="exhibit"><svg class="chart" viewBox="0 0 700 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Fernhill&#x27;s premium tier is priced below both main competitors; a EUR 4 rise adds about EUR 1.1m to 1.2m a year"><rect x="192" y="42.3" width="344.9" height="43.0" fill="#D9822B"/><text x="544.9" y="69.3" font-size="15" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">63</text><text x="180.0" y="70.3" font-size="15" text-anchor="end" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Fernhill, after +EUR 4</text><rect x="192" y="157.0" width="350.4" height="43.0" fill="#B8C0CC"/><text x="550.4" y="184.0" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64</text><text x="180.0" y="185.0" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor A</text><rect x="192" y="271.7" width="366.8" height="43.0" fill="#B8C0CC"/><text x="566.8" y="298.7" font-size="15" text-anchor="start" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">67</text><text x="180.0" y="299.7" font-size="15" text-anchor="end" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Competitor B</text><line x1="192" x2="192" y1="8" y2="352.0" stroke="#14213D"/></svg></div><div class="side"><ul><li>25,000 premium members; EUR 4 a month adds about EUR 1.2m a year before churn.</li><li>After the 2024 price increase, churn rose 1.5 points for three months; the same pattern would cut the net gain to about EUR 1.1m.</li><li>Price change effective 1 March 2027.</li></ul></div></div><div class="takeaway">Even after the rise, Fernhill sits below both main competitors.</div><footer><div class="footnote">Fernhill&#x27;s current price is EUR 59; the chart shows the price after the proposed EUR 4 rise.</div><div class="source">Source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026; Fernhill growth model v4</div><span class="pn">6</span></footer><aside class="notes"><b>Speaker note</b> We carry EUR 1.2m in the total bridge on page 8 and flag the churn-adjusted EUR 1.1m as the risk-adjusted view.</aside></section><section class="slide l-table" id="s7" data-title="A new-city gym needs EUR 4.5m and pays back in about seven years, outside the board&#x27;s four-year limit"><div class="tracker">4 New city</div><h2 class="title long">A new-city gym needs EUR 4.5m and pays back in about seven years, outside the board&#x27;s four-year limit</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Measure</th><th>Value</th></tr><tr><td>Investment required</td><td>EUR 4.5m</td></tr><tr><td>Payback period, at the ramp of the last three openings</td><td>about 7 years</td></tr><tr><td>Board&#x27;s investment payback limit</td><td>4 years</td></tr></table></div><div class="side"><ul><li>Based on the ramp of the last three city openings, 2019-2023.</li><li>We recommend not opening a new city now, and revisiting once the three approved moves are embedded.</li></ul></div></div><footer><div class="source">Source: Opening P&amp;Ls 2019-2023; Fernhill growth model v4</div><span class="pn">7</span></footer><aside class="notes"><b>Speaker note</b> This is why the deck does not propose a new city for 2027-2028.</aside></section><section class="slide l-chart" id="s8" data-title="The three moves add about EUR 6.7m, reaching EUR 64.7m by 2028, EUR 1.3m short of the EUR 66m target"><div class="tracker">Total effect</div><h2 class="title long">The three moves add about EUR 6.7m, reaching EUR 64.7m by 2028, EUR 1.3m short of the EUR 66m target</h2><div class="header">Revenue bridge 2026 to 2028, EUR m per year</div><div class="content"><div class="exhibit"><svg class="chart" viewBox="0 0 1150 360" preserveAspectRatio="xMidYMid meet" role="img" aria-label="The three moves add about EUR 6.7m, reaching EUR 64.7m by 2028, EUR 1.3m short of the EUR 66m target"><rect x="46.4" y="105.0" width="120.0" height="203.0" fill="#14213D"/><line x1="8.0" x2="992.0" y1="77.0" y2="77.0" stroke="#14213D" stroke-width="1.5" stroke-dasharray="6 5"/><text x="1000.0" y="82.0" font-size="14" text-anchor="start" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Target EUR 66m by 2028</text><text x="106.4" y="97.0" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">58.0</text><text x="106.4" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2026</text><rect x="243.2" y="94.2" width="120.0" height="10.8" fill="#B8C0CC"/><text x="303.2" y="86.2" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+3.1</text><line x1="166.4" x2="243.2" y1="105.0" y2="105.0" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="303.2" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Off-peak membership</text><rect x="440.0" y="85.8" width="120.0" height="8.4" fill="#B8C0CC"/><text x="500.0" y="77.8" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+2.4</text><line x1="363.2" x2="440.0" y1="94.2" y2="94.2" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="500.0" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Corporate wellness</text><rect x="636.8" y="81.5" width="120.0" height="4.2" fill="#B8C0CC"/><text x="696.8" y="73.5" font-size="15" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">+1.2</text><line x1="560.0" x2="636.8" y1="85.8" y2="85.8" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="696.8" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Premium price</text><rect x="833.6" y="81.5" width="120.0" height="226.5" fill="#D9822B"/><text x="893.6" y="73.5" font-size="15" text-anchor="middle" fill="#14213D" font-weight="bold" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">64.7</text><line x1="756.8" x2="833.6" y1="81.5" y2="81.5" stroke="#B8C0CC" stroke-dasharray="3 3"/><text x="893.6" y="330.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">Revenue 2028 with the</text><text x="893.6" y="347.0" font-size="14" text-anchor="middle" fill="#14213D" font-weight="normal" stroke="#FFFFFF" stroke-width="4" paint-order="stroke" stroke-linejoin="round">three moves</text><line x1="8" x2="992" y1="308.0" y2="308.0" stroke="#14213D"/></svg></div></div><div class="takeaway">The remaining EUR 1.3m gap is smaller than the range on the off-peak move alone (EUR 2.0m to 3.8m); we recommend accepting it rather than opening a new city that would not pay back within four years.</div><footer><div class="footnote">Core revenue held flat at EUR 58.0m (membership numbers flat 2023-2026). The premium step uses the EUR 1.2m gross figure; net of the 2024 churn pattern it is about EUR 1.1m, widening the gap to about EUR 1.4m.</div><div class="source">Source: Fernhill growth model v4</div><span class="pn">8</span></footer><aside class="notes"><b>Speaker note</b> Numbers tie to the exec summary on page 2 and the model.</aside></section><section class="slide l-table" id="s9" data-title="Cannibalisation, slow hiring and 2024-style churn are the three risks to the EUR 6.7m gain"><div class="tracker">Risks</div><h2 class="title">Cannibalisation, slow hiring and 2024-style churn are the three risks to the EUR 6.7m gain</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Risk</th><th>Threshold</th><th>Effect</th></tr><tr><td>Off-peak cannibalisation</td><td>More than 15% of new off-peak members are downgrades from standard</td><td>Off-peak adds less than EUR 2.0m</td></tr><tr><td>Corporate sales ramp</td><td>Two hires must start by February 2027</td><td>Ramp to 40 contracts by 2028 slips</td></tr><tr><td>Premium churn repeats the 2024 pattern</td><td>1.5 extra points of churn for three months</td><td>Net gain falls to about EUR 1.1m, widening the total gap to about EUR 1.4m</td></tr></table></div><div class="side"><ul><li>What would change the answer: off-peak take-up below 6,000 members by the end of 2027.</li></ul></div></div><footer><div class="source">Source: Fernhill growth model v4; off-peak pilot 2026; Fernhill membership data 2024-2026</div><span class="pn">9</span></footer><aside class="notes"><b>Speaker note</b> Flag these explicitly; do not let the board discover them later.</aside></section><section class="slide l-table" id="s10" data-title="The board can approve EUR 1.9m on 10 December 2026, with COO Lena Marsh owning delivery from January 2027"><div class="tracker">Next steps</div><h2 class="title long">The board can approve EUR 1.9m on 10 December 2026, with COO Lena Marsh owning delivery from January 2027</h2><div class="content two"><div class="exhibit tbl"><table class="data"><tr><th>Step</th><th>Owner</th><th>By when</th></tr><tr><td>Board approval of EUR 1.9m</td><td>Board</td><td>10 December 2026</td></tr><tr><td>Off-peak launch marketing (EUR 0.8m)</td><td>COO Lena Marsh</td><td>January 2027</td></tr><tr><td>Two corporate sales hires and pilot extension (EUR 0.6m)</td><td>COO Lena Marsh</td><td>January to February 2027</td></tr><tr><td>Booking-app changes (EUR 0.5m)</td><td>COO Lena Marsh</td><td>January 2027</td></tr><tr><td>Premium price change (+EUR 4)</td><td>COO Lena Marsh</td><td>1 March 2027</td></tr><tr><td>Checkpoint: off-peak take-up versus the 6,000-member threshold</td><td>COO Lena Marsh</td><td>End of 2027</td></tr></table></div><div class="side"><ul><li>Risk: off-peak cannibalisation above 15% of sign-ups</li><li>Risk: corporate sales ramp depends on both hires starting by February 2027</li></ul></div></div><footer><div class="source">Source: Decision requested, Fernhill board paper, December 2026</div><span class="pn">10</span></footer><aside class="notes"><b>Speaker note</b> Ask for the decision explicitly. Offer the end-2027 checkpoint as the review point.</aside></section><section class="slide l-table" id="s11" data-title="Utilisation by time band, full detail"><div class="tracker">Appendix</div><h2 class="title">Utilisation by time band, full detail</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Time band</th><th class="num">Utilisation</th></tr><tr><td>6-10 am</td><td class="num">58%</td></tr><tr><td>10 am-4 pm</td><td class="num">31%</td></tr><tr><td>4-6 pm</td><td class="num">64%</td></tr><tr><td>6-9 pm</td><td class="num">92%</td></tr><tr><td>9-11 pm</td><td class="num">40%</td></tr></table></div></div><footer><div class="source">Source: Gate-entry data, 34 gyms, Jan to Aug 2026</div><span class="pn">A1</span></footer></section><section class="slide l-table" id="s12" data-title="Key assumptions and sources"><div class="tracker">Appendix</div><h2 class="title">Key assumptions and sources</h2><div class="content"><div class="exhibit tbl"><table class="data"><tr><th>Driver</th><th>Value</th><th>Basis</th></tr><tr><td>Off-peak members by 2028</td><td>10,800 (revenue range EUR 2.0m to 3.8m)</td><td>Fernhill growth model v4; pilot 420 sign-ups, 4 gyms</td></tr><tr><td>Off-peak price</td><td>EUR 24 a month against EUR 39 standard</td><td>Fernhill pricing</td></tr><tr><td>Off-peak cannibalisation (pilot)</td><td>6% of sign-ups</td><td>Off-peak pilot, May to Aug 2026</td></tr><tr><td>Corporate contracts by 2028</td><td>40 at an average EUR 60k a year</td><td>Fernhill growth model v4; pilot 6 employers</td></tr><tr><td>Premium price rise</td><td>+EUR 4 a month on 25,000 members</td><td>Fernhill membership data 2024-2026</td></tr><tr><td>Premium churn after the 2024 rise</td><td>+1.5 points for 3 months</td><td>Fernhill membership data 2024-2026</td></tr><tr><td>New-city investment and payback</td><td>EUR 4.5m, about 7 years</td><td>Opening P&amp;Ls 2019-2023</td></tr></table></div></div><footer><div class="source">Source: Fernhill growth model v4</div><span class="pn">A2</span></footer></section></div>
<div id="overview"><h1>Titles-only read-through</h1><ol><li>Which growth moves should Fernhill approve for 2027-2028? <span style='color:#8A93A3'>(1)</span></li><li>Off-peak membership, corporate contracts and a EUR 4 premium rise add about EUR 6.7m by 2028, leaving a EUR 1.3m gap we recommend ac

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

# Deck: Which growth moves should Fernhill approve for 2027-2028?

*Fictional company. All figures, people and documents invented for evaluation.*

**Opening (SCQA)**
- Situation: Fernhill Fitness runs 34 gyms and generated EUR 58.0m of revenue in 2026.
- Complication: The board wants EUR 66.0m by 2028, without opening gyms in new cities and with at most EUR 2m of investment.
- Question: Which growth moves should the board approve on 10 December 2026?
- Answer: Approve an off-peak membership, corporate wellness contracts and a EUR 4 premium price rise; together they add about EUR 6.7m by 2028, leaving a EUR 1.3m gap the board should accept rather than chase with a new city.

**Key line**
1. Daytime capacity is the largest unused asset; an off-peak membership adds about EUR 3.1m a year.
2. Corporate wellness contracts are proven in the pilot and add about EUR 2.4m a year.
3. The premium tier is priced below both main competitors; a EUR 4 rise adds about EUR 1.1m to 1.2m a year.
4. A new-city gym does not pay back within the board's four-year limit.

## 1. Which growth moves should Fernhill approve for 2027-2028?
layout: title
subtitle: Recommendation on off-peak membership, corporate wellness and premium pricing — and why a new city should wait
note: Pre-read for the 10 December 2026 board meeting. The decision we ask for is on page 2 and again on page 10.

## 2. Off-peak membership, corporate contracts and a EUR 4 premium rise add about EUR 6.7m by 2028, leaving a EUR 1.3m gap we recommend accepting
layout: summary
tracker: Executive summary
lead: Fernhill generated EUR 58.0m in 2026. The board's target is EUR 66.0m by 2028, without opening gyms in new cities and with at most EUR 2m of investment.
body:
- Off-peak membership at EUR 24 a month (against the EUR 39 standard membership) reaches about 10,800 members by 2028 and adds about EUR 3.1m a year (range EUR 2.0m to 3.8m), filling gyms that run at only 31% utilisation from 10am to 4pm against 92% in the evening peak.
- Corporate wellness contracts, proven in a six-employer pilot (1,150 employees enrolled), reach 40 contracts by 2028 at an average EUR 60k a year, adding about EUR 2.4m a year (range EUR 1.4m to 3.0m); needs two corporate sales hires.
- The premium tier, priced EUR 59 against EUR 64 and EUR 67 at the two nearest competitors, can rise EUR 4 a month on 25,000 members, adding about EUR 1.2m a year before churn (about EUR 1.1m net of the churn pattern seen after the 2024 increase).
- A new-city gym needs EUR 4.5m and pays back in about seven years at the ramp of the last three openings — outside the board's four-year limit; we recommend not pursuing one now.
ask: **Decision requested 10 December 2026:** approve EUR 1.9m (off-peak launch marketing EUR 0.8m; two corporate sales hires and pilot extension EUR 0.6m; booking-app changes EUR 0.5m). Owner: COO Lena Marsh. Off-peak and corporate hiring start January 2027; premium price change from 1 March 2027. The answer changes if off-peak take-up stays below 6,000 members by the end of 2027.
source: Fernhill growth model v4; gate-entry data, 34 gyms, Jan to Aug 2026; corporate pilot contracts 2026; competitor price lists, September 2026; opening P&Ls 2019-2023
note: Read the bold line and the ask. Everything after this page proves one of the four points.

## 3. Gyms run at 92% utilisation in the evening peak but only 31% from 10am to 4pm, the largest unused asset Fernhill has
layout: chart
tracker: Context
message: distribution
chart: bar
header: Utilisation by time band, % of capacity, average of 34 gyms, Jan to Aug 2026
highlight: 10 am-4 pm
| Time band | Utilisation |
|---|---|
| 6-10 am | 58 |
| 10 am-4 pm | 31 |
| 4-6 pm | 64 |
| 6-9 pm | 92 |
| 9-11 pm | 40 |
takeaway: The 10am-4pm trough runs six hours a day, every day, across all 34 gyms.
source: Gate-entry data, 34 gyms, Jan to Aug 2026; Fernhill growth model v4
note: This is the gap the off-peak membership is built to fill.

## 4. An off-peak membership at EUR 24 a month reaches about 10,800 members by 2028 and adds about EUR 3.1m a year
layout: chart
tracker: 1 Off-peak membership
message: ranking
chart: bar
header: Off-peak membership revenue by 2028, EUR m per year, by scenario
highlight: Base case (10,800 members)
| Scenario | Revenue |
|---|---|
| Low | 2.0 |
| Base case (10,800 members) | 3.1 |
| High | 3.8 |
body:
- Priced at EUR 24 a month against the EUR 39 standard membership, targeting the 31% daytime trough.
- Pilot in 4 gyms, May to Aug 2026: 420 sign-ups; 6% were existing members downgrading from standard.
- Risk: if more than 15% of sign-ups are downgrades rather than new members, the move adds less than EUR 2.0m (see page 9).
footnote: Member count and revenue range from Fernhill growth model v4; pilot cannibalisation rate measured over 4 months and may not hold at scale.
source: Gate-entry data, 34 gyms, Jan to Aug 2026; off-peak pilot, 4 gyms, May to Aug 2026; Fernhill growth model v4
note: 10,800 members x EUR 24 x 12 months is about EUR 3.1m, which ties to the base case.

## 5. Corporate wellness contracts are proven in the pilot; 40 contracts by 2028 add about EUR 2.4m a year
layout: chart
tracker: 2 Corporate wellness
message: ranking
chart: bar
header: Corporate wellness revenue by 2028, EUR m per year, by scenario
highlight: Base case (40 contracts)
| Scenario | Revenue |
|---|---|
| Low | 1.4 |
| Base case (40 contracts) | 2.4 |
| High | 3.0 |
body:
- Pilot: six employers signed, 1,150 employees enrolled, 2026.
- Average contract value EUR 60k a year; needs two corporate sales hires starting by February 2027.
- Risk: the ramp to 40 contracts depends on both hires starting on time (see page 9).
source: Corporate pilot contracts 2026; Fernhill growth model v4
note: 40 contracts x EUR 60k is EUR 2.4m, the base case.

## 6. Fernhill's premium tier is priced below both main competitors; a EUR 4 rise adds about EUR 1.1m to 1.2m a year
layout: chart
tracker: 3 Premium price
message: ranking
chart: hbar
header: Premium tier monthly price, EUR, comparable offer with pool, classes and sauna, September 2026
highlight: Fernhill, after +EUR 4
| Supplier | Price |
|---|---|
| Fernhill, after +EUR 4 | 63 |
| Competitor A | 64 |
| Competitor B | 67 |
takeaway: Even after the rise, Fernhill sits below both main competitors.
body:
- 25,000 premium members; EUR 4 a month adds about EUR 1.2m a year before churn.
- After the 2024 price increase, churn rose 1.5 points for three months; the same pattern would cut the net gain to about EUR 1.1m.
- Price change effective 1 March 2027.
footnote: Fernhill's current price is EUR 59; the chart shows the price after the proposed EUR 4 rise.
source: Competitor public price lists, September 2026; Fernhill membership data 2024-2026; Fernhill growth model v4
note: We carry EUR 1.2m in the total bridge on page 8 and flag the churn-adjusted EUR 1.1m as the risk-adjusted view.

## 7. A new-city gym needs EUR 4.5m and pays back in about seven years, outside the board's four-year limit
layout: table
tracker: 4 New city
| Measure | Value |
|---|---|
| Investment required | EUR 4.5m |
| Payback period, at the ramp of the last three openings | about 7 years |
| Board's investment payback limit | 4 years |
body:
- Based on the ramp of the last three city openings, 2019-2023.
- We recommend not opening a new city now, and revisiting once the three approved moves are embedded.
source: Opening P&Ls 2019-2023; Fernhill growth model v4
note: This is why the deck does not propose a new city for 2027-2028.

## 8. The three moves add about EUR 6.7m, reaching EUR 64.7m by 2028, EUR 1.3m short of the EUR 66m target
layout: chart
tracker: Total effect
message: flow
chart: waterfall
header: Revenue bridge 2026 to 2028, EUR m per year
reference: 66 | Target EUR 66m by 2028
highlight: Revenue 2028 with the three moves
| Step | EUR m | Type |
|---|---|---|
| Revenue 2026 | 58.0 | total |
| Off-peak membership | 3.1 | delta |
| Corporate wellness | 2.4 | delta |
| Premium price | 1.2 | delta |
| Revenue 2028 with the three moves | 64.7 | total |
takeaway: The remaining EUR 1.3m gap is smaller than the range on the off-peak move alone (EUR 2.0m to 3.8m); we recommend accepting it rather than opening a new city that would not pay back within four years.
footnote: Core revenue held flat at EUR 58.0m (membership numbers flat 2023-2026). The premium step uses the EUR 1.2m gross figure; net of the 2024 churn pattern it is about EUR 1.1m, widening the gap to about EUR 1.4m.
source: Fernhill growth model v4
note: Numbers tie to the exec summary on page 2 and the model.

## 9. Cannibalisation, slow hiring and 2024-style churn are the three risks to the EUR 6.7m gain
layout: table
tracker: Risks
| Risk | Threshold | Effect |
|---|---|---|
| Off-peak cannibalisation | More than 15% of new off-peak members are downgrades from standard | Off-peak adds less than EUR 2.0m |
| Corporate sales ramp | Two hires must start by February 2027 | Ramp to 40 contracts by 2028 slips |
| Premium churn repeats the 2024 pattern | 1.5 extra points of churn for three months | Net gain falls to about EUR 1.1m, widening the total gap to about EUR 1.4m |
body:
- What would change the answer: off-peak take-up below 6,000 members by the end of 2027.
source: Fernhill growth model v4; off-peak pilot 2026; Fernhill membership data 2024-2026
note: Flag these explicitly; do not let the board discover them later.

## 10. The board can approve EUR 1.9m on 10 December 2026, with COO Lena Marsh owning delivery from January 2027
layout: table
tracker: Next steps
| Step | Owner | By when |
|---|---|---|
| Board approval of EUR 1.9m | Board | 10 December 2026 |
| Off-peak launch marketing (EUR 0.8m) | COO Lena Marsh | January 2027 |
| Two corporate sales hires and pilot extension (EUR 0.6m) | COO Lena Marsh | January to February 2027 |
| Booking-app changes (EUR 0.5m) | COO Lena Marsh | January 2027 |
| Premium price change (+EUR 4) | COO Lena Marsh | 1 March 2027 |
| Checkpoint: off-peak take-up versus the 6,000-member threshold | COO Lena Marsh | End of 2027 |
body:
- Risk: off-peak cannibalisation above 15% of sign-ups
- Risk: corporate sales ramp depends on both hires starting by February 2027
source: Decision requested, Fernhill board paper, December 2026
note: Ask for the decision explicitly. Offer the end-2027 checkpoint as the review point.

## A1. Utilisation by time band, full detail
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

## A2. Key assumptions and sources
layout: table
tracker: Appendix
| Driver | Value | Basis |
|---|---|---|
| Off-peak members by 2028 | 10,800 (revenue range EUR 2.0m to 3.8m) | Fernhill growth model v4; pilot 420 sign-ups, 4 gyms |
| Off-peak price | EUR 24 a month against EUR 39 standard | Fernhill pricing |
| Off-peak cannibalisation (pilot) | 6% of sign-ups | Off-peak pilot, May to Aug 2026 |
| Corporate contracts by 2028 | 40 at an average EUR 60k a year | Fernhill growth model v4; pilot 6 employers |
| Premium price rise | +EUR 4 a month on 25,000 members | Fernhill membership data 2024-2026 |
| Premium churn after the 2024 rise | +1.5 points for 3 months | Fernhill membership data 2024-2026 |
| New-city investment and payback | EUR 4.5m, about 7 years | Opening P&Ls 2019-2023 |
source: Fernhill growth model v4

