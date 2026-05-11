# html-explainer

A Claude Code plugin that generates polished, interactive single-page HTML
explainers for technical systems, frameworks, plans, and designs — with a
fixed design system, 18 reusable section patterns, 6 SVG diagram recipes,
and a mandatory Playwright screenshot verification step before delivery.

Built on the look-and-feel of an investor-grade reference page (slate-navy
"trust" palette, ≥18 px body, sticky scroll-spy TOC, accessible SVGs).

## Install

In any Claude Code session:

```
/plugin marketplace add ifrahdrordavid/claude-html-explainer
/plugin install html-explainer@html-explainer
```

Then restart Claude Code (or run `/reload-plugins` if your version supports
it). The skill auto-fires on prompts like:

- "create an HTML to explain X"
- "make an HTML presentation for the X system"
- "HTML walkthrough of Y"
- "/html-explainer X"

You can also invoke it directly via `/html-explainer:html-explainer`.

## What you get

Asking the skill *"create an HTML to explain how PostgreSQL MVCC works"*
produces a folder containing:

```
~/drafts/<topic-kebab>-html/
├── index.html             ← single-page explainer
├── assets/
│   ├── styles.css         ← 893 lines, copied verbatim from the reference build
│   ├── app.js             ← scroll-spy + smooth scroll + Escape-closes-details
│   └── (any extras)
├── screenshot.py          ← Playwright verifier the skill runs to catch defects
└── .screenshots/          ← one PNG per section, used for visual verification
```

The HTML is self-contained: no build step, no frameworks, no CDN beyond
Google Fonts. Open `index.html` in any browser.

## What's in the box

- **`SKILL.md`** — 7-step procedural driver (parse → research → plan →
  generate → verify → ship → report). ~225 lines.
- **`assets/styles.css`** — Design system: 18 px body floor, slate-navy
  trust palette (#4338CA primary, #0EA5E9 accent), 8 px spacing scale,
  light/dark/alt surfaces. Hand-written; no Tailwind. ~893 lines.
- **`assets/app.js`** — Vanilla JS: IntersectionObserver scroll-spy,
  smooth scroll with focus management, Escape closes open `<details>`.
  ~67 lines.
- **`assets/screenshot.py`** — Headless Chromium via Playwright. Opens every
  `<details>`, screenshots each section by id, writes `.screenshots/*.png`
  for the skill to read back and visually verify.
- **`reference/section-patterns.md`** — 18 copy-paste section snippets
  (hero, problem framing, concept cards, pipeline timeline, sample-data
  table, story walkthrough, decision tree, dependency DAG, multi-input
  layout, cycle/loop, side-by-side diff, engineering invariants, source
  map, open problems, FAQ disclosures, CTA…).
- **`reference/svg-recipes.md`** — 6 named diagrams with exact viewBoxes
  and parametrization notes (pipeline timeline, decision tree, multi-input
  layout, cycle/feedback loop, dependency DAG, side-by-side diff).
- **`reference/design-system.md`** — Token tables, typography scale,
  palette, spacing, breakpoints, light/dark guidance.
- **`reference/interaction.md`** + **`accessibility.md`** — Behavior docs
  and a11y checklist (Lighthouse a11y target ≥ 95).
- **`examples/v4-snippets.md`** — Real working HTML fragments from the
  reference build for direct copy.

## Defaults encoded (and why)

| Choice | Why |
|---|---|
| Body 18 px floor | Trust-palette long-form reading research |
| Slate-navy palette | Stripe / Vercel / Linear cross-reference |
| No Tailwind / Bootstrap | Hand-written CSS for full control and zero build |
| Playwright verification loop | Two visual bugs shipped without it in v3 |
| Dark-section `<code>` rule | Without it, inline code becomes invisible white boxes on slate-navy |
| Cycle/loop SVG `r ≥ 50` | 7-character labels (`baseline`, `diagnose`) overflowed at r=32 |
| Collaborator tone by default | User explicitly course-corrected away from pitch tone |
| No emojis | User preference (unless explicitly requested) |
| No invented numbers | Hero stat blocks drop if no real metric exists |

## Requirements

The skill needs Playwright + headless Chromium installed for the
verification step:

```bash
pip install playwright
python3 -m playwright install chromium
```

(The skill will print this hint if `screenshot.py` errors with
`playwright not installed`.)

## Uninstall

```
/plugin uninstall html-explainer@html-explainer
/plugin marketplace remove html-explainer
```

## License

MIT — see [LICENSE](LICENSE).

## Acknowledgments

The design system was synthesized from public UI/UX writing on
Stripe, Vercel, and Linear's design systems, plus academic and industry
work on legible long-form web typography. CSS and JS are derived from a
production reference build (the "GantryForge court-trial VLM" walkthrough)
that went through four iterations of human review before being lifted into
this skill.
