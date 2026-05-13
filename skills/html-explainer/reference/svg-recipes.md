# SVG diagram recipes

Six named diagrams used by the section patterns. Each one:
- has a fixed `viewBox` you should NOT change without rechecking labels
- declares the required `<title>` and `<desc>` for screen readers
- color-codes with the palette tokens (don't introduce new hues)

**Every SVG also needs an a11y wrapper:**
```html
<svg
  role="img"
  aria-labelledby="{{ID}}-title {{ID}}-desc"
  focusable="false"
  viewBox="0 0 W H"
  class="{{class-name}}-svg"
>
  <title id="{{ID}}-title">{{PLAIN_TITLE}}</title>
  <desc id="{{ID}}-desc">{{2_TO_4_SENTENCE_DESCRIPTION}}</desc>
  ...
</svg>
```

And for charts, a screen-reader-only data table immediately after:
```html
<table class="visually-hidden">
  <caption>{{TABLE_CAPTION}}</caption>
  <thead><tr><th>Row</th><th>Cols…</th></tr></thead>
  <tbody>...</tbody>
</table>
```

---

## 1. Pipeline timeline

**Used in:** Section pattern §5 (Pipeline timeline, dark section)
**viewBox:** `0 0 1200 460`
**Top half:** Stage 1 box → arrow → Stage 2 box → arrow → Report box
**Bottom half:** Horizontal track at y=280 with 7–9 phase nodes (`circle r=14`)
**Phase node colors:**
- `#4338CA` (indigo) — baseline / setup
- `#D97706` (amber) — adversarial / contested
- `#64748B` (slate) — gates / dismissals
- `#0EA5E9` (sky) — defense / resolution
- `#A78BFA` (violet) — closings / synthesis
- `#16A34A` (green) — verdict / output

```html
<figure class="pipeline-figure">
  <svg
    role="img"
    aria-labelledby="pipeline-title pipeline-desc"
    focusable="false"
    viewBox="0 0 1200 460"
    class="pipeline-svg"
  >
    <title id="pipeline-title">{{PLAIN_TITLE}}</title>
    <desc id="pipeline-desc">{{DESCRIPTION}}</desc>

    <!-- Stage 1 box -->
    <rect x="20" y="40" width="340" height="100" rx="8" fill="#1F2A44" stroke="#334155" />
    <text x="40" y="72" fill="#F1F5F9" font-size="22" font-weight="700">Stage 1 &middot; {{STAGE_1_NAME}}</text>
    <text x="40" y="100" fill="#94A3B8" font-size="16">{{STAGE_1_LINE_1}}</text>
    <text x="40" y="124" fill="#94A3B8" font-size="16">{{STAGE_1_LINE_2}}</text>

    <!-- Arrow 1 -->
    <line x1="360" y1="90" x2="430" y2="90" stroke="#64748B" stroke-width="2"/>
    <polygon points="430,84 442,90 430,96" fill="#64748B"/>

    <!-- Stage 2 box -->
    <rect x="440" y="40" width="500" height="100" rx="8" fill="#1F2A44" stroke="#334155" />
    <text x="460" y="72" fill="#F1F5F9" font-size="22" font-weight="700">Stage 2 &middot; {{STAGE_2_NAME}}</text>
    <text x="460" y="100" fill="#94A3B8" font-size="16">{{STAGE_2_LINE_1}}</text>
    <text x="460" y="124" fill="#94A3B8" font-size="16">{{STAGE_2_LINE_2}}</text>

    <!-- Arrow 2 -->
    <line x1="940" y1="90" x2="1010" y2="90" stroke="#64748B" stroke-width="2"/>
    <polygon points="1010,84 1022,90 1010,96" fill="#64748B"/>

    <!-- Report / Output box -->
    <rect x="1020" y="40" width="160" height="100" rx="8" fill="#0EA5E9" stroke="#0284C7" />
    <text x="1040" y="72" fill="#0F172A" font-size="20" font-weight="700">{{OUTPUT_LABEL}}</text>
    <text x="1040" y="100" fill="#0F172A" font-size="16">{{OUTPUT_LINE_1}}</text>
    <text x="1040" y="124" fill="#0F172A" font-size="16">{{OUTPUT_LINE_2}}</text>

    <!-- Phase track header -->
    <text x="20" y="200" fill="#F1F5F9" font-size="20" font-weight="700">{{TRACK_LABEL}}</text>

    <!-- Track line -->
    <line x1="40" y1="280" x2="1160" y2="280" stroke="#475569" stroke-width="3"/>

    <!-- One phase node group per phase. Spacing ~135px between nodes for 8 nodes.
         For 7 nodes, spacing ~170px. Adjust translate(...) accordingly. -->
    <g class="phase-node" transform="translate(60,280)">
      <circle r="14" fill="#4338CA" stroke="#A5B4FC" stroke-width="2"/>
      <text y="-26" text-anchor="middle" fill="#F1F5F9" font-size="16" font-weight="600">{{PHASE_ID}}</text>
      <text y="46" text-anchor="middle" fill="#CBD5E1" font-size="14">{{PHASE_NAME_L1}}</text>
      <text y="64" text-anchor="middle" fill="#CBD5E1" font-size="14">{{PHASE_NAME_L2}}</text>
    </g>
    <!-- repeat per phase, varying transform translate(x,280) and the fill color -->

    <!-- Trailing caption inside SVG -->
    <text x="600" y="430" text-anchor="middle" fill="#94A3B8" font-size="16" font-style="italic">
      {{TRAILING_NOTE}}
    </text>
  </svg>
  <figcaption class="figcaption">{{CAPTION_BELOW_SVG}}</figcaption>
</figure>
```

**Parametrization checklist:**
- Phase node count → space evenly between x=60 and x=1140
- Phase node fill → pick from the 6 color slots above
- Phase node label below circle → max 2 lines, ~12 chars each
- If you need 10+ phases, increase viewBox width or switch to a vertical
  variant.

---

## 2. Decision tree

**Used in:** Section pattern §8 (Decision tree)
**viewBox:** `0 0 1100 560`
**Layout:** START pill on top center → 3 to 4 question rectangles stacked
vertically → each Q branches to a terminal pill (PASS / FAIL / NULL).
**Terminal pill colors:**
- PASS — `fill="#DCFCE7"`, `stroke="#16A34A"`, text `#166534`
- FAIL — `fill="#FEE2E2"`, `stroke="#DC2626"`, text `#991B1B`
- NULL — `fill="#FEF3C7"`, `stroke="#D97706"`, text `#92400E`

```html
<figure class="tree-figure">
  <svg
    role="img"
    aria-labelledby="tree-title tree-desc"
    focusable="false"
    viewBox="0 0 1100 560"
    class="tree-svg"
  >
    <title id="tree-title">{{TITLE}}</title>
    <desc id="tree-desc">{{DESCRIPTION}}</desc>

    <!-- Start pill -->
    <g transform="translate(540,30)">
      <rect x="-80" y="0" width="160" height="48" rx="24" fill="#4338CA"/>
      <text x="0" y="30" text-anchor="middle" fill="#fff" font-size="20" font-weight="700">START</text>
    </g>

    <!-- Q1 box at y=120, then Q2 at y=220, Q3 at y=320, Q4 at y=420 -->
    <g transform="translate(540,120)">
      <rect x="-180" y="0" width="360" height="64" rx="8" fill="#fff" stroke="#CBD5E1" stroke-width="2"/>
      <text x="0" y="28" text-anchor="middle" fill="#0F172A" font-size="18" font-weight="700">Q1. {{Q1_QUESTION}}</text>
      <text x="0" y="52" text-anchor="middle" fill="#475569" font-size="16">{{Q1_TAG}}</text>
    </g>

    <!-- Connector from START to Q1 -->
    <line x1="540" y1="54" x2="540" y2="120" stroke="#94A3B8" stroke-width="2"/>

    <!-- Q1 yes-branch to NULL/terminal on the right -->
    <line x1="720" y1="152" x2="900" y2="152" stroke="#94A3B8" stroke-width="2"/>
    <polygon points="900,146 912,152 900,158" fill="#94A3B8"/>
    <text x="780" y="142" text-anchor="middle" fill="#475569" font-size="16" font-weight="600">yes</text>
    <g transform="translate(950,128)">
      <rect x="0" y="0" width="120" height="48" rx="8" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>
      <text x="60" y="30" text-anchor="middle" fill="#92400E" font-size="20" font-weight="700">NULL</text>
    </g>

    <!-- Q1 no-branch continues to Q2 -->
    <line x1="540" y1="184" x2="540" y2="220" stroke="#94A3B8" stroke-width="2"/>
    <text x="555" y="206" fill="#475569" font-size="16" font-weight="600">no</text>

    <!-- Q2 box, Q3 box, etc. follow the same pattern at y=220, y=320, y=420.
         For each, draw the "rejected" branch to a terminal pill on the right
         and the "continue" line down to the next Q. -->

    <!-- Final Q's two-branch terminal: PASS on the left, FAIL on the right -->
    <line x1="360" y1="452" x2="200" y2="452" stroke="#94A3B8" stroke-width="2"/>
    <polygon points="200,446 188,452 200,458" fill="#94A3B8"/>
    <text x="280" y="442" text-anchor="middle" fill="#475569" font-size="16" font-weight="600">yes</text>
    <g transform="translate(60,428)">
      <rect x="0" y="0" width="140" height="48" rx="8" fill="#DCFCE7" stroke="#16A34A" stroke-width="2"/>
      <text x="70" y="30" text-anchor="middle" fill="#166534" font-size="20" font-weight="700">PASS</text>
    </g>

    <line x1="720" y1="452" x2="900" y2="452" stroke="#94A3B8" stroke-width="2"/>
    <polygon points="900,446 912,452 900,458" fill="#94A3B8"/>
    <text x="780" y="442" text-anchor="middle" fill="#475569" font-size="16" font-weight="600">no</text>
    <g transform="translate(950,428)">
      <rect x="0" y="0" width="140" height="48" rx="8" fill="#FEE2E2" stroke="#DC2626" stroke-width="2"/>
      <text x="70" y="30" text-anchor="middle" fill="#991B1B" font-size="20" font-weight="700">FAIL</text>
    </g>
  </svg>
  <figcaption class="figcaption">{{CAPTION}}</figcaption>
</figure>
```

**Parametrization checklist:**
- 3–4 questions max. More than 4 and the tree gets cramped.
- Each Q box at `y = 120 + (i * 100)`.
- Each rejected branch terminates on the right (NULL or FAIL).
- Final Q has PASS on the left, FAIL on the right.

---

## 3. Multi-input layout

**Used in:** Section pattern §10 (Multi-input layout)
**viewBox:** `0 0 1100 540`
**Layout:** Central bay/floor rect; robot/system circle inside; 6 input
nodes positioned around the perimeter; dashed lines from each input to the
central element.
**Input colors:** indigo `#4338CA` (high reliability), sky `#0EA5E9`
(top-down), violet `#A78BFA` (oblique / lower reliability).

```html
<figure class="cameras-figure">
  <svg
    role="img"
    aria-labelledby="cams-title cams-desc"
    focusable="false"
    viewBox="0 0 1100 540"
    class="cameras-svg"
  >
    <title id="cams-title">{{TITLE}}</title>
    <desc id="cams-desc">{{DESCRIPTION}}</desc>

    <!-- Floor / area -->
    <rect x="280" y="100" width="540" height="360" rx="12" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="550" y="284" text-anchor="middle" fill="#94A3B8" font-size="18" font-style="italic">{{AREA_LABEL}}</text>

    <!-- Optional anchors inside the area (e.g. source / destination zones) -->
    <rect x="320" y="140" width="200" height="60" rx="4" fill="#CBD5E1"/>
    <text x="420" y="178" text-anchor="middle" fill="#0F172A" font-size="16" font-weight="600">{{ZONE_1}}</text>

    <rect x="580" y="360" width="200" height="60" rx="4" fill="#CBD5E1"/>
    <text x="680" y="398" text-anchor="middle" fill="#0F172A" font-size="16" font-weight="600">{{ZONE_2}}</text>

    <!-- Central system -->
    <circle cx="550" cy="280" r="34" fill="#1E293B"/>
    <text x="550" y="286" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">{{SYSTEM_LABEL}}</text>

    <!-- Inputs around the perimeter. Position each at a distinct cardinal/diagonal point.
         x,y options that work well for 6 inputs:
           (160,180), (160,380), (940,180), (940,380), (550,50), (550,500) -->
    <g class="cam">
      <circle cx="160" cy="180" r="22" fill="#4338CA"/>
      <text x="160" y="186" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">{{KEY_1}}</text>
      <text x="160" y="232" text-anchor="middle" fill="#0F172A" font-size="16" font-weight="600">{{NAME_1}}</text>
      <!-- dashed connector to area edge -->
      <line x1="178" y1="186" x2="280" y2="240" stroke="#4338CA" stroke-width="2" stroke-dasharray="4,3"/>
    </g>

    <!-- repeat for each input; change fill color and connector endpoint to point toward the central area -->
  </svg>
  <figcaption class="figcaption">{{CAPTION_COLOR_KEY}}</figcaption>
</figure>
```

**Parametrization checklist:**
- 4–6 inputs is the sweet spot. More than 6 → clutter; switch to a fan/tree.
- Color-code by role/reliability, not by position.
- Each input has its short key (inside the circle, max 4 chars) and full
  name (below the circle, max 16 chars).

---

## 4. Cycle / feedback loop

**Used in:** Section pattern §12 (Cycle / feedback loop)
**viewBox:** `0 0 1100 520`
**Layout:** Central knowledge-base circle (r=90) with 5–8 outer nodes
(`r=56`) arranged around it. Arcs connect adjacent outer nodes (clockwise
flow). Green dashed arrows show "read" / "write" relationships between an
outer node and the center.

### CRITICAL: r must be ≥ 50

7-character labels (`baseline`, `diagnose`, `research`, `validate`,
`distill`) only fit when the outer circle radius is at least 50. The
reference value is **r=56** with **font-size 17**. v3 used r=32 and labels
overflowed — caught only by Playwright screenshot.

```html
<figure class="loop-figure">
  <svg
    role="img"
    aria-labelledby="loop-title loop-desc"
    focusable="false"
    viewBox="0 0 1100 520"
    class="loop-svg"
  >
    <title id="loop-title">{{TITLE}}</title>
    <desc id="loop-desc">{{DESCRIPTION_NAMING_THE_NODES_AND_THE_RW_RELATIONSHIPS}}</desc>

    <defs>
      <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#94A3B8"/>
      </marker>
      <marker id="arr-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#16A34A"/>
      </marker>
    </defs>

    <!-- Center knowledge base -->
    <circle cx="550" cy="260" r="90" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="2"/>
    <text x="550" y="252" text-anchor="middle" fill="#3730A3" font-size="20" font-weight="700">{{CENTER_NAME}}</text>
    <text x="550" y="280" text-anchor="middle" fill="#3730A3" font-size="15">{{CENTER_SUBLINE}}</text>

    <!-- Seven outer nodes on a circle of radius ~250 centered at (550,260).
         If you have N nodes, place them at angle = (2π / N) * i, starting from top.
         Concrete coordinates for N=7 (matches v4 calibration loop):
           top         (550, 70)
           top-right   (870, 135)
           right       (990, 320)
           bot-right   (810, 445)
           bot-left    (290, 445)
           left        (110, 320)
           top-left    (230, 135)
    -->
    <g class="loop-node">
      <circle cx="550" cy="70" r="56" fill="#4338CA"/>
      <text x="550" y="78" text-anchor="middle" fill="#fff" font-size="17" font-weight="700">{{NODE_1}}</text>
    </g>
    <g class="loop-node">
      <circle cx="870" cy="135" r="56" fill="#4338CA"/>
      <text x="870" y="143" text-anchor="middle" fill="#fff" font-size="17" font-weight="700">{{NODE_2}}</text>
    </g>
    <!-- repeat for each node, using the (x,y) above. -->

    <!-- Outer arcs (clockwise flow). Each path uses a quadratic-bezier through
         a midpoint outside the node ring. Pattern:
           M <node-i-right-edge> Q <midpoint> <node-i+1-left-edge>
         marker-end="url(#arr)" puts an arrow at the destination. -->
    <path d="M 605 80 Q 740 50 815 120" stroke="#94A3B8" stroke-width="2.5" fill="none" marker-end="url(#arr)"/>
    <path d="M 920 175 Q 1010 220 1015 270" stroke="#94A3B8" stroke-width="2.5" fill="none" marker-end="url(#arr)"/>
    <path d="M 990 380 Q 970 440 870 440" stroke="#94A3B8" stroke-width="2.5" fill="none" marker-end="url(#arr)"/>
    <path d="M 750 460 Q 550 510 350 460" stroke="#94A3B8" stroke-width="2.5" fill="none" marker-end="url(#arr)"/>
    <path d="M 230 440 Q 130 440 110 380" stroke="#94A3B8" stroke-width="2.5" fill="none" marker-end="url(#arr)"/>
    <path d="M 85 270 Q 80 220 175 175" stroke="#94A3B8" stroke-width="2.5" fill="none" marker-end="url(#arr)"/>
    <path d="M 285 120 Q 360 50 495 80" stroke="#94A3B8" stroke-width="2.5" fill="none" marker-end="url(#arr)"/>

    <!-- Optional feedback arrows: green dashed lines between outer node and center -->
    <path d="M 285 180 Q 380 220 462 240" stroke="#16A34A" stroke-width="2.5" fill="none" stroke-dasharray="6,4" marker-end="url(#arr-green)"/>
    <text x="350" y="215" fill="#166534" font-size="15" font-weight="600" font-style="italic">{{WRITE_LABEL}}</text>

    <path d="M 640 240 Q 800 230 935 295" stroke="#16A34A" stroke-width="2.5" fill="none" stroke-dasharray="6,4" marker-end="url(#arr-green)"/>
    <text x="800" y="230" fill="#166534" font-size="15" font-weight="600" font-style="italic">{{READ_LABEL}}</text>
  </svg>
  <figcaption class="figcaption">{{CAPTION_EXPLAINING_RW}}</figcaption>
</figure>
```

**Parametrization checklist:**
- Node count 5–8 is ideal.
- For other N: divide 2π by N, place each at `(550 + 250*sin(θ), 260 - 250*cos(θ))`.
- Each node radius **must** be ≥ 50. Default r=56.
- Label font-size 17 — don't reduce.
- Connecting arcs use quadratic beziers through a midpoint *outside* the
  ring (radius ~280 from center) so they curve around, not through.

---

## 5. Dependency DAG

**Used in:** Section pattern §9 (Dependency DAG)
**viewBox:** `0 0 1200 540`
**Layout:** Phase columns across the top (dashed vertical dividers); boxes
per node; quadratic-bezier edges between parent and child with arrow markers;
optional dashed rounded-rect "coupling group" containers around grouped
nodes.
**Box fill conventions:**
- Cascade root (parents that gate children): solid `#4338CA` with white text
- Dependent (NULL if parent fails): white with `#4338CA` 2px border
- Independent (no parent): `#EEF2FF` with `#A5B4FC` 2px border

```html
<figure class="dag-figure">
  <svg
    role="img"
    aria-labelledby="dag-title dag-desc"
    focusable="false"
    viewBox="0 0 1200 540"
    class="dag-svg"
  >
    <title id="dag-title">{{TITLE}}</title>
    <desc id="dag-desc">{{DESCRIPTION}}</desc>

    <!-- Phase headers across the top -->
    <text x="80"   y="30" fill="#475569" font-size="16" font-weight="700">{{PHASE_1}}</text>
    <text x="240"  y="30" fill="#475569" font-size="16" font-weight="700">{{PHASE_2}}</text>
    <text x="430"  y="30" fill="#475569" font-size="16" font-weight="700">{{PHASE_3}}</text>
    <text x="700"  y="30" fill="#475569" font-size="16" font-weight="700">{{PHASE_4}}</text>
    <text x="1000" y="30" fill="#475569" font-size="16" font-weight="700">{{PHASE_5}}</text>

    <!-- Vertical phase dividers -->
    <line x1="200"  y1="50" x2="200"  y2="510" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="380"  y1="50" x2="380"  y2="510" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="660"  y1="50" x2="660"  y2="510" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="4,4"/>
    <line x1="940"  y1="50" x2="940"  y2="510" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="4,4"/>

    <!-- Independent node (light-fill box) -->
    <g>
      <rect x="40" y="80" width="160" height="60" rx="8" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="2"/>
      <text x="120" y="106" text-anchor="middle" fill="#0F172A" font-size="16" font-weight="700">{{N_INDEP_ID}}</text>
      <text x="120" y="124" text-anchor="middle" fill="#475569" font-size="13">{{N_INDEP_LABEL}}</text>
    </g>

    <!-- Coupling group container (optional). Surround grouped nodes with this rect. -->
    <rect x="220" y="170" width="420" height="280" rx="10" fill="rgba(67,56,202,0.04)" stroke="#A5B4FC" stroke-width="1.5" stroke-dasharray="6,4"/>
    <text x="430" y="190" text-anchor="middle" fill="#4338CA" font-size="14" font-weight="700">{{GROUP_LABEL}}</text>

    <!-- Cascade-root node (solid indigo) -->
    <g>
      <rect x="240" y="210" width="140" height="60" rx="8" fill="#4338CA" stroke="#312E81" stroke-width="2"/>
      <text x="310" y="236" text-anchor="middle" fill="#fff" font-size="16" font-weight="700">{{N_ROOT_ID}}</text>
      <text x="310" y="254" text-anchor="middle" fill="#E0E7FF" font-size="13">{{N_ROOT_LABEL}}</text>
    </g>

    <!-- Dependent node (outlined) -->
    <g>
      <rect x="410" y="210" width="160" height="60" rx="8" fill="#fff" stroke="#4338CA" stroke-width="2"/>
      <text x="490" y="236" text-anchor="middle" fill="#0F172A" font-size="16" font-weight="700">{{N_CHILD_ID}}</text>
      <text x="490" y="254" text-anchor="middle" fill="#475569" font-size="13">{{N_CHILD_LABEL}}</text>
    </g>

    <!-- Edge: straight line for adjacent nodes -->
    <line x1="380" y1="240" x2="410" y2="240" stroke="#94A3B8" stroke-width="2"/>
    <polygon points="410,234 422,240 410,246" fill="#94A3B8"/>

    <!-- Edge: quadratic-bezier for non-adjacent fan-out
         M <parent-right-edge> Q <midpoint> <child-left-edge> -->
    <path d="M 570 340 Q 640 340 700 245" stroke="#94A3B8" stroke-width="2" fill="none"/>
    <polygon points="697,242 703,232 705,246" fill="#94A3B8"/>

    <!-- Legend -->
    <g transform="translate(40,490)">
      <rect width="20" height="14" rx="3" fill="#4338CA"/>
      <text x="28" y="12" fill="#475569" font-size="13">Cascade root (parents that gate children)</text>
    </g>
    <g transform="translate(380,490)">
      <rect width="20" height="14" rx="3" fill="#fff" stroke="#4338CA" stroke-width="2"/>
      <text x="28" y="12" fill="#475569" font-size="13">Dependent (NULL if parent FAILs)</text>
    </g>
    <g transform="translate(700,490)">
      <rect width="20" height="14" rx="3" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="2"/>
      <text x="28" y="12" fill="#475569" font-size="13">Independent (no parent)</text>
    </g>
  </svg>
  <figcaption class="figcaption">{{CAPTION_REFERENCING_CODE_SYMBOL}}</figcaption>
</figure>
```

**Parametrization checklist:**
- 3–5 phase columns. More → switch viewBox to 0 0 1400 540.
- 6–12 nodes total. More → use coupling-group containers to chunk visually.
- Box width: 140–200 px depending on label length. Keep height at 50–60 px.
- Edges: prefer straight `<line>` when source and target are at the same y;
  use `<path d="M ... Q ... ...">` quadratic-bezier for fan-outs.
- Always include the legend at the bottom.

---

## 6. Side-by-side diff (HTML, not SVG)

**Used in:** Section pattern §13 (Side-by-side diff)
**Not an SVG** — the diff cards are pure HTML/CSS via `.diff-grid` +
`.diff-card`. Listed here for completeness since the section pattern refers
back here.

See `section-patterns.md` §13 for the full HTML template.

---

## Diagram label rendered size (it depends on the page, not the viewBox)

SVG `<text>` is in **viewBox units**, not CSS pixels. When the SVG element
is rendered on the page, its viewBox is scaled to fit the SVG's CSS width.
A label's rendered px size is therefore:

```
rendered_text_px = font_size_in_viewBox × (svg_rendered_width_px / viewBox_width)
```

Two consequences worth knowing:

- **A diagram's text shrinks on narrower screens.** A tree SVG with
  `viewBox="0 0 1100 624"` and `font-size="13"` for pill sublabels
  renders that text at ~12 px when the SVG is 990 px wide (a typical
  content column), at ~16 px when the SVG is 1400 px wide, at ~20 px
  when the SVG is 1700 px wide. The viewBox font number alone tells you
  nothing about how it'll look — you have to know the rendered width.
- **Bumping the page's root font-size (`html { font-size: % }`) does
  not affect SVG internal text.** That bumps `rem`; SVG `font-size` is
  in user units. To make diagram labels render bigger, either widen the
  SVG container (the *Wide-screen overrides* recipe in
  `design-system.md` does this as a side effect — capping figures at
  1680 px) or bump the SVG `font-size` attributes themselves (which
  often forces re-layout of the surrounding shapes, because SVG
  `<text>` does not wrap).

Pair this with the `r ≥ 50` rule in §4 (cycle/loop) and the implicit
"label must fit inside its shape at the chosen `font-size`" check for
every box / pill / circle in this recipe set. Always re-screenshot
after changing either an SVG `font-size` or the page's layout cap.

## a11y checklist for every SVG

Every informational SVG **must** include:

1. `role="img"` on the `<svg>` tag.
2. `aria-labelledby="{{ID}}-title {{ID}}-desc"`.
3. `focusable="false"` (prevents IE/Edge tab traps).
4. `<title id="{{ID}}-title">{{plain title}}</title>` — first child.
5. `<desc id="{{ID}}-desc">{{2-4 sentence description}}</desc>` —
   describe what the diagram conveys, not its visual structure.
6. Where the SVG IS a data chart (verdict tree, multi-row comparison), a
   sibling `<table class="visually-hidden">` immediately after with the
   same data as rows.

Skip these only on purely decorative SVGs (e.g. brand-mark icons), where
you should use `aria-hidden="true"` instead.

## Color discipline

Don't introduce hues outside the v4 palette. The 6 SVG-relevant fills:

- `#4338CA` indigo — primary, structural
- `#0EA5E9` sky — accent / output highlight
- `#A78BFA` violet — synthesis / oblique
- `#16A34A` green — success / write-back
- `#D97706` amber — warning / contested
- `#DC2626` red — failure / terminal-fail

For neutral structure: `#94A3B8` (lines), `#CBD5E1` (subtle borders),
`#EEF2FF` (light-indigo backgrounds), `#F1F5F9` (floor / area fill).
