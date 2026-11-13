"""Screenshot Jessica's slides at 1280x720 (final frames) and flag overflow.

Steps through the section with Reveal.next(), as a presenter would, waits for
each clip to finish, and saves one PNG per slide. Uses installed Google Chrome
(Playwright channel "chrome") because it plays the MP4 clips.

usage: quarto render slides.qmd && python3 scripts/check_jessica_slides.py docs <out_dir>
"""
import os, subprocess, sys, time
from playwright.sync_api import sync_playwright

docs, out = sys.argv[1], sys.argv[2]
IDS = ["jessica-divider", "jessica-start", "jessica-timeline", "jessica-flattening", "jessica-old",
       "jessica-loop", "jessica-corridor", "jessica-network", "jessica-team", "jessica-fails", "jessica-hierarchy",
       "jessica-scale", "jessica-judgement", "jessica-question"]

OVERFLOW = """() => {
  const s = Reveal.getCurrentSlide();
  const box = document.querySelector('.reveal .slides').getBoundingClientRect();
  const bad = [];
  s.querySelectorAll('*').forEach(e => {
    if (e.closest('.notes') || e.classList.contains('motion-replay')) return;
    const r = e.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return;
    if (r.bottom > box.bottom + 2 || r.right > box.right + 2)
      bad.push(`${e.tagName.toLowerCase()}.${[...e.classList].join('.')} bottom=${Math.round(r.bottom - box.bottom)} right=${Math.round(r.right - box.right)}`);
  });
  return bad.slice(0, 5);
}"""

# Python's built-in http.server can't answer HTTP Range requests, which Chrome needs for <video>.
srv = subprocess.Popen([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "range_server.py"),
                        docs, "8766"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2)
try:
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": 1280, "height": 720})
        pg.goto("http://127.0.0.1:8766/slides.html", wait_until="networkidle")
        pg.wait_for_function("window.Reveal && Reveal.isReady && Reveal.isReady()")
        for i, sid in enumerate(IDS):
            if i == 0:
                pg.evaluate(f"location.hash = '#/{sid}'")
            else:
                pg.evaluate("Reveal.next()")
            cur = pg.evaluate("Reveal.getCurrentSlide().id")
            assert cur == sid, (cur, sid)
            pg.wait_for_timeout(9000 if sid in ("jessica-timeline", "jessica-loop", "jessica-fails") else 1500)
            vids = pg.evaluate("() => [...Reveal.getCurrentSlide().querySelectorAll('video')].map(v => ({t: +v.currentTime.toFixed(1), playing: !v.paused}))")
            if vids:
                print(f"   video after 1.5 s: {vids}")
                pg.wait_for_timeout(13000)  # let the clip reach its final frame
            pg.screenshot(path=f"{out}/{i+1:02d}-{sid}.png")
            bad = pg.evaluate(OVERFLOW)
            print(f"{i+1:02d} {sid}: {'OK' if not bad else 'OVERFLOW ' + '; '.join(bad)}")
        b.close()
finally:
    srv.terminate()
