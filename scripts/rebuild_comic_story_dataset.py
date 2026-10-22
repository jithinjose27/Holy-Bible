import os
import json
from render_graphic_novel_panels import render_artistic_panel

OUTPUT_DIR = "public/assets/genesis"
STORY_DATA_FILE = "src/data/genesis_story_data.json"

# Load existing story data to upgrade with in-panel comic speech bubbles and poses
with open(STORY_DATA_FILE, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# Comprehensive dialogue and speech bubble positions for Genesis 1 to 50
def enrich_chapter_bubbles(ch, panels):
    enriched = []
    
    for p in panels:
        scene = p["scene"]
        ref = p["reference"]
        img = p["image"]
        narration = p.get("narration", "")
        dialogue = p.get("dialogue", [])
        alt = p.get("altText", "")
        style = p.get("style", "nature")

        bubbles = []

        # 1. Narration Box (Top-Left or Bottom-Left)
        if narration:
            bubbles.append({
                "type": "narration",
                "text": narration,
                "speaker": ref,
                "position": { "top": "16px", "left": "16px", "maxWidth": "70%" }
            })

        # 2. Character Dialogues & Divine Proclamations
        if ch == 1:
            if scene == 2:
                # "Let there be light!"
                bubbles.append({
                    "type": "divine",
                    "text": "LET THERE BE LIGHT!",
                    "speaker": "The Almighty",
                    "position": { "top": "22%", "left": "50%", "transform": "translateX(-50%)", "maxWidth": "85%" }
                })
                bubbles.append({
                    "type": "sfx",
                    "sfx": "RADIANCE",
                    "position": { "bottom": "15%", "right": "12%" }
                })
            elif scene == 3:
                bubbles.append({
                    "type": "divine",
                    "text": "A wide space will appear between the waters!",
                    "speaker": "The Almighty",
                    "position": { "top": "24%", "right": "20px", "maxWidth": "65%" }
                })
            elif scene == 4:
                bubbles.append({
                    "type": "divine",
                    "text": "Let dry ground appear, and let the earth bring forth plants with seeds and fruit trees!",
                    "speaker": "The Almighty",
                    "position": { "top": "20%", "right": "20px", "maxWidth": "65%" }
                })
            elif scene == 8:
                bubbles.append({
                    "type": "divine",
                    "text": "Let us make human beings in our image, like ourselves.",
                    "speaker": "The Almighty",
                    "position": { "top": "20%", "left": "50%", "transform": "translateX(-50%)", "maxWidth": "80%" }
                })

        elif ch == 2:
            if scene == 3:
                bubbles.append({
                    "type": "speech",
                    "speaker": "Adam",
                    "text": "Finally, bone of my bones and flesh of my flesh!",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "bottom": "25%", "right": "24px", "maxWidth": "55%" }
                })

        elif ch == 3:
            if scene == 1:
                bubbles.append({
                    "type": "speech",
                    "speaker": "The Serpent",
                    "text": "Did God really say, 'You must not eat from any tree in the garden'?",
                    "tailDirection": "top-right",
                    "isAdapted": False,
                    "position": { "top": "25%", "left": "24px", "maxWidth": "55%" }
                })
                bubbles.append({
                    "type": "speech",
                    "speaker": "Eve",
                    "text": "We may eat fruit from the trees, but God said of the tree in the middle, 'Do not eat it or you will die.'",
                    "tailDirection": "bottom-right",
                    "isAdapted": False,
                    "position": { "bottom": "20%", "right": "24px", "maxWidth": "60%" }
                })
            elif scene == 2:
                bubbles.append({
                    "type": "divine",
                    "text": "Where are you, Adam?",
                    "speaker": "The Lord God",
                    "position": { "top": "22%", "left": "24px", "maxWidth": "50%" }
                })
                bubbles.append({
                    "type": "speech",
                    "speaker": "Adam",
                    "text": "I heard your sound in the garden, and I was afraid because I was naked; so I hid.",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "bottom": "18%", "right": "24px", "maxWidth": "60%" }
                })

        elif ch == 4:
            if scene == 2:
                bubbles.append({
                    "type": "divine",
                    "text": "Where is your brother Abel?",
                    "speaker": "The Lord",
                    "position": { "top": "24%", "left": "24px", "maxWidth": "55%" }
                })
                bubbles.append({
                    "type": "speech",
                    "speaker": "Cain",
                    "text": "I do not know! Am I my brother’s keeper?",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "bottom": "22%", "right": "24px", "maxWidth": "55%" }
                })

        elif ch == 11:
            if scene == 1:
                bubbles.append({
                    "type": "shout",
                    "speaker": "Builders of Babel",
                    "text": "Come! Let us build a city with a tower reaching to the heavens!",
                    "tailDirection": "bottom-left",
                    "isAdapted": True,
                    "position": { "bottom": "22%", "right": "24px", "maxWidth": "60%" }
                })

        elif ch == 12:
            if scene == 1:
                bubbles.append({
                    "type": "divine",
                    "text": "Go from your country to the land I will show you... all peoples on earth will be blessed through you.",
                    "speaker": "The Lord",
                    "position": { "top": "22%", "left": "50%", "transform": "translateX(-50%)", "maxWidth": "80%" }
                })

        elif ch == 15:
            if scene == 1:
                bubbles.append({
                    "type": "divine",
                    "text": "Look up at the sky and count the stars—so shall your offspring be!",
                    "speaker": "The Lord",
                    "position": { "top": "20%", "left": "24px", "maxWidth": "65%" }
                })
                bubbles.append({
                    "type": "thought",
                    "speaker": "Abram",
                    "text": "Sovereign Lord, what can you give me since I remain childless?",
                    "position": { "bottom": "20%", "right": "24px", "maxWidth": "55%" }
                })

        elif ch == 22:
            if scene == 1:
                bubbles.append({
                    "type": "speech",
                    "speaker": "Isaac",
                    "text": "Father, the fire and wood are here, but where is the lamb for the burnt offering?",
                    "tailDirection": "bottom-right",
                    "isAdapted": False,
                    "position": { "top": "25%", "left": "24px", "maxWidth": "55%" }
                })
                bubbles.append({
                    "type": "speech",
                    "speaker": "Abraham",
                    "text": "God Himself will provide the lamb for the offering, my son.",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "bottom": "20%", "right": "24px", "maxWidth": "55%" }
                })
            elif scene == 2:
                bubbles.append({
                    "type": "shout",
                    "speaker": "Angel of the Lord",
                    "text": "Abraham, Abraham! Do not lay a hand on the boy!",
                    "tailDirection": "top-right",
                    "isAdapted": False,
                    "position": { "top": "20%", "left": "24px", "maxWidth": "65%" }
                })

        elif ch == 24:
            if scene == 1:
                bubbles.append({
                    "type": "speech",
                    "speaker": "Rebekah",
                    "text": "Drink, my lord, and I will draw water for your camels as well!",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "bottom": "20%", "right": "24px", "maxWidth": "55%" }
                })

        elif ch == 25:
            if scene == 2:
                bubbles.append({
                    "type": "shout",
                    "speaker": "Esau",
                    "text": "Quick! Let me have some of that red stew! I am famished!",
                    "tailDirection": "bottom-right",
                    "isAdapted": False,
                    "position": { "top": "25%", "left": "24px", "maxWidth": "55%" }
                })
                bubbles.append({
                    "type": "speech",
                    "speaker": "Jacob",
                    "text": "First sell me your birthright.",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "bottom": "20%", "right": "24px", "maxWidth": "50%" }
                })

        elif ch == 28:
            if scene == 1:
                bubbles.append({
                    "type": "divine",
                    "text": "I am with you and will watch over you wherever you go, and I will bring you back to this land.",
                    "speaker": "The Lord",
                    "position": { "top": "20%", "left": "50%", "transform": "translateX(-50%)", "maxWidth": "80%" }
                })
            elif scene == 2:
                bubbles.append({
                    "type": "speech",
                    "speaker": "Jacob",
                    "text": "Surely the Lord is in this place! This is none other than the house of God (Bethel)!",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "bottom": "20%", "right": "24px", "maxWidth": "60%" }
                })

        elif ch == 32:
            if scene == 1:
                bubbles.append({
                    "type": "speech",
                    "speaker": "The Angel",
                    "text": "Let me go, for the dawn is breaking.",
                    "tailDirection": "top-right",
                    "isAdapted": False,
                    "position": { "top": "25%", "left": "24px", "maxWidth": "50%" }
                })
                bubbles.append({
                    "type": "shout",
                    "speaker": "Jacob",
                    "text": "I will not let you go unless you bless me!",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "bottom": "20%", "right": "24px", "maxWidth": "55%" }
                })

        elif ch == 37:
            if scene == 1:
                bubbles.append({
                    "type": "speech",
                    "speaker": "Joseph",
                    "text": "Listen to this dream I had: We were binding sheaves of grain, and my sheaf stood upright while yours bowed down to mine!",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "bottom": "22%", "right": "24px", "maxWidth": "60%" }
                })

        elif ch == 41:
            if scene == 1:
                bubbles.append({
                    "type": "speech",
                    "speaker": "Pharaoh",
                    "text": "I had a dream, and no one can interpret it. Can you reveal its meaning?",
                    "tailDirection": "bottom-right",
                    "isAdapted": False,
                    "position": { "top": "25%", "left": "24px", "maxWidth": "55%" }
                })
                bubbles.append({
                    "type": "speech",
                    "speaker": "Joseph",
                    "text": "I cannot do it, but God will give Pharaoh the answer he desires.",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "bottom": "20%", "right": "24px", "maxWidth": "55%" }
                })

        elif ch == 45:
            if scene == 1:
                bubbles.append({
                    "type": "shout",
                    "speaker": "Joseph",
                    "text": "I am Joseph! Does my father still live? Come close to me!",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "top": "24%", "right": "24px", "maxWidth": "60%" }
                })
                bubbles.append({
                    "type": "speech",
                    "speaker": "Joseph",
                    "text": "Do not be distressed or angry with yourselves for selling me here, because it was to save lives that God sent me ahead of you.",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "bottom": "18%", "left": "24px", "maxWidth": "70%" }
                })

        elif ch == 50:
            if scene == 2:
                bubbles.append({
                    "type": "speech",
                    "speaker": "Joseph",
                    "text": "Do not be afraid. Am I in the place of God? You intended to harm me, but God intended it for good to save many lives.",
                    "tailDirection": "bottom-left",
                    "isAdapted": False,
                    "position": { "bottom": "20%", "left": "24px", "maxWidth": "70%" }
                })

        else:
            # For general dialogues across other chapters
            for dIdx, d in enumerate(dialogue):
                speaker_name = d.get("speaker", "Speaker")
                clean_text = d.get("text", "").replace("‘", "").replace("’", "").replace("“", "").replace("”", "")
                is_god = "Almighty" in speaker_name or "Lord" in speaker_name or "God" in speaker_name
                bubbles.append({
                    "type": "divine" if is_god else "speech",
                    "text": clean_text,
                    "speaker": speaker_name,
                    "tailDirection": "bottom-left" if dIdx % 2 == 0 else "bottom-right",
                    "isAdapted": d.get("isAdapted", False),
                    "position": {
                        "top": f"{20 + dIdx * 25}%",
                        "right": "24px" if dIdx % 2 == 0 else "auto",
                        "left": "auto" if dIdx % 2 == 0 else "24px",
                        "maxWidth": "60%"
                    }
                })

        # Render graphic novel illustration for this panel if needed
        disk_path = os.path.join(OUTPUT_DIR, str(ch), f"panel-{scene}.jpg")
        pose_type = None
        if "prayer" in alt.lower() or "kneel" in alt.lower():
            pose_type = "kneeling_prayer"
        elif "embrace" in alt.lower() or "weep" in alt.lower():
            pose_type = "reunion_embrace"
        elif "pharaoh" in alt.lower() or "throne" in alt.lower():
            pose_type = "egyptian_throne"
        elif "adam" in alt.lower() and "eve" in alt.lower():
            pose_type = "man_and_woman"
        elif len(dialogue) >= 2 or len(bubbles) >= 3:
            pose_type = "two_figures_dialogue"
        elif "staff" in alt.lower() or "walk" in alt.lower() or "gaze" in alt.lower():
            pose_type = "standing_staff"

        render_artistic_panel(disk_path, theme=style, pose=pose_type)

        enriched.append({
            "panelId": p.get("panelId", f"gen-{ch}-{scene}"),
            "scene": scene,
            "reference": ref,
            "image": img,
            "aspectRatio": "aspect-16/9",
            "altText": alt,
            "style": style,
            "bubbles": bubbles
        })

    return enriched

