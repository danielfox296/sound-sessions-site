"""Generated brand imagery: a single light in a dark field, ink/ice duotone."""
import math, random
from PIL import Image, ImageDraw, ImageFilter
W, H = 1600, 1000
INK = (10, 11, 13); ICE = (98, 182, 232)
def lerp(a, b, t): return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))
def grain(img, amt=10):
    px = img.load(); random.seed(7)
    for y in range(0, H, 2):
        for x in range(0, W, 2):
            n = random.randint(-amt, amt)
            r, g, b = px[x, y]
            px[x, y] = (max(0,min(255,r+n)), max(0,min(255,g+n)), max(0,min(255,b+n)))
    return img
def one_light(path, cx=0.62, cy=0.42, rad=0.55, peak=0.85):
    img = Image.new('RGB', (W, H), INK); px = img.load()
    for y in range(H):
        for x in range(W):
            d = math.hypot((x/W-cx), (y/H-cy)*H/W) / rad
            t = max(0.0, peak*math.exp(-d*d*3.2))
            px[x, y] = lerp(INK, ICE, t*0.9)
    img = img.filter(ImageFilter.GaussianBlur(2))
    grain(img).save(path, quality=82, optimize=True)
def waves(path):
    img = Image.new('RGB', (W, H), INK); d = ImageDraw.Draw(img)
    for k in range(90):
        yb = H*0.15 + k*(H*0.8/90); amp = 26*math.sin(k/90*math.pi)**2 + 2
        pts = [(x, yb + amp*math.sin(x/140 + k*0.35)) for x in range(0, W, 6)]
        c = lerp(INK, ICE, 0.10 + 0.5*math.sin(k/90*math.pi)**2)
        d.line(pts, fill=c, width=1)
    grain(img.filter(ImageFilter.GaussianBlur(0.6)), 6).save(path, quality=82, optimize=True)
def ripple(path):
    img = Image.new('RGB', (W, H), INK); d = ImageDraw.Draw(img)
    cx, cy = W*0.5, H*0.58
    for r in range(30, 1300, 26):
        t = max(0.0, 0.62*math.exp(-((r-330)/520)**2))
        d.ellipse([cx-r, cy-r*0.42, cx+r, cy+r*0.42], outline=lerp(INK, ICE, t), width=2)
    grain(img.filter(ImageFilter.GaussianBlur(1.0)), 6).save(path, quality=82, optimize=True)
one_light('img/hero/light-01.jpg'); waves('img/hero/waves-02.jpg'); ripple('img/hero/ripple-03.jpg')
print('art done')
