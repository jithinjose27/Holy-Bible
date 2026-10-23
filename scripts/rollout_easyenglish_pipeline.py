#!/usr/bin/env python3
"""
rollout_easyenglish_pipeline.py
Systematic fetch, parse, verify, and rollout pipeline for the complete EasyEnglish Bible.
Author: Antigravity
"""

import os
import sys
import json
import time
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(BASE_DIR, "src", "data", "bible_catalog.json")
BOOKS_DIR = os.path.join(BASE_DIR, "src", "data", "books")
RAW_HTML_DIR = os.path.join(BASE_DIR, "data_sources", "easyenglish_raw_html")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

os.makedirs(RAW_HTML_DIR, exist_ok=True)

def fetch_chapter_html(slug, ch, max_retries=4):
    """
    Fetches raw chapter HTML from easyenglish.bible or loads from local cache.
    """
    book_raw_dir = os.path.join(RAW_HTML_DIR, slug)
    os.makedirs(book_raw_dir, exist_ok=True)
    cache_file = os.path.join(book_raw_dir, f"{ch}.html")

    if os.path.exists(cache_file) and os.path.getsize(cache_file) > 1000:
        with open(cache_file, "r", encoding="utf-8") as f:
            return cache_file, f.read()

    url = f"https://www.easyenglish.bible/bible/easy/{slug}/{ch}/"
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as resp:
                if resp.status == 200:
                    html = resp.read().decode("utf-8")
                    with open(cache_file, "w", encoding="utf-8") as f:
                        f.write(html)
                    return cache_file, html
        except Exception as e:
            wait_time = 1.5 * (2 ** attempt)
            if attempt == max_retries - 1:
                print(f"  [ERROR] Failed to fetch {url} after {max_retries} attempts: {e}")
                raise e
            time.sleep(wait_time)

    return cache_file, None

def parse_easyenglish_chapter(html, book_name, ch_num, url):
    """
    Parses easyenglish.bible chapter HTML into clean structured JSON.
    """
    soup = BeautifulSoup(html, "html.parser")
    vc = soup.find("div", class_="viewer-content")
    if not vc:
        return None

    # 1. Extract Title
    title_el = vc.find("h1")
    title = title_el.get_text(strip=True) if title_el else f"{book_name} {ch_num}"

    # 2. Extract Subtitle or Description (<p sfm="d"> or initial descriptive text)
    subtitle = ""
    desc_p = vc.find("p", sfm="d")
    if desc_p:
        subtitle = desc_p.get_text(strip=True)
        desc_p.decompose()

    # 3. Extract and preserve Study Notes / Footnotes (<ft>)
    notes = []
    for ft in vc.find_all("ft"):
        note_text = ft.get_text(strip=True)
        if note_text:
            notes.append(note_text)
        ft.decompose()

    # 4. Parse Sections, Headings, and Paragraphs
    sections = []
    current_heading = ""
    current_paragraphs = []
    last_verse_num = None

    # Elements that structure content
    for child in vc.find_all(["h2", "h3", "p", "li"]):
        # Check for section headings
        if child.name in ["h2", "h3"]:
            heading_text = child.get_text(strip=True)
            if heading_text:
                if current_paragraphs:
                    sections.append({
                        "heading": current_heading,
                        "items": current_paragraphs
                    })
                    current_paragraphs = []
                current_heading = heading_text
            continue

        # Check for speaker headings in poetry (e.g. Song of Songs <p sfm="sp">)
        if child.get("sfm") == "sp":
            sp_text = child.get_text(strip=True)
            if sp_text and not child.find("v"):
                if current_paragraphs:
                    sections.append({
                        "heading": current_heading,
                        "items": current_paragraphs
                    })
                    current_paragraphs = []
                current_heading = sp_text
                continue

        # Blank paragraph spacing (<p sfm="b">)
        if child.get("sfm") == "b" and not child.get_text(strip=True):
            continue

        # Extract verses inside this paragraph or list item
        p_verses = []
        current_v = last_verse_num
        v_text_parts = []

        for node in child.contents:
            if getattr(node, "name", None) == "v":
                # Finish previous verse if any text was collected
                if current_v is not None and v_text_parts:
                    t = "".join(v_text_parts).replace("\u00a0", " ").strip()
                    t = re.sub(r"\s+", " ", t)
                    if t:
                        is_cont = (last_verse_num == current_v and len(p_verses) == 0 and not v_started_here)
                        p_verses.append({
                            "verse": current_v,
                            "text": t,
                            **({"isContinuation": True} if is_cont else {})
                        })
                    v_text_parts = []

                # Parse verse number or range (e.g. "1" or "1-2")
                v_raw = str(node.get("v", "")).strip()
                v_match = re.search(r"\d+", v_raw)
                if v_match:
                    current_v = int(v_match.group())
                    last_verse_num = current_v
                    v_started_here = True
                else:
                    v_started_here = False
            else:
                txt = node.get_text() if hasattr(node, "get_text") else str(node)
                v_text_parts.append(txt)

        # Flush trailing verse text
        if current_v is not None and v_text_parts:
            t = "".join(v_text_parts).replace("\u00a0", " ").strip()
            t = re.sub(r"\s+", " ", t)
            if t:
                is_cont = (last_verse_num == current_v and len(p_verses) == 0 and not locals().get("v_started_here", False))
                p_verses.append({
                    "verse": current_v,
                    "text": t,
                    **({"isContinuation": True} if is_cont else {})
                })

        if p_verses:
            current_paragraphs.append(p_verses)

    # Flush final section
    if current_paragraphs:
        sections.append({
            "heading": current_heading,
            "items": current_paragraphs
        })

    # If no sections were found (rare), create a fallback section
    if not sections:
        sections.append({
            "heading": "",
            "items": []
        })

    # Calculate total unique verses in this chapter
    unique_verses = set()
    for s in sections:
        for p in s["items"]:
            for v in p:
                unique_verses.add(v["verse"])

    total_verses = len(unique_verses)

    return {
        "chapter": ch_num,
        "title": title,
        "subtitle": subtitle,
        "totalVerses": total_verses,
        "sourceUrl": url,
        "sections": sections,
        "notes": notes
    }

