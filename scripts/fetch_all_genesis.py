import urllib.request
import time
import json
import os
import sys
from bs4 import BeautifulSoup, NavigableString

OUTPUT_FILE = "src/data/genesis_bible_text.json"
CACHE_DIR = "src/data/raw_html"

os.makedirs("src/data", exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

def fetch_html(ch):
    cache_path = os.path.join(CACHE_DIR, f"genesis_{ch}.html")
    if os.path.exists(cache_path):
        with open(cache_path, "r", encoding="utf-8") as f:
            return f.read()

    url = f"https://www.easyenglish.bible/bible/easy/genesis/{ch}/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                content = resp.read().decode('utf-8', errors='ignore')
                with open(cache_path, "w", encoding="utf-8") as f:
                    f.write(content)
                return content
        except Exception as e:
            print(f"Attempt {attempt+1} failed for ch {ch}: {e}")
            time.sleep(1)
    raise RuntimeError(f"Failed to fetch chapter {ch}")

def parse_chapter_html(ch, html):
    soup = BeautifulSoup(html, 'html.parser')
    chunk = soup.find('div', class_='chunk')
    if not chunk:
        raise ValueError(f"Could not find div.chunk in chapter {ch}")

    h1 = chunk.find('h1')
    chapter_title = h1.get_text().strip() if h1 else f"Genesis {ch}"

    sections = []
    current_section = {
        "heading": "",
        "items": []
    }
    
    current_verse_num = 0
    all_verses = {}
    footnotes = []

    for fn in chunk.find_all('div', sfm='f'):
        fr = fn.find('span', sfm='fr')
        ref = fr.get_text().strip() if fr else ""
        text = fn.get_text().replace(ref, "").strip()
        footnotes.append({"ref": ref, "text": text})

    for el in chunk.children:
        if el.name == 'h2':
            heading_text = el.get_text().strip()
            if current_section["items"] or current_section["heading"]:
                sections.append(current_section)
            current_section = {
                "heading": heading_text,
                "items": []
            }
        elif el.name == 'p':
            p_verses = []
            verse_in_p = None
            text_accumulator = ""

            for node in el.children:
                if node.name == 'v':
                    if verse_in_p is not None and text_accumulator.strip():
                        clean_text = " ".join(text_accumulator.split())
                        all_verses[verse_in_p] = all_verses.get(verse_in_p, "") + (" " if all_verses.get(verse_in_p) else "") + clean_text
                        p_verses.append({"verse": verse_in_p, "text": clean_text})
                        text_accumulator = ""
                    
                    try:
                        v_num_str = node.get_text().strip()
                        verse_in_p = int(v_num_str)
                        current_verse_num = verse_in_p
                    except:
                        pass
                elif isinstance(node, NavigableString):
                    text_accumulator += str(node)
                elif node.name in ['w', 'span', 'i', 'b', 'em', 'strong']:
                    text_accumulator += node.get_text()
            
            if verse_in_p is not None and text_accumulator.strip():
                clean_text = " ".join(text_accumulator.split())
                all_verses[verse_in_p] = all_verses.get(verse_in_p, "") + (" " if all_verses.get(verse_in_p) else "") + clean_text
                p_verses.append({"verse": verse_in_p, "text": clean_text})
            elif text_accumulator.strip():
                clean_text = " ".join(text_accumulator.split())
                if current_verse_num in all_verses:
                    all_verses[current_verse_num] += " " + clean_text
                p_verses.append({"verse": current_verse_num, "text": clean_text, "isContinuation": True})

            if p_verses:
                current_section["items"].append(p_verses)

    if current_section["items"] or current_section["heading"]:
        sections.append(current_section)

    sorted_verses = [{"verse": k, "text": all_verses[k]} for k in sorted(all_verses.keys())]

    # Chapter subtitle/theme from first heading or known subject
    subtitle = ""
    for s in sections:
        if s["heading"]:
            subtitle = s["heading"]
            break

    return {
        "book": "Genesis",
        "chapter": ch,
        "title": chapter_title,
        "subtitle": subtitle,
        "sourceUrl": f"https://www.easyenglish.bible/bible/easy/genesis/{ch}/",
        "sections": sections,
        "verses": sorted_verses,
        "totalVerses": len(sorted_verses),
        "footnotes": footnotes
    }

def main():
    print("Fetching and parsing Genesis 1–50 from EasyEnglish Bible...")
    chapters_data = []
    
    for ch in range(1, 51):
        try:
            html = fetch_html(ch)
            c_data = parse_chapter_html(ch, html)
            chapters_data.append(c_data)
            print(f"[{ch}/50] Genesis {ch}: {c_data['totalVerses']} verses, subtitle: {c_data['subtitle'] or '(Intro)'}")
            time.sleep(0.1) # polite delay
        except Exception as e:
            print(f"Error on chapter {ch}: {e}")
            sys.exit(1)

    result = {
        "translation": "EasyEnglish Bible (EASY)",
        "book": "Genesis",
        "totalChapters": len(chapters_data),
        "copyrightNotice": "Scripture quotations are from the EasyEnglish Bible Copyright © MissionAssist 2018, 2024 – UK Charitable Incorporated Organisation 1162807. Used by permission. All rights reserved.",
        "officialSourceUrl": "https://www.easyenglish.bible/bible/easy/genesis/1/",
        "chapters": chapters_data
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully parsed and saved all 50 chapters to {OUTPUT_FILE}!")

if __name__ == "__main__":
    main()
