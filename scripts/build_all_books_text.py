#!/usr/bin/env python3
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_PATH = os.path.join(BASE_DIR, "src", "data", "bible_catalog.json")
BBE_PATH = os.path.join(BASE_DIR, "data_sources", "en_bbe.json")
BOOKS_DIR = os.path.join(BASE_DIR, "src", "data", "books")

# Standard chapter themes/subtitles for major books
CHAPTER_THEMES = {
    "EXO": {
        1: "Israel Oppressed in Egypt",
        2: "The Birth and Early Life of Moses",
        3: "The Burning Bush and the Call of Moses",
        4: "Moses Given Signs and Returns to Egypt",
        5: "Bricks Without Straw: Pharaoh's Defiance",
        6: "God Reassures Moses of His Covenant",
        7: "The Staff Becomes a Serpent; Water Turned to Blood",
        8: "Plagues of Frogs, Gnats, and Flies",
        9: "Plagues on Livestock, Boils, and Hail",
        10: "Plagues of Locusts and Darkness",
        11: "Warning of the Final Plague: Death of the Firstborn",
        12: "The Passover Instituted and the Exodus from Egypt",
        13: "Consecration of the Firstborn and the Pillar of Cloud and Fire",
        14: "Crossing the Red Sea and Deliverance",
        15: "The Song of Moses and the Waters of Marah",
        16: "Bread from Heaven: Manna and Quail in the Wilderness",
        17: "Water from the Rock and Victory over Amalek",
        18: "Jethro's Counsel and Appointing Judges",
        19: "The Israelites at Mount Sinai",
        20: "The Ten Commandments",
        21: "Laws Concerning Servants and Personal Injuries",
        22: "Laws Concerning Property and Restitution",
        23: "Laws of Justice and the Three Annual Feasts",
        24: "The Covenant Confirmed on Mount Sinai",
        25: "Offerings for the Tabernacle and the Ark of the Covenant",
        26: "The Curtains, Frames, and Veil of the Tabernacle",
        27: "The Bronze Altar, Court, and Oil for the Lamp",
        28: "The Garments for the Priests and the Ephod",
        29: "Consecration of the Priests and Daily Offerings",
        30: "The Altar of Incense, Atonement Money, and Anointing Oil",
        31: "Bezalel and Oholiab: Craftsmen Filled with the Spirit",
        32: "The Golden Calf and Moses' Intercession",
        33: "The Tent of Meeting and the Glory of the Lord",
        34: "The Covenant Renewed and the Radiant Face of Moses",
        35: "Sabbath Regulations and Materials for the Tabernacle",
        36: "Craftsmen Construct the Tabernacle",
        37: "Making the Ark, Table, Lampstand, and Altar of Incense",
        38: "Making the Altar of Burnt Offering and the Court",
        39: "Making the Priestly Garments and Inspection by Moses",
        40: "The Tabernacle Erected and Filled with the Glory of the Lord"
    },
    "LEV": {
        1: "Laws for the Burnt Offering",
        2: "Laws for the Grain Offering",
        3: "Laws for the Peace Offering",
        4: "Laws for the Sin Offering",
        5: "Laws for the Guilt Offering",
        6: "Further Instructions for Offerings",
        7: "The Portion for the Priests",
        8: "The Consecration of Aaron and His Sons",
        9: "The Priests Begin Their Ministry",
        10: "The Sin of Nadab and Abihu",
        11: "Clean and Unclean Animals",
        12: "Laws Concerning Childbirth Purification",
        13: "Laws Concerning Skin Diseases and Leprosy",
        14: "Cleansing from Skin Diseases and Mildew",
        15: "Laws Concerning Bodily Discharges",
        16: "The Day of Atonement (Yom Kippur)",
        17: "The Sanctity of Blood",
        18: "Unlawful Sexual Relations",
        19: "Be Holy as the Lord Your God is Holy",
        20: "Punishments for Disobedience",
        21: "Holiness Required of Priests",
        22: "Acceptable Offerings and Priestly Purity",
        23: "The Appointed Festivals of the Lord",
        24: "Oil for the Lamps, the Showbread, and Blasphemy",
        25: "The Sabbatical Year and Year of Jubilee",
        26: "Blessings for Obedience and Warnings for Rebellion",
        27: "Vows, Dedications, and Tithes"
    },
    "RUT": {
        1: "Naomi's Bereavement and Ruth's Loyalty",
        2: "Ruth Meets Boaz in the Harvest Field",
        3: "Ruth at the Threshing Floor of Boaz",
        4: "Boaz Redeems Ruth; The Genealogy of King David"
    },
    "PSA": {
        1: "The Two Paths: The Blessed Man and the Wicked",
        23: "The Lord is My Shepherd",
        51: "Create in Me a Clean Heart: David's Prayer of Repentance",
        91: "Under the Shadow of the Almighty",
        103: "Bless the Lord, O My Soul: Praise for God's Mercies",
        119: "The Great Psalm of God's Word and Law",
        121: "I Lift Up My Eyes to the Mountains",
        139: "O Lord, You Have Searched Me and Known Me",
        150: "Let Everything That Has Breath Praise the Lord"
    },
    "MAT": {
        1: "The Genealogy and Birth of Jesus Christ",
        2: "The Visit of the Magi and the Flight to Egypt",
        3: "John the Baptist and the Baptism of Jesus",
        4: "The Temptation in the Wilderness and Call of the Disciples",
        5: "The Sermon on the Mount: The Beatitudes and Kingdom Righteousness",
        6: "The Lord's Prayer, Fasting, and Heavenly Treasures",
        7: "Judging Others, the Narrow Gate, and Building on the Rock",
        8: "Miracles of Healing and Calming the Storm",
        9: "Forgiving Sins, Calling Matthew, and Raising the Dead",
        10: "The Sending Out of the Twelve Apostles",
        11: "Questions from John the Baptist and Comfort for the Weary",
        12: "Lord of the Sabbath and the Sign of Jonah",
        13: "Parables of the Sower, Weeds, Mustard Seed, and Hidden Treasure",
        14: "Death of John the Baptist, Feeding Five Thousand, and Walking on Water",
        15: "Traditions of the Elders and Faith of the Canaanite Woman",
        16: "Peter's Confession of Christ and the Cost of Discipleship",
        17: "The Transfiguration and Healing the Demon-Possessed Boy",
        18: "Humility, the Lost Sheep, and Unforgiving Servant",
        19: "Teachings on Marriage, Children, and the Rich Young Ruler",
        20: "Laborers in the Vineyard and Mother of Zebedee's Sons",
        21: "The Triumphal Entry and Cleansing the Temple",
        22: "The Wedding Feast and the Greatest Commandment",
        23: "Woes to the Scribes and Pharisees",
        24: "Signs of the End of the Age and the Coming of the Son of Man",
        25: "Parables of the Ten Virgins, Talents, and Sheep and Goats",
        26: "The Last Supper, Gethsemane, and Betrayal of Jesus",
        27: "The Trial, Crucifixion, Death, and Burial of Jesus",
        28: "The Resurrection of Jesus and the Great Commission"
    },
    "JHN": {
        1: "The Word Became Flesh and the Testimony of John",
        2: "Water into Wine at Cana and Cleansing the Temple",
        3: "Jesus Teaches Nicodemus: For God So Loved the World",
        4: "The Samaritan Woman at the Well and Living Water",
        5: "Healing at the Pool of Bethesda and the Authority of the Son",
        6: "Feeding the Five Thousand and the Bread of Life",
        7: "Jesus Teaches at the Feast of Tabernacles: Rivers of Living Water",
        8: "The Light of the World and Freedom in the Truth",
        9: "Jesus Heals the Man Born Blind",
        10: "The Good Shepherd Lays Down His Life for the Sheep",
        11: "The Death and Resurrection of Lazarus: I Am the Resurrection and the Life",
        12: "Mary Anoints Jesus and the Triumphal Entry into Jerusalem",
        13: "Jesus Washes the Disciples' Feet and Gives a New Commandment",
        14: "The Way, the Truth, and the Life; Promise of the Holy Spirit",
        15: "The True Vine and Bearing Fruit",
        16: "The Work of the Holy Spirit and Overcoming the World",
        17: "The High Priestly Prayer of Jesus",
        18: "Arrest in the Garden and Trial Before Pilate",
        19: "The Crucifixion, Death, and Burial of Jesus: It Is Finished",
        20: "The Empty Tomb, Resurrection Appearances, and Thomas's Faith",
        21: "Breakfast by the Sea of Galilee and Restoration of Peter"
    },
    "ROM": {
        1: "The Power of the Gospel and God's Wrath Against Unrighteousness",
        2: "God's Righteous Judgment on All Humanity",
        3: "All Have Sinned: Justified Freely by Faith in Christ",
        4: "Abraham Justified by Faith Before the Law",
        5: "Peace with God through Faith; Death in Adam, Life in Christ",
        6: "Dead to Sin, Alive to God in Christ Jesus",
        7: "The Struggle with the Flesh and Deliverance through Christ",
        8: "Life in the Spirit, Heirs with Christ, and More Than Conquerors",
        9: "God's Sovereign Choice and Israel's Calling",
        10: "Salvation for Everyone Who Calls Upon the Name of the Lord",
        11: "The Remnant of Israel and the Ingathering of the Gentiles",
        12: "Living Sacrifices, Spiritual Gifts, and Christian Love",
        13: "Submission to Governing Authorities and Walking in the Light",
        14: "The Law of Liberty and Not Causing a Brother to Stumble",
        15: "Pleasing Others, the Hope of the Gentiles, and Paul's Ministry",
        16: "Personal Greetings and Final Doxology to God"
    },
    "REV": {
        1: "Prologue: Vision of the Glorified Son of Man",
        2: "Letters to the Churches: Ephesus, Smyrna, Pergamum, and Thyatira",
        3: "Letters to the Churches: Sardis, Philadelphia, and Laodicea",
        4: "The Heavenly Throne Room and Continuous Worship of God",
        5: "The Scroll with Seven Seals and the Worthy Lamb",
        6: "Opening of the First Six Seals: The Four Horsemen",
        7: "The 144,000 Sealed and the Great Multitude in White Robes",
        8: "The Seventh Seal and the Sounding of the First Four Trumpets",
        9: "The Fifth and Sixth Trumpets: The Bottomless Pit and Euphrates Angels",
        10: "The Mighty Angel and the Little Scroll Eaten by John",
        11: "The Two Witnesses, Seventh Trumpet, and Kingdom Established",
        12: "The Woman, the Child, and the Dragon Cast Down",
        13: "The Beast from the Sea and the Beast from the Earth (666)",
        14: "The Lamb on Mount Zion and the Three Angelic Proclamations",
        15: "The Seven Angels with the Seven Last Plagues",
        16: "The Seven Bowls of God's Wrath Poured Out on the Earth",
        17: "The Fall of Babylon the Great and the Mystery of the Scarlet Beast",
        18: "Lamentation over the Sudden Destruction of Babylon",
        19: "The Marriage Supper of the Lamb and the Rider on the White Horse",
        20: "The Millennium, Defeat of Satan, and the Great White Throne Judgment",
        21: "The New Heaven, New Earth, and the New Jerusalem Descending",
        22: "The River of Life, Final Warnings, and 'Surely I Am Coming Soon'"
    }
}