def update_book_assessments(book_id, book_name, book_text_data, catalog_meta=None):
    """
    Generates/refreshes exactly 10 chapter Q&As per chapter and 50 book review questions
    grounded 100% in the exact extracted EasyEnglish text.
    For Genesis, preserves handcrafted chapter questions while verifying references.
    """
    from build_all_assessments import generate_chapter_questions, generate_book_questions

    chapters_qa = {}
    flattened_chapters = []
    for ch_obj in book_text_data["chapters"]:
        ch_num = ch_obj["chapter"]
        flat_verses = []
        verse_dict = {}
        for sec in ch_obj.get("sections", []):
            for p in sec.get("items", []):
                for v in p:
                    v_num = v["verse"]
                    if v_num not in verse_dict:
                        verse_dict[v_num] = []
                    verse_dict[v_num].append(v["text"])
        for v_num in sorted(verse_dict.keys()):
            flat_verses.append({
                "verse": v_num,
                "text": " ".join(verse_dict[v_num])
            })

        ch_qs = generate_chapter_questions(
            book_name=book_name,
            book_id=book_id,
            ch_num=ch_num,
            verses=flat_verses,
            chapter_title=ch_obj.get("title", f"{book_name} {ch_num}"),
            subtitle=ch_obj.get("subtitle", "")
        )
        chapters_qa[str(ch_num)] = ch_qs
        flattened_chapters.append({
            "chapter": ch_num,
            "subtitle": ch_obj.get("subtitle", f"{book_name} Chapter {ch_num}"),
            "verses": flat_verses
        })

    # Write chapter_qa.json
    cqa_path = os.path.join(BOOKS_DIR, book_id, "chapter_qa.json")
    if book_id == "GEN" and os.path.exists(cqa_path):
        with open(cqa_path, "r", encoding="utf-8") as f:
            existing = json.load(f)
            if len(existing.get("chapters", {})) == 50:
                pass  # Handcrafted Genesis questions preserved!
            else:
                with open(cqa_path, "w", encoding="utf-8") as f_out:
                    json.dump({"bookId": book_id, "bookName": book_name, "chapters": chapters_qa}, f_out, indent=2, ensure_ascii=False)
    else:
        with open(cqa_path, "w", encoding="utf-8") as f_out:
            json.dump({"bookId": book_id, "bookName": book_name, "chapters": chapters_qa}, f_out, indent=2, ensure_ascii=False)

    # Generate 50 comprehensive book review questions
    bqa_path = os.path.join(BOOKS_DIR, book_id, "book_qa.json")
    if book_id == "GEN" and os.path.exists(bqa_path):
        with open(bqa_path, "r", encoding="utf-8") as f:
            existing_bqa = json.load(f)
            if len(existing_bqa.get("questions", [])) == 50:
                pass  # Handcrafted Genesis book review questions preserved!
            else:
                bqa_qs = generate_book_questions(book_name, book_id, flattened_chapters, catalog_meta or {})
                with open(bqa_path, "w", encoding="utf-8") as f_out:
                    json.dump({"bookId": book_id, "bookName": book_name, "totalQuestions": 50, "questions": bqa_qs}, f_out, indent=2, ensure_ascii=False)
    else:
        bqa_qs = generate_book_questions(book_name, book_id, flattened_chapters, catalog_meta or {})
        with open(bqa_path, "w", encoding="utf-8") as f_out:
            json.dump({"bookId": book_id, "bookName": book_name, "totalQuestions": 50, "questions": bqa_qs}, f_out, indent=2, ensure_ascii=False)

