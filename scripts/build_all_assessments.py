#!/usr/bin/env python3
import json
import os
import re
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(BASE_DIR, "src", "data", "bible_catalog.json")
BOOKS_DIR = os.path.join(BASE_DIR, "src", "data", "books")

# Common biblical entities and distractor pools
DISTRACTOR_NAMES = [
    "Abraham", "Moses", "David", "Solomon", "Elijah", "Elisha", "Samuel", "Joshua",
    "Aaron", "Joseph", "Daniel", "Isaiah", "Jeremiah", "Ezekiel", "Gideon", "Samson",
    "Peter", "Paul", "John", "James", "Philip", "Stephen", "Barnabas", "Timothy",
    "Caleb", "Jonathan", "Boaz", "Nehemiah", "Ezra", "Mordecai", "Job", "Hezekiah",
    "Josiah", "Gideon", "Barak", "Jephthah", "Silas", "Titus", "Apollos", "Luke"
]

DISTRACTOR_PLACES = [
    "Jerusalem", "Bethlehem", "Nazareth", "Capernaum", "Jericho", "Mount Sinai",
    "Mount Carmel", "Mount Zion", "Mount of Olives", "Jordan River", "Sea of Galilee",
    "Red Sea", "Egypt", "Babylon", "Nineveh", "Damascus", "Antioch", "Hebron",
    "Samaria", "Shechem", "Shiloh", "Bethel", "Beersheba", "Gaza", "Joppa", "Tyre",
    "Sidon", "Ephesus", "Corinth", "Philippi", "Thessalonica", "Rome", "Athens"
]

DISTRACTOR_NUMBERS = [
    "3", "7", "10", "12", "14", "40", "50", "70", "100", "120", "144", "300", "500", "1,000", "7,000"
]

def clean_sentence(text):
    text = re.sub(r'\[.*?\]', '', text)
    text = " ".join(text.split())
    return text

def pick_distractors(correct, pool, count=3):
    filtered = [p for p in pool if p.lower() != correct.lower()]
    random.shuffle(filtered)
    return filtered[:count]

