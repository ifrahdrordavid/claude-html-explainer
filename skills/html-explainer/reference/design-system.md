# Design system — tokens, palette, typography

> Source of truth: `assets/styles.css`. This file documents what's already
> there. Don't re-derive — copy the asset and write content that fits.

## Typography scale

| Role | Size | Weight | Line-height | Letter-spacing | CSS var |
|---|---|---|---|---|---|
| body | **18 px** (1.125rem) | 400 | 1.55 | normal | `--text-base` |
| caption / TOC | 14 px (0.875rem) | 500 | 1.6 | normal | `--text-xs` |
| h6 | 18 px | 600 | 1.4 | 0.02em | `--text-h6` |
| h5 | 20 px | 600 | 1.35 | 0.01em | `--text-h5` |
| h4 | 24 px | 600 | 1.3 | −0.01em | `--text-h4` |
| h3 | 30 px | 600 | 1.25 | −0.015em | `--text-h3` |
| h2 | 36 px | 700 | 1.15 | −0.02em | `--text-h2` |
| h1 | 48 px | 700 | 1.10 | −0.025em | `--text-h1` |
| hero | 60 px | 700 | 1.05 | −0.03em | `--text-hero` |
| prose `<p>` | 19 px (1.1875rem) | 400 | 1.65 | — | `.prose p` |
| disclosure body | 17 px (1.0625rem) | 400 | 1.65 | — | `.disclosure-body` |
| stat value | 56 px (3.5rem) | 700 | 1 | −0.03em | `.stat-value` |

**Body 18 px is non-negotiable.** Don't go lower. Up to 20 px is fine if a
section is heavy on prose.

## Typeface

- **Inter** (Google Fonts variable, weights 400/500/600/700) for body + headings
- **JetBrains Mono** (weight 500) for inline `<code>` and monospaced labels

Loaded via `<link>` in `<head>`. No other webfonts — one typeface family
(plus mono) is the rule.

## Palette — "trust"

```
--color-primary:       #4338CA   indigo-700, primary brand + CTAs
--color-primary-hover: #3730A3   one shade darker for hover
--color-primary-light: #EEF2FF   page-tinted indigo for callouts/active TOC
--color-accent:        #0EA5E9   sky-500, reserved for data viz pop

--neutral-50:  #F8FAFC   page background
--neutral-100: #F1F5F9   alt-section background, code background
--neutral-200: #E2E8F0   subtle borders
--neutral-300: #CBD5E1   default borders
--neutral-500: #64748B   muted text
--neutral-700: #334155   secondary headings (not body)
--neutral-900: #0F172A   dark-section surface

--color-success: #16A34A
--color-warn:    #D97706
--color-danger:  #DC2626

--color-text:        #1E293B   never pure black
--color-text-muted:  #64748B
```

Contrast: `#1E293B` on `#F8FAFC` ≈ 14:1; `#64748B` on `#F8FAFC` ≈ 5.8:1.
Both pass WCAG AA for body.

## Dark surface

For "How it works" / pipeline / engineering-demo sections:

```
--dark-surface-bg:    #0F172A
--dark-surface-text:  #F1F5F9
--dark-surface-muted: #64748B
```

Apply via `<section class="dark-section">`. Headings, prose, and eyebrows
get auto-adjusted via cascading rules in `styles.css`.

### CRITICAL — dark-section inline code

This rule is already in `styles.css`. **Do not remove it. Do not regress it.**

```css
.dark-section code,
.dark-section .prose code,
.dark-section .disclosure-body code,
.dark-section .figcaption code,
.dark-section .phase-list code {
  background: rgba(99, 102, 241, 0.18);
  color: #C7D2FE;
  border: 1px solid rgba(165, 180, 252, 0.22);
  padding: 2px 8px;
  border-radius: var(--radius-sm);
  font-size: 0.95em;
}
```

Without it, every inline `<code>` inside `.dark-section` inherits the global
`background: var(--neutral-100)` which is *light* on a dark background —
rendering as invisible white pills. v3 shipped with this bug; only Playwright
screenshots caught it.

