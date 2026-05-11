# Section patterns — copy-paste library

Each pattern has:
- a class hook (CSS class to use)
- when to include it
- a copy-pastable HTML snippet with `{{PLACEHOLDERS}}` you replace per-topic

**Pick 8–12 patterns per page, not all of them.** Always include hero (1),
big idea (3), engineering invariants (14), FAQ (17), CTA (18). The rest are
optional, choose based on whether the topic has the matching shape.

---

## Frame — every page starts with this

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{{PAGE_TITLE}}</title>
<meta name="description" content="{{ONE_SENTENCE_PAGE_DESCRIPTION}}" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap">
<link rel="stylesheet" href="assets/styles.css" />
</head>
<body>

<a href="#main" class="skip-link">Skip to main content</a>

<header role="banner" class="site-header">
  <div class="site-header__inner">
    <div class="brand">
      <span class="brand-mark" aria-hidden="true">
        <svg viewBox="0 0 32 32" width="28" height="28" focusable="false">
          <rect x="2" y="2" width="28" height="28" rx="6" fill="#4338CA" />
          <path d="M9 22 L9 10 L16 14 L23 10 L23 22" stroke="#fff" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="16" cy="22" r="1.6" fill="#fff" />
        </svg>
      </span>
      <span class="brand-text">{{BRAND_NAME}}</span>
      <span class="brand-divider" aria-hidden="true">/</span>
      <span class="brand-product">{{PRODUCT_OR_TOPIC}}</span>
    </div>
    <nav aria-label="Primary navigation" class="primary-nav">
      <a href="#{{KEY_SECTION_1_ID}}">{{KEY_SECTION_1_LABEL}}</a>
      <a href="#{{KEY_SECTION_2_ID}}">{{KEY_SECTION_2_LABEL}}</a>
      <a href="#{{KEY_SECTION_3_ID}}">{{KEY_SECTION_3_LABEL}}</a>
      <a href="#{{KEY_SECTION_4_ID}}">{{KEY_SECTION_4_LABEL}}</a>
    </nav>
  </div>
</header>

<main id="main">

  <!-- HERO goes here -->

  <div class="layout">
    <aside class="page-toc-wrap" aria-label="Table of contents wrapper">
      <nav aria-label="Page sections" id="page-toc" class="page-toc">
        <p class="toc-title">On this page</p>
        <ol>
          <li><a href="#{{SECTION_1_ID}}">{{SECTION_1_LABEL}}</a></li>
          <li><a href="#{{SECTION_2_ID}}">{{SECTION_2_LABEL}}</a></li>
          <!-- one <li> per section in the same order as sections appear below -->
        </ol>
      </nav>
    </aside>

    <article class="content">
      <!-- all numbered sections go here, in TOC order -->
    </article>
  </div>
</main>

<footer role="contentinfo" class="site-footer">
  <div class="site-footer__inner">
    <p>&copy; {{YEAR}} {{BRAND_NAME}} &mdash; {{ONE_LINE_FOOTER}}.</p>
    <p class="footer-muted">{{OPTIONAL_FOOTER_MUTED_LINE}}</p>
  </div>
</footer>

<script src="assets/app.js" defer></script>
</body>
</html>
```

**TOC ordering rule.** The `<ol>` inside `#page-toc` must list section ids
in the same order the `<section>` elements appear in `<article>`. Mismatches
produce a TOC where scrolling the page activates the wrong link.

---

## 1. Hero

**Class:** `.hero` (full-bleed gradient section, sits OUTSIDE `.layout`)
**When to include:** Always.
**Copy guidance:** Headline is one bold thesis with an accented clause. Lede
explains who the page is for and what they get. Stats are optional — only
include if the numbers are real.

