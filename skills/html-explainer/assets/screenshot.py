#!/usr/bin/env python3
"""
Screenshot every TOC section of an html-explainer page for visual verification.

Usage:
    python3 screenshot.py                 # defaults to ./index.html → ./.screenshots/
    python3 screenshot.py path/to.html    # explicit HTML, screenshots next to it

Behavior:
- Loads the HTML in headless Chromium at 1440x900 @ 2x DPR
- Opens every <details> so disclosure bodies are captured
- Reads section IDs from the TOC (<nav id="page-toc"> a[href^="#"])
- Adds the full hero (.hero) and any standalone CTA / footer sections
- Writes one PNG per section into <html-dir>/.screenshots/<id>.png
- Also writes a "full_page.png" for layout sanity

Exit code is non-zero only if Playwright itself errors. Per-section errors are
printed but don't abort the run, so you get partial coverage when one section
has a layout issue.
"""
import sys
import pathlib
from playwright.sync_api import sync_playwright


def main(html_arg: str | None = None) -> int:
    html = pathlib.Path(html_arg or "index.html").resolve()
    if not html.exists():
        print(f"[ERR] HTML not found: {html}")
        return 1

    out = html.parent / ".screenshots"
    out.mkdir(exist_ok=True)
    print(f"[INFO] HTML:  {html}")
    print(f"[INFO] OUT:   {out}")

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        ctx = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=2,
        )
        page = ctx.new_page()
        page.goto(f"file://{html}")
        page.wait_for_load_state("networkidle")

        # Open all <details> so disclosure bodies render in screenshots.
        page.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
        page.wait_for_timeout(500)

        # Discover section IDs from the TOC.
        toc_ids = page.evaluate(
            """() => {
              const links = document.querySelectorAll('#page-toc a[href^="#"]');
              return Array.from(links).map(a => a.getAttribute('href').slice(1));
            }"""
        )

        # Always include hero + cta + footer if present.
        extra_ids = page.evaluate(
            """() => {
              const ids = [];
              const hero = document.querySelector('.hero');
              if (hero) ids.push({sel: '.hero', name: 'hero'});
              const cta = document.querySelector('#cta, .cta-section');
              if (cta) ids.push({sel: cta.id ? '#' + cta.id : '.cta-section', name: 'cta'});
              return ids;
            }"""
        )

        # Full page first
        try:
            full = out / "full_page.png"
            page.screenshot(path=str(full), full_page=True)
            print(f"[OK] full_page -> {full}")
        except Exception as exc:
            print(f"[ERR] full_page: {exc}")

        # Hero / CTA / footer extras
        for extra in extra_ids:
            try:
                loc = page.locator(extra["sel"])
                loc.scroll_into_view_if_needed()
                page.wait_for_timeout(150)
                box = loc.bounding_box()
                if box:
                    target = out / f"{extra['name']}.png"
                    loc.screenshot(path=str(target))
                    print(f"[OK] {extra['name']} -> {target} ({int(box['width'])}x{int(box['height'])})")
                else:
                    print(f"[WARN] no bbox for {extra['sel']}")
            except Exception as exc:
                print(f"[ERR] {extra['sel']}: {exc}")

        # Per-section screenshots from the TOC
        for sid in toc_ids:
            try:
                loc = page.locator(f"#{sid}")
                if loc.count() == 0:
                    print(f"[WARN] TOC points to #{sid} but no element has that id")
                    continue
                loc.scroll_into_view_if_needed()
                page.wait_for_timeout(200)
                box = loc.bounding_box()
                if box:
                    target = out / f"{sid}.png"
                    loc.screenshot(path=str(target))
                    print(f"[OK] {sid} -> {target} ({int(box['width'])}x{int(box['height'])})")
                else:
                    print(f"[WARN] no bbox for #{sid}")
            except Exception as exc:
                print(f"[ERR] {sid}: {exc}")

        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
