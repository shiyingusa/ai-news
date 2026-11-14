(function () {
  'use strict';
  document.addEventListener('click', function (event) {
    var button = event.target.closest('.copy-link');
    if (!button) return;
    var url = button.getAttribute('data-url');
    var done = button.getAttribute('data-done') || 'Copied';
    var label = button.textContent;
    function confirmCopy() {
      button.textContent = done;
      setTimeout(function () { button.textContent = label; }, 1800);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(confirmCopy, function () { window.prompt('', url); });
    } else {
      window.prompt('', url);
    }
  });
  // Keep the active section tab in view on narrow screens.
  var current = document.querySelector('.section-nav-list a[aria-current]');
  if (current) {
    var list = current.closest('.section-nav-list');
    if (list && list.scrollWidth > list.clientWidth) {
      list.scrollLeft = current.offsetLeft - list.clientWidth / 2 + current.offsetWidth / 2;
    }
  }
})();
