import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUTPUT_BASE = "public/assets/genesis"

def draw_gradient(draw, width, height, top_color, bottom_color):
    for y in range(height):
        factor = y / height
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * factor)
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * factor)
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * factor)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def draw_stars(draw, width, height, count=120):
    random.seed(42)
    for _ in range(count):
        x = random.randint(0, width)
        y = random.randint(0, int(height * 0.75))
        size = random.choice([1, 1, 1, 2, 3])
        brightness = random.randint(180, 255)
        if size == 1:
            draw.point((x, y), fill=(brightness, brightness, brightness))
        else:
            draw.ellipse([x - size, y - size, x + size, y + size], fill=(brightness, brightness, brightness))

def draw_celestial_glow(overlay_draw, cx, cy, radius, color):
    for r in range(radius, 10, -10):
        alpha = int(45 * (1 - r / radius))
        overlay_draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(color[0], color[1], color[2], alpha))

def draw_sun_rays(overlay_draw, cx, cy, width, height, ray_count=24, ray_color=(255, 240, 180, 25)):
    for i in range(ray_count):
        angle = i * (2 * math.pi / ray_count)
        length = max(width, height) * 1.5
        x2 = cx + math.cos(angle) * length
        y2 = cy + math.sin(angle) * length
        overlay_draw.line([(cx, cy), (x2, y2)], fill=ray_color, width=14)

def draw_mountains(draw, width, height, y_base, peak_count=5, color=(30, 40, 50)):
    points = [(0, height)]
    step = width / (peak_count * 2)
    current_x = 0
    while current_x <= width + 50:
        points.append((current_x, y_base + random.randint(-40, 40)))
        current_x += step
        points.append((current_x, y_base - random.randint(80, 160)))
        current_x += step
    points.append((width, height))
    draw.polygon(points, fill=color)

def draw_rolling_hills(draw, width, height, y_base, color=(20, 35, 25)):
    points = [(0, height)]
    for x in range(0, width + 40, 30):
        y = y_base + int(math.sin(x * 0.008) * 35 + math.cos(x * 0.015) * 15)
        points.append((x, y))
    points.append((width, height))
    draw.polygon(points, fill=color)

def draw_character_silhouette(draw, cx, cy, height_px=140, pose="standing_staff", color=(15, 20, 25)):
    # Draw expressive comic character silhouettes
    head_rad = int(height_px * 0.12)
    head_cy = cy - height_px + head_rad
    # Head
    draw.ellipse([cx - head_rad, head_cy - head_rad, cx + head_rad, head_cy + head_rad], fill=color)
    
    if pose == "standing_staff":
        # Body / Robe
        neck_y = head_cy + head_rad
        torso_bottom = cy - int(height_px * 0.45)
        # Cloak spreading down
        draw.polygon([
            (cx - head_rad, neck_y),
            (cx + head_rad, neck_y),
            (cx + head_rad * 3, cy),
            (cx - head_rad * 3, cy)
        ], fill=color)
        # Staff in right hand
        staff_x = cx + head_rad * 3 + 8
        draw.line([(staff_x, cy - height_px * 1.1), (staff_x, cy)], fill=color, width=4)
        # Arm reaching to staff
        draw.line([(cx + head_rad, neck_y + 15), (staff_x, neck_y + 35)], fill=color, width=6)

    elif pose == "kneeling_prayer":
        # Kneeling profile
        neck_y = head_cy + head_rad
        draw.polygon([
            (cx - head_rad * 2, neck_y),
            (cx + head_rad * 2, neck_y),
            (cx + head_rad * 4, cy),
            (cx - head_rad * 3, cy)
        ], fill=color)
        # Outstretched hands in prayer
        draw.line([(cx + head_rad * 2, neck_y + 10), (cx + head_rad * 4.5, neck_y - 15)], fill=color, width=5)

    elif pose == "two_figures_dialogue":
        # Person 1 (Left)
        draw.ellipse([cx - 50 - head_rad, head_cy - head_rad, cx - 50 + head_rad, head_cy + head_rad], fill=color)
        draw.polygon([(cx - 50 - head_rad, head_cy + head_rad), (cx - 50 + head_rad, head_cy + head_rad), (cx - 50 + 25, cy), (cx - 50 - 25, cy)], fill=color)
        # Person 2 (Right, facing left)
        draw.ellipse([cx + 50 - head_rad, head_cy - head_rad, cx + 50 + head_rad, head_cy + head_rad], fill=color)
        draw.polygon([(cx + 50 - head_rad, head_cy + head_rad), (cx + 50 + head_rad, head_cy + head_rad), (cx + 50 + 25, cy), (cx + 50 - 25, cy)], fill=color)
        # Gesturing hand
        draw.line([(cx - 50 + 10, head_cy + head_rad + 20), (cx - 10, head_cy + head_rad + 10)], fill=color, width=5)

    elif pose == "reunion_embrace":
        # Two brothers embracing
        draw.ellipse([cx - 20 - head_rad, head_cy - head_rad, cx - 20 + head_rad, head_cy + head_rad], fill=color)
        draw.ellipse([cx + 20 - head_rad, head_cy - head_rad, cx + 20 + head_rad, head_cy + head_rad], fill=color)
        draw.polygon([(cx - 45, cy), (cx - 30, head_cy + head_rad), (cx + 30, head_cy + head_rad), (cx + 45, cy)], fill=color)
        draw.line([(cx - 25, head_cy + 25), (cx + 35, head_cy + 25)], fill=color, width=7)

    elif pose == "man_and_woman":
        # Adam and Eve silhouettes
        draw.ellipse([cx - 40 - head_rad, head_cy - head_rad, cx - 40 + head_rad, head_cy + head_rad], fill=color)
        draw.polygon([(cx - 40 - 20, cy), (cx - 40, head_cy + head_rad), (cx - 40 + 20, cy)], fill=color)
        draw.ellipse([cx + 40 - head_rad, head_cy - head_rad + 8, cx + 40 + head_rad, head_cy + head_rad + 8], fill=color)
        draw.polygon([(cx + 40 - 20, cy), (cx + 40, head_cy + head_rad + 8), (cx + 40 + 20, cy)], fill=color)
        # Holding hands
        draw.line([(cx - 30, cy - 30), (cx + 30, cy - 30)], fill=color, width=4)

    elif pose == "egyptian_throne":
        # Seated ruler and standing vizier
        draw.rectangle([cx - 90, cy - 70, cx - 30, cy], fill=color)
        draw.ellipse([cx - 60 - head_rad, cy - 70 - head_rad * 2, cx - 60 + head_rad, cy - 70], fill=color)
        # Standing figure bowing
        draw.ellipse([cx + 60 - head_rad, head_cy - head_rad + 15, cx + 60 + head_rad, head_cy + head_rad + 15], fill=color)
        draw.polygon([(cx + 40, cy), (cx + 60, head_cy + head_rad + 15), (cx + 80, cy)], fill=color)

