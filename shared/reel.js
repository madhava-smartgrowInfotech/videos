// Reel harness: registers the GSAP master timeline and exposes a deterministic
// seek API for render.mjs. Opened without ?render it plays as a looping preview.
//
//   ?render  frame-accurate mode: timeline paused, driven by window.__seek(t)
//   ?safe    overlays the Instagram Reels UI zones (also toggled with "s" in preview)
window.Reel = (() => {
  const params = new URLSearchParams(location.search);
  const RENDER = params.has('render');
  const DURATION = 10;
  const W = 1080, H = 1920;
  // Text and logos must stay inside this box; backgrounds may bleed full-frame.
  const SAFE = { left: 80, right: 1000, top: 260, bottom: 1480 };

  const stage = () => document.getElementById('stage');

  const ready = (async () => {
    if (document.readyState === 'loading') {
      await new Promise(r => document.addEventListener('DOMContentLoaded', r, { once: true }));
    }
    await Promise.all([...document.fonts].map(f => f.load().catch(() => {})));
    await document.fonts.ready;
    await Promise.all([...document.images].map(img => (img.decode ? img.decode().catch(() => {}) : null)));
  })();

  function safeOverlay(show) {
    let el = document.getElementById('__safe');
    if (!show) { if (el) el.remove(); return; }
    if (el) return;
    el = document.createElement('div');
    el.id = '__safe';
    el.style.cssText = `position:absolute;inset:0;z-index:99999;pointer-events:none;font:600 22px Inter,sans-serif;color:#fff;`;
    const zone = (x, y, w, h, label) =>
      `<div style="position:absolute;left:${x}px;top:${y}px;width:${w}px;height:${h}px;background:rgba(255,0,60,.28);outline:2px dashed rgba(255,0,60,.9);display:flex;align-items:center;justify-content:center;text-shadow:0 1px 3px #000">${label}</div>`;
    el.innerHTML =
      zone(0, 0, W, SAFE.top, 'IG header') +
      zone(0, SAFE.bottom, W, H - SAFE.bottom, 'IG caption / audio') +
      zone(SAFE.right - 60, 1050, W - SAFE.right + 60, SAFE.bottom - 1050, '') +
      `<div style="position:absolute;left:${SAFE.left}px;top:${SAFE.top}px;width:${SAFE.right - SAFE.left}px;height:${SAFE.bottom - SAFE.top}px;outline:2px dashed rgba(0,200,120,.9)"></div>`;
    stage().appendChild(el);
  }

  function fit() {
    const s = Math.min(innerWidth / W, innerHeight / H);
    const st = stage();
    st.style.transform = `translate(${(innerWidth - W * s) / 2}px, ${(innerHeight - H * s) / 2}px) scale(${s})`;
  }

  function register(tl) {
    tl.pause(0);
    const d = tl.duration();
    if (Math.abs(d - DURATION) > 0.01) console.warn(`[reel] timeline is ${d.toFixed(3)}s, expected ${DURATION}s`);
    window.__duration = DURATION;
    window.__timelineDuration = d;
    window.__seek = t => { tl.seek(Math.max(0, Math.min(DURATION, t)), false); };
    window.__ready = ready.then(() => { tl.seek(0, false); return true; });
    if (params.has('safe')) ready.then(() => safeOverlay(true));

    if (!RENDER) {
      ready.then(() => {
        fit();
        addEventListener('resize', fit);
        tl.eventCallback('onComplete', () => gsap.delayedCall(0.8, () => tl.play(0)));
        tl.play(0);
        addEventListener('keydown', e => {
          if (e.key === ' ') tl.paused(!tl.paused());
          if (e.key === 's') safeOverlay(!document.getElementById('__safe'));
          if (e.key === 'ArrowRight') { tl.pause(); tl.seek(Math.min(DURATION, tl.time() + 1 / 30), false); }
          if (e.key === 'ArrowLeft') { tl.pause(); tl.seek(Math.max(0, tl.time() - 1 / 30), false); }
        });
      });
    }
    return tl;
  }

  return { register, ready, RENDER, DURATION, W, H, SAFE };
})();