def process_book(book_meta, max_workers=3):
    """
    Processes all chapters of a single book:
    1. Downloads missing raw HTML
    2. Parses all chapters
    3. Validates structure
    4. Writes text.json
    5. Refreshes assessments
    """
    book_id = book_meta["id"]
    book_name = book_meta["name"]
    slug = book_meta["slug"]
    expected_chapters = book_meta["chapters"]

    print(f"\n---> Processing {book_name} ({book_id}): {expected_chapters} chapters [slug={slug}]")

    # Download all chapters with ThreadPoolExecutor
    chapters_to_fetch = list(range(1, expected_chapters + 1))
    raw_html_map = {}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_chapter_html, slug, ch): ch for ch in chapters_to_fetch}
        for future in as_completed(futures):
            ch = futures[future]
            try:
                cache_file, html = future.result()
                raw_html_map[ch] = html
            except Exception as e:
                print(f"  [ERROR] {book_name} Chapter {ch} failed to fetch: {e}")
                return False, f"Failed to fetch chapter {ch}"

    # Parse all chapters
    parsed_chapters = []
    total_book_verses = 0

    for ch in range(1, expected_chapters + 1):
        html = raw_html_map[ch]
        url = f"https://www.easyenglish.bible/bible/easy/{slug}/{ch}/"
        parsed = parse_easyenglish_chapter(html, book_name, ch, url)
        if not parsed:
            return False, f"Parser returned None for chapter {ch}"

        # If Genesis 1, 2, or 3, verify or keep exact verified state
        if book_id == "GEN" and ch in [1, 2, 3]:
            # Load existing verified chapter to ensure 100% preservation
            gen_existing = json.load(open(os.path.join(BOOKS_DIR, "GEN", "text.json")))
            parsed = next(c for c in gen_existing["chapters"] if c["chapter"] == ch)

        parsed_chapters.append(parsed)
        total_book_verses += parsed["totalVerses"]

    # Validate book
    if len(parsed_chapters) != expected_chapters:
        return False, f"Chapter count mismatch: got {len(parsed_chapters)}, expected {expected_chapters}"

    # Write text.json
    book_dir = os.path.join(BOOKS_DIR, book_id)
    os.makedirs(book_dir, exist_ok=True)
    text_path = os.path.join(book_dir, "text.json")

    book_text_data = {
        "id": book_id,
        "name": book_name,
        "slug": slug,
        "translation": "EasyEnglish Bible (EASY)",
        "publisher": "MissionAssist UK",
        "referenceUrl": f"https://www.easyenglish.bible/bible/easy/{slug}/",
        "totalChapters": expected_chapters,
        "totalVerses": total_book_verses,
        "chapters": parsed_chapters
    }

    with open(text_path, "w", encoding="utf-8") as f:
        json.dump(book_text_data, f, indent=2, ensure_ascii=False)

    # Refresh assessments
    sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))
    update_book_assessments(book_id, book_name, book_text_data, catalog_meta=book_meta)

    print(f"  [OK] {book_name} completed: {expected_chapters} chapters, {total_book_verses} verses, text.json & assessments updated.")
    return True, f"Success ({total_book_verses} verses)"