def render_artistic_panel(dest_path, theme="cosmic", pose=None, width=1280, height=720):
    # Check if this is an AI high-res masterpiece we want to preserve
    if os.path.exists(dest_path):
        size = os.path.getsize(dest_path)
        # If larger than 250KB, it's our AI masterpiece (like Genesis 1:1, 1:2, Gen 2:1)
        if size > 250000:
            print(f"Preserving benchmark artwork asset: {dest_path}")
            return

    img = Image.new('RGB', (width, height), (15, 23, 42))
    draw = ImageDraw.Draw(img)
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)

    if theme == "cosmic":
        # Deep Indigo to Primeval Waters
        draw_gradient(draw, width, height, (5, 8, 22), (15, 30, 60))
        draw_stars(draw, width, height, count=180)
        draw_celestial_glow(ov_draw, width // 2, height // 3, 280, (180, 220, 255))
        draw_sun_rays(ov_draw, width // 2, height // 3, width, height, ray_count=20, ray_color=(255, 255, 255, 20))
        # Cosmic Ocean below
        for i in range(4):
            y_base = height - 160 + i * 40
            pts = [(0, height)]
            for x in range(0, width + 50, 40):
                pts.append((x, y_base + int(math.sin(x * 0.02 + i) * 22)))
            pts.append((width, height))
            ov_draw.polygon(pts, fill=(8, 20, 45, 110 + i * 35))

    elif theme == "light":
        # Radiant golden creation burst
        draw_gradient(draw, width, height, (254, 240, 138), (15, 23, 42))
        draw_sun_rays(ov_draw, width // 2, height // 2, width, height, ray_count=36, ray_color=(255, 255, 255, 45))
        draw_celestial_glow(ov_draw, width // 2, height // 2, 220, (255, 255, 255))

    elif theme == "nature":
        # Emerald paradise / Eden hills
        draw_gradient(draw, width, height, (254, 215, 170), (16, 185, 129))
        draw_celestial_glow(ov_draw, width // 3, height // 3, 160, (255, 245, 180))
        draw_mountains(draw, width, height, height // 2, peak_count=4, color=(20, 83, 45))
        draw_rolling_hills(draw, width, height, height - 140, color=(6, 78, 59))
        if pose:
            draw_character_silhouette(draw, width // 2, height - 80, height_px=150, pose=pose, color=(10, 35, 25))

    elif theme == "desert":
        # Ancient Near Eastern dunes and star canopy
        draw_gradient(draw, width, height, (30, 27, 75), (234, 88, 12))
        draw_stars(draw, width, height, count=140)
        # Crescent moon / bright star
        ov_draw.ellipse([width - 240, 80, width - 170, 150], fill=(255, 250, 220, 220))
        # Golden sand dunes
        ov_draw.polygon([(0, height), (0, 520), (400, 460), (900, 530), (width, 480), (width, height)], fill=(194, 65, 12, 240))
        ov_draw.polygon([(0, height), (0, 580), (600, 520), (1100, 590), (width, 540), (width, height)], fill=(154, 52, 18, 255))
        if pose:
            draw_character_silhouette(draw, width // 3, height - 60, height_px=155, pose=pose, color=(40, 15, 10))

    elif theme == "water":
        # Great Deluge / High Seas
        draw_gradient(draw, width, height, (15, 23, 42), (30, 58, 138))
        # Heavy rain & lightning
        ov_draw.line([(width // 2 - 40, 40), (width // 2, 200), (width // 2 - 20, 320)], fill=(224, 242, 254, 180), width=4)
        for i in range(5):
            y_base = 380 + i * 65
            pts = [(0, height)]
            for x in range(0, width + 40, 30):
                pts.append((x, y_base + int(math.sin(x * 0.015 + i * 1.5) * 32)))
            pts.append((width, height))
            ov_draw.polygon(pts, fill=(10, 35, 75, 120 + i * 30))
        # Ark silhouette in midground
        ark_cx = width // 2
        ark_cy = 430
        ov_draw.polygon([
            (ark_cx - 90, ark_cy + 30),
            (ark_cx - 110, ark_cy),
            (ark_cx + 110, ark_cy),
            (ark_cx + 90, ark_cy + 30)
        ], fill=(30, 20, 15, 240))
        ov_draw.rectangle([ark_cx - 50, ark_cy - 25, ark_cx + 50, ark_cy], fill=(45, 30, 20, 240))

    elif theme == "palace":
        # Regal Egyptian Throne & Colonnade
        draw_gradient(draw, width, height, (69, 26, 3), (202, 138, 4))
        # Giant Egyptian colonnade pillars
        for col_x in [160, 360, width - 360, width - 160]:
            ov_draw.rectangle([col_x - 35, 80, col_x + 35, height], fill=(180, 130, 50, 180))
            ov_draw.rectangle([col_x - 50, 60, col_x + 50, 90], fill=(217, 160, 60, 220))
        draw_celestial_glow(ov_draw, width // 2, 240, 200, (255, 230, 120))
        if pose:
            draw_character_silhouette(draw, width // 2, height - 70, height_px=140, pose=pose, color=(35, 20, 10))

    elif theme == "fire":
        # Altar fire & glowing embers
        draw_gradient(draw, width, height, (15, 23, 42), (185, 28, 28))
        cx = width // 2
        # Stone altar
        draw.rectangle([cx - 140, height - 190, cx + 140, height - 100], fill=(45, 35, 35))
        # Rising flame plumes
        for i in range(16):
            fx = cx - 110 + i * 15
            fy = height - 190 - random.randint(70, 160)
            ov_draw.polygon([(fx, height - 190), (fx + 12, fy), (fx + 24, height - 190)], fill=(255, 120 + i * 6, 20, 190))
        if pose:
            draw_character_silhouette(draw, cx + 220, height - 90, height_px=150, pose=pose, color=(20, 15, 20))

    else:
        # Default pastoral / covenant landscape
        draw_gradient(draw, width, height, (55, 48, 163), (245, 158, 11))
        draw_mountains(draw, width, height, height // 2 + 50, color=(30, 35, 55))
        draw_rolling_hills(draw, width, height, height - 120, color=(15, 25, 20))
        if pose:
            draw_character_silhouette(draw, width // 2, height - 70, height_px=140, pose=pose, color=(15, 20, 25))

    # Comic Vignette & Clean Inking Framing
    for y in range(35):
        alpha = int(140 * (1 - y / 35))
        ov_draw.line([(0, y), (width, y)], fill=(0, 0, 0, alpha))
        ov_draw.line([(0, height - 1 - y), (width, height - 1 - y)], fill=(0, 0, 0, alpha))
    for x in range(35):
        alpha = int(140 * (1 - x / 35))
        ov_draw.line([(x, 0), (x, height)], fill=(0, 0, 0, alpha))
        ov_draw.line([(width - 1 - x, 0), (width - 1 - x, height)], fill=(0, 0, 0, alpha))

    # Graphic Novel Framing Corners
    corner_len = 45
    ov_draw.line([(20, 20), (20 + corner_len, 20)], fill=(255, 255, 255, 180), width=3)
    ov_draw.line([(20, 20), (20, 20 + corner_len)], fill=(255, 255, 255, 180), width=3)
    ov_draw.line([(width - 20, 20), (width - 20 - corner_len, 20)], fill=(255, 255, 255, 180), width=3)
    ov_draw.line([(width - 20, 20), (width - 20, 20 + corner_len)], fill=(255, 255, 255, 180), width=3)
    ov_draw.line([(20, height - 20), (20 + corner_len, height - 20)], fill=(255, 255, 255, 180), width=3)
    ov_draw.line([(20, height - 20), (20, height - 20 - corner_len)], fill=(255, 255, 255, 180), width=3)
    ov_draw.line([(width - 20, height - 20), (width - 20 - corner_len, height - 20)], fill=(255, 255, 255, 180), width=3)
    ov_draw.line([(width - 20, height - 20), (width - 20, height - 20 - corner_len)], fill=(255, 255, 255, 180), width=3)

    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    img.save(dest_path, "JPEG", quality=90)
    print(f"Rendered graphic novel panel: {dest_path}")

print("Artistic panel renderer ready.")