def main():
    print("Rebuilding complete comic story dataset with in-panel speech bubbles and graphic novel art...")
    upgraded_chapters = []

    for ch_data in existing_data["chapters"]:
        ch = ch_data["chapter"]
        print(f"Upgrading Genesis {ch} comic panels...")
        all_raw_panels = [p for page in ch_data["pages"] for p in page["panels"]]
        enriched_panels = enrich_chapter_bubbles(ch, all_raw_panels)

        # Repaginate into 2-panel or 3-panel comic tiers
        comic_pages = []
        page_panels = []
        for p in enriched_panels:
            page_panels.append(p)
            if len(page_panels) >= 2:
                comic_pages.append({
                    "page": len(comic_pages) + 1,
                    "panels": page_panels
                })
                page_panels = []
        if page_panels:
            comic_pages.append({
                "page": len(comic_pages) + 1,
                "panels": page_panels
            })

        upgraded_chapters.append({
            "book": "Genesis",
            "chapter": ch,
            "title": ch_data["title"],
            "subtitle": ch_data.get("subtitle", ""),
            "synopsis": ch_data.get("synopsis", ""),
            "themeColor": ch_data.get("themeColor", "#0f172a"),
            "totalPanels": len(enriched_panels),
            "totalPages": len(comic_pages),
            "pages": comic_pages
        })

    new_dataset = {
        "version": "2.0.0",
        "book": "Genesis",
        "totalChapters": len(upgraded_chapters),
        "chapters": upgraded_chapters
    }

    with open(STORY_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(new_dataset, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully upgraded all 50 chapters in {STORY_DATA_FILE}!")

if __name__ == "__main__":
    main()