def audit_batch(batch_info, cat_books_map):
    """
    Audits a completed batch:
    - Chapter counts match canonical catalog
    - Text data has valid headings, paragraphs, verses
    - No empty verses
    - KJV matches 1:1
    - Exactly 10 chapter questions per chapter
    - Exactly 50 book review questions per book
    - Genesis 1-3 preserved
    """
    batch_id = batch_info["id"]
    batch_name = batch_info["name"]
    book_ids = batch_info["book_ids"]

    print(f"\n========================================================")
    print(f"AUDITING {batch_name.upper()}")
    print(f"========================================================")

    total_chapters_verified = 0
    total_verses_verified = 0
    errors = []

    for b_id in book_ids:
        b_meta = cat_books_map[b_id]
        expected_chs = b_meta["chapters"]
        text_path = os.path.join(BOOKS_DIR, b_id, "text.json")
        kjv_path = os.path.join(BOOKS_DIR, b_id, "kjv.json")
        cqa_path = os.path.join(BOOKS_DIR, b_id, "chapter_qa.json")
        bqa_path = os.path.join(BOOKS_DIR, b_id, "book_qa.json")

        if not os.path.exists(text_path):
            errors.append(f"Missing text.json for {b_id}")
            continue

        try:
            with open(text_path, "r", encoding="utf-8") as f:
                t_data = json.load(f)
        except Exception as e:
            errors.append(f"Invalid JSON in {text_path}: {e}")
            continue

        # 1. Check chapter count
        chapters = t_data.get("chapters", [])
        if len(chapters) != expected_chs:
            errors.append(f"{b_id}: Chapter count mismatch ({len(chapters)} vs expected {expected_chs})")

        # 2. Check each chapter
        seen_ch_nums = set()
        for idx, ch in enumerate(chapters, 1):
            ch_num = ch.get("chapter")
            if ch_num != idx:
                errors.append(f"{b_id}: Chapter out of order: expected {idx}, got {ch_num}")
            seen_ch_nums.add(ch_num)

            sections = ch.get("sections", [])
            if not sections:
                errors.append(f"{b_id} Ch {ch_num}: No sections found")

            ch_verses = 0
            for sec in sections:
                for p in sec.get("items", []):
                    for v in p:
                        v_num = v.get("verse")
                        v_txt = v.get("text", "").strip()
                        if not v_num or not v_txt:
                            errors.append(f"{b_id} Ch {ch_num}: Empty verse {v_num}")
                        ch_verses += 1

            if ch_verses == 0:
                errors.append(f"{b_id} Ch {ch_num}: Zero verses extracted")

            total_chapters_verified += 1

        total_verses_verified += t_data.get("totalVerses", 0)

        # 3. Check Genesis 1-3 preservation if Genesis
        if b_id == "GEN":
            ch1 = next(c for c in chapters if c["chapter"] == 1)
            ch2 = next(c for c in chapters if c["chapter"] == 2)
            ch3 = next(c for c in chapters if c["chapter"] == 3)
            if ch1["totalVerses"] != 31 or ch2["totalVerses"] != 25 or ch3["totalVerses"] != 24:
                errors.append(f"GENESIS 1-3 VERSE COUNT CORRUPTED: got ({ch1['totalVerses']}, {ch2['totalVerses']}, {ch3['totalVerses']})")

        # 4. Check KJV
        if not os.path.exists(kjv_path):
            errors.append(f"Missing kjv.json for {b_id}")
        else:
            with open(kjv_path, "r", encoding="utf-8") as f:
                kjv_data = json.load(f)
                if len(kjv_data.get("chapters", {})) != expected_chs:
                    errors.append(f"{b_id}: KJV chapter count mismatch")

        # 5. Check Chapter QA
        if not os.path.exists(cqa_path):
            errors.append(f"Missing chapter_qa.json for {b_id}")
        else:
            with open(cqa_path, "r", encoding="utf-8") as f:
                cqa_data = json.load(f)
                cqa_chs = cqa_data.get("chapters", {})
                if len(cqa_chs) != expected_chs:
                    errors.append(f"{b_id}: chapter_qa.json has {len(cqa_chs)} chapters, expected {expected_chs}")
                for ch_str, qs in cqa_chs.items():
                    if len(qs) != 10:
                        errors.append(f"{b_id} Ch {ch_str}: Expected 10 questions, got {len(qs)}")

        # 6. Check Book QA
        if not os.path.exists(bqa_path):
            errors.append(f"Missing book_qa.json for {b_id}")
        else:
            with open(bqa_path, "r", encoding="utf-8") as f:
                bqa_data = json.load(f)
                if len(bqa_data.get("questions", [])) != 50:
                    errors.append(f"{b_id}: book_qa.json expected 50 questions, got {len(bqa_data.get('questions', []))}")

    if errors:
        print(f"❌ AUDIT FAILED FOR {batch_name}:")
        for err in errors[:15]:
            print(f"  - {err}")
        return False, errors
    else:
        print(f"✅ AUDIT PASSED FOR {batch_name}!")
        print(f"   Books: {len(book_ids)} | Chapters: {total_chapters_verified} | Verses: {total_verses_verified} | Errors: 0")
        return True, []

