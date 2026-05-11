/* GantryForge investor explainer — scroll-spy + small UX niceties */
(function () {
  'use strict';

  // 1) Scroll-spy on TOC links using IntersectionObserver
  var sections = document.querySelectorAll('main section[id]');
  var tocLinks = document.querySelectorAll('#page-toc a');

  function setActive(id) {
    tocLinks.forEach(function (link) {
      var isActive = link.getAttribute('href') === '#' + id;
      link.classList.toggle('toc-active', isActive);
      if (isActive) {
        link.setAttribute('aria-current', 'true');
      } else {
        link.removeAttribute('aria-current');
      }
    });
  }

  if ('IntersectionObserver' in window && sections.length && tocLinks.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        // pick the intersecting entry whose top is closest to the viewport top
        var visible = entries.filter(function (e) { return e.isIntersecting; });
        if (!visible.length) return;
        visible.sort(function (a, b) {
          return Math.abs(a.boundingClientRect.top) - Math.abs(b.boundingClientRect.top);
        });
        setActive(visible[0].target.id);
      },
      { rootMargin: '-25% 0px -65% 0px', threshold: [0, 0.25, 0.5] }
    );
    sections.forEach(function (s) { observer.observe(s); });
  }

  // 2) Smooth scroll for in-page anchors, but respect prefers-reduced-motion
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var href = a.getAttribute('href');
      if (!href || href === '#') return;
      var target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      var top = target.getBoundingClientRect().top + window.pageYOffset - 80;
      window.scrollTo({ top: top, behavior: reduce ? 'auto' : 'smooth' });
      // move focus to the section heading for accessibility
      var heading = target.querySelector('h1, h2, h3');
      if (heading) {
        heading.setAttribute('tabindex', '-1');
        heading.focus({ preventScroll: true });
      }
      history.replaceState(null, '', href);
    });
  });

  // 3) Escape closes any open <details>
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('details[open]').forEach(function (d) {
        // do not auto-close the TOC if it's a details element — none here
        d.removeAttribute('open');
      });
    }
  });
})();
