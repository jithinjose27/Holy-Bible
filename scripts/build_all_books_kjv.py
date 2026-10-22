import json
import os

with open("src/data/bible_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

kjv_dir = "data_sources/Bible-kjv"
books_out_dir = "src/data/books"
os.makedirs(books_out_dir, exist_ok=True)

book_name_map = {
    "1 Samuel": "1Samuel",
    "2 Samuel": "2Samuel",
    "1 Kings": "1Kings",
    "2 Kings": "2Kings",
    "1 Chronicles": "1Chronicles",
    "2 Chronicles": "2Chronicles",
    "Song of Songs": "SongofSolomon",
    "1 Thessalonians": "1Thessalonians",
    "2 Thessalonians": "2Thessalonians",
    "1 Timothy": "1Timothy",
    "2 Timothy": "2Timothy",
    "1 Peter": "1Peter",
    "2 Peter": "2Peter",
    "1 John": "1John",
    "2 John": "2John",
    "3 John": "3John",
}

total_books = 0
total_chapters = 0
total_verses = 0

for t in catalog["testaments"]:
    for b in t["books"]:
        b_name = b["name"]
        b_id = b["id"]
        file_name = book_name_map.get(b_name, b_name.replace(" ", "")) + ".json"
        in_path = os.path.join(kjv_dir, file_name)
        if not os.path.exists(in_path):
            raise FileNotFoundError(f"Missing KJV source for {b_name} ({in_path})")

        with open(in_path, "r", encoding="utf-8") as f_in:
            raw_data = json.load(f_in)

        # Convert to standard normalized mapping: chapters: { "1": { "1": "text", ... } }
        normalized_chapters = {}
        for ch_obj in raw_data["chapters"]:
            ch_num = str(ch_obj["chapter"])
            v_map = {}
            for v_obj in ch_obj["verses"]:
                v_num = str(v_obj["verse"])
                v_map[v_num] = v_obj["text"]
                total_verses += 1
            normalized_chapters[ch_num] = v_map
            total_chapters += 1

        book_dir = os.path.join(books_out_dir, b_id)
        os.makedirs(book_dir, exist_ok=True)

        out_data = {
            "translation": "King James Version (KJV)",
            "book": b_name,
            "bookId": b_id,
            "totalChapters": len(normalized_chapters),
            "chapters": normalized_chapters
        }

        out_path = os.path.join(book_dir, "kjv.json")
        with open(out_path, "w", encoding="utf-8") as f_out:
            json.dump(out_data, f_out, ensure_ascii=False)

        total_books += 1

print(f"Successfully processed {total_books}/66 books into {books_out_dir}/")
print(f"Total normalized chapters: {total_chapters}/1189")
print(f"Total normalized verses: {total_verses}/31102")
