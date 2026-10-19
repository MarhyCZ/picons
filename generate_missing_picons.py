#!/usr/bin/env python3
"""
Generate missing CZ/SK picons in Marhy's signature flat rectangular style:
- 640x640 px and 1024x1024 px PNG
- Solid brand-colored background
- Clean, centered white silhouette logo (~70% bounding box)
"""

import os
import sys
import subprocess
import urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

BASE_DIR = "/Users/ondre/Projects/picons"
DIR_640 = os.path.join(BASE_DIR, "640")
DIR_1024 = os.path.join(BASE_DIR, "1024")
TMP_DIR = "/tmp/picon_sources"

os.makedirs(TMP_DIR, exist_ok=True)
os.makedirs(DIR_640, exist_ok=True)
os.makedirs(DIR_1024, exist_ok=True)

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def render_html_to_png(html_content, out_path, size):
    html_file = os.path.join(TMP_DIR, f"temp_{size}.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    cmd = [
        CHROME_BIN,
        "--headless",
        "--disable-gpu",
        f"--screenshot={out_path}",
        f"--window-size={size},{size}",
        html_file
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

def download_file(url, local_path):
    if not os.path.exists(local_path):
        req = urllib.request.Request(url, headers={"User-Agent": "AntigravityBot/1.0 (ondrej.hala@roboton.com)"})
        with urllib.request.urlopen(req) as resp, open(local_path, "wb") as out:
            out.write(resp.read())
    return local_path

def create_picon_from_mask(mask_img, bg_hex, base_name):
    """Takes a mask image (L or alpha), centers white logo on bg_hex for 640 and 1024."""
    for size, out_dir in [(640, DIR_640), (1024, DIR_1024)]:
        canvas = Image.new("RGBA", (size, size), bg_hex)
        max_w = int(size * 0.70)
        max_h = int(size * 0.70)
        
        # Scale mask
        w, h = mask_img.size
        ratio = min(max_w / w, max_h / h)
        new_w, new_h = max(1, int(w * ratio)), max(1, int(h * ratio))
        scaled_mask = mask_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # White logo
        white = Image.new("RGBA", (new_w, new_h), (255, 255, 255, 255))
        pos_x = (size - new_w) // 2
        pos_y = (size - new_h) // 2
        
        canvas.paste(white, (pos_x, pos_y), scaled_mask)
        out_path = os.path.join(out_dir, f"{base_name}.png")
        canvas.save(out_path, "PNG")
    print(f"Generated {base_name}.png (640 & 1024)")

def make_symlink(src_name, target_name):
    for d in [DIR_640, DIR_1024]:
        src = os.path.join(d, f"{src_name}.png")
        dst = os.path.join(d, f"{target_name}.png")
        if os.path.exists(dst) or os.path.islink(dst):
            os.remove(dst)
        if os.path.exists(src):
            os.link(src, dst)
            print(f"Linked {target_name}.png -> {src_name}.png in {os.path.basename(d)}")

# 1. Existing channels that just need symlinks
print("--- 1. Symlinking existing channels ---")
make_symlink("seznamcz", "seznamcztv")
make_symlink("seznamcz", "seznamcztvt2")
make_symlink("slagrtv", "slageroriginal")
make_symlink("slagr2", "slagermuzika")

# 2. Warner TV
print("--- 2. Generating Warner TV ---")
warnertv_raw = download_file(
    "https://upload.wikimedia.org/wikipedia/commons/c/c9/WarnerTV_2021.png",
    os.path.join(TMP_DIR, "warnertv_raw.png")
)
w_im = Image.open(warnertv_raw).convert("RGBA")
_, _, _, w_mask = w_im.split()
create_picon_from_mask(w_mask, "#002244", "warnertv")
make_symlink("warnertv", "test4")

# Nova Krimi
print("--- 2b. Generating Nova Krimi ---")
novakrimi_raw = download_file(
    "https://upload.wikimedia.org/wikipedia/commons/7/7b/Logo_Nova_Krimi.png",
    os.path.join(TMP_DIR, "novakrimi_raw.png")
)
raw_nk = Image.open(novakrimi_raw).convert("RGB")
bg_nk = (128, 54, 38)
mask_nk = Image.new("L", raw_nk.size, 0)
for x in range(raw_nk.width):
    for y in range(raw_nk.height):
        px = raw_nk.getpixel((x, y))
        if max(abs(px[0]-bg_nk[0]), abs(px[1]-bg_nk[1]), abs(px[2]-bg_nk[2])) > 35:
            mask_nk.putpixel((x, y), 255)
mask_nk = mask_nk.crop(mask_nk.getbbox())
create_picon_from_mask(mask_nk, "#800020", "novakrimi")

# 12. Český Impuls
print("--- 12. Generating Český Impuls ---")
ci_html = """<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#0b2545;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="font-family:'Arial Black', Impact, sans-serif;font-size:16vw;font-weight:900;color:#ffffff;line-height:0.9;letter-spacing:-0.5vw;">ČESKÝ</div>
<div style="font-family:'Arial Black', Impact, sans-serif;font-size:16vw;font-weight:900;color:#f5a623;line-height:0.9;letter-spacing:-0.5vw;margin-top:1.5vh;">IMPULS</div>
<div style="font-family:'Helvetica Neue', Arial, sans-serif;font-size:6.5vw;font-weight:700;color:#ffffff;letter-spacing:0.8vw;margin-top:2.5vh;">RÁDIO PRO POHODU</div>
</body></html>"""
render_html_to_png(ci_html, os.path.join(DIR_640, "ceskyimpuls.png"), 640)
render_html_to_png(ci_html, os.path.join(DIR_1024, "ceskyimpuls.png"), 1024)

# 13. Radio Čas & Čas Rock
print("--- 13. Generating Radio Čas & Rock ---")
cas_svg_path = download_file(
    "https://upload.wikimedia.org/wikipedia/commons/e/ed/Logo_Radio_%C4%8Cas.svg",
    os.path.join(TMP_DIR, "radio_cas.svg")
)
with open(cas_svg_path, "r", encoding="utf-8") as f:
    cas_svg = f.read()
import re
cas_svg_scalable = re.sub(r'(width|height)="[^"]+"', '', cas_svg)

cas_html = f"""<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#ffc107;display:flex;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="width:72vw;height:auto;filter:brightness(0) invert(1);">
{cas_svg_scalable}
</div>
</body></html>"""
render_html_to_png(cas_html, os.path.join(DIR_640, "radiocas.png"), 640)
render_html_to_png(cas_html, os.path.join(DIR_1024, "radiocas.png"), 1024)

cas_rock_html = f"""<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#1a1a1a;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="width:68vw;height:auto;filter:brightness(0) invert(1);">
{cas_svg_scalable}
</div>
<div style="font-family:'Arial Black', Impact, sans-serif;font-size:14vw;font-weight:900;color:#ffffff;letter-spacing:1vw;margin-top:2vh;">ROCK</div>
</body></html>"""
render_html_to_png(cas_rock_html, os.path.join(DIR_640, "radiocasrock.png"), 640)
render_html_to_png(cas_rock_html, os.path.join(DIR_1024, "radiocasrock.png"), 1024)

# 15. Radio Dechovka
print("--- 15. Generating Radio Dechovka ---")
dechovka_raw = download_file(
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_Radia_Dechovka_s_kmito%C4%8Dty.png",
    os.path.join(TMP_DIR, "dechovka_raw.png")
)
raw_dec = Image.open(dechovka_raw).convert("RGBA")
alpha_dec = raw_dec.split()[3].crop(raw_dec.split()[3].getbbox())
w_d, h_d = alpha_dec.size
mask_dec = alpha_dec.crop((0, 0, w_d, int(h_d * 0.68)))
create_picon_from_mask(mask_dec, "#800020", "radiodechovka")

# 17. Ukrajinske Radio
print("--- 17. Generating Ukrajinske Radio ---")
ukr_html = """<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#0057b7;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="border:1vw solid #ffffff;border-radius:2.5vw;padding:2vw 5vw;text-align:center;">
  <div style="font-family:'Helvetica Neue', Arial, sans-serif;font-size:9vw;font-weight:900;color:#ffffff;letter-spacing:0.5vw;">УКРАЇНСЬКЕ</div>
  <div style="font-family:'Arial Black', Impact, sans-serif;font-size:18vw;font-weight:900;color:#ffffff;line-height:0.9;margin-top:1vh;">РАДІО</div>
</div>
</body></html>"""
render_html_to_png(ukr_html, os.path.join(DIR_640, "ukrajinskeradio.png"), 640)
render_html_to_png(ukr_html, os.path.join(DIR_1024, "ukrajinskeradio.png"), 1024)

# 3. A11
print("--- 3. Generating A11 ---")
a11_html = """<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#0055b8;display:flex;align-items:center;justify-content:center;width:100vw;height:100vh;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 460" style="width:70vw;height:auto;fill:#ffffff;">
<path d="m509.4 207.7l-74-88.6q19.2-15.9 41.2-36.3 22-20.3 43.1-42 21-21.7 36.3-40.1h140.4v458.6h-127.6v-303.2q-11.5 13.4-27.1 26.8-15.7 13.3-32.3 24.8z"></path>
<path d="m813 207.7l-74-88.6q19.2-15.9 41.2-36.3 22-20.3 43-42 21.1-21.7 36.4-40.1h140.4v458.6h-127.6v-303.2q-11.5 13.4-27.1 26.8-15.7 13.3-32.3 24.8z"></path>
<path d="m215.8 459.3h-135.3l154.5-458.6h157l154.5 458.6h-134.7l-26.2-82.3h-143.6zm44.7-172.9h95.1l-47.2-149.3z"></path>
</svg>
</body></html>"""
render_html_to_png(a11_html, os.path.join(DIR_640, "a11.png"), 640)
render_html_to_png(a11_html, os.path.join(DIR_1024, "a11.png"), 1024)
print("Generated a11.png (640 & 1024)")

# 4. JTV (Jihočeská televize)
print("--- 4. Generating JTV ---")
jtv_raw = download_file(
    "https://upload.wikimedia.org/wikipedia/commons/f/f0/Logo_JTV.png",
    os.path.join(TMP_DIR, "jtv_raw.png")
)
jtv_im = Image.open(jtv_raw).convert("RGBA")
# JTV logo has alpha channel
_, _, _, jtv_mask = jtv_im.split()
create_picon_from_mask(jtv_mask, "#004b97", "jtv")

# 5. JC 1 and JC 2
print("--- 5. Generating JC 1 & JC 2 ---")
jc1_raw = download_file(
    "https://www.jc1.cz/images/J1_strnky.png",
    os.path.join(TMP_DIR, "jc1_raw.png")
)
jc1_im = Image.open(jc1_raw).convert("RGBA")
# In J1_strnky.png, convert light/white to alpha
jc1_gray = ImageOps.invert(jc1_im.convert("L"))
# threshold
jc1_mask = jc1_gray.point(lambda p: 255 if p > 100 else 0)
create_picon_from_mask(jc1_mask, "#0080c0", "jc1")

# JC 2: clean badge with JČ2
jc2_html = """<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#0080c0;display:flex;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="font-family:'Helvetica Neue', Arial, sans-serif;font-size:32vw;font-weight:900;color:#ffffff;letter-spacing:-1vw;">JČ2</div>
</body></html>"""
render_html_to_png(jc2_html, os.path.join(DIR_640, "jc2.png"), 640)
render_html_to_png(jc2_html, os.path.join(DIR_1024, "jc2.png"), 1024)
print("Generated jc2.png (640 & 1024)")

# 6. Prima sport
print("--- 6. Generating Prima sport ---")
# Use the official Prima logo paths from prima.svg and add SPORT
prima_svg_path = os.path.join(BASE_DIR, "source/svg/CZ-SK/prima.svg")
with open(prima_svg_path, "r", encoding="utf-8") as f:
    prima_svg = f.read()
# extract inner svg content
prima_sport_html = f"""<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#f36917;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="width:65vw;height:auto;display:flex;justify-content:center;">
{prima_svg.replace('class="cls-1"', 'style="display:none;"').replace('viewBox="0 0 283.46 283.46"', 'viewBox="40 100 200 90" style="width:100%;height:auto;"')}
</div>
<div style="font-family:'Arial Black', Impact, sans-serif;font-size:11vw;font-weight:900;color:#ffffff;letter-spacing:1.2vw;margin-top:2vh;">SPORT</div>
</body></html>"""
render_html_to_png(prima_sport_html, os.path.join(DIR_640, "primasport.png"), 640)
render_html_to_png(prima_sport_html, os.path.join(DIR_1024, "primasport.png"), 1024)
print("Generated primasport.png (640 & 1024)")

# 7. Hit TV & Test 5
print("--- 7. Generating Hit TV ---")
hittv_html = """<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#d90429;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="border:1.2vw solid #ffffff;border-radius:3vw;padding:2vw 6vw;display:flex;flex-direction:column;align-items:center;">
  <div style="font-family:'Arial Black', Impact, sans-serif;font-size:20vw;font-weight:900;color:#ffffff;line-height:0.85;letter-spacing:-0.5vw;">HIT</div>
  <div style="font-family:'Helvetica Neue', Arial, sans-serif;font-size:9vw;font-weight:900;color:#ffffff;letter-spacing:1.5vw;margin-top:1vw;">TELEVIZE</div>
</div>
</body></html>"""
render_html_to_png(hittv_html, os.path.join(DIR_640, "hittv.png"), 640)
render_html_to_png(hittv_html, os.path.join(DIR_1024, "hittv.png"), 1024)
make_symlink("hittv", "test5")

# 8. ABC TV
print("--- 8. Generating ABC TV ---")
abctv_html = """<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#00509d;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="display:flex;align-items:baseline;">
  <span style="font-family:'Arial Black', Impact, sans-serif;font-size:24vw;font-weight:900;color:#ffffff;letter-spacing:-1vw;">ABC</span>
  <span style="font-family:'Helvetica Neue', Arial, sans-serif;font-size:12vw;font-weight:900;color:#ffffff;margin-left:2vw;">TV</span>
</div>
</body></html>"""
render_html_to_png(abctv_html, os.path.join(DIR_640, "abctv.png"), 640)
render_html_to_png(abctv_html, os.path.join(DIR_1024, "abctv.png"), 1024)
print("Generated abctv.png (640 & 1024)")

# 9. ČRo Pohoda
print("--- 9. Generating ČRo Pohoda ---")
pohoda_svg_path = download_file(
    "https://upload.wikimedia.org/wikipedia/commons/8/84/%C4%8CRo_Pohoda_Logo_2021.svg",
    os.path.join(TMP_DIR, "cro_pohoda.svg")
)
with open(pohoda_svg_path, "r", encoding="utf-8") as f:
    pohoda_svg = f.read()

pohoda_html = f"""<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#800080;display:flex;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="width:70vw;height:auto;filter:brightness(0) invert(1);">
{pohoda_svg}
</div>
</body></html>"""
render_html_to_png(pohoda_html, os.path.join(DIR_640, "cropohodat2.png"), 640)
render_html_to_png(pohoda_html, os.path.join(DIR_1024, "cropohodat2.png"), 1024)
make_symlink("cropohodat2", "cropohoda")

# 10. ČRo Radiožurnál Sport
print("--- 10. Generating ČRo Radiožurnál Sport ---")
rz_sport_svg_path = download_file(
    "https://upload.wikimedia.org/wikipedia/commons/6/6b/%C4%8CRo_Radio%C5%BEurn%C3%A1l_Sport_Logo_2021.svg",
    os.path.join(TMP_DIR, "cro_rz_sport.svg")
)
with open(rz_sport_svg_path, "r", encoding="utf-8") as f:
    rz_sport_svg = f.read()

rz_sport_html = f"""<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#00a651;display:flex;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="width:70vw;height:auto;filter:brightness(0) invert(1);">
{rz_sport_svg}
</div>
</body></html>"""
render_html_to_png(rz_sport_html, os.path.join(DIR_640, "crorzsportt2.png"), 640)
render_html_to_png(rz_sport_html, os.path.join(DIR_1024, "crorzsportt2.png"), 1024)
make_symlink("crorzsportt2", "croradiozurnalsport")

# 11. Radio Impuls
print("--- 11. Generating Radio Impuls ---")
impuls_raw = download_file(
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/R%C3%A1dio_Impuls.png",
    os.path.join(TMP_DIR, "impuls_raw.png")
)
imp_im = Image.open(impuls_raw).convert("RGBA")
# Impuls logo: convert non-transparent pixels to mask
_, _, _, imp_mask = imp_im.split()
create_picon_from_mask(imp_mask, "#f5a623", "radioimpuls")

# 12. Český Impuls
print("--- 12. Generating Český Impuls ---")
cesky_impuls_raw = download_file(
    "https://upload.wikimedia.org/wikipedia/commons/2/23/%C4%8Cesk%C3%BD_Impuls.png",
    os.path.join(TMP_DIR, "cesky_impuls_raw.png")
)
ci_im = Image.open(cesky_impuls_raw).convert("RGBA")
_, _, _, ci_mask = ci_im.split()
create_picon_from_mask(ci_mask, "#0b2545", "ceskyimpuls")

# 13. Radio Čas
print("--- 13. Generating Radio Čas ---")
cas_svg_path = download_file(
    "https://upload.wikimedia.org/wikipedia/commons/e/ed/Logo_Radio_%C4%8Cas.svg",
    os.path.join(TMP_DIR, "radio_cas.svg")
)
with open(cas_svg_path, "r", encoding="utf-8") as f:
    cas_svg = f.read()

cas_html = f"""<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#ffc107;display:flex;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="width:70vw;height:auto;filter:brightness(0) invert(1);">
{cas_svg}
</div>
</body></html>"""
render_html_to_png(cas_html, os.path.join(DIR_640, "radiocas.png"), 640)
render_html_to_png(cas_html, os.path.join(DIR_1024, "radiocas.png"), 1024)
print("Generated radiocas.png (640 & 1024)")

# 14. Radio Čas Rock
print("--- 14. Generating Radio Čas Rock ---")
cas_rock_html = f"""<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#1a1a1a;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="width:65vw;height:auto;filter:brightness(0) invert(1);">
{cas_svg}
</div>
<div style="font-family:'Arial Black', Impact, sans-serif;font-size:13vw;font-weight:900;color:#e63946;letter-spacing:1vw;margin-top:2vh;">ROCK</div>
</body></html>"""
render_html_to_png(cas_rock_html, os.path.join(DIR_640, "radiocasrock.png"), 640)
render_html_to_png(cas_rock_html, os.path.join(DIR_1024, "radiocasrock.png"), 1024)
print("Generated radiocasrock.png (640 & 1024)")

# 15. Radio Dechovka
print("--- 15. Generating Radio Dechovka ---")
dechovka_raw = download_file(
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/Logo_Radia_Dechovka_s_kmito%C4%8Dty.png",
    os.path.join(TMP_DIR, "dechovka_raw.png")
)
dec_im = Image.open(dechovka_raw).convert("RGBA")
# invert and threshold for mask
dec_gray = dec_im.convert("L")
dec_mask = dec_gray.point(lambda p: 255 if p < 180 else 0)
create_picon_from_mask(dec_mask, "#800020", "radiodechovka")

# 16. Rock Zone 105,9
print("--- 16. Generating Rock Zone 105,9 ---")
rockzone_html = """<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#111111;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="font-family:'Arial Black', Impact, sans-serif;font-size:16vw;font-weight:900;color:#ffffff;line-height:0.9;letter-spacing:-0.5vw;">ROCK</div>
<div style="font-family:'Arial Black', Impact, sans-serif;font-size:16vw;font-weight:900;color:#ffffff;line-height:0.9;letter-spacing:-0.5vw;">ZONE</div>
<div style="font-family:'Helvetica Neue', Arial, sans-serif;font-size:8vw;font-weight:900;color:#ff0055;letter-spacing:0.8vw;margin-top:1.5vh;">105.9 FM</div>
</body></html>"""
render_html_to_png(rockzone_html, os.path.join(DIR_640, "rockzone1059.png"), 640)
render_html_to_png(rockzone_html, os.path.join(DIR_1024, "rockzone1059.png"), 1024)
make_symlink("rockzone1059", "rockzone")

# 17. Ukrajinske Radio
print("--- 17. Generating Ukrajinske Radio ---")
ukr_html = """<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#0057b7;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="border:1vw solid #ffffff;border-radius:2.5vw;padding:2vw 5vw;text-align:center;">
  <div style="font-family:'Helvetica Neue', Arial, sans-serif;font-size:9vw;font-weight:900;color:#ffffff;letter-spacing:0.5vw;">УКРАЇНСЬКЕ</div>
  <div style="font-family:'Arial Black', Impact, sans-serif;font-size:18vw;font-weight:900;color:#ffd700;line-height:0.9;margin-top:1vh;">РАДІО</div>
</div>
</body></html>"""
render_html_to_png(ukr_html, os.path.join(DIR_640, "ukrajinskeradio.png"), 640)
render_html_to_png(ukr_html, os.path.join(DIR_1024, "ukrajinskeradio.png"), 1024)
print("Generated ukrajinskeradio.png (640 & 1024)")

# 18. CRA Info channels & Test carriers
print("--- 18. Generating CRA and Test info channels ---")
cra_html = """<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#003366;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="font-family:'Arial Black', Impact, sans-serif;font-size:22vw;font-weight:900;color:#ffffff;letter-spacing:-1vw;">CRA</div>
<div style="font-family:'Helvetica Neue', Arial, sans-serif;font-size:7vw;font-weight:700;color:#00a8e8;letter-spacing:0.5vw;margin-top:1vh;">DVB-T2 VYSÍLÁNÍ</div>
</body></html>"""
render_html_to_png(cra_html, os.path.join(DIR_640, "naladtesenadigitalnivysilanicra.png"), 640)
render_html_to_png(cra_html, os.path.join(DIR_1024, "naladtesenadigitalnivysilanicra.png"), 1024)
make_symlink("naladtesenadigitalnivysilanicra", "televizepresantenu")

test_html = """<!DOCTYPE html>
<html><body style="margin:0;padding:0;overflow:hidden;background:#2b2d42;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100vw;height:100vh;">
<div style="font-family:'Arial Black', Impact, sans-serif;font-size:22vw;font-weight:900;color:#8d99ae;letter-spacing:-1vw;">TEST</div>
<div style="font-family:'Helvetica Neue', Arial, sans-serif;font-size:8vw;font-weight:700;color:#edf2f4;letter-spacing:1vw;">MUX 24</div>
</body></html>"""
render_html_to_png(test_html, os.path.join(DIR_640, "dbtest1.png"), 640)
render_html_to_png(test_html, os.path.join(DIR_1024, "dbtest1.png"), 1024)
make_symlink("dbtest1", "dbtest2")

print("\n--- ALL PICONS GENERATED SUCCESSFULLY! ---")
