// Floating concept switcher for client review. Include with <script src="shared/switcher.js" defer></script>
(() => {
  if (window.self !== window.top) return; // not inside the index page's previews
  if (location.hostname.endsWith(".github.io")) return; // hidden on the shared client links
  const concepts = [
    ['index.html', 'All three'],
    ['a.html', 'A  Primera Plana'],
    ['a-v2.html', 'A v2'],
    ['b.html', 'B  Rótulo'],
    ['b-v2.html', 'B v2'],
    ['c.html', 'C  Wheatpaste'],
  ];
  const here = location.pathname.split('/').pop() || 'index.html';
  const nav = document.createElement('nav');
  nav.setAttribute('aria-label', 'Concept switcher');
  nav.className = 'lat-switcher';
  nav.innerHTML = concepts
    .map(([href, label]) => `<a href="${href}"${href === here ? ' aria-current="page"' : ''}>${label}</a>`)
    .join('');
  const css = document.createElement('style');
  css.textContent = `
    .lat-switcher{position:fixed;right:16px;bottom:16px;z-index:9999;display:flex;gap:2px;padding:4px;
      background:#1b1714;border-radius:999px;box-shadow:0 6px 24px rgba(0,0,0,.35);font:600 13px/1 "IBM Plex Sans",system-ui,sans-serif}
    .lat-switcher a{color:#f7f4e9;text-decoration:none;padding:9px 14px;border-radius:999px;white-space:pre}
    .lat-switcher a:hover{background:rgba(255,255,255,.12)}
    .lat-switcher a[aria-current]{background:#f4c542;color:#1b1714}
    .lat-switcher a:focus-visible{outline:2px solid #f4c542;outline-offset:2px}
    @media (max-width:700px){.lat-switcher{left:8px;right:8px;overflow-x:auto}.lat-switcher a{padding:8px 9px}}`;
  document.head.append(css);
  document.body.append(nav);
})();
