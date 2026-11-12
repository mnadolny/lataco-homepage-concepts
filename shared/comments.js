// Loads Proto Comments (pinned review comments) on every page.
// Skipped inside the scaled preview iframes on index.html; the widget's own
// device-preview frames (?pc-frame) still load it.
(function () {
  if (window.top !== window && !/[?&]pc-frame\b/.test(location.search)) return;
  var s = document.createElement('script');
  s.src = 'https://proto-comments.mattn-protos.workers.dev/widget/proto-comments.js';
  s.dataset.project = 'lataco';
  s.dataset.api = 'https://proto-comments.mattn-protos.workers.dev';
  document.head.appendChild(s);
})();
