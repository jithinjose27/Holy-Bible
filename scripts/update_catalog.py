import json

catalog_data = {
  "testaments": [
    {
      "name": "Old Testament",
      "id": "OT",
      "books": [
        { "name": "Genesis", "id": "GEN", "slug": "genesis", "chapters": 50, "order": 1, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Exodus", "id": "EXO", "slug": "exodus", "chapters": 40, "order": 2, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Leviticus", "id": "LEV", "slug": "leviticus", "chapters": 27, "order": 3, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Numbers", "id": "NUM", "slug": "numbers", "chapters": 36, "order": 4, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Deuteronomy", "id": "DEU", "slug": "deuteronomy", "chapters": 34, "order": 5, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Joshua", "id": "JOS", "slug": "joshua", "chapters": 24, "order": 6, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Judges", "id": "JDG", "slug": "judges", "chapters": 21, "order": 7, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Ruth", "id": "RUT", "slug": "ruth", "chapters": 4, "order": 8, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "1 Samuel", "id": "1SA", "slug": "1-samuel", "chapters": 31, "order": 9, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "2 Samuel", "id": "2SA", "slug": "2-samuel", "chapters": 24, "order": 10, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "1 Kings", "id": "1KI", "slug": "1-kings", "chapters": 22, "order": 11, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "2 Kings", "id": "2KI", "slug": "2-kings", "chapters": 25, "order": 12, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "1 Chronicles", "id": "1CH", "slug": "1-chronicles", "chapters": 29, "order": 13, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "2 Chronicles", "id": "2CH", "slug": "2-chronicles", "chapters": 36, "order": 14, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Ezra", "id": "EZR", "slug": "ezra", "chapters": 10, "order": 15, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Nehemiah", "id": "NEH", "slug": "nehemiah", "chapters": 13, "order": 16, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Esther", "id": "EST", "slug": "esther", "chapters": 10, "order": 17, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Job", "id": "JOB", "slug": "job", "chapters": 42, "order": 18, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Psalms", "id": "PSA", "slug": "psalm", "chapters": 150, "order": 19, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Proverbs", "id": "PRO", "slug": "proverbs", "chapters": 31, "order": 20, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Ecclesiastes", "id": "ECC", "slug": "ecclesiastes", "chapters": 12, "order": 21, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Song of Songs", "id": "SNG", "slug": "song-of-songs", "chapters": 8, "order": 22, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Isaiah", "id": "ISA", "slug": "isaiah", "chapters": 66, "order": 23, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Jeremiah", "id": "JER", "slug": "jeremiah", "chapters": 52, "order": 24, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Lamentations", "id": "LAM", "slug": "lamentations", "chapters": 5, "order": 25, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Ezekiel", "id": "EZK", "slug": "ezekiel", "chapters": 48, "order": 26, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Daniel", "id": "DAN", "slug": "daniel", "chapters": 12, "order": 27, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Hosea", "id": "HOS", "slug": "hosea", "chapters": 14, "order": 28, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Joel", "id": "JOL", "slug": "joel", "chapters": 3, "order": 29, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Amos", "id": "AMO", "slug": "amos", "chapters": 9, "order": 30, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Obadiah", "id": "OBA", "slug": "obadiah", "chapters": 1, "order": 31, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Jonah", "id": "JON", "slug": "jonah", "chapters": 4, "order": 32, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Micah", "id": "MIC", "slug": "micah", "chapters": 7, "order": 33, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Nahum", "id": "NAM", "slug": "nahum", "chapters": 3, "order": 34, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Habakkuk", "id": "HAB", "slug": "habakkuk", "chapters": 3, "order": 35, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Zephaniah", "id": "ZEP", "slug": "zephaniah", "chapters": 3, "order": 36, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Haggai", "id": "HAG", "slug": "haggai", "chapters": 2, "order": 37, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Zechariah", "id": "ZEC", "slug": "zechariah", "chapters": 14, "order": 38, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Malachi", "id": "MAL", "slug": "malachi", "chapters": 4, "order": 39, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True }
      ]
    },
    {
      "name": "New Testament",
      "id": "NT",
      "books": [
        { "name": "Matthew", "id": "MAT", "slug": "matthew", "chapters": 28, "order": 40, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Mark", "id": "MRK", "slug": "mark", "chapters": 16, "order": 41, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Luke", "id": "LUK", "slug": "luke", "chapters": 24, "order": 42, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "John", "id": "JHN", "slug": "john", "chapters": 21, "order": 43, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Acts", "id": "ACT", "slug": "acts", "chapters": 28, "order": 44, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Romans", "id": "ROM", "slug": "romans", "chapters": 16, "order": 45, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "1 Corinthians", "id": "1CO", "slug": "1-corinthians", "chapters": 16, "order": 46, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "2 Corinthians", "id": "2CO", "slug": "2-corinthians", "chapters": 13, "order": 47, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Galatians", "id": "GAL", "slug": "galatians", "chapters": 6, "order": 48, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Ephesians", "id": "EPH", "slug": "ephesians", "chapters": 6, "order": 49, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Philippians", "id": "PHP", "slug": "philippians", "chapters": 4, "order": 50, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Colossians", "id": "COL", "slug": "colossians", "chapters": 4, "order": 51, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "1 Thessalonians", "id": "1TH", "slug": "1-thessalonians", "chapters": 5, "order": 52, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "2 Thessalonians", "id": "2TH", "slug": "2-thessalonians", "chapters": 3, "order": 53, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "1 Timothy", "id": "1TI", "slug": "1-timothy", "chapters": 6, "order": 54, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "2 Timothy", "id": "2TI", "slug": "2-timothy", "chapters": 4, "order": 55, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Titus", "id": "TIT", "slug": "titus", "chapters": 3, "order": 56, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Philemon", "id": "PHM", "slug": "philemon", "chapters": 1, "order": 57, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Hebrews", "id": "HEB", "slug": "hebrews", "chapters": 13, "order": 58, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "James", "id": "JAS", "slug": "james", "chapters": 5, "order": 59, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "1 Peter", "id": "1PE", "slug": "1-peter", "chapters": 5, "order": 60, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "2 Peter", "id": "2PE", "slug": "2-peter", "chapters": 3, "order": 61, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "1 John", "id": "1JN", "slug": "1-john", "chapters": 5, "order": 62, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "2 John", "id": "2JN", "slug": "2-john", "chapters": 1, "order": 63, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "3 John", "id": "3JN", "slug": "3-john", "chapters": 1, "order": 64, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Jude", "id": "JUD", "slug": "jude", "chapters": 1, "order": 65, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True },
        { "name": "Revelation", "id": "REV", "slug": "revelation", "chapters": 22, "order": 66, "hasFullText": True, "hasKjv": True, "hasChapterQA": True, "hasBookQA": True }
      ]
    }
  ]
}

with open("src/data/bible_catalog.json", "w", encoding="utf-8") as f:
    json.dump(catalog_data, f, indent=2, ensure_ascii=False)

print("Updated src/data/bible_catalog.json with all 66 books, slugs, and order.")