```html
<section class="hero" aria-labelledby="hero-heading">
  <div class="hero-inner">
    <p class="eyebrow">{{EYEBROW_TAG}} &middot; {{SUB_EYEBROW}}</p>
    <h1 id="hero-heading" class="hero-text">
      {{HEADLINE_LEAD}} <span class="hero-accent">{{HEADLINE_ACCENT}}</span>
    </h1>
    <p class="hero-lede">
      {{LEDE_2_TO_4_SENTENCES_EXPLAINING_WHO_AND_WHAT}}
    </p>

    <!-- OPTIONAL: stat strip. Drop if no real numbers. -->
    <div class="hero-stats" role="group" aria-label="System summary">
      <div class="stat">
        <div class="stat-value">{{N1}}</div>
        <div class="stat-label">{{LABEL_1}}<br/><span class="stat-sub">{{SUB_1}}</span></div>
      </div>
      <div class="stat">
        <div class="stat-value">{{N2}}<span class="stat-unit">{{UNIT_2}}</span></div>
        <div class="stat-label">{{LABEL_2}}<br/><span class="stat-sub">{{SUB_2}}</span></div>
      </div>
      <div class="stat">
        <div class="stat-value">{{N3}}</div>
        <div class="stat-label">{{LABEL_3}}<br/><span class="stat-sub">{{SUB_3}}</span></div>
      </div>
    </div>

    <div class="hero-cta">
      <a class="btn btn-primary" href="#{{PRIMARY_DEST}}">{{PRIMARY_CTA}}</a>
      <a class="btn btn-ghost" href="#{{SECONDARY_DEST}}">{{SECONDARY_CTA}}</a>
      <a class="btn btn-ghost" href="#{{TERTIARY_DEST}}">{{TERTIARY_CTA}}</a>
    </div>
  </div>
</section>
```

---

## 2. Problem framing

**Class:** plain `<section>` + `.callout`
**When to include:** When the system solves a named, specific problem.
**Tone:** Concrete. Name failure modes, not generalities.

```html
<section id="problem" aria-labelledby="h-problem">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-problem">{{H2_PROBLEM_STATEMENT}}</h2>
  <div class="prose">
    <p>{{PARAGRAPH_1_NAMING_THE_PROBLEM}}</p>
    <p>{{PARAGRAPH_2_CONCRETE_EXAMPLES}}</p>
    <div class="callout">
      <p class="callout-title">{{THESIS_TITLE}}</p>
      <p>{{ONE_SENTENCE_THESIS}}</p>
    </div>
  </div>
</section>
```

Callout variants: `.callout-warn` (amber-tinted), `.callout-ok` (green-tinted).

---

## 3. Big idea

**Class:** plain `<section>` + `.bullet-list`
**When to include:** Always.
**Copy guidance:** Lead with the one-line core idea. Then an ordered list
expanding it into 6–10 steps or moves.

```html
<section id="big-idea" aria-labelledby="h-bigidea">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-bigidea">{{H2_ONE_LINE_THESIS}}</h2>
  <div class="prose">
    <p>{{INTRO_PARAGRAPH}}</p>
    <ol class="bullet-list">
      <li>{{POINT_1_WITH_STRONG_OR_EM_FOR_KEY_TERM}}</li>
      <li>{{POINT_2}}</li>
      <li>{{POINT_3}}</li>
      <!-- 6-10 points total -->
    </ol>
    <p>{{OPTIONAL_CLOSING_PARAGRAPH}}</p>
  </div>
</section>
```

Use `<strong>` for the canonical name of each component; `<em>` for
parenthetical definitions; `<code>` for file names or symbols.

---

## 4. Concept cards grid

**Class:** `.cast-grid` containing `<details class="cast-card">` per role
**When to include:** When the system has ≥4 named roles, components, or
sub-systems worth their own card.
**Cards are `<details>`** so they expand on click — keeps the grid compact
and lets readers drill in.

