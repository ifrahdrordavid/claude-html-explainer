#!/usr/bin/env python3
"""
Screenshot key sections of an html-explainer page at multiple viewport widths,
to verify it spreads correctly on wide / ultra-wide displays.

The default `screenshot.py` shoots at one viewport (1440 × 900 @ 2x DPR), which
is enough to catch SVG overflow, dark-section code visibility, and TOC
misalignment — but it cannot tell you whether the page also looks good on a
27"/4K/50" monitor. Use this verifier whenever:

- the user is going to view the page on a wide display
- you've added wide-screen overrides (page-shell max-width, TOC clamp,
  card-grid minmax floors, SVG-figure caps) and want to confirm them
- you've bumped the root font-size and want to confirm the card grids
  still hold their text comfortably at every breakpoint

Usage:
    python3 screenshot-wide.py                       # defaults: ./index.html, widths 1440/2000/2560/3840
    python3 screenshot-wide.py path/to/index.html
    python3 screenshot-wide.py path/to/index.html 1440 2200 2880

Output:
    <html-dir>/.screenshots-wide/w<width>_<section_id>.png
    <html-dir>/.screenshots-wide/w<width>_top.png    (hero + header crop)

Per-section locator screenshots (not full-page) — on a 156%-scaled page at
3840px viewport a full-page screenshot can exceed Chromium's max canvas size
and fails. Per-element locators stay within bounds.

Read each PNG back (Read tool, absolute path) and check: no horizontal
overflow, no clipped tables, card grids add columns at wider widths, the
SVG diagrams are visibly bigger but capped (not ballooning), prose columns
are still readable (≤ ~85ch), the TOC text doesn't wrap into ribbons.
"""
import sys
import pathlib
from playwright.sync_api import sync_playwright


DEFAULT_WIDTHS = [1440, 2000, 2560, 3840]


def main() -> int:
    args = sys.argv[1:]
    html_arg = None
    widths = []
    for a in args:
        if a.isdigit():
            widths.append(int(a))
        else:
            html_arg = a
    widths = widths or DEFAULT_WIDTHS

    html = pathlib.Path(html_arg or "index.html").resolve()
    if not html.exists():
        print(f"[ERR] HTML not found: {html}")
        return 1

    out = html.parent / ".screenshots-wide"
    out.mkdir(exist_ok=True)
    print(f"[INFO] HTML:    {html}")
    print(f"[INFO] OUT:     {out}")
    print(f"[INFO] WIDTHS:  {widths}")

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for w in widths:
            ctx = browser.new_context(
                viewport={"width": w, "height": 1200},
                device_scale_factor=1,
            )
            page = ctx.new_page()
            page.goto(f"file://{html}")
            page.wait_for_load_state("networkidle")

            # Open all <details> so disclosure bodies render in screenshots.
            page.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
            page.wait_for_timeout(400)

            # Section ids from the TOC.
            toc_ids = page.evaluate(
                """() => {
                  const links = document.querySelectorAll('#page-toc a[href^="#"]');
                  return Array.from(links).map(a => a.getAttribute('href').slice(1));
                }"""
            )

            # Hero + header strip — bounded crop, not full page.
            try:
                hero = page.locator(".hero")
                if hero.count():
                    hero.scroll_into_view_if_needed()
                    page.wait_for_timeout(120)
                    target = out / f"w{w}_top.png"
                    hero.screenshot(path=str(target))
                    bx = hero.bounding_box()
                    print(f"[OK]  w{w}_top -> {target} ({int(bx['width'])}x{int(bx['height'])})")
            except Exception as exc:
                print(f"[ERR] w{w}_top: {exc}")

            for sid in toc_ids:
                try:
                    loc = page.locator(f"#{sid}")
                    if loc.count() == 0:
                        print(f"[WARN] w{w} TOC -> #{sid}: no matching element")
                        continue
                    loc.scroll_into_view_if_needed()
                    page.wait_for_timeout(150)
                    bx = loc.bounding_box()
                    if bx:
                        target = out / f"w{w}_{sid}.png"
                        loc.screenshot(path=str(target))
                        print(f"[OK]  w{w}_{sid} -> {target} ({int(bx['width'])}x{int(bx['height'])})")
                    else:
                        print(f"[WARN] w{w}_{sid}: no bounding box")
                except Exception as exc:
                    print(f"[ERR] w{w}_{sid}: {exc}")

            ctx.close()
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
