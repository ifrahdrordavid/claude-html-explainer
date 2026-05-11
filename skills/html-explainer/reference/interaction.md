# Interaction patterns

All three behaviors live in `assets/app.js`. You don't need to write any
new JS for a standard explainer — just reference the script:

```html
<script src="assets/app.js" defer></script>
```

at the end of `<body>` (after `<footer>`).

## 1. Scroll-spy TOC

`IntersectionObserver` watches every `<main> section[id]`. When a section
becomes the closest-to-viewport-top, the matching `#page-toc a[href="#id"]`
gets `.toc-active` + `aria-current="true"`; others lose them.

CSS hook `.page-toc a.toc-active` styles the active entry — indigo color,
700 weight, indigo left-border, light-indigo background.

**Requirements:** every section in `<main>` that should be tracked must
have an `id`. Every TOC `<a>`'s `href` must point to one of those ids.

## 2. Smooth scroll with focus management

Every `a[href^="#"]` click is intercepted:
- `preventDefault`
- Calculate the section's top minus 80 px (offsets the sticky header)
- `window.scrollTo({ top, behavior: 'smooth' | 'auto' })` — auto when
  `prefers-reduced-motion: reduce`
- Move keyboard focus to the section's first `h1/h2/h3` so screen-reader
  users land where sighted users land
- Update the URL hash via `history.replaceState` without jumping

**This is non-negotiable for a11y.** Tab navigation should land on the same
content as anchor clicks.

## 3. Escape closes open `<details>`

A `keydown` listener on `document` catches the `Escape` key and removes
the `open` attribute from every `details[open]` on the page.

This is a quality-of-life touch: readers who expanded six FAQ entries can
collapse them all in one keystroke instead of clicking each header.

## What `app.js` does NOT do

- No analytics, no telemetry, no fetch calls.
- No DOM mutation beyond toggling classes/attributes.
- No third-party libraries (no jQuery, no Alpine, nothing).
- No mode toggles (no light/dark switcher; the design system is light by
  default with selective `.dark-section` for sections that want gravity).

If you need new behavior, add it as a separate `<script>` tag with the
`defer` attribute and a clear comment. **Don't fork `app.js`** — keep this
reference file the canonical version so cross-skill consistency holds.

## Progressive enhancement guarantees

The page must remain functional with JS disabled:

- `<details>` opens/closes natively (browser behavior, not JS)
- TOC links still navigate (just without smooth scroll or focus management)
- No content is gated on JS — every paragraph, table, SVG renders without it

If you find yourself needing JS to *show* content, you've gone wrong.
