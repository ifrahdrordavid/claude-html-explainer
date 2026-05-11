# Accessibility checklist

Every generated page must pass these. Lighthouse a11y score ≥ 95 is the
shipping bar.

## Document structure

- `<html lang="en">` (or appropriate language code).
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
  **without** `user-scalable=no` — never disable zoom.
- One `<h1>` per page. No skipped heading levels (h2 → h3 → h4, never
  h2 → h4).
- Landmarks present and correctly labeled:
  - `<header role="banner">` for site header
  - `<main id="main">` wrapping the article
  - `<nav aria-label="Primary navigation">` for site nav
  - `<nav aria-label="Page sections">` for the TOC
  - `<footer role="contentinfo">`
  - Each `<section>` has `aria-labelledby="h-...":` pointing at its heading

## Skip link

```html
<a href="#main" class="skip-link">Skip to main content</a>
```

Must be the **first** focusable element in `<body>`. CSS in `styles.css`
hides it off-screen until it receives focus.

## Focus management

- `:focus-visible` outline ring on every interactive element. Already in
  `styles.css`: `2px solid var(--color-primary)` with `3px` offset.
- Tab order matches visual order — don't use `tabindex` greater than 0.
- After an in-page anchor click, focus moves to the section heading (done
  by `app.js`).

## SVGs

Every **informational** SVG:

```html
<svg
  role="img"
  aria-labelledby="x-title x-desc"
  focusable="false"
  viewBox="..."
>
  <title id="x-title">{{plain title}}</title>
  <desc id="x-desc">{{2-4 sentence description of what the diagram conveys}}</desc>
  ...
</svg>
```

Every chart-shaped SVG (verdict tree, comparison diagram) also has a
sibling screen-reader-only data table:

```html
<table class="visually-hidden">
  <caption>{{table caption}}</caption>
  <thead>...</thead>
  <tbody>
    <tr><td>...</td></tr>
  </tbody>
</table>
```

**Decorative** SVGs (brand mark, ornament): use `aria-hidden="true"` and
no `<title>`. The brand-mark example in the frame template uses this.

## Color and contrast

- Never use color as the sole signal. Verdict pills carry both text
  ("PASS") and color (green). Phase nodes carry both a label and a fill.
- Body text contrast: `#1E293B` on `#F8FAFC` ≈ 14:1 (well above 4.5:1
  WCAG AA).
- Muted text contrast: `#64748B` on `#F8FAFC` ≈ 5.8:1 (above 4.5:1 for
  normal text).
- Dark-section text contrast: `#F1F5F9` on `#0F172A` ≈ 17:1 (well above).
- `.dark-section code` uses tinted indigo `#C7D2FE` on `rgba(99,102,241,0.18)`
  with `#A5B4FC` border — passes contrast and is visible. **Do not lose
  this rule when editing CSS.**

## Motion

- `@media (prefers-reduced-motion: reduce)` zeros out animation and
  transition durations. Already in `styles.css`.
- `app.js` reads `matchMedia('(prefers-reduced-motion: reduce)')` and falls
  back to `behavior: 'auto'` for `window.scrollTo`.

## Link text

- Every link describes its destination: "Walk through a verdict", "Where
  the code lives", "Send thoughts". Never "click here" or bare "more".
- External link text should include the destination type when ambiguous:
  "View the source on GitHub", not just "GitHub".

## Forms (rare in explainers)

If you add a form (search, contact, feedback widget):
- Every `<input>` has an associated `<label>`.
- Error messages live in `aria-describedby`d elements.
- Submit buttons use `<button type="submit">`, not styled anchors.

## Keyboard

- All interactive elements reachable via Tab.
- `<details>` opens on Enter/Space (browser default — don't intercept).
- Escape closes open `<details>` (handled by `app.js`).
- No keyboard traps.

## Testing

Before declaring done:

1. Tab through the page from top. Every focusable element gets a visible
   ring. No invisible jumps.
2. Open Chrome DevTools → Lighthouse → run an a11y-only audit.
   Score must be ≥ 95. Investigate any 80+ score that fails to hit 95.
3. Open with screen reader if available (VoiceOver on macOS, NVDA on
   Windows). Skim section by section; verify SVG `<title>`/`<desc>` are
   announced.

## What the Playwright screenshot check does NOT verify

- Tab order, focus rings, keyboard interaction.
- Screen reader announcements.
- Color-contrast ratios in non-default themes.

Screenshots catch visual defects (overflow, invisible text). They don't
catch a missing `<label>` or a broken Tab order. The above checklist
covers the gaps.
