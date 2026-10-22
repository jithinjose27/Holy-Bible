import os
import json
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = "public/assets/genesis"
STORY_DATA_FILE = "src/data/genesis_story_data.json"
os.makedirs("src/data", exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Helper to create smooth gradient backgrounds with manhwa comic visual elements
def create_manhwa_panel(dest_path, width=1280, height=720, colors=((20, 30, 60), (5, 10, 25)), style="cosmic", title="", ref=""):
    # If file already exists and is not an auto-generated placeholder (e.g. AI image), preserve it!
    if os.path.exists(dest_path):
        size = os.path.getsize(dest_path)
        if size > 150000: # AI generated images are ~700KB - 1.1MB
            print(f"Preserving existing high-res asset: {dest_path}")
            return

    img = Image.new('RGB', (width, height), colors[0])
    draw = ImageDraw.Draw(img)

    # Vertical gradient
    c1, c2 = colors[0], colors[1]
    for y in range(height):
        factor = y / height
        r = int(c1[0] + (c2[0] - c1[0]) * factor)
        g = int(c1[1] + (c2[1] - c1[1]) * factor)
        b = int(c1[2] + (c2[2] - c1[2]) * factor)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Add stylized visual motifs based on theme style
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)

    if style == "cosmic":
        # Celestial light rays and stars
        cx, cy = width // 2, height // 3
        for i in range(16):
            angle = i * (math.pi / 8)
            lx = cx + math.cos(angle) * width
            ly = cy + math.sin(angle) * height
            ov_draw.line([(cx, cy), (lx, ly)], fill=(255, 240, 180, 25), width=18)
        # Glowing orb
        for rad in range(120, 20, -10):
            alpha = int(30 * (1 - rad / 120))
            ov_draw.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], fill=(255, 255, 255, alpha))
        # Deep waves below
        for i in range(3):
            wave_y = height - 160 + i * 40
            points = [(0, height)]
            for x in range(0, width + 50, 40):
                y = wave_y + int(math.sin(x * 0.02 + i) * 20)
                points.append((x, y))
            points.append((width, height))
            ov_draw.polygon(points, fill=(10, 25, 50, 90 + i * 40))

    elif style == "light":
        # Radiant burst of creation
        cx, cy = width // 2, height // 2
        for i in range(32):
            angle = i * (math.pi / 16)
            lx = cx + math.cos(angle) * width * 1.2
            ly = cy + math.sin(angle) * height * 1.2
            ov_draw.line([(cx, cy), (lx, ly)], fill=(255, 250, 210, 40), width=12)
        ov_draw.ellipse([cx - 150, cy - 150, cx + 150, cy + 150], fill=(255, 255, 255, 120))

    elif style == "nature":
        # Mountains & emerald foliage
        cx, cy = width // 2, height // 2
        # Sun at horizon
        ov_draw.ellipse([cx - 80, height // 2 - 80, cx + 80, height // 2 + 80], fill=(255, 215, 100, 150))
        # Mountain peaks
        ov_draw.polygon([(0, height), (300, 280), (700, height)], fill=(40, 70, 50, 180))
        ov_draw.polygon([(400, height), (850, 240), (1280, height)], fill=(30, 55, 40, 200))
        # Gentle hills
        ov_draw.polygon([(0, height), (0, 460), (400, 420), (900, 480), (width, 440), (width, height)], fill=(20, 45, 30, 240))

    elif style == "desert":
        # Golden dunes under vast twilight/starlit sky
        cx = width // 3
        # Moon / Star
        ov_draw.ellipse([width - 250, 100, width - 170, 180], fill=(255, 250, 220, 180))
        # Dunes
        ov_draw.polygon([(0, height), (0, 520), (350, 480), (800, 540), (width, 490), (width, height)], fill=(180, 120, 60, 220))
        ov_draw.polygon([(0, height), (0, 580), (550, 520), (1050, 590), (width, 540), (width, height)], fill=(140, 90, 40, 240))

    elif style == "water":
        # Tempest / River / Great flood
        cx, cy = width // 2, height // 2
        for i in range(5):
            y_base = 350 + i * 70
            pts = [(0, height)]
            for x in range(0, width + 40, 30):
                pts.append((x, y_base + int(math.sin(x * 0.015 + i * 1.5) * 35)))
            pts.append((width, height))
            ov_draw.polygon(pts, fill=(15, 45, 85, 120 + i * 30))

    elif style == "palace":
        # Regal Egyptian / Royal pillars and banners
        for x in [120, 320, width - 320, width - 120]:
            ov_draw.rectangle([x - 40, 100, x + 40, height], fill=(180, 150, 80, 160))
            ov_draw.rectangle([x - 55, 80, x + 55, 110], fill=(210, 180, 100, 200))
        # Center glow
        ov_draw.ellipse([width // 2 - 200, 120, width // 2 + 200, 520], fill=(255, 230, 150, 45))

    elif style == "fire":
        # Altar of sacrifice / Burning embers / Covenant smoke
        cx = width // 2
        ov_draw.rectangle([cx - 150, height - 220, cx + 150, height - 120], fill=(60, 50, 50, 220))
        # Flames
        for i in range(12):
            fx = cx - 120 + i * 20
            fy = height - 220 - int(math.sin(i) * 90) - 50
            ov_draw.polygon([(fx, height - 220), (fx + 15, fy), (fx + 30, height - 220)], fill=(255, 140 + i * 5, 40, 180))

    else:
        # Pastoral / Covenant landscape
        ov_draw.polygon([(0, height), (0, 450), (450, 400), (900, 480), (width, 420), (width, height)], fill=(30, 60, 45, 200))

    # Manhwa comic cinematic vignette & borders
    # Top and bottom letterbox / subtle vignette
    for y in range(40):
        alpha = int(180 * (1 - y / 40))
        ov_draw.line([(0, y), (width, y)], fill=(0, 0, 0, alpha))
        ov_draw.line([(0, height - 1 - y), (width, height - 1 - y)], fill=(0, 0, 0, alpha))
    for x in range(40):
        alpha = int(180 * (1 - x / 40))
        ov_draw.line([(x, 0), (x, height)], fill=(0, 0, 0, alpha))
        ov_draw.line([(width - 1 - x, 0), (width - 1 - x, height)], fill=(0, 0, 0, alpha))

    # Corner panel framing marks
    frame_color = (255, 255, 255, 160)
    corner_len = 50
    # Top-left
    ov_draw.line([(24, 24), (24 + corner_len, 24)], fill=frame_color, width=3)
    ov_draw.line([(24, 24), (24, 24 + corner_len)], fill=frame_color, width=3)
    # Top-right
    ov_draw.line([(width - 24, 24), (width - 24 - corner_len, 24)], fill=frame_color, width=3)
    ov_draw.line([(width - 24, 24), (width - 24, 24 + corner_len)], fill=frame_color, width=3)
    # Bottom-left
    ov_draw.line([(24, height - 24), (24 + corner_len, height - 24)], fill=frame_color, width=3)
    ov_draw.line([(24, height - 24), (24, height - 24 - corner_len)], fill=frame_color, width=3)
    # Bottom-right
    ov_draw.line([(width - 24, height - 24), (width - 24 - corner_len, height - 24)], fill=frame_color, width=3)
    ov_draw.line([(width - 24, height - 24), (width - 24, height - 24 - corner_len)], fill=frame_color, width=3)

    # Composite overlay
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    # Save optimized JPEG
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    img.save(dest_path, "JPEG", quality=85)
    print(f"Generated manhwa panel: {dest_path}")

print("Asset generation function defined.")