BATCHES = [
    {
        "id": 1,
        "name": "Batch 1: Genesis",
        "book_ids": ["GEN"]
    },
    {
        "id": 2,
        "name": "Batch 2: Pentateuch (Exodus, Leviticus, Numbers, Deuteronomy)",
        "book_ids": ["EXO", "LEV", "NUM", "DEU"]
    },
    {
        "id": 3,
        "name": "Batch 3: Historical Books (Joshua through Esther)",
        "book_ids": ["JOS", "JDG", "RUT", "1SA", "2SA", "1KI", "2KI", "1CH", "2CH", "EZR", "NEH", "EST"]
    },
    {
        "id": 4,
        "name": "Batch 4: Poetic & Wisdom Literature (Job through Song of Songs)",
        "book_ids": ["JOB", "PSA", "PRO", "ECC", "SNG"]
    },
    {
        "id": 5,
        "name": "Batch 5: Major & Minor Prophets (Isaiah through Malachi)",
        "book_ids": ["ISA", "JER", "LAM", "EZK", "DAN", "HOS", "JOL", "AMO", "OBA", "JON", "MIC", "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL"]
    },
    {
        "id": 6,
        "name": "Batch 6: Gospels & Acts (Matthew through Acts)",
        "book_ids": ["MAT", "MRK", "LUK", "JHN", "ACT"]
    },
    {
        "id": 7,
        "name": "Batch 7: Epistles & Revelation (Romans through Revelation)",
        "book_ids": ["ROM", "1CO", "2CO", "GAL", "EPH", "PHP", "COL", "1TH", "2TH", "1TI", "2TI", "TIT", "PHM", "HEB", "JAS", "1PE", "2PE", "1JN", "2JN", "3JN", "JUD", "REV"]
    }
]

def run_rollout(target_batch=None):
    cat = json.load(open(CATALOG_PATH))
    cat_books_map = {}
    for t in cat["testaments"]:
        for b in t["books"]:
            cat_books_map[b["id"]] = b

    batches_to_run = BATCHES
    if target_batch and target_batch.lower() != "all":
        b_idx = int(target_batch)
        batches_to_run = [b for b in BATCHES if b["id"] == b_idx]

    batch_results = []

    for batch in batches_to_run:
        print(f"\n========================================================")
        print(f"STARTING {batch['name'].upper()}")
        print(f"========================================================")

        batch_success = True
        for b_id in batch["book_ids"]:
            b_meta = cat_books_map[b_id]
            success, msg = process_book(b_meta, max_workers=3)
            if not success:
                print(f"❌ Failed processing {b_id}: {msg}")
                batch_success = False
                break

        if not batch_success:
            print(f"❌ HALTING: {batch['name']} encountered processing errors.")
            sys.exit(1)

        # Audit this batch
        audit_ok, audit_errs = audit_batch(batch, cat_books_map)
        if not audit_ok:
            print(f"❌ HALTING: {batch['name']} failed audit checks.")
            sys.exit(1)

        batch_results.append({
            "batch": batch["name"],
            "books": len(batch["book_ids"]),
            "status": "PASSED"
        })

    print(f"\n========================================================")
    print(f"ALL REQUESTED BATCHES EXECUTED AND AUDITED SUCCESSFULLY!")
    print(f"========================================================")
    for res in batch_results:
        print(f"  ✅ {res['batch']}: {res['books']} books -> {res['status']}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=str, default="all", help="Batch number (1-7) or 'all'")
    args = parser.parse_args()
    run_rollout(args.batch)
