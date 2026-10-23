#!/usr/bin/env python3
import json
import os
import sys
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(BASE_DIR, "src", "data", "bible_catalog.json")
BOOKS_DIR = os.path.join(BASE_DIR, "src", "data", "books")

def validate():
    print("=" * 60)
    print("HOLY BIBLE READER — FULL CANONICAL AUDIT & VALIDATION")
    print("=" * 60)

    if not os.path.exists(CATALOG_PATH):
        print("FAIL: Catalog file missing:", CATALOG_PATH)
        return False

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    testaments = catalog.get("testaments", [])
    if len(testaments) != 2:
        print(f"FAIL: Expected 2 testaments, found {len(testaments)}")
        return False

    all_books = []
    for t in testaments:
        all_books.extend(t.get("books", []))

    if len(all_books) != 66:
        print(f"FAIL: Expected 66 books, found {len(all_books)}")
        return False

    ot_books = testaments[0].get("books", [])
    nt_books = testaments[1].get("books", [])
    if len(ot_books) != 39:
        print(f"FAIL: Expected 39 OT books, found {len(ot_books)}")
        return False
    if len(nt_books) != 27:
        print(f"FAIL: Expected 27 NT books, found {len(nt_books)}")
        return False

    total_chapters_expected = sum(b["chapters"] for b in all_books)
    if total_chapters_expected != 1189:
        print(f"FAIL: Expected 1189 total chapters in catalog, found {total_chapters_expected}")
        return False

    print(f"✓ Catalog verified: 66 books (39 OT, 27 NT), {total_chapters_expected} chapters")

    # Detailed Audit per Book
    errors = []
    audited_books = 0
    total_chapters_verified = 0
    total_chapter_questions = 0
    total_book_questions = 0
    total_verses_text = 0
    total_verses_kjv = 0

    for book in all_books:
        book_id = book["id"]
        book_name = book["name"]
        expected_chapters = book["chapters"]
        book_dir = os.path.join(BOOKS_DIR, book_id)

        if not os.path.isdir(book_dir):
            errors.append(f"[{book_id}] Directory missing: {book_dir}")
            continue

        text_file = os.path.join(book_dir, "text.json")
        kjv_file = os.path.join(book_dir, "kjv.json")
        chapter_qa_file = os.path.join(book_dir, "chapter_qa.json")
        book_qa_file = os.path.join(book_dir, "book_qa.json")

        for f_path, label in [(text_file, "text.json"), (kjv_file, "kjv.json"), (chapter_qa_file, "chapter_qa.json"), (book_qa_file, "book_qa.json")]:
            if not os.path.isfile(f_path):
                errors.append(f"[{book_id}] Missing required file: {label}")

        if errors and len(errors) > 20:
            break

        # 1. Audit Text.json
        try:
            with open(text_file, "r", encoding="utf-8") as f:
                text_data = json.load(f)
            chapters = text_data.get("chapters", [])
            if len(chapters) != expected_chapters:
                errors.append(f"[{book_id}] text.json has {len(chapters)} chapters, expected {expected_chapters}")
            else:
                for idx, ch in enumerate(chapters, 1):
                    ch_num = ch.get("chapter")
                    if ch_num != idx:
                        errors.append(f"[{book_id}] Ch {ch_num} out of order (expected {idx})")

                    ch_verse_count = 0
                    seen_badges = set()
                    sections = ch.get("sections", [])
                    if sections:
                        for sec in sections:
                            for p in sec.get("items", []):
                                for v in p:
                                    v_num = v.get("verse")
                                    v_txt = v.get("text", "").strip()
                                    if v_num and v_txt:
                                        ch_verse_count += 1

                                    # Check for duplicate non-continuation badge
                                    if not v.get("isContinuation"):
                                        if v_num in seen_badges:
                                            errors.append(f"[{book_id}] Ch {ch_num}: Duplicate verse badge for verse {v_num}")
                                        seen_badges.add(v_num)

                                    # Check for embedded foreign verse numbers in text (e.g. "3 God will keep..." inside verse 2)
                                    m = re.search(r'[.!?‘\'"”]\s*(\d{1,3})\s+[A-Z]', v_txt)
                                    if m and int(m.group(1)) == v_num + 1:
                                        errors.append(f"[{book_id}] Ch {ch_num}: Embedded verse number '{m.group(0)}' inside verse {v_num} text")
                    elif "verses" in ch:
                        ch_verse_count = len(ch["verses"])

                    if ch_verse_count == 0:
                        errors.append(f"[{book_id}] Ch {ch_num} has 0 verses in text.json")
                    total_verses_text += ch_verse_count
        except Exception as e:
            errors.append(f"[{book_id}] text.json failed to parse: {e}")

        # 2. Audit KJV.json
        try:
            with open(kjv_file, "r", encoding="utf-8") as f:
                kjv_data = json.load(f)
            kjv_chapters = kjv_data.get("chapters", {})
            if len(kjv_chapters) != expected_chapters:
                errors.append(f"[{book_id}] kjv.json has {len(kjv_chapters)} chapters, expected {expected_chapters}")
            else:
                for ch_str, v_dict in kjv_chapters.items():
                    if len(v_dict) == 0:
                        errors.append(f"[{book_id}] Ch {ch_str} has 0 verses in kjv.json")
                    total_verses_kjv += len(v_dict)
        except Exception as e:
            errors.append(f"[{book_id}] kjv.json failed to parse: {e}")

        # 3. Audit Chapter QA
        try:
            with open(chapter_qa_file, "r", encoding="utf-8") as f:
                c_qa_data = json.load(f)
            qa_chapters = c_qa_data.get("chapters", {})
            if len(qa_chapters) != expected_chapters:
                errors.append(f"[{book_id}] chapter_qa.json has {len(qa_chapters)} chapters, expected {expected_chapters}")
            else:
                for ch_idx in range(1, expected_chapters + 1):
                    ch_key = str(ch_idx)
                    q_list = qa_chapters.get(ch_key, [])
                    if len(q_list) != 10:
                        errors.append(f"[{book_id}] Ch {ch_key} has {len(q_list)} questions, expected 10")
                    total_chapter_questions += len(q_list)
                    for q_idx, q in enumerate(q_list, 1):
                        q_text = q.get("question", "")
                        opts = q.get("options", [])
                        c_idx = q.get("correctAnswerIndex")
                        c_ans = q.get("correctAnswer")
                        ref = q.get("reference", "")
                        exp = q.get("explanation", "")

                        if not q_text or len(q_text) < 5:
                            errors.append(f"[{book_id}] Ch {ch_key} Q{q_idx} empty/short question")
                        if len(opts) != 4:
                            errors.append(f"[{book_id}] Ch {ch_key} Q{q_idx} has {len(opts)} options, expected 4")
                        if c_idx is None or c_idx < 0 or c_idx >= 4:
                            errors.append(f"[{book_id}] Ch {ch_key} Q{q_idx} invalid correctAnswerIndex: {c_idx}")
                        elif opts[c_idx] != c_ans:
                            errors.append(f"[{book_id}] Ch {ch_key} Q{q_idx} correctAnswer mismatch: '{c_ans}' != '{opts[c_idx]}'")
                        if not ref:
                            errors.append(f"[{book_id}] Ch {ch_key} Q{q_idx} missing reference")
                        if not exp or len(exp) < 5:
                            errors.append(f"[{book_id}] Ch {ch_key} Q{q_idx} missing/short explanation")
        except Exception as e:
            errors.append(f"[{book_id}] chapter_qa.json failed to parse: {e}")

        # 4. Audit Book QA
        try:
            with open(book_qa_file, "r", encoding="utf-8") as f:
                b_qa_data = json.load(f)
            b_questions = b_qa_data.get("questions", [])
            if len(b_questions) != 50:
                errors.append(f"[{book_id}] book_qa.json has {len(b_questions)} questions, expected 50")
            total_book_questions += len(b_questions)
            for q_idx, q in enumerate(b_questions, 1):
                q_text = q.get("question", "")
                opts = q.get("options", [])
                c_idx = q.get("correctAnswerIndex")
                c_ans = q.get("correctAnswer")
                ref = q.get("reference", "")
                exp = q.get("explanation", "")

                if not q_text or len(q_text) < 5:
                    errors.append(f"[{book_id}] Book QA Q{q_idx} empty/short question")
                if len(opts) != 4:
                    errors.append(f"[{book_id}] Book QA Q{q_idx} has {len(opts)} options, expected 4")
                if c_idx is None or c_idx < 0 or c_idx >= 4:
                    errors.append(f"[{book_id}] Book QA Q{q_idx} invalid correctAnswerIndex: {c_idx}")
                elif opts[c_idx] != c_ans:
                    errors.append(f"[{book_id}] Book QA Q{q_idx} correctAnswer mismatch: '{c_ans}' != '{opts[c_idx]}'")
                if not ref:
                    errors.append(f"[{book_id}] Book QA Q{q_idx} missing reference")
                if not exp or len(exp) < 5:
                    errors.append(f"[{book_id}] Book QA Q{q_idx} missing/short explanation")
        except Exception as e:
            errors.append(f"[{book_id}] book_qa.json failed to parse: {e}")

        total_chapters_verified += expected_chapters
        audited_books += 1

    print("\n" + "=" * 60)
    print("AUDIT RESULTS:")
    print("=" * 60)
    print(f"Books Audited:               {audited_books} / 66")
    print(f"Total Chapters Verified:     {total_chapters_verified} / 1,189")
    print(f"Total Verses (EasyEnglish):  {total_verses_text:,}")
    print(f"Total Verses (KJV):          {total_verses_kjv:,}")
    print(f"Total Chapter Questions:     {total_chapter_questions:,} (Expected: 11,890)")
    print(f"Total Book Review Questions: {total_book_questions:,} (Expected: 3,300)")

    if errors:
        print(f"\n❌ VALIDATION FAILED with {len(errors)} error(s):")
        for err in errors[:25]:
            print("  -", err)
        if len(errors) > 25:
            print(f"  ... and {len(errors) - 25} more errors.")
        return False
    else:
        print("\n✅ VALIDATION PASSED 100%! All 66 books, 1,189 chapters, dual translations, and 15,190 questions are complete, verified, and intact with 0 errors!")
        return True

if __name__ == "__main__":
    success = validate()
    sys.exit(0 if success else 1)
