import urllib.request
import time
import re
import json
from bs4 import BeautifulSoup, NavigableString

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
        "items": [] # can be paragraph or verse group
    }
    
    current_verse_num = 0
    all_verses = {}
    footnotes = []

    # Find footnotes if any
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
            # Walk children
            verse_in_p = None
            text_accumulator = ""

            for node in el.children:
                if node.name == 'v':
                    # flush previous text to previous verse if any
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
                # Continuation paragraph of previous verse
                clean_text = " ".join(text_accumulator.split())
                if current_verse_num in all_verses:
                    all_verses[current_verse_num] += " " + clean_text
                p_verses.append({"verse": current_verse_num, "text": clean_text, "isContinuation": True})

            if p_verses:
                current_section["items"].append(p_verses)

    if current_section["items"] or current_section["heading"]:
        sections.append(current_section)

    sorted_verses = [{"verse": k, "text": all_verses[k]} for k in sorted(all_verses.keys())]

    return {
        "book": "Genesis",
        "chapter": ch,
        "title": chapter_title,
        "sourceUrl": f"https://www.easyenglish.bible/bible/easy/genesis/{ch}/",
        "sections": sections,
        "verses": sorted_verses,
        "totalVerses": len(sorted_verses),
        "footnotes": footnotes
    }

if __name__ == '__main__':
    for ch in [1, 2, 12, 37, 50]:
        url = f"https://www.easyenglish.bible/bible/easy/genesis/{ch}/"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            data = parse_chapter_html(ch, resp.read().decode('utf-8', errors='ignore'))
            print(f"Chapter {ch}: {data['title']}, {data['totalVerses']} verses, {len(data['sections'])} sections, first heading: {data['sections'][0]['heading'] if data['sections'] else 'None'}")
