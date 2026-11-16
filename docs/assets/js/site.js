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

// Saved stories (kept in this browser), native share sheet, and lazy comments.
(function () {
  'use strict';
  var KEY = 'adr-saved';
  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; }
  }
  function store(list) {
    try { localStorage.setItem(KEY, JSON.stringify(list.slice(0, 200))); } catch (e) {}
  }
  function updateCount() {
    var n = load().length;
    document.querySelectorAll('.saved-count').forEach(function (el) {
      el.textContent = n ? ' ' + n : '';
      el.hidden = !n;
    });
  }
  function paintButton(btn) {
    var on = load().some(function (s) { return s.url === btn.dataset.url; });
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    btn.textContent = on ? btn.dataset.saved : btn.dataset.save;
  }
  document.querySelectorAll('.save-story').forEach(paintButton);
  updateCount();
  document.addEventListener('click', function (event) {
    var btn = event.target.closest('.save-story');
    if (btn) {
      var list = load().filter(function (s) { return s.url !== btn.dataset.url; });
      if (btn.getAttribute('aria-pressed') !== 'true') {
        list.unshift({ url: btn.dataset.url, title: btn.dataset.title, section: btn.dataset.section, date: btn.dataset.date });
      }
      store(list); paintButton(btn); updateCount();
      return;
    }
    var share = event.target.closest('.native-share');
    if (share && navigator.share) {
      navigator.share({ title: share.dataset.title, url: share.dataset.url }).catch(function () {});
      return;
    }
    var clear = event.target.closest('.saved-clear');
    if (clear) { store([]); renderSaved(); updateCount(); }
  });
  if (navigator.share) {
    document.querySelectorAll('.native-share').forEach(function (b) { b.hidden = false; });
  }
  function renderSaved() {
    var ol = document.querySelector('.saved-list');
    if (!ol) return;
    var list = load();
    ol.textContent = '';
    if (!list.length) {
      var p = document.createElement('p'); p.textContent = ol.dataset.empty; ol.appendChild(p);
    }
    list.forEach(function (s) {
      var li = document.createElement('li');
      var a = document.createElement('a'); a.href = s.url; a.textContent = s.title;
      var meta = document.createElement('span'); meta.className = 'saved-meta';
      meta.textContent = [s.section, s.date].filter(Boolean).join(' · ');
      li.appendChild(a); li.appendChild(meta); ol.appendChild(li);
    });
    var clear = document.querySelector('.saved-clear');
    if (clear) clear.hidden = !list.length;
  }
  renderSaved();
  // giscus: load when the reader gets near the comments.
  var slot = document.querySelector('.giscus-slot');
  if (slot) {
    var loadGiscus = function () {
      if (slot.dataset.loaded) return;
      slot.dataset.loaded = '1';
      var s = document.createElement('script');
      s.src = 'https://giscus.app/client.js';
      s.async = true;
      s.crossOrigin = 'anonymous';
      var attrs = {
        'data-repo': slot.dataset.repo, 'data-repo-id': slot.dataset.repoId,
        'data-category': slot.dataset.category, 'data-category-id': slot.dataset.categoryId,
        'data-mapping': 'specific', 'data-term': slot.dataset.term, 'data-strict': '1',
        'data-reactions-enabled': '1', 'data-emit-metadata': '0', 'data-input-position': 'top',
        'data-theme': 'preferred_color_scheme', 'data-lang': slot.dataset.lang, 'data-loading': 'lazy'
      };
      Object.keys(attrs).forEach(function (k) { s.setAttribute(k, attrs[k]); });
      slot.appendChild(s);
    };
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries, obs) {
        if (entries.some(function (e) { return e.isIntersecting; })) { loadGiscus(); obs.disconnect(); }
      }, { rootMargin: '600px' }).observe(slot);
    } else { loadGiscus(); }
  }
})();