```html
<section id="{{SECTION_ID}}" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_NAMING_THE_CAST}}</h2>
  <div class="prose">
    <p>{{INTRO_PARAGRAPH_EXPLAINING_CARDS_OPEN_FOR_DETAIL}}</p>
  </div>

  <div class="cast-grid">
    <details class="cast-card" data-role="{{ROLE_KEY_1}}">
      <summary>
        <span class="cast-icon" aria-hidden="true">{{ICON_CHAR_OR_SVG}}</span>
        <span class="cast-name">{{ROLE_NAME_1}}</span>
        <span class="cast-tag">{{PHASE_OR_TAG}}</span>
      </summary>
      <div class="cast-body">
        <p>{{ROLE_DESCRIPTION_2_TO_4_SENTENCES}}</p>
      </div>
    </details>

    <!-- repeat for each role; aim for 4-9 cards -->
  </div>
</section>
```

`{{ICON_CHAR_OR_SVG}}` can be a single emoji-equivalent character (the
v4 source uses unicode glyphs like `&#x1F441;` for an eye). Pure plain
character is fine — the icon slot is decorative.

---

## 5. Pipeline timeline (dark section)

**Class:** `class="dark-section"` on `<section>` + `.pipeline-figure` + inline SVG
**When to include:** When the system has named phases or stages worth
showing as a horizontal track.
**SVG recipe:** `reference/svg-recipes.md` §1.

```html
<section id="{{SECTION_ID}}" class="dark-section" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_TWO_STAGES_OR_PIPELINE_SHAPE}}</h2>
  <div class="prose">
    <p><strong>Stage&nbsp;1 &mdash; {{STAGE_1_NAME}}.</strong> {{STAGE_1_DESCRIPTION}}</p>
    <p><strong>Stage&nbsp;2 &mdash; {{STAGE_2_NAME}}.</strong> {{STAGE_2_DESCRIPTION}}</p>
  </div>

  <figure class="pipeline-figure">
    <!-- SVG: see svg-recipes.md §1. viewBox 0 0 1200 460. -->
  </figure>

  <details class="disclosure">
    <summary>
      <span>{{DEEP_DIVE_LABEL}}</span>
      <span class="disclosure-icon" aria-hidden="true">+</span>
    </summary>
    <div class="disclosure-body">
      <ol class="phase-list">
        <li><strong>{{PHASE_1_NAME}} &mdash;</strong> {{PHASE_1_DETAIL}}</li>
        <!-- one li per phase -->
      </ol>
    </div>
  </details>
</section>
```

---

## 6. Sample data table

**Class:** `.verdict-card` wrapping `.verdict-card__header` + `.verdict-table`
**When to include:** When there is real run output / sample data to show.
**Don't invent numbers.** If you don't have real data, skip this pattern.

```html
<section id="{{SECTION_ID}}" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_WHAT_THE_OUTPUT_LOOKS_LIKE}}</h2>
  <div class="prose">
    <p>{{INTRO_LINKING_TO_SOURCE_FILE_IN_CODE}}</p>
  </div>

  <figure class="verdict-card">
    <div class="verdict-card__header">
      <div>
        <p class="verdict-card__eyebrow">{{FILENAME_OR_CONTEXT}}</p>
        <p class="verdict-card__title">{{HEADLINE_SUMMARY_E_G_14_BEHAVIORS_ALL_PASS}}</p>
      </div>
      <span class="verdict-pill verdict-pill--pass">{{STATUS_PILL}}</span>
    </div>

    <table class="verdict-table">
      <caption class="visually-hidden">{{TABLE_CAPTION_FOR_SCREEN_READERS}}</caption>
      <thead>
        <tr><th>{{COL_1}}</th><th>{{COL_2}}</th><th>{{COL_3}}</th><th>{{COL_4}}</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><code>{{ROW_KEY}}</code></td>
          <td><span class="vd vd-pass">PASS</span></td>
          <td>{{HOW_IT_WAS_DECIDED}}</td>
          <td>{{TIME_OR_METRIC}}</td>
        </tr>
        <!-- one row per record. .vd-fail and .vd-null are the other variants. -->
      </tbody>
    </table>
    <figcaption class="figcaption">{{CAPTION_EXPLAINING_THE_TABLE}}</figcaption>
  </figure>

  <!-- Optional follow-up disclosure -->
  <details class="disclosure">
    <summary><span>{{FOLLOWUP_LABEL}}</span><span class="disclosure-icon" aria-hidden="true">+</span></summary>
    <div class="disclosure-body">
      <p>{{FOLLOWUP_BODY}}</p>
    </div>
  </details>
</section>
```

