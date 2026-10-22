#!/usr/bin/env python3
"""
Generate complete set of high-resolution PWA icons and favicons
for The Holy Bible Reader.
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_bible_icon(size, is_maskable=False):
    """
    Renders a premium, dignified biblical icon with gold accents
    on a deep mahogany leather background.
    """
    # Create high-resolution base canvas with antialiasing (4x supersampling)
    scale = 4
    canvas_size = size * scale
    img = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    center = canvas_size / 2
    
    # Maskable safe-zone factor: content must reside strictly within inner 80%
    content_factor = 0.72 if is_maskable else 0.88
    
    # 1. Background Gradient / Base
    if is_maskable:
        # Full bleed solid/radial gradient covering entire square for Android adaptive icons
        for r in range(int(canvas_size * 0.8), 0, -2):
            frac = r / (canvas_size * 0.8)
            # Interpolate from deep dark amber/mahogany #261102 to rich amber #78350f
            red = int(0x26 + (0x78 - 0x26) * frac)
            green = int(0x11 + (0x35 - 0x11) * frac)
            blue = int(0x02 + (0x0f - 0x02) * frac)
            draw.ellipse([center - r, center - r, center + r, center + r], fill=(red, green, blue, 255))
        # Fill corners
        base_bg = Image.new("RGBA", (canvas_size, canvas_size), (0x26, 0x11, 0x02, 255))
        base_bg.paste(img, (0, 0), img)
        img = base_bg
        draw = ImageDraw.Draw(img)
    else:
        # Rounded squircle for standalone / desktop / apple icon
        pad = canvas_size * 0.04
        corner_radius = canvas_size * 0.22
        # Outer soft shadow
        shadow = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
        s_draw = ImageDraw.Draw(shadow)
        s_draw.rounded_rectangle([pad, pad + 12, canvas_size - pad, canvas_size - pad + 12], 
                                radius=corner_radius, fill=(0, 0, 0, 90))
        shadow = shadow.filter(ImageFilter.GaussianBlur(radius=8 * scale))
        img.paste(shadow, (0, 0), shadow)
        
        # Rounded rectangle background
        draw.rounded_rectangle([pad, pad, canvas_size - pad, canvas_size - pad], 
                               radius=corner_radius, fill=(0x3d, 0x1a, 0x06, 255))
        # Subtle gold border
        draw.rounded_rectangle([pad, pad, canvas_size - pad, canvas_size - pad], 
                               radius=corner_radius, outline=(0xd9, 0x77, 0x06, 180), width=int(2 * scale))

    # 2. Celestial Warm Radiance (Glow) in center
    glow = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow)
    glow_radius = int(canvas_size * 0.35 * content_factor)
    g_draw.ellipse([center - glow_radius, center - glow_radius, center + glow_radius, center + glow_radius],
                   fill=(0xfb, 0xbf, 0x24, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=16 * scale))
    img.paste(glow, (0, 0), glow)

    # 3. Draw Stylized Open Bible & Cross
    # Dimensions based on content area
    book_w = canvas_size * 0.62 * content_factor
    book_h = canvas_size * 0.42 * content_factor
    top_y = center - (book_h * 0.45)
    bottom_y = top_y + book_h
    spine_x = center

    # Left Page & Right Page Curves
    page_color_base = (0xfa, 0xf5, 0xeb, 255) # Warm paper
    page_edge_gold = (0xd9, 0x77, 0x06, 255) # Gold gilded edge
    ribbon_red = (0xb9, 0x1c, 0x1c, 255) # Rich velvet bookmark ribbon

    # Gilded Page Edge Layer (underneath)
    gilded_thick = 8 * scale
    draw.polygon([
        (spine_x, bottom_y + gilded_thick),
        (spine_x - book_w / 2, bottom_y + gilded_thick * 0.5),
        (spine_x - book_w / 2, bottom_y),
        (spine_x, bottom_y)
    ], fill=page_edge_gold)
    draw.polygon([
        (spine_x, bottom_y + gilded_thick),
        (spine_x + book_w / 2, bottom_y + gilded_thick * 0.5),
        (spine_x + book_w / 2, bottom_y),
        (spine_x, bottom_y)
    ], fill=page_edge_gold)

    # Left Page
    left_coords = [
        (spine_x, top_y + 12 * scale),
        (spine_x - book_w * 0.25, top_y),
        (spine_x - book_w * 0.5, top_y + 6 * scale),
        (spine_x - book_w * 0.5, bottom_y),
        (spine_x - book_w * 0.25, bottom_y - 4 * scale),
        (spine_x, bottom_y + 8 * scale)
    ]
    draw.polygon(left_coords, fill=page_color_base)
    draw.line(left_coords, fill=(0xd4, 0xcc, 0xb8, 255), width=int(1.5 * scale))

    # Right Page
    right_coords = [
        (spine_x, top_y + 12 * scale),
        (spine_x + book_w * 0.25, top_y),
        (spine_x + book_w * 0.5, top_y + 6 * scale),
        (spine_x + book_w * 0.5, bottom_y),
        (spine_x + book_w * 0.25, bottom_y - 4 * scale),
        (spine_x, bottom_y + 8 * scale)
    ]
    draw.polygon(right_coords, fill=page_color_base)
    draw.line(right_coords, fill=(0xd4, 0xcc, 0xb8, 255), width=int(1.5 * scale))

    # Text lines on left page (stylized horizontal bars)
    line_col = (0xb4, 0x53, 0x09, 130)
    for i in range(4):
        ly = top_y + (16 + i * 11) * scale
        lx1 = spine_x - book_w * 0.42
        lx2 = spine_x - book_w * 0.12
        draw.line([(lx1, ly), (lx2, ly)], fill=line_col, width=int(2.5 * scale))

    # Text lines on right page
    for i in range(4):
        ly = top_y + (16 + i * 11) * scale
        lx1 = spine_x + book_w * 0.12
        lx2 = spine_x + book_w * 0.42
        draw.line([(lx1, ly), (lx2, ly)], fill=line_col, width=int(2.5 * scale))

    # Velvet Ribbon Bookmark hanging down center
    ribbon_w = 7 * scale
    ribbon_pts = [
        (spine_x - ribbon_w / 2, top_y + 10 * scale),
        (spine_x + ribbon_w / 2, top_y + 10 * scale),
        (spine_x + ribbon_w / 2 + 6 * scale, bottom_y + 26 * scale),
        (spine_x + 6 * scale, bottom_y + 21 * scale),
        (spine_x - ribbon_w / 2 + 6 * scale, bottom_y + 26 * scale)
    ]
    draw.polygon(ribbon_pts, fill=ribbon_red)

    # 4. Gilded Golden Cross resting gracefully above the center spine
    cross_w = 8 * scale
    cross_h = 38 * scale
    cross_top = top_y - cross_h * 0.65
    cross_center_y = cross_top + cross_h * 0.38
    cross_arm_w = 26 * scale
    
    # Gold radiant glow behind cross
    gold_glow = (0xf5, 0x9e, 0x0b, 255)
    # Vertical cross beam
    draw.rounded_rectangle([
        spine_x - cross_w / 2, cross_top,
        spine_x + cross_w / 2, cross_top + cross_h
    ], radius=2 * scale, fill=gold_glow, outline=(0xfd, 0xba, 0x74, 255), width=int(scale))
    
    # Horizontal cross beam
    draw.rounded_rectangle([
        spine_x - cross_arm_w / 2, cross_center_y - cross_w / 2,
        spine_x + cross_arm_w / 2, cross_center_y + cross_w / 2
    ], radius=2 * scale, fill=gold_glow, outline=(0xfd, 0xba, 0x74, 255), width=int(scale))

    # Center jewel / radiance
    draw.ellipse([
        spine_x - 3 * scale, cross_center_y - 3 * scale,
        spine_x + 3 * scale, cross_center_y + 3 * scale
    ], fill=(0xff, 0xff, 0xff, 240))

    # Downsample using high quality Lanczos resampling for pixel-perfect sharpness
    final_img = img.resize((size, size), Image.Resampling.LANCZOS)
    return final_img

def main():
    icons_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "public", "icons"))
    os.makedirs(icons_dir, exist_ok=True)
    
    configs = [
        ("icon-192.png", 192, False),
        ("icon-512.png", 512, False),
        ("icon-maskable-192.png", 192, True),
        ("icon-maskable-512.png", 512, True),
        ("apple-touch-icon.png", 180, False),
        ("favicon-32x32.png", 32, False),
        ("favicon-16x16.png", 16, False),
    ]
    
    print("Generating crisp, dignified PWA icons...")
    for filename, size, maskable in configs:
        out_path = os.path.join(icons_dir, filename)
        img = create_bible_icon(size, is_maskable=maskable)
        img.save(out_path, "PNG", optimize=True)
        print(f"  ✓ Created {filename} ({size}x{size}{', maskable' if maskable else ''})")
    
    # Also save favicon.ico in public/
    public_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "public"))
    ico_path = os.path.join(public_dir, "favicon.ico")
    fav32 = create_bible_icon(32, False)
    fav16 = create_bible_icon(16, False)
    fav32.save(ico_path, format="ICO", sizes=[(32, 32), (16, 16)])
    print(f"  ✓ Created favicon.ico at public/favicon.ico")
    
    # Also copy apple-touch-icon to public root for fallback crawlers
    apple_root = os.path.join(public_dir, "apple-touch-icon.png")
    apple_img = create_bible_icon(180, False)
    apple_img.save(apple_root, "PNG", optimize=True)
    print(f"  ✓ Created apple-touch-icon.png at public/apple-touch-icon.png")

if __name__ == "__main__":
    main()
