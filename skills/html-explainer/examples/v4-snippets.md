# v4 reference snippets

These are **real, working** HTML fragments cut from the GantryForge v4 build.
They render at v4 quality with `assets/styles.css` and `assets/app.js`. Use
them as direct-copy references when the abstract patterns in
`reference/section-patterns.md` feel too thin.

The v4 source lives at `/home/drorifrah/drafts/gantryforge-system-walkthrough-v4/index.html`
if you need to inspect the full context.

---

## Hero (full real example)

```html
<section class="hero" aria-labelledby="hero-heading">
  <div class="hero-inner">
    <p class="eyebrow">System walkthrough &middot; Built on Google Gemini 3 Flash</p>
    <h1 id="hero-heading" class="hero-text">A system that evaluates robot video <span class="hero-accent">by putting every behavior on trial.</span></h1>
    <p class="hero-lede">
      This page is a guided tour of GantryForge's video behavioral evaluator &mdash; not a pitch.
      If you're reading it, you're being invited to look under the hood, push back on the design,
      and help fix the parts that are weakest. Each section explains a piece of the system, in
      plain language up front and with file paths and code symbols when you want to dig deeper.
    </p>
    <div class="hero-stats" role="group" aria-label="System summary">
      <div class="stat">
        <div class="stat-value">9</div>
        <div class="stat-label">Distinct courtroom roles per behavior<br/><span class="stat-sub">observers, judge, prosecution, witnesses, defense, jury, etc.</span></div>
      </div>
      <div class="stat">
        <div class="stat-value">8<span class="stat-unit">+</span></div>
        <div class="stat-label">Trial phases, plus appeals<br/><span class="stat-sub">repeated 5&times; in parallel, majority-aggregated</span></div>
      </div>
      <div class="stat">
        <div class="stat-value">6</div>
        <div class="stat-label">Synchronized camera angles<br/><span class="stat-sub">each weighted by mined reliability</span></div>
      </div>
    </div>
    <div class="hero-cta">
      <a class="btn btn-primary" href="#how-it-works">Walk through a verdict</a>
      <a class="btn btn-ghost" href="#sourcemap">Where the code lives</a>
      <a class="btn btn-ghost" href="#open">Where I'd value your input</a>
    </div>
  </div>
</section>
```

**Tone analysis:**
- `eyebrow` names the document type + the tech foundation, separated by a
  middle-dot.
