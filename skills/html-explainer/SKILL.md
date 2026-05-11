---
name: html-explainer
description: >
  Generate a polished, interactive single-page HTML explainer for a technical
  system, framework, plan, or design. Uses an established design system
  (18px body floor, slate-navy "trust" palette, sticky scroll-spy TOC,
  accessible SVGs) and a library of section patterns: hero, role cards,
  pipeline timelines, decision trees, DAGs, side-by-side diffs, sample-data
  cards, story walkthroughs, FAQ disclosures, source maps, open problems.
  Verifies visually with Playwright screenshots before delivery. Use whenever
  someone wants to create an HTML file/page to explain a system, present a
  plan, walk through a framework, document a design, or onboard a
  collaborator. Triggers on: "create an HTML for X", "make an HTML
  presentation", "HTML walkthrough", "explain X in HTML", "/html-explainer".
---

# html-explainer — Single-page interactive explainer generator

Produce a v4-quality HTML explainer in one shot: hero → big idea → labeled
sections → SVG diagrams → FAQ → CTA, with sticky scroll-spy TOC, accessible
markup, and Playwright-verified screenshots.

> **The look-and-feel is decided.** CSS and JS in `assets/` are copied
> verbatim from a validated reference build and must not be re-derived from
> scratch. If the user wants a custom variant, deliver v4 first, then
> override.

## When this fires

- "create an HTML to explain / present / walk through X"
- "make an HTML for the X system"
- "I need an HTML document for X"
- "build me a single-page HTML for X"
- "/html-explainer X"

Do NOT fire for: editing an existing HTML file the user already has open,
generating fragments embedded in another tool, or generating a static-site
build. This skill produces one folder with one `index.html` + assets.

## Step 1 — Parse the request

Extract from the user's message:

| Slot | Default | When to ask |
|---|---|---|
| **Topic** | the X in "explain X" | always required |
| **Audience** | technical collaborator | only ask if "investors", "non-technical", "engineer onboarding" not stated |
| **Source material paths** | none | only use if the user listed files / dirs |
| **Output directory** | `~/drafts/<topic-kebab>-html/` | only ask if user gave a path |
| **Sendmac after** | yes if shippable | skip ask if the topic is trivial |

If anything is ambiguous and the default does not obviously apply, use a
single `AskUserQuestion` call with all open slots at once. Skip the question
entirely when reasonable defaults exist — the user prefers fewer prompts.

## Step 2 — Research (only if source material given)

Only run when the user supplied codebase paths, docs, or plans. For purely
conceptual topics, skip this step.

- Spawn parallel `Explore` agents (subagent_type="Explore") to map source
  material in parallel; do not duplicate their work in the main thread.
- Synthesize into `<output_dir>/research/SYNTHESIS.md`: one-paragraph thesis,
  named entities, key facts, things to surface. Keep it under 200 lines.

## Step 3 — Plan section flow

Read `reference/section-patterns.md` for the 16-pattern catalog. Pick **8–12**
that fit the topic — never include all.

**Always include:** hero, big idea, engineering invariants (or equivalent
"rules of the system"), FAQ, CTA.

**Default ordering:** hero → problem (if named) → big idea → concept cards
(if ≥4 roles) → pipeline timeline → sample data (if real run output) →
story walkthrough (if narrative helps) → decision tree / DAG / multi-input
(whichever fits) → cycle/loop (if feedback) → diff (if comparing) →
engineering invariants → source map (if codebase) → open problems → FAQ → CTA.

Drop sections that don't apply. Don't invent data to fill a section pattern.

## Step 4 — Generate files

Create `<output_dir>/` and `<output_dir>/assets/`, then:

1. **Copy verbatim** (use `cp`, no edits):
   - `~/.claude/skills/html-explainer/assets/styles.css` → `<output_dir>/assets/styles.css`
   - `~/.claude/skills/html-explainer/assets/app.js` → `<output_dir>/assets/app.js`
   - `~/.claude/skills/html-explainer/assets/screenshot.py` → `<output_dir>/screenshot.py`

2. **Generate `<output_dir>/index.html`** using:
   - The frame: doctype, `<head>` with Google Fonts (Inter + JetBrains Mono),
     `<header>` with brand, two-column `<div class="layout">` with TOC aside +
     content article, `<footer>`, `<script src="assets/app.js" defer>`.
   - Section bodies: copy-paste from `reference/section-patterns.md`,
     replacing `{{PLACEHOLDERS}}` with topic content.
   - SVGs: pull from `reference/svg-recipes.md`, parametrize node count,
     labels, colors, keeping the exact viewBoxes.
   - Hero/lede/CTA copy: write for the stated audience. Default tone is
     **collaborator-oriented, not investor-oriented**. No pitch language
     unless explicitly requested.

3. **TOC ordering must match section order on the page.** Build the TOC `<ol>`
   in the same order sections appear in the article. Mismatches were the
   single most common defect in the source session — double-check before
   moving on.

4. Every nav/TOC link must resolve to a real section id.

## Step 5 — Verify (non-negotiable)