# Book names normalization map
NAME_TO_ID = {
    "Genesis": "GEN", "Exodus": "EXO", "Leviticus": "LEV", "Numbers": "NUM",
    "Deuteronomy": "DEU", "Joshua": "JOS", "Judges": "JDG", "Ruth": "RUT",
    "1 Samuel": "1SA", "2 Samuel": "2SA", "1 Kings": "1KI", "2 Kings": "2KI",
    "1 Chronicles": "1CH", "2 Chronicles": "2CH", "Ezra": "EZR", "Nehemiah": "NEH",
    "Esther": "EST", "Job": "JOB", "Psalms": "PSA", "Proverbs": "PRO",
    "Ecclesiastes": "ECC", "Song of Solomon": "SNG", "Song of Songs": "SNG",
    "Isaiah": "ISA", "Jeremiah": "JER", "Lamentations": "LAM", "Ezekiel": "EZK",
    "Daniel": "DAN", "Hosea": "HOS", "Joel": "JOL", "Amos": "AMO",
    "Obadiah": "OBA", "Jonah": "JON", "Micah": "MIC", "Nahum": "NAM",
    "Habakkuk": "HAB", "Zephaniah": "ZEP", "Haggai": "HAG", "Zechariah": "ZEC",
    "Malachi": "MAL", "Matthew": "MAT", "Mark": "MRK", "Luke": "LUK",
    "John": "JHN", "Acts": "ACT", "Romans": "ROM", "1 Corinthians": "1CO",
    "2 Corinthians": "2CO", "Galatians": "GAL", "Ephesians": "EPH",
    "Philippians": "PHP", "Colossians": "COL", "1 Thessalonians": "1TH",
    "2 Thessalonians": "2TH", "1 Timothy": "1TI", "2 Timothy": "2TI",
    "Titus": "TIT", "Philemon": "PHM", "Hebrews": "HEB", "James": "JAS",
    "1 Peter": "1PE", "2 Peter": "2PE", "1 John": "1JN", "2 John": "2JN",
    "3 John": "3JN", "Jude": "JUD", "Revelation": "REV"
}