Verdict-pill variants: `.verdict-pill--pass` (green), `.verdict-pill--fail`
(red). The cell-level chips are `.vd .vd-pass`, `.vd .vd-fail`, `.vd .vd-null`.

---

## 7. Story walkthrough

**Class:** `class="alt-bg"` on `<section>` + `.story-list`
**When to include:** When a sequenced narrative ("then this happens, then
that…") clarifies a process the reader has to follow.

```html
<section id="{{SECTION_ID}}" class="alt-bg" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_NARRATIVE_FRAMING}}</h2>
  <div class="prose">
    <p>{{INTRO_SETTING_UP_THE_NARRATIVE}}</p>
  </div>

  <ol class="story-list">
    <li>
      <span class="story-step">{{STEP_LABEL_1}}</span>
      <p><strong>{{ACTOR_1}}</strong> {{ACTION_1}}: <em>"{{QUOTE_OR_OBSERVATION}}"</em></p>
    </li>
    <!-- one <li> per step; 8-12 steps reads cleanly -->
  </ol>

  <div class="prose">
    <div class="callout">
      <p class="callout-title">{{WHY_THIS_MATTERS_TITLE}}</p>
      <p>{{ONE_PARAGRAPH_TAKEAWAY}}</p>
    </div>
  </div>
</section>
```

The `<li>` elements auto-number via CSS counters (the indigo circle on the
left). Don't add manual numbers.

---

## 8. Decision tree

**Class:** `.tree-figure` containing inline SVG + a hidden a11y `<table>`
**When to include:** When there are sequential yes/no gates leading to
distinct terminal verdicts.
**SVG recipe:** `reference/svg-recipes.md` §2.

```html
<section id="{{SECTION_ID}}" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_NAMING_THE_VERDICTS}}</h2>
  <div class="prose">
    <p>{{INTRO_EXPLAINING_GATE_LOGIC}}</p>
  </div>

  <figure class="tree-figure">
    <!-- SVG: see svg-recipes.md §2. viewBox 0 0 1100 560. -->
    <figcaption class="figcaption">{{CAPTION_EXPLAINING_THE_GATES}}</figcaption>
  </figure>

  <table class="visually-hidden">
    <caption>{{TABLE_CAPTION}}</caption>
    <thead><tr><th>Step</th><th>Question</th><th>If yes</th><th>If no</th></tr></thead>
    <tbody>
      <tr><td>Q1</td><td>{{Q1}}</td><td>{{Q1_YES}}</td><td>{{Q1_NO}}</td></tr>
      <!-- one row per gate -->
    </tbody>
  </table>
</section>
```

The visually-hidden table is the screen-reader equivalent of the SVG —
required for accessibility.

---

## 9. Dependency DAG

**Class:** `.dag-figure` containing inline SVG
**When to include:** When components form a parent/child dependency graph,
with a "parent fails → children skip" cascade.
**SVG recipe:** `reference/svg-recipes.md` §5.

```html
<section id="{{SECTION_ID}}" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_DAG_HEADLINE}}</h2>
  <div class="prose">
    <p>{{INTRO_EXPLAINING_DEPENDS_ON_RELATIONSHIPS_AND_CASCADE}}</p>
  </div>

  <figure class="dag-figure">
    <!-- SVG: see svg-recipes.md §5. viewBox 0 0 1200 540. -->
    <figcaption class="figcaption">{{CAPTION_EXPLAINING_CASCADE_AND_CODE_SYMBOL}}</figcaption>
  </figure>
</section>
```

---

## 10. Multi-input layout

**Class:** `.cameras-figure` containing inline SVG
**When to include:** When multiple inputs (cameras, sensors, sources)
converge on a single system, especially with per-input reliability or role.
**SVG recipe:** `reference/svg-recipes.md` §3.

```html
<section id="{{SECTION_ID}}" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_MULTI_INPUT_HEADLINE}}</h2>
  <div class="prose">
    <p>{{INTRO_NAMING_INPUTS_AND_THEIR_ROLES}}</p>
    <p>{{INTRO_PARAGRAPH_2_PROCESS_OR_WEIGHTING}}</p>
  </div>

  <figure class="cameras-figure">
    <!-- SVG: see svg-recipes.md §3. viewBox 0 0 1100 540. -->
    <figcaption class="figcaption">{{CAPTION_COLOR_KEY}}</figcaption>
  </figure>
</section>
```

---

## 11. Feature cards grid

**Class:** `.appeals-grid` containing `.appeal-card` articles
**When to include:** When the system has 3–6 named auxiliary features
(safety nets, fallbacks, escape hatches) worth grouping.

```html
<section id="{{SECTION_ID}}" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_FEATURES_HEADLINE}}</h2>
  <div class="prose">
    <p>{{INTRO}}</p>
  </div>

  <div class="appeals-grid">
    <article class="appeal-card">
      <h3>{{FEATURE_NAME_1}}</h3>
      <p>{{FEATURE_DESCRIPTION_1}}</p>
    </article>
    <article class="appeal-card">
      <h3>{{FEATURE_NAME_2}}</h3>
      <p>{{FEATURE_DESCRIPTION_2}}</p>
      <details class="disclosure">
        <summary><span>{{DEEP_DIVE_LABEL}}</span><span class="disclosure-icon" aria-hidden="true">+</span></summary>
        <div class="disclosure-body">
          <ul class="bullet-list">
            <li>{{NESTED_DETAIL}}</li>
          </ul>
        </div>
      </details>
    </article>
    <!-- 3-6 cards -->
  </div>
</section>
```

---

## 12. Cycle / feedback loop

**Class:** `class="alt-bg"` on `<section>` + `.loop-figure`
**When to include:** When the system has a feedback loop (especially
read-from-knowledge / write-to-knowledge pattern, or a multi-step optimizer).
**SVG recipe:** `reference/svg-recipes.md` §4.
**Critical:** circles MUST be `r ≥ 50`. v3 used `r=32` and labels overflowed.

```html
<section id="{{SECTION_ID}}" class="alt-bg" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_LOOP_HEADLINE}}</h2>
  <div class="prose">
    <p>{{INTRO_NAMING_THE_NODES_OF_THE_LOOP}}</p>
    <p>{{INTRO_PARAGRAPH_2_DECISION_RULE_IF_ANY}}</p>
  </div>

  <figure class="loop-figure">
    <!-- SVG: see svg-recipes.md §4. viewBox 0 0 1100 520. r=56 on outer nodes. -->
    <figcaption class="figcaption">{{CAPTION_EXPLAINING_READ_WRITE_RELATIONSHIPS}}</figcaption>
  </figure>

  <div class="prose">
    <div class="callout callout-ok">
      <p class="callout-title">{{DECISION_RULE_TITLE}}</p>
      <p>{{DECISION_RULE_BODY}}</p>
    </div>
  </div>
</section>
```

---

## 13. Side-by-side diff

**Class:** `.diff-grid` with two `.diff-card` articles (before / after)
**When to include:** When comparing v1 vs v2, current vs proposed, or any
two-state evolution worth showing in parallel.

```html
<section id="{{SECTION_ID}}" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_EVOLUTION_HEADLINE}}</h2>
  <div class="prose">
    <p>{{INTRO_EXPLAINING_THE_VERSION_DELTA}}</p>
  </div>

  <div class="diff-grid">
    <article class="diff-card">
      <header class="diff-card__header diff-card__header--before">
        <span class="diff-version">{{VERSION_LABEL_BEFORE}}</span>
        <span class="diff-state">{{STATE_LABEL_BEFORE}}</span>
      </header>
      <div class="diff-card__body">
        <h4>{{ASPECT_1}}</h4>
        <p class="diff-quote">"{{QUOTE_OR_DESCRIPTION}}"</p>
        <h4>{{ASPECT_2}}</h4>
        <p class="diff-quote">{{ASPECT_2_BEFORE_DETAIL}}</p>
        <h4>{{FAILURE_HEADING}}</h4>
        <p class="diff-quote diff-quote--bad">{{FAILURE_DESCRIPTION}}</p>
      </div>
    </article>

    <article class="diff-card">
      <header class="diff-card__header diff-card__header--after">
        <span class="diff-version">{{VERSION_LABEL_AFTER}}</span>
        <span class="diff-state">{{STATE_LABEL_AFTER}}</span>
      </header>
      <div class="diff-card__body">
        <h4>{{ASPECT_1}}</h4>
        <p class="diff-quote">"{{NEW_QUOTE_OR_DESCRIPTION}}"</p>
        <h4>{{ASPECT_2}}</h4>
        <p class="diff-quote">{{ASPECT_2_AFTER_DETAIL}}</p>
        <h4>{{OUTCOME_HEADING}}</h4>
        <p class="diff-quote diff-quote--good">{{OUTCOME_DESCRIPTION}}</p>
      </div>
    </article>
  </div>

  <div class="prose">
    <div class="callout callout-ok">
      <p class="callout-title">{{LESSON_TITLE}}</p>
      <p>{{LESSON_BODY}}</p>
    </div>
  </div>
</section>
```

Stacked variant available — the grid collapses to 1 column at < 900 px.

---

## 14. Engineering invariants grid

**Class:** `.eng-grid` containing `.eng-card` articles
**When to include:** Always (or use a topic-appropriate equivalent like
"rules of the system" or "principles we hold steady").

```html
<section id="{{SECTION_ID}}" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_INVARIANTS_HEADLINE}}</h2>
  <div class="prose">
    <p>{{INTRO_FRAMING_WHY_THESE_INVARIANTS_MATTER}}</p>
  </div>

  <div class="eng-grid">
    <article class="eng-card">
      <h3>{{INVARIANT_1_NAME}}</h3>
      <p>{{INVARIANT_1_BODY_REFERENCING_CODE_OR_CONFIG}}</p>
    </article>
    <!-- 5-7 cards -->
  </div>

  <details class="disclosure">
    <summary><span>{{DEEP_TOUR_LABEL}}</span><span class="disclosure-icon" aria-hidden="true">+</span></summary>
    <div class="disclosure-body">
      <ul class="bullet-list">
        <li>{{DEEPER_DETAIL_1}}</li>
      </ul>
    </div>
  </details>
</section>
```

---

## 15. Source map

**Class:** `.src-table-wrap` containing `.src-table`
**When to include:** When the explainer references a codebase the reader
might dig into.

```html
<section id="{{SECTION_ID}}" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_WHERE_THE_CODE_LIVES}}</h2>
  <div class="prose">
    <p>{{INTRO_READING_ORDER_HINT}}</p>
  </div>
  <div class="src-table-wrap">
    <table class="src-table">
      <thead>
        <tr><th>Path</th><th>What it does</th><th>Size</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><code>{{PATH}}</code></td>
          <td>{{ONE_LINE_DESCRIPTION_OF_FILE}}</td>
          <td>{{LINE_COUNT_OR_BYTES}}</td>
        </tr>
        <!-- one row per load-bearing file -->
      </tbody>
    </table>
  </div>
</section>
```

---

## 16. Open problems

**Class:** `class="alt-bg"` on `<section>` + `.open-grid` + `.open-card`
**When to include:** When you want to invite outside input on the
under-decided parts of the system.

```html
<section id="{{SECTION_ID}}" class="alt-bg" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_OPEN_PROBLEMS}}</h2>
  <div class="prose">
    <p>{{INTRO_INVITING_PUSHBACK}}</p>
  </div>

  <div class="open-grid">
    <article class="open-card">
      <h3>{{PROBLEM_TITLE_1}}</h3>
      <p>{{PROBLEM_DESCRIPTION_INCLUDING_WHY_ITS_HARD}}</p>
    </article>
    <!-- 5-8 cards -->
  </div>
</section>
```

The amber left-border on `.open-card` signals "unresolved" without text.

---

## 17. FAQ disclosures

**Class:** list of `<details class="disclosure">`
**When to include:** When the audience will ask predictable clarifying
questions (always for collaborator-audience pages).

```html
<section id="{{SECTION_ID}}" aria-labelledby="h-{{SECTION_ID}}">
  <p class="section-eyebrow">{{EYEBROW}}</p>
  <h2 id="h-{{SECTION_ID}}">{{H2_THINGS_TO_KNOW}}</h2>

  <details class="disclosure">
    <summary><span>{{Q_1}}</span><span class="disclosure-icon" aria-hidden="true">+</span></summary>
    <div class="disclosure-body">
      <p>{{A_1}}</p>
    </div>
  </details>

  <details class="disclosure">
    <summary><span>{{Q_2}}</span><span class="disclosure-icon" aria-hidden="true">+</span></summary>
    <div class="disclosure-body">
      <p>{{A_2}}</p>
    </div>
  </details>

  <!-- 6-10 Qs is the sweet spot -->
</section>
```

---

## 18. CTA / engagement

**Class:** `class="cta-section"` (indigo gradient, white text)
**When to include:** Always last. Tone is engagement-oriented for
collaborator pages ("send thoughts" / "where to dig in"), only sales-y if
the user requested an investor frame.

```html
<section id="cta" class="cta-section" aria-labelledby="h-cta">
  <h2 id="h-cta">{{CTA_HEADLINE}}</h2>
  <p class="cta-lede">{{CTA_LEDE_TELLING_READER_WHAT_TO_DO_NEXT}}</p>
  <a class="btn btn-primary btn-large" href="{{CTA_HREF_E_G_MAILTO_OR_ANCHOR}}">{{CTA_BUTTON_LABEL}}</a>
</section>
```

For collaborator-audience pages, use `mailto:` with a pre-filled subject:
```html
href="mailto:dev1@con-techx.com?subject=Feedback%20on%20{{TOPIC}}"
```

For investor-audience pages (only on explicit request), use a stronger
imperative ("Schedule a demo", "See the data") and a strict-color CTA.

---

## Inline patterns inside any section

### Callouts (3 variants)

```html
<div class="callout">                    <!-- indigo, neutral attention -->
  <p class="callout-title">{{TITLE}}</p>
  <p>{{BODY}}</p>
</div>

<div class="callout callout-warn">       <!-- amber, caution -->
  <p class="callout-title">{{TITLE}}</p>
  <p>{{BODY}}</p>
</div>

<div class="callout callout-ok">         <!-- green, decision rule / confirmation -->
  <p class="callout-title">{{TITLE}}</p>
  <p>{{BODY}}</p>
</div>
```

### Bullet list (compact)

```html
<ul class="bullet-list">
  <li>{{POINT_WITH_STRONG_LEAD}}</li>
</ul>
```

### Inline code

```html
<code>{{SYMBOL_OR_FILENAME}}</code>
```

Auto-styled neutral-100 background; inside `.dark-section` auto-restyled to
tinted indigo. Don't override.

### Verdict chip (PASS / FAIL / NULL)

```html
<span class="vd vd-pass">PASS</span>
<span class="vd vd-fail">FAIL</span>
<span class="vd vd-null">NULL</span>
```

Outside table cells, these chips work anywhere — useful for status badges
in prose.