- `hero-text` lead is concrete ("a system that evaluates robot video");
  accent finishes with the differentiator ("by putting every behavior on
  trial"). Not a slogan.
- `hero-lede` opens with "not a pitch" — sets collaborator tone explicitly.
- Three stats with real numbers + sublines that name the units.
- Three CTAs at three levels of commitment: primary action, code dive,
  feedback ask.

---

## Concept card (single example, from the cast grid)

```html
<details class="cast-card" data-role="observer">
  <summary>
    <span class="cast-icon" aria-hidden="true">&#x1F441;</span>
    <span class="cast-name">Blind Observers</span>
    <span class="cast-tag">Phase 0</span>
  </summary>
  <div class="cast-body">
    <p>Two parallel calls. The <strong>spatial analyst</strong> records positions, distances, orientations, and contacts with timestamps. The <strong>temporal analyst</strong> records sequences, speeds, and pauses. Neither is permitted to judge. Their output becomes the <em>stipulated facts</em> of the trial.</p>
  </div>
</details>
```

**Notes:**
- `data-role` is unused by CSS — it's a CSS hook for future per-role
  styling and a doc-readability aid.
- `cast-icon` is a unicode glyph (`&#x1F441;` = eye). `aria-hidden` because
  the icon is decorative; the name is the actual semantic.
- The card opens to reveal a paragraph; the paragraph uses `<strong>` for
  the canonical names and `<em>` for parenthetical definitions.

---

## Sample verdict card (real run output)

```html
<figure class="verdict-card">
  <div class="verdict-card__header">
    <div>
      <p class="verdict-card__eyebrow">final_report.json &middot; pickup_perfect</p>
      <p class="verdict-card__title">14 behaviors &middot; 14 PASS &middot; 14 min elapsed</p>
    </div>
    <span class="verdict-pill verdict-pill--pass">All PASS</span>
  </div>

  <table class="verdict-table">
    <caption class="visually-hidden">Per-behavior verdicts from final_report.json on pickup_perfect</caption>
    <thead>
      <tr><th>Behavior</th><th>Verdict</th><th>How it was decided</th><th>Time</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><code>B01_arm_reaches_toward_block</code></td>
        <td><span class="vd vd-pass">PASS</span></td>
        <td>Jury: <strong>7/7 PASS</strong> (threshold = 4)</td>
        <td>281.5s</td>
      </tr>
      <tr>
        <td><code>U01_no_arm_jitter</code></td>
        <td><span class="vd vd-pass">PASS</span></td>
        <td>Jury: <strong>7/7 PASS</strong> (threshold = 3) <span class="vd-note">stochastic profile</span></td>
        <td>221.1s</td>
      </tr>
      <tr>
        <td><code>U02_no_object_teleportation</code></td>
        <td><span class="vd vd-pass">PASS</span></td>
        <td><strong>Per-camera trial</strong> &mdash; 5 PASS across 5 cameras, early-terminated</td>
        <td>0s</td>
      </tr>
    </tbody>
  </table>
  <figcaption class="figcaption">
    Notice the three different verdict routes: <strong>full jury</strong> when the prosecution had a case, <strong>motion to dismiss</strong> when it didn't (judge wins by default), and <strong>per-camera</strong> when behaviors are angle-sensitive.
  </figcaption>
</figure>
```

**Notes:**
- Eyebrow is monospace (auto-applied by `.verdict-card__eyebrow`); use the
  source file path or run identifier.
- Cell-level chips (`<span class="vd vd-pass">`) are 4 px padding pills
  with 999 px radius — fine inside data tables.
- The figcaption explains *what to notice* about the table, not just what
  the table is.

---

## Diff card (real comparison, v2 vs v4 query)

```html
<div class="diff-grid">
  <article class="diff-card">
    <header class="diff-card__header diff-card__header--before">
      <span class="diff-version">U04_v2</span>
      <span class="diff-state">Baseline</span>
    </header>
    <div class="diff-card__body">
      <h4>How a collision was defined</h4>
      <p class="diff-quote">"Any arm link or gripper component visibly &gt;1cm inside another solid for 2+ consecutive frames."</p>
      <h4>Which camera was authoritative</h4>
      <p class="diff-quote">"IsometricView: <strong>best</strong> for detecting gripper-through-block clipping during lift. The 3D perspective shows penetration that side views may miss."</p>
      <h4>Failure mode</h4>
      <p class="diff-quote diff-quote--bad">
        On <code>block_aware_retract</code> the wrist's normal proximity to the block during lift was flagged as collision from <code>IsometricView</code>. A perspective overlap was scored FAIL.
      </p>
    </div>
  </article>

  <article class="diff-card">
    <header class="diff-card__header diff-card__header--after">
      <span class="diff-version">U04_v4</span>
      <span class="diff-state">After the lesson</span>
    </header>
    <div class="diff-card__body">
      <h4>How a collision was redefined</h4>
      <p class="diff-quote">"Geometry visible on <strong>both sides</strong> of the penetrated object, or clearly below a surface confirmed in <strong>SideView cameras</strong>." (The <em>emergence test</em>.)</p>
      <h4>Camera authority was inverted</h4>
      <p class="diff-quote">"SideView1/SideView2 are <strong>authoritative</strong>. IsometricView is <strong>prone to depth compression</strong> &mdash; objects at different Z-depths appear co-located."</p>
      <h4>Outcome</h4>
      <p class="diff-quote diff-quote--good">
        Wrist proximity is no longer flagged. Real collisions still caught via SideView confirmation + emergence test.
      </p>
    </div>
  </article>
</div>
```

**Notes:**
- Two parallel cards in a 2-col grid (collapses to 1-col below 900 px).
- Each card has its own header strip: amber for "before", green for "after".
- Inside each card, `<h4>` headings are uppercase tracking-out labels for
  aspects. Quotes from the source document are wrapped in `<p class="diff-quote">`
  with optional `--bad` / `--good` variants for failure / outcome.

---

## Story walkthrough (single step)

```html
<li>
  <span class="story-step">Phase 3 &middot; witness re-watch</span>
  <p><strong>Witness</strong> reaffirms or retracts. Here, the witness retracts: <em>"RETRACT. Upon re-watching, at 4.2s the pad is in contact with the block top &mdash; what I described as a gap was the next frame at 4.25s, after the arm had already begun lifting. I was confusing arm position with pad position."</em></p>
</li>
```

The CSS auto-numbers via `counter-increment`. The numbered indigo circle on
the left is drawn by `::before`. Don't add manual numbers.

---

## Open-problems card

```html
<article class="open-card">
  <h3>Jury composition</h3>
  <p>Seven jurors at temperatures <code>[0.0, 0.1, 0.2, 0.3, 0.1, 0.2, 0.0]</code>. The number, the spread, and the per-behavior threshold profile (hallucination-prone / stochastic / subtle / default) were tuned empirically. Is there a principled way to set these? Should we use higher-T jurors as "outsider" voices and weight them differently in the tiebreak?</p>
</article>
```

**Pattern:** card states *what is uncertain* and *what would resolve it*.
End with a question, not a statement. The amber left-border signals
"unresolved" visually.

---

## CTA (collaborator audience — v4 actual)

```html
<section id="cta" class="cta-section" aria-labelledby="h-cta">
  <h2 id="h-cta">If you have time to dig in&hellip;</h2>
  <p class="cta-lede">Pick any of the open problems above &mdash; or tell me what looks suspicious. I'd rather hear that something is wrong now than ship it and find out later. There's no commitment expected; this page is the front door.</p>
  <a class="btn btn-primary btn-large" href="mailto:dev1@con-techx.com?subject=GantryForge%20court-trial%20VLM%20%E2%80%94%20feedback">Send thoughts</a>
</section>
```

**Tone notes:**
- "If you have time to dig in…" not "Get started today!"
- "There's no commitment expected" — explicitly de-stakes the engagement.
- One CTA, one button. The mailto pre-fills the subject so the inbound
  message is filterable.

---

## Inline patterns

### Definition list — Toulmin-style structured argument

```html
<p>
  <strong>Toulmin</strong> (claim &middot; ground &middot; warrant &middot; qualifier &middot; rebuttal).
  Every <em>ground</em> must cite a specific camera and timestamp.
</p>
```

### Code-symbol callout

```html
<p>The branching lives in <code>_run_per_camera_trial</code> and <code>_run_multicam_escalation</code>.</p>
```

Inline code reads cleanly. Don't link to source unless the page has a
formal source map section.

### Hidden screen-reader-only data table after a chart

```html
<table class="visually-hidden">
  <caption>Three-verdict decision tree</caption>
  <thead><tr><th>Step</th><th>Question</th><th>If yes</th><th>If no</th></tr></thead>
  <tbody>
    <tr><td>Q1</td><td>Parent behavior FAIL/NULL?</td><td>NULL</td><td>Continue</td></tr>
    <tr><td>Q2</td><td>Relevant phase visible?</td><td>Continue</td><td>NULL</td></tr>
    <tr><td>Q3</td><td>Subject present?</td><td>Continue</td><td>NULL</td></tr>
    <tr><td>Q4</td><td>Event occurred?</td><td>PASS</td><td>FAIL</td></tr>
  </tbody>
</table>
```

The `.visually-hidden` class clips the element to 1 px but keeps it in the
accessibility tree. Screen readers announce it normally.

---

## Wide-screen + type-scale overrides (scoped `<style>`)

Real working block, lifted from a session where the user said "my screen
is 50″, you can take up at least half of it — and the smallest font
should be at least 20 px." Goes in the page's `<head>` **after** the
`<link>` to `assets/styles.css`, never as edits to `styles.css`. See
`reference/design-system.md` → *Wide-screen overrides* and *Type-scale
enlargement* for the full reasoning.

```html
<style>
  /* ---- Type scale: smallest CSS font (0.8125rem cast-tag) lands ≥20px; rest scales in proportion. ---- */
  html { font-size: 156%; }

  /* ---- Spread on wide screens: widen the page shell well past the stock 1440px island,
     but never narrower than the original 1440px. ---- */
  .site-header__inner,
  .hero-inner,
  .layout,
  .site-footer__inner { max-width: max(1440px, min(2880px, 94vw)); }

  /* Wider, fluid TOC rail so the bumped TOC text doesn't wrap to ribbons. Guarded ≥1100px so the
     stock mobile single-column rule (≤1024px) still wins (this <style> comes after styles.css). */
  @media (min-width: 1100px) {
    .layout { grid-template-columns: clamp(280px, 17vw, 360px) minmax(0, 1fr); }
  }

  /* Reading columns: let prose/callouts breathe wider, but not into eye-strain territory. */
  .prose,
  .callout,
  .hero-lede { max-width: min(82ch, 100%); }
  .figcaption { max-width: min(95ch, 100%); }

  /* Card grids: cards must be wide enough for the bumped body text. min(100%, …) keeps the
     "collapse to one column when narrow" behavior without any media query. */
  .hero-stats { grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); }
  .cast-grid  { grid-template-columns: repeat(auto-fit, minmax(min(100%, 600px), 1fr)); }
  .appeals-grid,
  .eng-grid,
  .grid-2     { grid-template-columns: repeat(auto-fit, minmax(min(100%, 480px), 1fr)); }
  .open-grid  { grid-template-columns: repeat(auto-fit, minmax(min(100%, 540px), 1fr)); }

  /* Keep the big SVG diagrams from ballooning to full ultra-wide width — cap + center. */
  .pipeline-figure svg, .tree-figure svg, .loop-figure svg,
  .dag-figure svg, .cameras-figure svg, .bars-figure svg {
    max-width: 1680px; display: block; margin: 0 auto;
  }

  /* ---- Scoped fix: the .src-table last column is styled for short metrics (nowrap/muted/small);
     when a specific table puts real prose there, let it wrap and read as body text. ---- */
  #hooks .src-table td:last-child { white-space: normal; color: inherit; font-size: 1rem; }
  #hooks .src-table td:nth-child(2) { white-space: normal; }
</style>
```

**Drop-in advice:**

- Pick a `min(N, 94vw)` cap that matches the audience. `2880 px` is
  good for 4K / 5K. Drop to `2400 px` if the page is prose-heavy
  (long-line readability beats fill).
- The `min(100%, N)` inside `minmax()` is what makes the grids
  collapse cleanly to one column on narrow viewports — don't strip
  it.
- The `#hooks` scoped fix at the bottom is per-section. Repeat the
  pattern for any other `.src-table` whose last column is prose, OR
  restructure the table so the last column stays a short metric.

Always re-verify with `screenshot-wide.py` (Step 5b in `SKILL.md`).

---

## What to NOT copy from v4

- Hero stat numbers (9, 8+, 6) — those are specific to the GantryForge
  system. For a different topic, either use real numbers from that topic
  or drop the stat strip entirely.
- The brand name "GantryForge" — replace with the actual project / system /
  topic name.
- The mailto address — replace with the actual feedback channel (or use a
  GitHub issues URL, or whatever the user prefers).
- "Court-Trial VLM" framing — that's the v4 topic. Your topic gets its own
  framing.

Everything else (CSS classes, structure, accessibility wrappers, prose
register) is portable and should stay.