The skill is **not done** until Playwright screenshots have been generated
and Read back. This catches text-overflow, invisible-on-dark code blocks,
viewBox clipping, and TOC misalignment — none of which static review caught
in the source session.

```bash
cd <output_dir> && python3 screenshot.py
```

Expected output: `.screenshots/full_page.png`, `.screenshots/hero.png`,
`.screenshots/cta.png`, and one PNG per section id in the TOC.

Then **Read each PNG** in turn (`Read` tool with the absolute path — Claude
Code displays images visually). Check for:

| Defect | Where it usually appears |
|---|---|
| Text overflows circle/box/card | Cycle/loop SVG with `r<50`, DAG nodes with long labels |
| Inline `<code>` is invisible (white-on-white) | Inside `.dark-section`. CSS already has a fix — confirm it's loading |
| SVG clipped at viewBox edges | DAG with too many phase columns; pipeline timeline with too many nodes |
| TOC entry has no matching section | Add the section or remove the link |
| Section visibly empty | Placeholder slipped through; replace with real content or drop |
| Hero stat cards have no real numbers | Drop or replace |

If any defect is detected: fix the source in `index.html`, re-run
`screenshot.py`, re-Read the affected PNG. Iterate until clean. Don't ship
otherwise.

If `screenshot.py` errors with `playwright` not installed:

```bash
pip install playwright && python3 -m playwright install chromium
```

## Step 6 — Ship (if user wants Mac delivery)

```bash
sendmac <output_dir>/ <topic-kebab>
```

`sendmac` is at `/home/drorifrah/bin/sendmac`. If unavailable, report the
GCP path and stop.

## Step 7 — Report

Three lines, no preamble:

```
Wrote <N> sections to <output_dir>/index.html
Verified: <list of section ids screenshotted clean>
Open: <Mac path if shipped, else file:// URL>
```

## Defaults to keep (don't ask, don't change)

- Body font: **18 px** floor. Refuse below; up to 20 px allowed.
- Heading max: 60 px hero. Down to 48 px h1 if hero feels too loud — never
  larger.
- Palette: slate-navy trust (indigo #4338CA primary, sky #0EA5E9 accent).
  Can swap the primary hue but only to another cool/neutral; never warm.
- Always at least 2 SVG diagrams. Even concept-only pages get pipeline +
  cycle.
- Verification: always. Skip only if user says "don't bother screenshotting".
- Sendmac: auto if topic is shippable.
- Frameworks: none. Pure HTML + CSS + vanilla JS. Google Fonts via `<link>`
  is fine. No Tailwind, no Bootstrap, no build step.

## Critical defects encoded (don't reintroduce)

1. **Dark-section inline `<code>` rule.** Already in `styles.css` —
   `background: rgba(99,102,241,0.18); color: #C7D2FE; border: 1px solid
   rgba(165,180,252,0.22)`. If you ever edit the CSS, do not remove this
   rule. Without it, inline code in `.dark-section` renders as invisible
   white boxes on slate-navy.

2. **Cycle/loop SVG node radius.** The cycle/loop diagram circles MUST be
   `r ≥ 50` so 7-character labels (`baseline`, `diagnose`, etc.) fit. The
   reference recipe uses `r=56`. v3 used `r=32` and labels overflowed —
   caught only by screenshot verification.

3. **No emojis.** The user does not want emojis anywhere unless they
   explicitly ask. The `cast-icon` slot in concept cards is the exception —
   it's an `aria-hidden` visual marker, fine to use a single character.

4. **No invented numbers.** Hero stat cards must reference real data. If no
   real number exists for the topic, drop the stat block.

## Anti-patterns

- Re-deriving the design system from scratch. Don't. Copy the assets.
- Generating before reading the section patterns. Always load
  `reference/section-patterns.md` before writing the article body.
- Skipping the screenshot loop because "the HTML looks right." It looked
  right in v3 too.
- Pitch tone. Default to "collaborator looking under the hood", not
  "investor evaluating a deal."
- Using Tailwind / Bootstrap / a build tool. The CSS is self-contained.
- Adding a hero stat block with invented "10×" / "95%" / "$X saved" claims.
- One-line follow-up screenshot iteration: when fixing a defect, actually
  re-run `screenshot.py` and re-Read the relevant PNG. Don't trust the fix.

## Where things live

| Path | Purpose |
|---|---|
| `assets/styles.css` | v4 design system, ~893 lines, copied verbatim |
| `assets/app.js` | Scroll-spy + smooth scroll + Escape, ~67 lines, copied verbatim |
| `assets/screenshot.py` | Generic Playwright verifier, takes `[html-path]` arg |
| `reference/design-system.md` | Token tables, breakpoints, light/dark guidance |
| `reference/section-patterns.md` | 18 HTML snippets with `{{PLACEHOLDERS}}` |
| `reference/svg-recipes.md` | 6 SVG diagram templates with viewBoxes |
| `reference/interaction.md` | Pointers to `app.js` behaviors |
| `reference/accessibility.md` | A11y checklist |
| `examples/v4-snippets.md` | Real v4 fragments for direct copy |
