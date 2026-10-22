# Interactive Bible Reader with Comic / Manhwa Storytelling Mode

A modern, responsive Bible reading application using the **EasyEnglish Bible** as the source translation, featuring an optional illustrated storytelling mode that presents Bible chapters as full-colour comic or manhwa-style reading experiences.

---

## 📖 Key Experiences

### 1. Bible Reading Mode (Default Experience)
- **Peaceful, distraction-free reading**: Clean typography, generous line-height, and paper-like neutral backgrounds.
- **Complete Genesis 1–50**: Full text of all 50 chapters parsed directly from the authorized EasyEnglish Bible text.
- **Section Headings & Study Notes**: Distinct pericopes and linguistic footnotes preserved from the source.
- **Interactive Verses**: Click any verse number to copy the citation or bookmark it.
- **Search System**: Fast, client-side search across all 50 chapters with query highlighting and direct jump-to-verse.
- **Personalization**:
  - Themes: Paper White, Warm Sepia, Dark Charcoal, Midnight OLED.
  - Font scaling: Small, Medium, Large, Extra Large.
  - Bookmarks & Reading Progress tracker (persisted in `localStorage`).
- **Unobtrusive Story Action**: A compact `🎨 Read as Story` button in the chapter header toolbar opens Visual Story Mode without cluttering the scripture text.

---

### 2. Visual Story Mode (Comic / Manhwa Experience)
- **Dedicated Graphic Novel Interface**: Opens exclusively upon reader request.
- **Dual Reading Formats**:
  1. **Vertical Webtoon / Manhwa Scroll**: Continuous vertical reading optimized for mobile and immersive desktop scrolling.
  2. **Page-by-Page Comic**: Traditional sequential pages with page flip controls and keyboard navigation (`←` and `→`).
- **Chapter-Specific Narratives for Genesis 1–50**:
  - Sequential illustrated panels with chapter-specific artwork.
  - Prominent Bible verse range citations (e.g., `Genesis 1:1–2`).
  - Distinct **Narration Boxes** (`📜 Narration`), clearly separated from Scripture.
  - Dynamic **Dialogue Speech Bubbles** (`💬`), with creative adaptations explicitly marked.
- **Character Continuity & Art Direction**:
  - Includes a dedicated **Character & Visual Guide** modal detailing appearance, palette signatures, and historical context for Abraham, Sarah, Isaac, Rebekah, Jacob, Esau, Joseph, Judah, and key landscapes.
- **Seamless Return**: "Back to Bible" button returns the reader directly to the chapter without losing context.

---

## 🎨 Artwork Production Pipeline & Genesis 1 Masterpiece

- **AI-Generated Masterpieces**:
  - `Genesis 1:1–2`: The primeval cosmos and Spirit hovering over the deep waters.
  - `Genesis 1:3–5`: Dawn of divine light piercing primeval darkness.
  - `Genesis 2:1–3`: The Garden of Eden, the Tree of Life, and the sacred Sabbath rest.
- **Automated Illustration Pipeline**:
  - `scripts/build_story_dataset_and_artwork.py`: Renders stylized 16:9 cinematic manhwa graphic panels across all chapters with theme palettes, vignettes, and comic panel framing.
  - Any panel can be replaced or regenerated independently by placing new images in `public/assets/genesis/{chapter}/panel-{scene}.jpg`.

---

## ⚖️ Copyright & Text Accuracy

- **Translation**: EasyEnglish Bible (EASY) by MissionAssist (UK Registered Charity 1162807).
- **Mandatory Attribution**:
  > *Scripture quotations are from the EasyEnglish Bible Copyright © MissionAssist 2018, 2024 – UK Charitable Incorporated Organisation 1162807. Used by permission. All rights reserved.*
- **Official Source**: Each chapter includes direct hyperlinks to the authorized text on [EasyEnglish.bible](https://www.easyenglish.bible/bible/easy/).

---

## 🛠️ Project Structure

```
├── public/
│   └── assets/
│       └── genesis/
│           ├── 1/  (8 sequential manhwa panel illustrations)
│           ├── 2/  (3 sequential manhwa panel illustrations)
│           └── ... (panels for chapters 1 through 50)
├── scripts/
│   ├── fetch_all_genesis.py             # Fetches and parses Genesis 1-50 from EasyEnglish
│   ├── manhwa_artist.py                 # Panel artwork generation utility
│   └── build_story_dataset_and_artwork.py # Generates story database & graphic panels
├── src/
│   ├── components/
│   │   ├── Navbar.jsx                   # Book, chapter, theme, and tool navigation
│   │   ├── BibleReader.jsx              # Traditional Scripture reading interface
│   │   ├── VisualStoryReader.jsx        # Manhwa / comic reading experience
│   │   ├── SearchModal.jsx              # Full-text search across Genesis
│   │   ├── BookmarksDrawer.jsx          # Bookmarks and reading progress drawer
│   │   ├── CharacterGuideModal.jsx      # Visual art direction & character sheet
│   │   └── AboutCopyrightModal.jsx      # Copyright & translation details
│   ├── data/
│   │   ├── genesis_bible_text.json      # Structured EasyEnglish Bible text (Ch. 1-50)
│   │   ├── genesis_story_data.json      # Structured Manhwa story data (Ch. 1-50)
│   │   ├── character_reference_sheet.json # Visual guide & character continuity
│   │   └── bible_catalog.json           # All 66 books of the Bible catalog
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
├── package.json
└── vite.config.js
```

---

## 🚀 Running the Project

```bash
# Start development server
yarn dev

# Build for production
yarn build

# Preview production build
yarn preview
```

---

## 🌟 Extending to Future Books

To add subsequent books (e.g., Exodus):
1. Add the book entry to `src/data/bible_catalog.json` with `hasFullText: true`.
2. Adapt `scripts/fetch_all_genesis.py` to target the new book slug.
3. Define story scenes in `scripts/build_story_dataset_and_artwork.py` and run it to generate panel assets.
4. The frontend components automatically adapt to any book data schema.
