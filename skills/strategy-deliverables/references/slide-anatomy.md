# Slide Anatomy

## What it is

The fixed set of zones every content slide has, and what each zone may contain. A consistent anatomy lets the reader find the message, the proof and the source in the same place on every page, so attention goes to content. The deck builder uses it as the layout contract; the reviewer uses it to spot what is missing.

## When NOT to use

- **Title, divider and agenda pages.** They have their own simple layout.
- **Dense appendix tables.** Keep title, source and units, drop the highlight and takeaway; the page is for lookup.
- **Live workshop canvases** where the group fills a blank template. Use the workshop format, then rebuild results as proper slides.
- **A memo is the better format.** When the argument is mostly text with one or two numbers, write a [One-Page Memo](one-page-memo.md) instead of forcing it onto slides.

## Standard

A content slide has these zones, top to bottom:

1. **Tracker** (top edge, small): section name or key-line number, so the reader knows where they are.
2. **Action title**: one sentence, two lines at most ([Action Titles](action-titles.md)).
3. **Subtitle or chart header** (optional): what is measured, unit, period. "Revenue, EUR m, 2023 to 2030".
4. **Body**: one exhibit that proves the title. One chart, one table, or one simple framework. Two exhibits only when the message is a direct comparison of the two.
5. **Highlight**: the data point that carries the message is emphasised (colour, label, callout); everything else is muted grey.
6. **Takeaway box** (optional): one line that adds the implication when the title is already full. Never a repeat of the title.
7. **Footnotes and source** (bottom): data source, date, scope, definitions, and any estimate flagged as such.
8. **Page number.**

Testable rules:
- One message per slide; the body proves the title, no more and no less.
- Every number has a unit and every chart has a source line.
- Text is short enough to read in under a minute; no full paragraphs on presented slides.
- Direct labels instead of legends wherever possible.
- Same position, fonts, colours and number formats on every slide.

## Step by step

1. Take the action title from the ghost deck ([Storyline and Ghost Deck](storyline.md)).
2. Pick the comparison the title makes and the chart for it ([Chart Selection](chart-selection.md)).
3. Build the exhibit with only the data needed to prove the title.
4. Remove decoration: borders, 3D, gridlines, background images ([Slide Quality Red Flags](slide-quality-red-flags.md)).
5. Highlight the message data point; grey the rest.
6. Add unit, period, source and footnotes.
7. Add the tracker and check title length at real size.
8. Cover the title and ask: does the body alone point to the same conclusion? Then cover the body: does the title alone state it?

## Common mistakes

- **Two charts that make two points.** The reader does not know which one the title refers to. Split the page.
- **Takeaway box restating the title.** Takes space and adds nothing. Delete or replace with the implication.
- **Missing source line.** The first question in the room is "where is this from?". Without an answer the number loses its weight.
- **Bullet lists as body.** Six bullets with no hierarchy are a memo crammed onto a slide. Pick the one exhibit that proves the title.
- **Everything in colour.** When every bar is coloured, nothing is highlighted.
- **Inconsistent layout.** Title position or fonts jumping between slides makes the deck look assembled from several projects, and the reader starts doubting the numbers too.

## Worked example

*Fictional example. Company, figures and people are invented.*

Weak slide: title "Installed base". Body: a pie chart of age bands and a bullet list of five observations about service. No unit, no source.

Strong slide:
- Tracker: "1 Service opportunity".
- Title: "52% of the 60,000 installed pumps are older than eight years and have no service contract".
- Header: "Installed pumps by age band and contract status, number of pumps, end of 2025".
- Body: stacked horizontal bars by age band, split into "under contract" and "no contract".
- Highlight: the "older than eight years, no contract" segments in the accent colour, labelled "31,200 pumps".
- Takeaway: "At EUR 1,000 per pump per year, the uncovered base is a revenue pool of about EUR 31m."
- Source: "Alder ERP installed-base export, December 2025; contract status from service CRM."

## Output template

```markdown
**Slide <n>**
- Tracker: <section / key-line number>
- Action title: <full sentence, max two lines>
- Chart header: <measure>, <unit>, <period>
- Body: <chart type> showing <comparison>
- Highlight: <data point>, label "<value>"
- Takeaway (optional): <implication not already in the title>
- Footnotes: <definitions, estimates flagged>
- Source: <source>, <date>, <scope>
```

## Related

- [Action Titles](action-titles.md), [Chart Selection](chart-selection.md), [Deck Structure](deck-structure.md), [Storyline and Ghost Deck](storyline.md), [Slide Quality Red Flags](slide-quality-red-flags.md)