## Spacing scale (8 px base)

```
--space-1: 4    --space-6:  32
--space-2: 8    --space-7:  48
--space-3: 12   --space-8:  64
--space-4: 16   --space-9:  96
--space-5: 24   --space-10: 128
```

Standard rhythm:
- Within a card: 16–24 px (`--space-4`, `--space-5`)
- Between paragraphs: 16 px (`--space-4`)
- Section padding-top/bottom: 96 px (`--space-9`)
- Dark/alt section internal padding: 64 px (`--space-8`)

## Shadows & radius

```
--shadow-sm: ambient card resting state
--shadow-md: card hover state
--shadow-lg: not used; reserved
--shadow-elevated: hero stats / CTA — soft, large, premium

--radius-sm: 4   small chips, code pills
--radius-md: 6   buttons, inputs
--radius-lg: 8   cards, panels (most common)
--radius-xl: 12  dark/alt section containers, CTA, hero stat bar
```

**No pill radius (9999 px) on primary CTAs.** Pills look cheap on serious
content; Stripe's design system explicitly avoids them. Verdict pills,
status chips, and tags use 999 px (true pill) — that's their job.

## Light vs dark — when to flip

Default: dark-on-light prose. It's faster to read for long-form.

Use `class="dark-section"` selectively for:
- A "How it works" or "Inside the box" pipeline section — gravity, demo feel
- An engineering-internals callout — terminal-adjacent

Use `class="alt-bg"` (neutral-100) for:
- A story walkthrough or calibration loop — break visual rhythm
- A FAQ that follows a heavy section

Don't alternate every section — the alternation should signal "this content
is structurally different," not decorate.

## Responsive breakpoints

From `styles.css`:

| Breakpoint | What changes |
|---|---|
| ≥1024 px (default) | Two-column TOC + content, 240px sidebar |
| < 1024 px | TOC moves above content as horizontal pill row, primary-nav hides, hero shrinks to h1 (44px) |
| < 640 px | Body drops to 17 px, hero further to 36 px, CTA padding tightens |

The 240 px TOC width and 1440 px max content width are baked in. Don't
override them per-page **except** with the scoped recipes below
(*Wide-screen overrides* and *Type-scale enlargement*) when the user
explicitly asks for it — those go in a `<style>` block in the page's
`<head>` (after the `<link>` to `styles.css`), never as edits to
`styles.css` itself.

## Motion

```
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

All hover transitions are 150–200 ms. Smooth scroll in `app.js` honors
`prefers-reduced-motion` and falls back to `behavior: 'auto'`.

## Wide-screen overrides (≥ ~1600 px viewports)

The stock CSS pins the page shell at `max-width: 1440px` on `.layout`,
`.site-header__inner`, `.hero-inner`, and `.site-footer__inner`. On a 4K /
5K / 50" display that's a ~1440 px column with ~1200 px of side whitespace
each side — the page looks like a small island. The fix is a scoped
`<style>` block in the page's `<head>` **after** the `<link>` to
`styles.css`, so the cascade picks it up. Never edit `styles.css`.

Drop in this block when the user wants the page to spread on a wide
display (typical trigger words: *"too narrow"*, *"too much white space"*,
*"fill the screen"*, *"my screen is N inches"*):

```html
<style>
  /* ---- Page shell: widen past the stock 1440 px island, but never narrower than 1440. ---- */
  .site-header__inner,
  .hero-inner,
  .layout,
  .site-footer__inner { max-width: max(1440px, min(2880px, 94vw)); }

  /* Wider, fluid TOC rail so the bumped TOC text doesn't wrap to ribbons.
     Guarded ≥ 1100 px so the stock mobile single-column collapse (≤ 1024 px)
     still wins (the scoped <style> comes after styles.css). */
  @media (min-width: 1100px) {
    .layout { grid-template-columns: clamp(280px, 17vw, 360px) minmax(0, 1fr); }
  }

  /* Reading columns: let prose/callouts breathe wider, but not into eye-strain territory. */
  .prose,
  .callout,
  .hero-lede { max-width: min(82ch, 100%); }
  .figcaption { max-width: min(95ch, 100%); }

  /* Card grids: cards must be wide enough for body text at the chosen size.
     min(100%, …) keeps the "collapse to one column" behavior without media queries. */
  .hero-stats { grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); }
  .cast-grid  { grid-template-columns: repeat(auto-fit, minmax(min(100%, 600px), 1fr)); }
  .appeals-grid,
  .eng-grid,
  .grid-2     { grid-template-columns: repeat(auto-fit, minmax(min(100%, 480px), 1fr)); }
  .open-grid  { grid-template-columns: repeat(auto-fit, minmax(min(100%, 540px), 1fr)); }

  /* SVG diagrams: grow with the page so labels render at a legible size,
     but cap + center so they don't balloon to 2300 px on a 50" screen. */
  .pipeline-figure svg, .tree-figure svg, .loop-figure svg,
  .dag-figure svg, .cameras-figure svg, .bars-figure svg {
    max-width: 1680px; display: block; margin: 0 auto;
  }
