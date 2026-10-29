// Measures a concept page into a compact spec that tools/figma-build.js turns into Figma layers.
// Run in the browser at 1440 wide: await (await import('/homepage-concepts/tools/extract.js')).extract(sectionIndex)
// Node shapes (all coords relative to the section's top-left, integers):
//   r: [ 'r', x,y,w,h, fill|null, opacity, radius, stroke|null, strokeW, effects|null, g ]
//   i: [ 'i', x,y,w,h, src, [fx,fy,ox,oy], radius, g ]
//   t: [ 't', x,y,w,h, runs, align, lineHeight|0, letterSpacing, oneLine, g ]   runs: [text, fontIdx, color, underline]
//   c: [ 'c', x,y, size, kind, text, fill, primary, inline, g ]
//   l: [ 'l', x,y,w,h, fillColor, lineColor, g ]          two-tone logo
//   m: [ 'm', x,y,w,h, src, color, g ]                    color through an alpha mask image
//   p: [ 'p', x,y,w,h, svgPath, fill, g ]                 clip-path polygon
//   g: groups: [id, cx, cy, w, h, rotDeg]  (children of a rotated element measured unrotated)

const hex = (c) => {
  const m = c && c.match(/rgba?\(([^)]+)\)/); if (!m) return null;
  const [r, g, b, a = 1] = m[1].split(/[ ,/]+/).filter(Boolean).map(Number);
  if (a === 0) return null;
  const h = '#' + [r, g, b].map(v => Math.round(v).toString(16).padStart(2, '0')).join('');
  return a < 1 ? h + Math.round(a * 255).toString(16).padStart(2, '0') : h;
};
const R = Math.round;

