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
override per-page.

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
