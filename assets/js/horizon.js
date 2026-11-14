(function () {
  'use strict';

  var root = document.documentElement;

  /** Replace "⭐️ N/10" after a headline with a small score badge. */
  function processScoreBadges() {
    var scoreRe = /⭐️\s*(\d+(?:\.\d+)?)\/10/;
    var targets = document.querySelectorAll('.prose h2, .prose h3, .prose li, .prose p');
    targets.forEach(function (el) {
      var m = el.innerHTML.match(scoreRe);
      if (!m) return;
      var score = parseFloat(m[1]);
      var tier = score >= 9 ? 'high' : score >= 7.5 ? 'good' : 'mid';
      var label = (root.dataset.lang === 'zh' ? '评分 ' : 'Score ') + m[1] + '/10';
      el.innerHTML = el.innerHTML.replace(
        scoreRe,
        '<span class="score" data-tier="' + tier + '" title="' + label + '" aria-label="' + label + '">' + m[1] + '</span>'
      );
    });
  }

  /** Tag the source line, tag line and table of contents so CSS can style them. */
  function markSemanticElements() {
    var dateRe = /(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}, \d{2}:\d{2}|\d{1,2}月\d{1,2}日 \d{2}:\d{2}/;
    document.querySelectorAll('.prose p').forEach(function (p) {
      var text = p.textContent.trim();
      if (/^(Tags|标签)\s*:/.test(text)) {
        p.classList.add('tag-line');
      } else if (text.length < 200 && text.indexOf(' · ') !== -1 && dateRe.test(text)) {
        p.classList.add('source-line');
      }
    });
    document.querySelectorAll('.prose > p, .prose > ol, .prose > ul').forEach(function (el) {
      if (el.querySelector('a[href^="#"]') && /⭐️/.test(el.textContent)) el.classList.add('toc-block');
    });
  }

  /** EN / 中文 switch. Home and static pages swap in place; an issue page opens its other-language twin. */
  function setupLanguageToggle() {
    var buttons = document.querySelectorAll('[data-set-lang]');
    var isIssue = /summary-(en|zh)(\.html)?$/.test(window.location.pathname.replace(/\/$/, ''));

    function paint(lang) {
      buttons.forEach(function (b) {
        var on = b.getAttribute('data-set-lang') === lang;
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
    }

    function setLang(lang) {
      try { localStorage.setItem('adr-lang', lang); } catch (e) { /* storage may be blocked */ }
      if (isIssue) {
        var path = window.location.pathname;
        var target = path.replace(/summary-(en|zh)/, 'summary-' + lang);
        if (target !== path) window.location.href = target;
        return;
      }
      root.dataset.lang = lang;
      root.setAttribute('lang', lang === 'zh' ? 'zh-Hans' : 'en');
      paint(lang);
    }

    buttons.forEach(function (b) {
      b.addEventListener('click', function () { setLang(b.getAttribute('data-set-lang')); });
    });
    if (!isIssue) root.setAttribute('lang', root.dataset.lang === 'zh' ? 'zh-Hans' : 'en');
    paint(root.dataset.lang || 'en');
  }

  document.addEventListener('DOMContentLoaded', function () {
    markSemanticElements();
    processScoreBadges();
    setupLanguageToggle();
  });
})();
