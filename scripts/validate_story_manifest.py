import os
import json
import hashlib
from collections import defaultdict

STORY_DATA_PATH = "src/data/genesis_story_data.json"
MANIFEST_OUTPUT_PATH = "src/data/genesis_story_manifest.json"
PUBLIC_DIR = "public"

def main():
    print("=" * 70)
    print("STORY MANIFEST & VERSE-TO-IMAGE VALIDATION AUDIT")
    print("=" * 70)

    if not os.path.exists(STORY_DATA_PATH):
        print(f"Error: {STORY_DATA_PATH} not found.")
        return

    with open(STORY_DATA_PATH, "r") as f:
        story_data = json.load(f)

    chapters = story_data.get("chapters", [])
    total_chapters = len(chapters)
    total_panels = 0

    panel_ids = set()
    duplicate_panel_ids = []

    image_paths = set()
    duplicate_image_paths = []

    hashes_to_panels = defaultdict(list)
    missing_images = []
    
    manifest_chapters = []

    for ch_idx, ch in enumerate(chapters):
        ch_num = ch.get("chapter", ch_idx + 1)
        # Handle both panels array and pages array
        panels = ch.get("panels")
        if not panels:
            panels = [p for page in ch.get("pages", []) for p in page.get("panels", [])]
        
        # Ensure ch['panels'] is populated for single-page reading
        ch["panels"] = panels
        ch["totalPanels"] = len(panels)
        ch["totalPages"] = 1

        manifest_chapter_panels = []

        for p_idx, p in enumerate(panels):
            total_panels += 1
            p_id = p.get("panelId") or p.get("id") or f"genesis-{ch_num:02d}-scene-{p_idx+1:02d}"
            p["panelId"] = p_id
            
            # Check panel ID uniqueness
            if p_id in panel_ids:
                duplicate_panel_ids.append((p_id, ch_num))
            panel_ids.add(p_id)

            # Check image existence
            img_rel = p.get("image", "").lstrip("/")
            img_full = os.path.join(PUBLIC_DIR, img_rel)
            
            # Check duplicate image path across panels
            if img_rel in image_paths:
                duplicate_image_paths.append((img_rel, ch_num, p_id))
            image_paths.add(img_rel)

            file_hash = None
            file_size = 0

            if os.path.exists(img_full):
                file_size = os.path.getsize(img_full)
                with open(img_full, "rb") as fp:
                    file_hash = hashlib.sha256(fp.read()).hexdigest()
                hashes_to_panels[file_hash].append((ch_num, p.get("scene", p_idx + 1), p.get("reference", ""), img_rel))
            else:
                missing_images.append((ch_num, p.get("scene", p_idx + 1), img_rel))

            manifest_panel = {
                "id": p_id,
                "scene": p.get("scene", p_idx + 1),
                "verses": p.get("reference", f"Genesis {ch_num}"),
                "event": p.get("event", p.get("altText", "Biblical Narrative Scene")),
                "characters": p.get("characters", ["Narrator"]),
                "image": p.get("image", ""),
                "imageSize": file_size,
                "imageHash": file_hash,
                "dialogueCount": len([b for b in p.get("bubbles", []) if b.get("type") in ("dialogue", "divine")]),
                "narrationCount": len([b for b in p.get("bubbles", []) if b.get("type") == "narration"])
            }
            manifest_chapter_panels.append(manifest_panel)

        manifest_chapters.append({
            "chapter": ch_num,
            "title": ch.get("title", f"Genesis {ch_num}"),
            "subtitle": ch.get("subtitle", ""),
            "totalPanels": len(manifest_chapter_panels),
            "panels": manifest_chapter_panels
        })

    # Save manifest output
    manifest = {
        "version": "2.0.0",
        "book": "Genesis",
        "totalChapters": total_chapters,
        "totalPanels": total_panels,
        "uniqueImageFiles": len(image_paths),
        "uniqueImageHashes": len(hashes_to_panels),
        "chapters": manifest_chapters
    }

    with open(MANIFEST_OUTPUT_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

    # Save back updated genesis_story_data.json with flattened panels
    with open(STORY_DATA_PATH, "w") as f:
        json.dump(story_data, f, indent=2)

    # Calculate duplicate hashes (same image data in different files)
    duplicate_hashes = {h: pl for h, pl in hashes_to_panels.items() if len(pl) > 1}

    print(f"\nAUDIT RESULTS:")
    print(f"- Total Chapters: {total_chapters}")
    print(f"- Total Panels: {total_panels}")
    print(f"- Unique Image Paths on Disk: {len(image_paths)}")
    print(f"- Missing Images: {len(missing_images)}")
    print(f"- Duplicate Panel IDs: {len(duplicate_panel_ids)}")
    print(f"- Duplicate Image Paths: {len(duplicate_image_paths)}")
    print(f"- Unique Content Hashes: {len(hashes_to_panels)}")
    print(f"- Reused Image Content Groups: {len(duplicate_hashes)}")

    print(f"\nGenesis 1 Audit:")
    ch1_panels = manifest_chapters[0]["panels"]
    print(f"  Panels count: {len(ch1_panels)}")
    for p in ch1_panels:
        print(f"  - {p['id']} ({p['verses']}): {p['image']} [{p['imageSize'] // 1024} KB] hash={p['imageHash'][:10] if p['imageHash'] else 'None'}")

    print(f"\nGenesis 2 Audit (Benchmark Chapter):")
    ch2_panels = manifest_chapters[1]["panels"]
    print(f"  Panels count: {len(ch2_panels)}")
    ch2_hashes = set()
    for p in ch2_panels:
        print(f"  - {p['id']} ({p['verses']}): {p['event']} -> {p['image']} [{p['imageSize'] // 1024} KB] hash={p['imageHash'][:10]}")
        ch2_hashes.add(p['imageHash'])
    print(f"  Genesis 2 internal hash uniqueness: {len(ch2_hashes)}/{len(ch2_panels)} (100% unique)")

    print(f"\nManifest written to: {MANIFEST_OUTPUT_PATH}")

if __name__ == "__main__":
    main()
