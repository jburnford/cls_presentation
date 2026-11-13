"""Record scripted clips of Jessica's railway visualizations for the CLS deck.

Serves the local Sask_Railway_Visualizations repo and drives each page with
Playwright. The page's clock (Date, timers, requestAnimationFrame) is frozen and
advanced exactly one frame at a time, with a screenshot after each step, so the
clips play smoothly at 25 fps however long each screenshot takes. Output: an
H.264 MP4, a VP9 WebM and a final-frame JPEG poster per clip.

Needs playwright and imageio-ffmpeg (pip install playwright imageio-ffmpeg).
usage: python3 scripts/record_jessica_clips.py <Sask_Railway_Visualizations dir> images/jessica [clip ...]
"""
import os, shutil, subprocess, sys, tempfile, time
import imageio_ffmpeg
from playwright.sync_api import sync_playwright

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
FPS = 25
STEP = 1000 // FPS
W, H, DSF = 1280, 720, 1.5

SET_YEAR = """y => { const s = document.getElementById('yearSlider');
  s.value = y; s.dispatchEvent(new Event('input', {bubbles: true}));
  s.dispatchEvent(new Event('change', {bubbles: true})); }"""

def eh_setup(pg):
    for b in pg.query_selector_all(".filter-btn"):
        b.click()

def click(sel):
    return lambda p: p.click(sel)

# Each clip: page, setup before recording, (ms, action) steps, total length in ms.
CLIPS = {
    "one-hour-corridor": dict(page="one_hour_map", setup=None,
        steps=[(1000, click("#playBtn"))], length=12000),
    "network-graph": dict(page="network_graph", viewport=(1600, 900),
        setup=lambda p: p.evaluate(SET_YEAR, 1920),
        steps=[(2000, click("#forceBtn"))] +
              [(5200 + 70 * i, lambda p: (p.mouse.move(560, 520), p.mouse.wheel(0, 40))) for i in range(18)] +
              [(6700, lambda p: p.mouse.move(1590, 890))],
        length=11500),
    "railway-timeline": dict(page="railway_timeline", setup=None,
        steps=[(800, click("#playBtn"))], length=14500),
    "economic-hierarchy": dict(page="economic_hierarchy", setup=eh_setup,
        steps=[(800 + 1100 * i, click(f'.filter-btn[data-tier="{t}"]'))
               for i, t in enumerate(["City", "RSC", "LSC", "SSC", "GH", "ES"])], length=10500),
    "time-warped-cartogram": dict(page="demo_cartogram",
        setup=lambda p: p.evaluate("""() => { const s = document.getElementById('speedSlider');
            s.value = 1; s.dispatchEvent(new Event('input', {bubbles: true})); }"""),
        steps=[(1500, click("#animateBtn"))], length=9000),
}

def encode(frames_dir, out_dir, name):
    src = ["-framerate", str(FPS), "-i", os.path.join(frames_dir, "f%05d.jpg")]
    mp4 = os.path.join(out_dir, f"{name}.mp4")
    webm = os.path.join(out_dir, f"{name}.webm")
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", *src, "-c:v", "libx264", "-preset", "slow",
                    "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", mp4], check=True)
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", *src, "-c:v", "libvpx-vp9", "-b:v", "0",
                    "-crf", "34", "-row-mt", "1", "-pix_fmt", "yuv420p", webm], check=True)
    return mp4, webm

def record(pg, clip, out_dir, name):
    frames_dir = tempfile.mkdtemp(prefix=f"{name}-", dir=out_dir)
    steps = sorted(clip["steps"], key=lambda s: s[0])
    n = clip["length"] // STEP
    for k in range(n):
        t = k * STEP
        while steps and steps[0][0] <= t:
            steps.pop(0)[1](pg)
        pg.clock.run_for(STEP)
        pg.screenshot(path=os.path.join(frames_dir, f"f{k:05d}.jpg"), type="jpeg", quality=92)
    shutil.copy(os.path.join(frames_dir, f"f{n - 1:05d}.jpg"), os.path.join(out_dir, f"{name}-poster.jpg"))
    mp4, webm = encode(frames_dir, out_dir, name)
    shutil.rmtree(frames_dir)
    print(f"{name}: {n} frames, mp4 {os.path.getsize(mp4)//1024} KB, webm {os.path.getsize(webm)//1024} KB")

def main():
    repo, out_dir = sys.argv[1], sys.argv[2]
    names = sys.argv[3:] or list(CLIPS)
    os.makedirs(out_dir, exist_ok=True)
    srv = subprocess.Popen([sys.executable, "-m", "http.server", "8765", "--bind", "127.0.0.1"],
                           cwd=repo, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.5)
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            for name in names:
                clip = CLIPS[name]
                vw, vh = clip.get("viewport", (W, H))
                ctx = b.new_context(viewport={"width": vw, "height": vh}, device_scale_factor=W * DSF / vw)
                pg = ctx.new_page()
                pg.clock.install()
                pg.goto(f"http://127.0.0.1:8765/{clip['page']}.html", wait_until="networkidle", timeout=60000)
                # Let start-up timers run, and give map tiles real time to arrive.
                for _ in range(30):
                    pg.clock.run_for(100)
                    pg.wait_for_timeout(100)
                if clip["setup"]:
                    clip["setup"](pg)
                    for _ in range(30):
                        pg.clock.run_for(100)
                        pg.wait_for_timeout(100)
                record(pg, clip, out_dir, name)
                ctx.close()
            b.close()
    finally:
        srv.terminate()

if __name__ == "__main__":
    main()