def generate_chapter_questions(book_name, book_id, ch_num, verses, chapter_title, subtitle):
    """
    Generates exactly 10 questions for a given chapter using its verses.
    """
    slug = book_id.lower()
    total_v = len(verses)
    if total_v == 0:
        return []

    # Helper to get verse text by 1-indexed number
    def get_v(num):
        for v in verses:
            if v["verse"] == num:
                return v["text"]
        return verses[min(num - 1, total_v - 1)]["text"]

    questions = []

    # Q1: Opening verse / foundation of the chapter
    v1_text = get_v(1)
    q1_text = f"According to {book_name} {ch_num}:1, what is the opening statement or setting of this chapter?"
    opt1_correct = f"It records: “{v1_text[:65]}...”" if len(v1_text) > 65 else f"It records: “{v1_text}”"
    opt1_d = [
        f"It begins with a prayer of thanksgiving for deliverance in {book_name}",
        f"It opens with a formal census and counting of the congregation",
        f"It records a severe judgment pronounced against neighboring nations"
    ]
    options1 = [opt1_correct] + opt1_d
    c_idx1 = 0
    questions.append({
        "id": f"{slug}-{ch_num}-q1",
        "questionNumber": 1,
        "question": q1_text,
        "options": options1,
        "correctAnswerIndex": c_idx1,
        "correctAnswer": opt1_correct,
        "reference": f"{book_name} {ch_num}:1",
        "explanation": f"The chapter begins directly with the statement: '{v1_text}'."
    })

    # Pick 9 evenly spaced verses through the chapter for questions 2 to 10
    step = max(1, total_v // 10)
    selected_verse_nums = []
    for i in range(2, 11):
        target_v = min(total_v, max(2, (i - 1) * step))
        if target_v in selected_verse_nums and target_v < total_v:
            target_v += 1
        selected_verse_nums.append(target_v)

    question_templates = [
        ("What key instruction, event, or declaration is set forth in", "instruction"),
        ("What significant action or revelation occurs in", "action"),
        ("What truth or description is highlighted in", "truth"),
        ("According to the text, what happened or was commanded in", "event"),
        ("What central message or instruction is delivered in", "message"),
        ("What detail regarding God's work, covenant, or people is given in", "covenant"),
        ("What phrase or account is recorded in", "phrase"),
        ("How does the passage describe the circumstances or people in", "circumstance"),
        ("In the concluding portion of the chapter, what takes place in", "conclusion")
    ]

    for idx, v_num in enumerate(selected_verse_nums, start=2):
        v_text = get_v(v_num)
        prefix, q_type = question_templates[idx - 2]
        q_text = f"{prefix} {book_name} {ch_num}:{v_num}?"

        # Shorten verse text for option
        words = v_text.split()
        if len(words) > 12:
            summary = " ".join(words[:11]) + "..."
        else:
            summary = v_text

        opt_correct = f"“{summary}”"

        # Generate 3 plausible distractors
        alt_v1 = get_v(max(1, (v_num + 3) % total_v))
        alt_v2 = get_v(max(1, (v_num + 7) % total_v))
        alt_summary1 = " ".join(alt_v1.split()[:9]) + "..." if len(alt_v1.split()) > 9 else alt_v1
        alt_summary2 = " ".join(alt_v2.split()[:9]) + "..." if len(alt_v2.split()) > 9 else alt_v2

        opt_d1 = f"“{alt_summary1}”"
        opt_d2 = f"“{alt_summary2}”"
        opt_d3 = f"An instruction regarding sacrificial regulations in the temple sanctuary"

        # Ensure unique options
        opts = [opt_correct]
        for d in [opt_d1, opt_d2, opt_d3]:
            if d not in opts:
                opts.append(d)
        while len(opts) < 4:
            opts.append(f"A general genealogy and listing of tribal leaders ({len(opts)})")

        # Shuffle options and determine correct index
        c_index = (idx - 1) % 4
        # Put opt_correct at c_index
        opts.remove(opt_correct)
        opts.insert(c_index, opt_correct)

        questions.append({
            "id": f"{slug}-{ch_num}-q{idx}",
            "questionNumber": idx,
            "question": q_text,
            "options": opts,
            "correctAnswerIndex": c_index,
            "correctAnswer": opt_correct,
            "reference": f"{book_name} {ch_num}:{v_num}",
            "explanation": f"{book_name} {ch_num}:{v_num} records: '{v_text}'."
        })

    return questions

def generate_book_questions(book_name, book_id, chapters, catalog_meta):
    """
    Generates exactly 50 comprehensive questions for a given book.
    """
    slug = book_id.lower()
    total_ch = len(chapters)
    questions = []

    # Generate 50 questions spanning all chapters
    for q_idx in range(1, 51):
        target_ch_idx = int(((q_idx - 1) / 50.0) * total_ch)
        target_ch_idx = min(target_ch_idx, total_ch - 1)
        target_ch = chapters[target_ch_idx]
        ch_num = target_ch["chapter"]
        subtitle = target_ch.get("subtitle", f"{book_name} Chapter {ch_num}")
        verses = target_ch.get("verses", [])
        v_sample = verses[0]["text"] if verses else f"The text of {book_name} {ch_num}"

        if q_idx == 1:
            q_text = f"How does the Book of {book_name} open in Chapter 1?"
            opt_correct = f"It introduces the foundational theme: '{subtitle}' and records “{v_sample[:60]}...”"
            opt_d = [
                f"It begins with a prophetic apocalypse concerning the end of the age",
                f"It opens with an apology written from Roman imprisonment",
                f"It begins with a collection of musical hymns and psalms"
            ]
        elif q_idx == 50:
            q_text = f"What is the culminating focus or final emphasis of the Book of {book_name} in Chapter {total_ch}?"
            last_v = verses[-1]["text"] if verses else "the final fulfillment"
            opt_correct = f"It concludes Chapter {total_ch} with: “{last_v[:65]}...”"
            opt_d = [
                f"It concludes with the tragic destruction of the tabernacle",
                f"It ends with an unresolved genealogy without a conclusion",
                f"It terminates abruptly with a warning of eternal silence"
            ]
        else:
            q_text = f"In {book_name} Chapter {ch_num} ({subtitle}), what principal theme or narrative is described?"
            opt_correct = f"The events concerning {subtitle.lower()} and God's dealings with His people"
            opt_d = [
                f"A lengthy discourse on the building of Solomon's palace columns",
                f"The chronological succession of Persian emperors",
                f"A dispute regarding the inheritance laws of the daughters of Zelophehad"
            ]

        # Rotate correct answer index 0, 1, 2, 3
        c_index = (q_idx - 1) % 4
        opts = [opt_d[0], opt_d[1], opt_d[2]]
        opts.insert(c_index, opt_correct)

        questions.append({
            "id": f"{slug}-book-q{q_idx}",
            "questionNumber": q_idx,
            "question": q_text,
            "options": opts,
            "correctAnswerIndex": c_index,
            "correctAnswer": opt_correct,
            "reference": f"{book_name} {ch_num}:1–{len(verses)}",
            "explanation": f"Chapter {ch_num} of {book_name} focuses on {subtitle.lower()}, demonstrating God's guidance and truth throughout this portion of the biblical narrative."
        })

    return questions

def main():
    print("Loading catalog...")
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    all_books = []
    for t in catalog["testaments"]:
        all_books.extend(t["books"])

    total_books = len(all_books)
    total_chapter_questions = 0
    total_book_questions = 0

    print(f"Starting assessment generation for all {total_books} books...")

    for b_idx, book in enumerate(all_books, 1):
        book_id = book["id"]
        book_name = book["name"]
        book_dir = os.path.join(BOOKS_DIR, book_id)
        os.makedirs(book_dir, exist_ok=True)

        chapter_qa_path = os.path.join(book_dir, "chapter_qa.json")
        book_qa_path = os.path.join(book_dir, "book_qa.json")

        # Preserve Genesis handcrafted assessments
        if book_id == "GEN" and os.path.exists(chapter_qa_path) and os.path.exists(book_qa_path):
            print(f"[{book_id}] Genesis chapter_qa.json and book_qa.json already present. Preserving.")
            with open(chapter_qa_path, "r", encoding="utf-8") as f:
                c_data = json.load(f)
                total_chapter_questions += c_data.get("totalQuestions", 500)
            with open(book_qa_path, "r", encoding="utf-8") as f:
                b_data = json.load(f)
                total_book_questions += b_data.get("totalQuestions", 50)
            continue

        text_path = os.path.join(book_dir, "text.json")
        if not os.path.exists(text_path):
            print(f"Error: {text_path} does not exist!")
            continue

        with open(text_path, "r", encoding="utf-8") as f:
            book_text_data = json.load(f)

        chapters = book_text_data.get("chapters", [])
        total_ch = len(chapters)

        # 1. Build Chapter QA
        chapters_qa = {}
        for ch in chapters:
            ch_num = ch["chapter"]
            ch_verses = ch.get("verses", [])
            ch_title = ch.get("title", f"{book_name} {ch_num}")
            ch_subtitle = ch.get("subtitle", "")

            ch_questions = generate_chapter_questions(book_name, book_id, ch_num, ch_verses, ch_title, ch_subtitle)
            chapters_qa[str(ch_num)] = ch_questions
            total_chapter_questions += len(ch_questions)

        chapter_payload = {
            "book": book_name,
            "bookId": book_id,
            "totalChapters": total_ch,
            "totalQuestions": len(chapters) * 10,
            "questionsPerChapter": 10,
            "chapters": chapters_qa
        }

        with open(chapter_qa_path, "w", encoding="utf-8") as f:
            json.dump(chapter_payload, f, indent=2, ensure_ascii=False)

        # 2. Build 50-Question Book Review QA
        book_questions = generate_book_questions(book_name, book_id, chapters, book)
        total_book_questions += len(book_questions)

        book_qa_payload = {
            "book": book_name,
            "bookId": book_id,
            "title": f"The Book of {book_name} — Comprehensive Review",
            "totalQuestions": len(book_questions),
            "questions": book_questions
        }

        with open(book_qa_path, "w", encoding="utf-8") as f:
            json.dump(book_qa_payload, f, indent=2, ensure_ascii=False)

        print(f"[{book_id}] Generated {book_name}: {len(chapters) * 10} chapter questions + 50 book review questions.")

    print("\n==========================================")
    print("Assessment Generation Complete!")
    print(f"Total Books: {total_books}")
    print(f"Total Chapter Questions: {total_chapter_questions} (Target: 11,890)")
    print(f"Total Book Review Questions: {total_book_questions} (Target: 3,300)")
    print("==========================================")

if __name__ == "__main__":
    main()
