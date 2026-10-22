#!/usr/bin/env python3
import urllib.request
import time
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup, NavigableString

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(BASE_DIR, "src", "data", "bible_catalog.json")
CACHE_DIR = os.path.join(BASE_DIR, "src", "data", "raw_html")
BOOKS_DIR = os.path.join(BASE_DIR, "src", "data", "books")

os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(BOOKS_DIR, exist_ok=True)

def fetch_chapter_html(slug, ch):
    cache_path = os.path.join(CACHE_DIR, f"{slug}_{ch}.html")
    if os.path.exists(cache_path) and os.path.getsize(cache_path) > 1000:
        with open(cache_path, "r", encoding="utf-8") as f:
            return f.read()

    url = f"https://www.easyenglish.bible/bible/easy/{slug}/{ch}/"
    req = urllib.request.Request(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    )

    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read().decode('utf-8', errors='ignore')
                with open(cache_path, "w", encoding="utf-8") as f:
                    f.write(content)
                return content
        except Exception as e:
            if attempt == 3:
                print(f"Failed to fetch {slug} ch {ch} after 4 attempts: {e}")
                return None
            time.sleep(1 + attempt * 0.5)
    return None

def parse_chapter_html(book_name, slug, ch, html):
    if not html:
        return None

    soup = BeautifulSoup(html, 'html.parser')
    chunk = soup.find('div', class_='chunk')
    if not chunk:
        return None

    h1 = chunk.find('h1')
    chapter_title = h1.get_text().strip() if h1 else f"{book_name} {ch}"

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
        if el.name in ['h2', 'h3']:
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
            text_acc = ""

            for node in el.children:
                if node.name == 'v':
                    if verse_in_p is not None and text_acc.strip():
                        clean_text = " ".join(text_acc.split())
                        all_verses[verse_in_p] = all_verses.get(verse_in_p, "") + (" " if all_verses.get(verse_in_p) else "") + clean_text
                        p_verses.append({"verse": verse_in_p, "text": clean_text})
                        text_acc = ""

                    v_str = node.get_text().strip()
                    try:
                        if '-' in v_str:
                            verse_in_p = int(v_str.split('-')[0])
                        else:
                            verse_in_p = int(v_str)
                        current_verse_num = verse_in_p
                    except:
                        pass
                elif isinstance(node, NavigableString):
                    text_acc += str(node)
                elif node.name in ['w', 'span', 'i', 'b', 'em', 'strong']:
                    text_acc += node.get_text()

            if verse_in_p is not None and text_acc.strip():
                clean_text = " ".join(text_acc.split())
                all_verses[verse_in_p] = all_verses.get(verse_in_p, "") + (" " if all_verses.get(verse_in_p) else "") + clean_text
                p_verses.append({"verse": verse_in_p, "text": clean_text})
            elif text_acc.strip():
                clean_text = " ".join(text_acc.split())
                if current_verse_num in all_verses:
                    all_verses[current_verse_num] += " " + clean_text
                p_verses.append({"verse": current_verse_num, "text": clean_text, "isContinuation": True})

            if p_verses:
                current_section["items"].append(p_verses)

    if current_section["items"] or current_section["heading"]:
        sections.append(current_section)

    sorted_verses = [{"verse": k, "text": all_verses[k]} for k in sorted(all_verses.keys())]

    subtitle = ""
    for s in sections:
        if s["heading"]:
            subtitle = s["heading"]
            break

    return {
        "book": book_name,
        "chapter": ch,
        "title": chapter_title,
        "subtitle": subtitle,
        "sourceUrl": f"https://www.easyenglish.bible/bible/easy/{slug}/{ch}/",
        "sections": sections,
        "verses": sorted_verses,
        "totalVerses": len(sorted_verses),
        "footnotes": footnotes
    }

def process_book(book_meta):
    book_id = book_meta["id"]
    book_name = book_meta["name"]
    slug = book_meta["slug"]
    total_chapters = book_meta["chapters"]

    book_dir = os.path.join(BOOKS_DIR, book_id)
    os.makedirs(book_dir, exist_ok=True)
    target_file = os.path.join(book_dir, "text.json")

    # If file exists and has all chapters, verify and skip
    if os.path.exists(target_file):
        try:
            with open(target_file, "r", encoding="utf-8") as f:
                existing = json.load(f)
                if len(existing.get("chapters", [])) == total_chapters:
                    print(f"[{book_id}] {book_name} already complete ({total_chapters} ch). Skipping.")
                    return True
        except:
            pass

    print(f"[{book_id}] Processing {book_name} ({total_chapters} chapters)...")

    # Fetch chapters
    chapters = []
    chapter_results = {}

    def fetch_and_parse(ch):
        html = fetch_chapter_html(slug, ch)
        parsed = parse_chapter_html(book_name, slug, ch, html)
        return ch, parsed

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_and_parse, ch): ch for ch in range(1, total_chapters + 1)}
        for future in as_completed(futures):
            ch, parsed = future.result()
            if parsed:
                chapter_results[ch] = parsed
            else:
                print(f"[{book_id}] Warning: Chapter {ch} parsing returned None")

    # Order chapters 1 to total_chapters
    for ch in range(1, total_chapters + 1):
        if ch in chapter_results:
            chapters.append(chapter_results[ch])
        else:
            print(f"[{book_id}] Missing chapter {ch}!")

    if len(chapters) != total_chapters:
        print(f"[{book_id}] Error: Got {len(chapters)}/{total_chapters} chapters!")
        return False

    payload = {
        "translation": "EasyEnglish Bible",
        "book": book_name,
        "bookId": book_id,
        "totalChapters": total_chapters,
        "copyrightNotice": "Scripture quotations are from the EasyEnglish Bible Copyright © MissionAssist 2018, 2024. Used by permission.",
        "officialSourceUrl": f"https://www.easyenglish.bible/bible/easy/{slug}/1/",
        "chapters": chapters
    }

    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    size_kb = os.path.getsize(target_file) / 1024
    print(f"[{book_id}] Successfully generated text.json ({size_kb:.1f} KB, {total_chapters} chapters)")
    return True

def main():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    all_books = []
    for t in catalog["testaments"]:
        all_books.extend(t["books"])

    print(f"Total books to process: {len(all_books)}")

    # We can process books with a worker pool
    success_count = 0
    failed_books = []

    for idx, b in enumerate(all_books, 1):
        print(f"\n--- Book {idx}/{len(all_books)}: {b['name']} ({b['id']}) ---")
        ok = process_book(b)
        if ok:
            success_count += 1
        else:
            failed_books.append(b["id"])

    print(f"\n==========================================")
    print(f"Finished EasyEnglish Scripture Fetching!")
    print(f"Success: {success_count}/{len(all_books)}")
    if failed_books:
        print(f"Failed books: {failed_books}")
    print(f"==========================================")

if __name__ == "__main__":
    main()
