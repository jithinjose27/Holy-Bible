import React, { useState } from 'react';
import { 
  Book, 
  ChevronDown, 
  Search, 
  Bookmark, 
  Info, 
  Sun, 
  Moon, 
  Type, 
  ChevronLeft, 
  ChevronRight,
  ShieldCheck,
  Download,
  WifiOff
} from 'lucide-react';
import bibleCatalog from '../data/bible_catalog.json';

export default function Navbar({
  currentBook = "Genesis",
  currentChapter = 1,
  totalChapters = 50,
  onSelectChapter,
  onPrevChapter,
  onNextChapter,
  theme,
  onChangeTheme,
  fontSize,
  onChangeFontSize,
  onOpenSearch,
  onOpenBookmarks,
  onOpenCopyright,
  onOpenInstall,
  isInstalled = false,
  isOnline = true,
  bookmarkCount = 0
}) {
  const [isBookMenuOpen, setIsBookMenuOpen] = useState(false);
  const [isChapterMenuOpen, setIsChapterMenuOpen] = useState(false);

  const themes = [
    { id: 'paper', label: 'Paper', bg: 'bg-[#fbf9f5]' },
    { id: 'sepia', label: 'Sepia', bg: 'bg-[#f4ecd8]' },
    { id: 'dark', label: 'Dark', bg: 'bg-[#1c1917]' },
    { id: 'midnight', label: 'OLED', bg: 'bg-[#0b0f19]' }
  ];

  const fontSizes = [
    { id: 'small', label: 'A-', size: 'text-sm' },
    { id: 'medium', label: 'A', size: 'text-base' },
    { id: 'large', label: 'A+', size: 'text-lg' },
    { id: 'xlarge', label: 'A++', size: 'text-xl' }
  ];

  return (
    <header className="sticky top-0 z-40 w-full border-b border-stone-200/80 dark:border-stone-800/80 backdrop-blur-md bg-stone-50/90 dark:bg-stone-900/90 transition-colors">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between gap-2">
        {/* Brand & Mode Indicator */}
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-amber-700 to-amber-900 flex items-center justify-center text-amber-100 shadow-sm">
              <Book className="w-4 h-4" />
            </div>
            <div>
              <div className="flex items-center gap-1.5 sm:gap-2">
                <span className="font-cinzel font-bold text-sm sm:text-base md:text-lg text-stone-900 dark:text-stone-100 tracking-wide whitespace-nowrap">
                  <span className="hidden md:inline">The </span>Holy Bible
                </span>
                <span className="hidden lg:inline-block text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 bg-amber-100 dark:bg-amber-950/60 text-amber-800 dark:text-amber-400 rounded">
                  EasyEnglish
                </span>
                {!isOnline && (
                  <span className="inline-flex items-center gap-1 text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 bg-amber-200/80 dark:bg-amber-950 text-amber-900 dark:text-amber-300 rounded shadow-xs" title="You are offline. Full Genesis & Q&A are available offline.">
                    <WifiOff className="w-3 h-3 text-amber-700 dark:text-amber-400" /> Offline
                  </span>
                )}
              </div>
            </div>
          </div>
        </div>

        {/* Central Chapter Navigation & Pickers */}
        <div className="flex items-center gap-1 sm:gap-2">
          {/* Previous Chapter */}
          <button
            onClick={onPrevChapter}
            disabled={currentChapter <= 1}
            className="p-1.5 rounded-lg text-stone-500 hover:text-stone-800 dark:hover:text-stone-200 hover:bg-stone-200/60 dark:hover:bg-stone-800 disabled:opacity-30 disabled:pointer-events-none transition"
            title="Previous Chapter"
          >
            <ChevronLeft className="w-4 h-4" />
          </button>

          {/* Book Selector Dropdown */}
          <div className="relative">
            <button
              onClick={() => {
                setIsBookMenuOpen(!isBookMenuOpen);
                setIsChapterMenuOpen(false);
              }}
              className="flex items-center gap-1.5 px-2.5 py-1.5 text-xs sm:text-sm font-semibold rounded-lg bg-stone-200/50 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 text-stone-800 dark:text-stone-200 transition"
            >
              <span>{currentBook}</span>
              <ChevronDown className="w-3.5 h-3.5 opacity-60" />
            </button>

            {isBookMenuOpen && (
              <div className="absolute top-full left-0 mt-2 w-72 max-h-96 overflow-y-auto bg-white dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-xl shadow-xl p-3 z-50 animate-fade-in">
                <div className="text-[11px] font-bold uppercase tracking-wider text-stone-400 mb-2">
                  Old Testament
                </div>
                <div className="space-y-0.5">
                  {bibleCatalog.testaments[0].books.map((b) => (
                    <button
                      key={b.id}
                      onClick={() => {
                        if (b.name === "Genesis") {
                          onSelectChapter(1);
                        }
                        setIsBookMenuOpen(false);
                      }}
                      className={`w-full text-left px-2.5 py-1.5 rounded-lg text-xs flex items-center justify-between transition ${
                        b.name === currentBook
                          ? 'bg-amber-100 dark:bg-amber-950/60 text-amber-900 dark:text-amber-300 font-bold'
                          : b.hasFullText
                          ? 'text-stone-700 dark:text-stone-300 hover:bg-stone-100 dark:hover:bg-stone-800'
                          : 'text-stone-400 dark:text-stone-600 hover:bg-stone-50 dark:hover:bg-stone-800/40'
                      }`}
                    >
                      <span>{b.name}</span>
                    </button>
                  ))}
                </div>

                <div className="text-[11px] font-bold uppercase tracking-wider text-stone-400 mt-4 mb-2">
                  New Testament
                </div>
                <div className="space-y-0.5">
                  {bibleCatalog.testaments[1].books.map((b) => (
                    <button
                      key={b.id}
                      disabled={!b.hasFullText}
                      className="w-full text-left px-2.5 py-1.5 rounded-lg text-xs flex items-center justify-between text-stone-400 dark:text-stone-600 hover:bg-stone-50 dark:hover:bg-stone-800/40"
                    >
                      <span>{b.name}</span>
                      <span className="text-[10px] opacity-60">Soon</span>
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Chapter Selector Dropdown / Grid */}
          <div className="relative">
            <button
              onClick={() => {
                setIsChapterMenuOpen(!isChapterMenuOpen);
                setIsBookMenuOpen(false);
              }}
              className="flex items-center gap-1 px-2.5 py-1.5 text-xs sm:text-sm font-semibold rounded-lg bg-stone-200/50 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 text-stone-800 dark:text-stone-200 transition"
            >
              <span>Ch. {currentChapter}</span>
              <ChevronDown className="w-3.5 h-3.5 opacity-60" />
            </button>

            {isChapterMenuOpen && (
              <div className="absolute top-full left-1/2 -translate-x-1/2 mt-2 w-72 max-h-80 overflow-y-auto bg-white dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-xl shadow-xl p-3 z-50 animate-fade-in">
                <div className="text-xs font-bold text-stone-500 mb-2 text-center">
                  Select Chapter (1 to {totalChapters})
                </div>
                <div className="grid grid-cols-5 gap-1.5">
                  {Array.from({ length: totalChapters }, (_, i) => i + 1).map((ch) => (
                    <button
                      key={ch}
                      onClick={() => {
                        onSelectChapter(ch);
                        setIsChapterMenuOpen(false);
                      }}
                      className={`h-9 rounded-lg text-xs font-semibold flex items-center justify-center transition ${
                        ch === currentChapter
                          ? 'bg-amber-700 text-white shadow-xs font-bold'
                          : 'bg-stone-100 dark:bg-stone-800 text-stone-700 dark:text-stone-300 hover:bg-amber-100 dark:hover:bg-amber-950/40'
                      }`}
                    >
                      {ch}
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Next Chapter */}
          <button
            onClick={onNextChapter}
            disabled={currentChapter >= totalChapters}
            className="p-1.5 rounded-lg text-stone-500 hover:text-stone-800 dark:hover:text-stone-200 hover:bg-stone-200/60 dark:hover:bg-stone-800 disabled:opacity-30 disabled:pointer-events-none transition"
            title="Next Chapter"
          >
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>

        {/* Action Controls & Modal Triggers */}
        <div className="flex items-center gap-1 sm:gap-2">
          {/* PWA Install Button */}
          {!isInstalled ? (
            <button
              onClick={onOpenInstall}
              className="inline-flex items-center gap-1.5 px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-amber-700 hover:bg-amber-800 text-white shadow-xs transition cursor-pointer"
              title="Install Holy Bible App for Offline Reading"
            >
              <Download className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">Install</span>
            </button>
          ) : (
            <button
              onClick={onOpenInstall}
              className="hidden sm:inline-flex items-center gap-1 px-2 py-1.5 text-[11px] font-semibold rounded-lg text-emerald-800 dark:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-950/40 transition cursor-pointer"
              title="App is installed and running offline-ready"
            >
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
              <span>Offline Ready</span>
            </button>
          )}

          {/* Search Trigger */}
          <button
            onClick={onOpenSearch}
            className="p-2 text-stone-600 dark:text-stone-300 hover:bg-stone-200/60 dark:hover:bg-stone-800 rounded-lg transition"
            title="Search Bible (Ctrl+K)"
          >
            <Search className="w-4 h-4" />
          </button>

          {/* Bookmarks */}
          <button
            onClick={onOpenBookmarks}
            className="relative p-2 text-stone-600 dark:text-stone-300 hover:bg-stone-200/60 dark:hover:bg-stone-800 rounded-lg transition"
            title="Bookmarks and Progress"
          >
            <Bookmark className="w-4 h-4" />
            {bookmarkCount > 0 && (
              <span className="absolute top-1 right-1 w-2 h-2 rounded-full bg-amber-600" />
            )}
          </button>

          {/* Theme Selector Toggle */}
          <div className="hidden md:flex items-center bg-stone-200/50 dark:bg-stone-800/80 rounded-lg p-0.5">
            {themes.map((t) => (
              <button
                key={t.id}
                onClick={() => onChangeTheme(t.id)}
                className={`px-2 py-1 text-xs rounded-md font-medium transition ${
                  theme === t.id
                    ? 'bg-white dark:bg-stone-700 text-stone-900 dark:text-stone-100 shadow-xs'
                    : 'text-stone-500 hover:text-stone-800 dark:hover:text-stone-200'
                }`}
              >
                {t.label}
              </button>
            ))}
          </div>

          {/* Font Size Toggle */}
          <div className="hidden lg:flex items-center bg-stone-200/50 dark:bg-stone-800/80 rounded-lg p-0.5">
            {fontSizes.map((f) => (
              <button
                key={f.id}
                onClick={() => onChangeFontSize(f.id)}
                className={`px-1.5 py-1 text-[11px] rounded-md font-bold transition ${
                  fontSize === f.id
                    ? 'bg-white dark:bg-stone-700 text-stone-900 dark:text-stone-100 shadow-xs'
                    : 'text-stone-500 hover:text-stone-800 dark:hover:text-stone-200'
                }`}
              >
                {f.label}
              </button>
            ))}
          </div>

          {/* Copyright / About Modal Trigger */}
          <button
            onClick={onOpenCopyright}
            className="p-2 text-stone-400 hover:text-stone-700 dark:hover:text-stone-200 rounded-lg transition"
            title="Copyright & Permissions"
          >
            <ShieldCheck className="w-4 h-4" />
          </button>
        </div>
      </div>
    </header>
  );
}
