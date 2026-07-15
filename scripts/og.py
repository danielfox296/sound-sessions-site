"""Generate the default 1200x630 OG image."""
from PIL import Image, ImageDraw, ImageFont
W, H = 1200, 630
img = Image.new('RGB', (W, H), (10, 11, 13))
d = ImageDraw.Draw(img)
import math
pts = [(x, 430 + 60*math.sin(x/70)*math.exp(-((x-700)/420)**2)) for x in range(0, W, 4)]
d.line(pts, fill=(98, 182, 232), width=3)
try:
    f1 = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 76)
    f2 = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 30)
except Exception:
    f1 = f2 = ImageFont.load_default()
d.text((80, 180), 'SOUND SESSIONS', font=f1, fill=(245, 247, 250))
d.text((80, 290), 'A dark room. One light. Sound you feel before you hear.', font=f2, fill=(152, 161, 171))
img.save('img/og-default.png', optimize=True)
print('og done')