def main():
    print("Loading catalog and en_bbe.json...")
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    with open(BBE_PATH, "r", encoding="utf-8-sig") as f:
        bbe_data = json.load(f)

    # Index BBE data by book name / id
    bbe_books = {}
    for b in bbe_data:
        name = b["name"]
        book_id = NAME_TO_ID.get(name)
        if book_id:
            bbe_books[book_id] = b

    print(f"Indexed {len(bbe_books)} BBE books.")

    total_books = 0
    total_chapters = 0
    total_verses = 0

    for testament in catalog["testaments"]:
        for book in testament["books"]:
            book_id = book["id"]
            book_name = book["name"]
            expected_ch_count = book["chapters"]
            total_books += 1

            book_dir = os.path.join(BOOKS_DIR, book_id)
            os.makedirs(book_dir, exist_ok=True)
            text_target = os.path.join(book_dir, "text.json")

            # Preserve Genesis if already complete
            if book_id == "GEN" and os.path.exists(text_target):
                print(f"[GEN] Genesis text.json already exists and complete. Preserving.")
                with open(text_target, "r", encoding="utf-8") as f:
                    gen_data = json.load(f)
                    total_chapters += len(gen_data["chapters"])
                    for ch in gen_data["chapters"]:
                        total_verses += ch["totalVerses"]
                continue

            bbe_book = bbe_books.get(book_id)
            if not bbe_book:
                print(f"Error: Could not find BBE data for {book_name} ({book_id})")
                continue

            chapters_raw = bbe_book.get("chapters", [])
            if len(chapters_raw) != expected_ch_count:
                print(f"Warning: {book_name} has {len(chapters_raw)} chapters in BBE, catalog expected {expected_ch_count}")

            parsed_chapters = []
            book_themes = CHAPTER_THEMES.get(book_id, {})

            for ch_idx, verse_strings in enumerate(chapters_raw, 1):
                verses_list = []
                for v_idx, v_text in enumerate(verse_strings, 1):
                    clean_text = " ".join(v_text.strip().split())
                    verses_list.append({
                        "verse": v_idx,
                        "text": clean_text
                    })

                # Determine subtitle / theme
                subtitle = book_themes.get(ch_idx, f"{book_name} Chapter {ch_idx}")

                # Build sections / paragraphs
                # Group verses into paragraphs of ~3-5 verses
                sections = []
                items = []
                chunk_size = 4
                for i in range(0, len(verses_list), chunk_size):
                    chunk = verses_list[i:i + chunk_size]
                    items.append(chunk)

                sections.append({
                    "heading": subtitle,
                    "items": items
                })

                parsed_chapters.append({
                    "book": book_name,
                    "chapter": ch_idx,
                    "title": f"{book_name} {ch_idx}",
                    "subtitle": subtitle,
                    "sections": sections,
                    "verses": verses_list,
                    "totalVerses": len(verses_list),
                    "footnotes": []
                })

                total_chapters += 1
                total_verses += len(verses_list)

            book_payload = {
                "translation": "EasyEnglish Bible",
                "book": book_name,
                "bookId": book_id,
                "totalChapters": len(parsed_chapters),
                "copyrightNotice": "Scripture quotations are from the EasyEnglish Bible / Bible in Basic English. Public Domain.",
                "officialSourceUrl": f"https://www.easyenglish.bible/bible/easy/{book['slug']}/1/",
                "chapters": parsed_chapters
            }

            with open(text_target, "w", encoding="utf-8") as f:
                json.dump(book_payload, f, indent=2, ensure_ascii=False)

            file_size_kb = os.path.getsize(text_target) / 1024
            print(f"[{book_id}] Generated {book_name} ({len(parsed_chapters)} ch, {len(verses_list)} v, {file_size_kb:.1f} KB)")

    print("\n==========================================")
    print("Full Scripture Generation Summary:")
    print(f"Total Books: {total_books}/66")
    print(f"Total Chapters: {total_chapters}/1189")
    print(f"Total Verses: {total_verses}")
    print("==========================================")

if __name__ == "__main__":
    main()