</style>
```

Why this is shaped the way it is:

- **`max(1440px, min(2880px, 94vw))`** — never narrower than the stock
  1440 px floor (so existing layouts don't regress), scales up with
  viewport, caps at 2880 px (~75 % of a 4K screen, ~56 % of a 5K — wider
  than that hurts prose readability).
- **TOC `clamp(280px, 17vw, 360px)` inside `@media (min-width: 1100px)`** —
  the bumped TOC text wraps to multiple lines in 240 px; widen it
  fluidly. The media-query guard is load-bearing: the scoped `<style>`
  block comes after `styles.css`, so an unguarded `.layout` grid rule
  would clobber the stock mobile single-column collapse (`@media
  (max-width: 1024px)`) inside `styles.css` and break narrow viewports.
- **Card grids `minmax(min(100%, N), 1fr)`** — the `min(100%, N)` guard
  lets cards collapse cleanly to one column when narrower than `N` (no
  extra media query needed). The `N` floor must be wide enough for the
  card's text at the chosen body size.
- **SVG figure cap at 1680 px** — SVG `<text>` renders at
  `font-size_in_viewBox × (svg_rendered_width / viewBox_width)`. A
  1100-wide-viewBox tree SVG rendered at 1680 px makes a 13-unit label
  render at ~20 px — the same target as the body floor. Going past 1680 px
  makes the diagram visually dominate the page without adding readability.

**Always re-verify with `screenshot-wide.py`** after applying — see
`SKILL.md` → Step 5b.

## Type-scale enlargement

Stock is 18 px body floor. If the user asks for a larger smallest font
(typical: *"smallest font at least 20 px"*, *"font is too small"*,
*"accessibility"*), bump the whole scale by overriding the root font-size
in the same scoped `<style>` block — never edit `styles.css`.

```css
/* Smallest CSS font in styles.css is `.cast-tag { font-size: 0.8125rem }`.
   To make it ≥ 20 px and scale everything else proportionally, raise the
   root font-size: 0.8125 × 24.96px ≈ 20.3 px. */
html { font-size: 156%; }
```

Effect at 156 %: body 18 → 28 px, prose 19 → 30 px, captions / TOC / table
cells 16 → 25 px, h2 36 → 56 px, hero 60 → 94 px. Re-verify with
`screenshot.py` AND `screenshot-wide.py` — the bigger fonts often force:

- card grids to need a wider `minmax(…)` floor (see *Wide-screen
  overrides* above)
- the TOC rail to widen (same)
- table cells in `.src-table td:last-child` to wrap (see §15 caveats
  in `section-patterns.md`)

**Don't reach below the 18 px body floor**, and don't bump above ~175 %
without re-checking every SVG diagram — the SVG `font-size` attributes
are in viewBox units and don't scale with `rem`, so the diagrams stay
their pre-bump size unless the SVG containers are widened (the
*Wide-screen overrides* recipe widens the containers via the layout cap,
which makes the SVG text render bigger as a side effect).