function fontName(cs) {
  const fam = cs.fontFamily.split(',')[0].replace(/["']/g, '');
  const w = +cs.fontWeight, it = cs.fontStyle === 'italic';
  if (/^Sutro/.test(fam)) {
    const s = w <= 300 ? 'Light' : w <= 500 ? 'Medium' : w <= 700 ? 'Bold' : w <= 800 ? 'ExtraBold' : 'Heavy';
    return ['Sutro ', it ? s + ' Italic' : s];
  }
  let family = /Condensed/.test(fam) ? 'IBM Plex Sans Condensed' : /Plex/.test(fam) ? 'IBM Plex Sans' : 'Source Serif 4';
  if (/system-ui|sans-serif/.test(fam)) family = 'IBM Plex Sans';
  const s = w <= 300 ? 'Light' : w <= 400 ? 'Regular' : w <= 500 ? 'Medium' : w <= 600 ? 'SemiBold' : 'Bold';
  return [family, it ? (s === 'Regular' ? 'Italic' : s + ' Italic') : s];
}

export async function extract(sectionIndex, opts = {}) {
  // freeze motion and capture rotations
  const kill = document.createElement('style');
  kill.textContent = 'html{scrollbar-width:none}html::-webkit-scrollbar{display:none}*,*::before,*::after{animation:none!important;transition:none!important}.lat-switcher{display:none!important}';
  document.head.append(kill);
  await document.fonts.ready;
  const sections = [...document.body.children].flatMap(el =>
    el.tagName === 'MAIN' ? [...el.children] : [el]).filter(el =>
    !['SCRIPT', 'STYLE', 'NAV'].includes(el.tagName) || el.closest('header'))
    .filter(el => el.getBoundingClientRect().height > 0 && !el.classList.contains('lat-switcher') && el.tagName !== 'A');
  if (sectionIndex === 'list') return sections.map((s, i) => [i, s.tagName, s.className, R(s.getBoundingClientRect().top + scrollY), R(s.getBoundingClientRect().height)]);
  const sec = sections[sectionIndex];

  const groups = [], restore = [];
  sec.querySelectorAll('*').forEach(el => {
    const t = getComputedStyle(el).transform;
    if (t && t !== 'none') {
      const [a, b] = t.match(/matrix\(([^)]+)\)/)?.[1].split(',').map(Number) || [1, 0];
      const deg = Math.atan2(b, a) * 180 / Math.PI;
      if (Math.abs(deg) > 0.05) { el.dataset.g = groups.length; groups.push({ el, deg }); restore.push([el, el.style.transform]); }
    }
  });
  restore.forEach(([el]) => el.style.setProperty('transform', 'none', 'important'));

  const sr = sec.getBoundingClientRect(), ox = sr.left + scrollX, oy = sr.top + scrollY;
  const box = (r) => [R(r.left + scrollX - ox), R(r.top + scrollY - oy), R(r.width), R(r.height)];
  const grp = (el) => { const g = el.closest('[data-g]'); return g && sec.contains(g) ? +g.dataset.g : -1; };
  const fonts = [], fi = (f) => { const k = f.join('|'); let i = fonts.findIndex(x => x.join('|') === k); if (i < 0) { fonts.push(f); i = fonts.length - 1; } return i; };
  const out = [];
  const secCS = getComputedStyle(sec);
  const hidden = (el, cs) => cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0 ||
    (cs.position === 'absolute' && R(el.getBoundingClientRect().width) <= 1) || cs.clip === 'rect(0px, 0px, 0px, 0px)';

  function shadows(cs, b) {
    const sh = cs.boxShadow; if (!sh || sh === 'none') return { inset: [], drop: null };
    const parts = sh.split(/,(?![^(]*\))/).map(s => s.trim());
    const inset = [], drop = [];
    for (const p of parts) {
      const col = hex(p.match(/rgba?\([^)]+\)/)?.[0]); const nums = p.replace(/rgba?\([^)]+\)/, '').match(/-?[\d.]+px/g)?.map(parseFloat) || [];
      const [x = 0, y = 0, blur = 0, spread = 0] = nums;
      if (/inset/.test(p)) inset.push({ spread, col }); else if (col) drop.push([x, y, blur, spread, col]);
    }
    return { inset, drop: drop.length ? drop : null };
  }

  function pseudo(el, which, b) {
    const ps = getComputedStyle(el, which);
    if (!ps || ps.content === 'none' || ps.content === 'normal' || ps.display === 'none') return;
    if (ps.position !== 'absolute') return;
    const px = v => parseFloat(v);
    const pb = el.getBoundingClientRect(), cs = getComputedStyle(el);
    const L = pb.left + px(cs.borderLeftWidth), T = pb.top + px(cs.borderTopWidth);
    const W = pb.width - px(cs.borderLeftWidth) - px(cs.borderRightWidth), H = pb.height - px(cs.borderTopWidth) - px(cs.borderBottomWidth);
    let left = ps.left !== 'auto' ? px(ps.left) : null, right = ps.right !== 'auto' ? px(ps.right) : null, top = ps.top !== 'auto' ? px(ps.top) : null, bottom = ps.bottom !== 'auto' ? px(ps.bottom) : null;
    let w = ps.width !== 'auto' ? px(ps.width) : null, h = ps.height !== 'auto' ? px(ps.height) : null;
    if (w == null && left != null && right != null) w = W - left - right;
    if (h == null && top != null && bottom != null) h = H - top - bottom;
    if (left == null && right != null && w != null) left = W - right - w;
    if (top == null && bottom != null && h != null) top = H - bottom - h;
    if ([left, top, w, h].some(v => v == null || isNaN(v))) return;
    const bg = hex(ps.backgroundColor), bw = px(ps.borderTopWidth), bc = bw ? hex(ps.borderTopColor) : null;
    if (!bg && !bc) return;
    const r = { left: L + left, top: T + top, width: w, height: h };
    out.push(['r', ...box(r), bg, 1, px(ps.borderTopLeftRadius) || 0, bc, bw || 0, null, grp(el)]);
  }

  function textRuns(el) {
    // collect text through inline descendants only
    const runs = []; let any = false;
    const walk = (n) => {
      for (const c of n.childNodes) {
        if (c.nodeType === 3) {
          const s = c.textContent; if (!s) continue;
          const pcs = getComputedStyle(c.parentElement);
          let txt = s.replace(/\s+/g, ' ');
          if (pcs.textTransform === 'uppercase') txt = txt.toUpperCase();
          if (/\S/.test(txt)) any = true;
          runs.push([txt, fi(fontName(pcs)), hex(pcs.color), /underline/.test(pcs.textDecorationLine) ? 1 : 0]);
        } else if (c.nodeType === 1) {
          const ccs = getComputedStyle(c);
          if (c.tagName === 'BR') { runs.push(['\n', runs.length ? runs[runs.length - 1][1] : 0, null, 0]); continue; }
          if (ccs.display === 'inline' && !hidden(c, ccs) && !c.classList.contains('sr') && !c.classList.contains('chroma')) walk(c);
        }
      }
    };
    walk(el);
    if (!any) return null;
    // trim + merge
    let joined = runs; while (joined.length && !joined[0][0].trim()) joined.shift();
    if (joined.length) joined[0][0] = joined[0][0].replace(/^\s+/, '');
    while (joined.length && !joined[joined.length - 1][0].trim()) joined.pop();
    if (joined.length) joined[joined.length - 1][0] = joined[joined.length - 1][0].replace(/\s+$/, '');
    const merged = [];
    for (const r of joined) { const p = merged[merged.length - 1]; if (p && p[1] === r[1] && p[2] === r[2] && p[3] === r[3]) p[0] += r[0]; else merged.push([...r]); }
    merged.forEach(r => { if (!r[2]) r[2] = '#000000'; });
    return merged;
  }

  function visit(el) {
    const cs = getComputedStyle(el);
    if (hidden(el, cs) || el.classList.contains('sr') || el.classList.contains('lat-switcher')) return;
    const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) { if (cs.display !== 'contents') return; }
    const b = box(r), g = grp(el);

    if (el.classList.contains('chroma')) {
      const span = el.querySelector(':scope > span'); const pr = span.getBoundingClientRect();
      const kind = el.classList.contains('chroma--deluxe') ? 'deluxe' : 'shaded';
      out.push(['c', ...box(pr).slice(0, 2), R(parseFloat(cs.fontSize)), kind, el.dataset.text,
        hex(getComputedStyle(el, '::before').color), hex(getComputedStyle(span).color), kind === 'deluxe' ? hex(getComputedStyle(el, '::after').color) : null, g]);
      return;
    }
    if (el.classList.contains('logo')) {
      out.push(['l', ...b, hex(getComputedStyle(el, '::before').backgroundColor), hex(getComputedStyle(el, '::after').backgroundColor), g]);
      return;
    }
    const mask = cs.webkitMaskImage || cs.maskImage;
    if (mask && mask !== 'none') {
      const src = mask.match(/img\/([^")]+)/)?.[1];
      out.push(['m', ...b, src, hex(cs.backgroundColor), g]);
      return;
    }
    // background / borders / shadows
    const bg = hex(cs.backgroundColor);
    const clip = cs.clipPath;
    if (clip && clip.startsWith('polygon') && bg) {
      const pts = clip.slice(8, -1).split(',').map(p => p.trim().split(/\s+/).map((v, i) => v.endsWith('%') ? parseFloat(v) / 100 * (i ? r.height : r.width) : parseFloat(v)));
      out.push(['p', ...b, 'M ' + pts.map(([x, y]) => `${R(x * 10) / 10} ${R(y * 10) / 10}`).join(' L ') + ' Z', bg, g]);
    } else {
      const { inset, drop } = shadows(cs, b);
      const rad = parseFloat(cs.borderTopLeftRadius) || 0;
      const bw = ['Top', 'Right', 'Bottom', 'Left'].map(s => cs[`border${s}Style`] !== 'none' ? parseFloat(cs[`border${s}Width`]) : 0);
      const bcol = ['Top', 'Right', 'Bottom', 'Left'].map(s => hex(cs[`border${s}Color`]));
      const uniform = bw.every(w => w === bw[0]) && bcol.every(c => c === bcol[0]) && bw[0] > 0;
      if (bg || (uniform && bcol[0]) || drop) out.push(['r', ...b, bg, 1, rad, uniform ? bcol[0] : null, uniform ? bw[0] : 0, drop, g]);
      if (!uniform) {
        const [x, y, w, h] = b;
        if (bw[0] && bcol[0]) out.push(['r', x, y, w, R(bw[0]), bcol[0], 1, 0, null, 0, null, g]);
        if (bw[2] && bcol[2]) out.push(['r', x, y + h - R(bw[2]), w, R(bw[2]), bcol[2], 1, 0, null, 0, null, g]);
        if (bw[3] && bcol[3]) out.push(['r', x, y, R(bw[3]), h, bcol[3], 1, 0, null, 0, null, g]);
        if (bw[1] && bcol[1]) out.push(['r', x + w - R(bw[1]), y, R(bw[1]), h, bcol[1], 1, 0, null, 0, null, g]);
      }
      // inset shadow rings (e.g. board inner lines)
      let prev = 0;
      for (const s of inset) {
        if (s.col && s.col !== bg && s.spread > prev) {
          const [x, y, w, h] = b, t = s.spread - prev;
          out.push(['r', x + prev, y + prev, w - 2 * prev, h - 2 * prev, null, 1, 0, s.col, t, null, g]);
        }
        prev = s.spread;
      }
    }
    pseudo(el, '::before', b); pseudo(el, '::after', b);

    if (el.tagName === 'IMG') {
      const nw = el.naturalWidth, nh = el.naturalHeight, W = r.width, H = r.height;
      const [px, py] = cs.objectPosition.split(' ').map(v => parseFloat(v) / 100);
      let crop = [1, 1, 0, 0];
      if (cs.objectFit === 'cover' && nw && nh) {
        const s = Math.max(W / nw, H / nh), fx = W / (nw * s), fy = H / (nh * s);
        crop = [+fx.toFixed(4), +fy.toFixed(4), +((1 - fx) * px).toFixed(4), +((1 - fy) * py).toFixed(4)];
      } else if (cs.objectFit === 'contain') crop = 'fit';
      out.push(['i', ...b, el.getAttribute('src').replace(/^img\//, ''), crop, parseFloat(cs.borderTopLeftRadius) || 0, g]);
      return;
    }
    if (el.tagName === 'INPUT') {
      const pc = getComputedStyle(el, '::placeholder');
      const pl = parseFloat(cs.paddingLeft) + parseFloat(cs.borderLeftWidth);
      const fs = parseFloat(cs.fontSize);
      out.push(['t', b[0] + R(pl), b[1] + R((r.height - fs * 1.3) / 2), R(r.width - pl * 2), R(fs * 1.3), [[el.placeholder, fi(fontName(cs)), hex(pc.color) || '#888888', 0]], 'left', 0, 0, 1, g]);
      return;
    }
    if (cs.display !== 'inline') {
      const runs = textRuns(el);
      if (runs) {
        const pl = parseFloat(cs.paddingLeft) + parseFloat(cs.borderLeftWidth), pr = parseFloat(cs.paddingRight) + parseFloat(cs.borderRightWidth);
        const pt = parseFloat(cs.paddingTop) + parseFloat(cs.borderTopWidth), pb = parseFloat(cs.paddingBottom) + parseFloat(cs.borderBottomWidth);
        const rg = document.createRange(); rg.selectNodeContents(el);
        const tops = new Set([...rg.getClientRects()].filter(q => q.width > 0.5).map(q => Math.round(q.top / 4)));
        const lh = cs.lineHeight === 'normal' ? 0 : parseFloat(cs.lineHeight);
        const oneLine = tops.size <= 1 || cs.whiteSpace === 'nowrap' ? 1 : 0;
        const align = cs.textAlign === 'center' ? 'center' : (cs.textAlign === 'right' || cs.textAlign === 'end') ? 'right' : 'left';
        const cb = { left: r.left + pl, top: r.top + pt, width: r.width - pl - pr, height: r.height - pt - pb };
        out.push(['t', ...box(cb), runs, align, R(lh * 10) / 10,
          cs.letterSpacing === 'normal' ? 0 : +parseFloat(cs.letterSpacing).toFixed(2), oneLine, g]);
      }
    }
    for (const c of el.children) {
      const ccs = getComputedStyle(c);
      if (ccs.display === 'inline' && c.tagName !== 'IMG' && !c.classList.contains('chroma') && !c.classList.contains('logo') && !(ccs.webkitMaskImage && ccs.webkitMaskImage !== 'none') && ![...c.querySelectorAll('img,.chroma,.logo,input')].length && hex(ccs.backgroundColor) == null) continue;
      visit(c);
    }
  }

  // section background
  const out0 = [];
  visit(sec);
  const gs = groups.filter(gg => sec.contains(gg.el)).map(gg => { const b = box(gg.el.getBoundingClientRect()); return [+gg.el.dataset.g, b[0] + b[2] / 2, b[1] + b[3] / 2, b[2], b[3], +gg.deg.toFixed(2)]; });
  restore.forEach(([el, t]) => { el.style.transform = t; delete el.dataset.g; });
  kill.remove();
  return { i: sectionIndex, x: R(ox), bodyBg: hex(getComputedStyle(document.body).backgroundColor), pageH: document.documentElement.scrollHeight, name: (sec.getAttribute('aria-label') || sec.className || sec.tagName).toString().slice(0, 40), y: R(oy), h: R(sr.height), clip: secCS.overflow !== 'visible' || secCS.overflowX === 'clip' ? 1 : 0, fonts, groups: gs, nodes: out };
}
