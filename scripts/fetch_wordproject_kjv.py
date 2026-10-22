import urllib.request
import re
import json
import time
import os
from bs4 import BeautifulSoup

OUTPUT_FILE = "src/data/genesis_kjv_text.json"
CACHE_DIR = "src/data/kjv_html"
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs("src/data", exist_ok=True)

def fetch_kjv_chapter(ch):
    cache_file = os.path.join(CACHE_DIR, f"kjv_gen_{ch}.html")
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return f.read()

    url = f"https://www.wordproject.org/bibles/kj/01/{ch}.htm"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read().decode('utf-8', errors='ignore')
                with open(cache_file, "w", encoding="utf-8") as f:
                    f.write(content)
                return content
        except Exception as e:
            print(f"Error fetching ch {ch} (attempt {attempt+1}): {e}")
            time.sleep(1)
    raise RuntimeError(f"Failed to fetch KJV chapter {ch}")

def parse_kjv_chapter(ch, html):
    soup = BeautifulSoup(html, 'html.parser')
    text_div = soup.find('div', id='textBody') or soup.find('div', class_='textBody')
    if not text_div:
        raise ValueError(f"Could not find textBody in KJV ch {ch}")

    # Remove script and style tags
    for s in text_div(['script', 'style', 'hr']):
        s.decompose()

    verses = {}
    lines = [l.strip() for l in text_div.get_text().split('\n') if l.strip()]

    current_verse = 0
    for line in lines:
        if line.startswith("Chapter ") or line.startswith("<!--") or "Wordproject" in line:
            continue
        
        # Check if line starts with a number like "2 And the earth..."
        m = re.match(r'^(\d+)\s+(.*)', line)
        if m:
            current_verse = int(m.group(1))
            verses[current_verse] = m.group(2).strip()
        else:
            # First line without number is verse 1!
            if current_verse == 0 and len(verses) == 0:
                current_verse = 1
                verses[1] = line.strip()
            elif current_verse > 0:
                # continuation of current verse
                verses[current_verse] += " " + line.strip()

    return verses

def main():
    print("Fetching and parsing Genesis 1-50 KJV text from WordProject...")
    all_kjv = {
        "translation": "King James Version (KJV)",
        "source": "WordProject",
        "sourceUrl": "https://www.wordproject.org/bibles/kj/01/",
        "book": "Genesis",
        "totalChapters": 50,
        "chapters": {}
    }

    for ch in range(1, 51):
        html = fetch_kjv_chapter(ch)
        v_dict = parse_kjv_chapter(ch, html)
        all_kjv["chapters"][str(ch)] = v_dict
        print(f"KJV Genesis {ch}: {len(v_dict)} verses parsed.")
        time.sleep(0.05)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_kjv, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully saved all 50 chapters of KJV text to {OUTPUT_FILE}!")

if __name__ == "__main__":
    main()
