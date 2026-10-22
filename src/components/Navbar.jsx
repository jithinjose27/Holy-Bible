import React, { useState, useMemo } from 'react';
import { 
  Book, 
  ChevronDown, 
  Search, 
  Bookmark, 
  ChevronLeft, 
  ChevronRight, 
  ShieldCheck, 
  Download, 
  WifiOff, 
  Sun, 
  Moon, 
  Palette,
  Award,
  Trophy,
  Filter,
  X
} from 'lucide-react';
import bibleCatalog from '../data/bible_catalog.json';

export default function Navbar({
  currentBookId = "GEN",
  currentBook = "Genesis",
  currentChapter = 1,
  totalChapters = 50,
  onSelectBook,
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
  onOpenBookReview,
  isInstalled = false,
  isOnline = true,
  bookmarkCount = 0
}) {
  const [isBookMenuOpen, setIsBookMenuOpen] = useState(false);
  const [isChapterMenuOpen, setIsChapterMenuOpen] = useState(false);
  const [bookQuery, setBookQuery] = useState('');

  const themes = [
    { id: 'paper', label: 'Paper' },
    { id: 'sepia', label: 'Sepia' },
    { id: 'dark', label: 'Dark' },
    { id: 'midnight', label: 'OLED' }
  ];

  const fontSizes = [
    { id: 'small', label: 'A-' },
    { id: 'medium', label: 'A' },
    { id: 'large', label: 'A+' },
    { id: 'xlarge', label: 'A++' }
  ];

  // Mobile quick theme cycle
  const handleCycleTheme = () => {
    const cycle = ['paper', 'sepia', 'dark', 'midnight'];
    const nextIdx = (cycle.indexOf(theme) + 1) % cycle.length;
    onChangeTheme(cycle[nextIdx]);
  };

  // Filtered books for search inside book selector
  const filteredOt = useMemo(() => {
    const q = bookQuery.trim().toLowerCase();
    const books = bibleCatalog.testaments[0]?.books || [];
    if (!q) return books;
    return books.filter(b => b.name.toLowerCase().includes(q) || b.id.toLowerCase().includes(q));
  }, [bookQuery]);

  const filteredNt = useMemo(() => {
    const q = bookQuery.trim().toLowerCase();
    const books = bibleCatalog.testaments[1]?.books || [];
    if (!q) return books;
    return books.filter(b => b.name.toLowerCase().includes(q) || b.id.toLowerCase().includes(q));
  }, [bookQuery]);

  const handleBookClick = (book) => {
    if (onSelectBook) {
      onSelectBook(book.id);
    }
    onSelectChapter(1);
    setIsBookMenuOpen(false);
    setBookQuery('');
  };

  return (
    <header className="sticky top-0 z-40 w-full border-b border-stone-200/90 dark:border-stone-800/90 backdrop-blur-md bg-stone-50/95 dark:bg-stone-900/95 transition-colors shadow-xs">
      <div className="max-w-7xl mx-auto px-3 sm:px-6">
        
        {/* =========================================
            MOBILE LAYOUT (< sm / under 640px)
            Two dedicated rows: Top Bar + Nav Bar
            Guarantees 0 horizontal overflow at 320px-430px
           ========================================= */}
        <div className="sm:hidden">
          {/* Mobile Top Row: Brand & Actions */}
          <div className="h-14 flex items-center justify-between gap-1">
            {/* Brand */}
            <div className="flex items-center gap-1.5 min-[340px]:gap-2 min-w-0">
              <div className="w-7 h-7 min-[340px]:w-8 min-[340px]:h-8 rounded-lg bg-gradient-to-br from-amber-700 to-amber-900 flex items-center justify-center text-amber-100 shadow-xs shrink-0">
                <Book className="w-3.5 h-3.5 min-[340px]:w-4 min-[340px]:h-4" />
              </div>
              <div className="flex items-center gap-1.5 min-w-0">
                <span className="font-cinzel font-bold text-xs min-[340px]:text-sm sm:text-[15px] text-stone-900 dark:text-stone-100 tracking-wide whitespace-nowrap">
                  Holy Bible
                </span>
                <span className="hidden min-[400px]:inline-block text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 bg-amber-100 dark:bg-amber-950/70 text-amber-800 dark:text-amber-400 rounded shrink-0">
                  EasyEnglish
                </span>
                {!isOnline && (
                  <span className="inline-flex items-center gap-0.5 text-[9px] uppercase font-bold px-1.5 py-0.2 bg-amber-200 text-amber-900 dark:bg-amber-950 dark:text-amber-300 rounded shrink-0" title="Offline Mode">
                    <WifiOff className="w-2.5 h-2.5" /> Off
                  </span>
                )}
              </div>
            </div>

            {/* Mobile Actions */}
            <div className="flex items-center gap-1 shrink-0">
              {onOpenBookReview && (
                <button
                  onClick={onOpenBookReview}
                  className="p-1.5 rounded-lg bg-amber-100 dark:bg-amber-950/80 text-amber-900 dark:text-amber-300 hover:bg-amber-200 transition cursor-pointer"
                  title="50-Question Book Review"
                  aria-label="50-Question Book Review"
                >
                  <Award className="w-4 h-4 text-amber-700 dark:text-amber-400" />
                </button>
              )}

              {!isInstalled && (
                <button
                  onClick={onOpenInstall}
                  className="p-1.5 rounded-lg bg-amber-700 text-white hover:bg-amber-800 shadow-xs transition cursor-pointer"
                  title="Install App"
                  aria-label="Install App"
                >
                  <Download className="w-4 h-4" />
                </button>
              )}

              <button
                onClick={onOpenSearch}
                className="p-1.5 rounded-lg text-stone-700 dark:text-stone-300 hover:bg-stone-200/60 dark:hover:bg-stone-800 transition cursor-pointer"
                title="Search Scripture"
                aria-label="Search Scripture"
              >
                <Search className="w-4 h-4" />
              </button>

              <button
                onClick={onOpenBookmarks}
                className="relative p-1.5 rounded-lg text-stone-700 dark:text-stone-300 hover:bg-stone-200/60 dark:hover:bg-stone-800 transition cursor-pointer"
                title="Bookmarks"
                aria-label="Bookmarks"
              >
                <Bookmark className="w-4 h-4" />
                {bookmarkCount > 0 && (
                  <span className="absolute top-1 right-1 w-2 h-2 rounded-full bg-amber-600" />
                )}
              </button>

              <button
                onClick={handleCycleTheme}
                className="p-1.5 rounded-lg text-stone-700 dark:text-stone-300 hover:bg-stone-200/60 dark:hover:bg-stone-800 transition cursor-pointer"
                title={`Theme: ${theme.toUpperCase()} (tap to switch)`}
                aria-label="Switch Theme"
              >
                {theme === 'paper' && <Sun className="w-4 h-4 text-amber-700" />}
                {theme === 'sepia' && <Palette className="w-4 h-4 text-amber-800" />}
                {theme === 'dark' && <Moon className="w-4 h-4 text-stone-300" />}
                {theme === 'midnight' && <Moon className="w-4 h-4 text-blue-400" />}
              </button>

              <button
                onClick={onOpenCopyright}
                className="p-1.5 rounded-lg text-stone-500 dark:text-stone-400 hover:bg-stone-200/60 dark:hover:bg-stone-800 transition cursor-pointer"
                title="About & Permissions"
                aria-label="About"
              >
                <ShieldCheck className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Mobile Bottom Row: Chapter & Book Navigation Bar */}
          <div className="h-11 flex items-center justify-center gap-2 border-t border-stone-200/60 dark:border-stone-800/60 py-1">
            {/* Prev Chapter */}
            <button
              onClick={onPrevChapter}
              disabled={currentChapter <= 1}
              className="h-8 w-8 flex items-center justify-center rounded-lg text-stone-700 dark:text-stone-300 hover:bg-stone-200/70 dark:hover:bg-stone-800 disabled:opacity-30 disabled:pointer-events-none transition cursor-pointer"
              title="Previous Chapter"
              aria-label="Previous Chapter"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>

            {/* Book Selector */}
            <div className="relative">
              <button
                onClick={() => {
                  setIsBookMenuOpen(!isBookMenuOpen);
                  setIsChapterMenuOpen(false);
                }}
                className="h-8 flex items-center gap-1 px-3 text-xs font-semibold rounded-lg bg-stone-200/70 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 text-stone-800 dark:text-stone-200 transition cursor-pointer"
              >
                <span className="truncate max-w-[120px]">{currentBook}</span>
                <ChevronDown className="w-3.5 h-3.5 opacity-60 shrink-0" />
              </button>

              {isBookMenuOpen && (
                <div className="fixed inset-x-3 top-28 mt-2 max-h-[75vh] flex flex-col bg-white dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-xl shadow-2xl p-3 z-50 animate-fade-in">
                  {/* Search filter for books */}
                  <div className="pb-2 border-b border-stone-200 dark:border-stone-800 flex items-center gap-2">
                    <Search className="w-4 h-4 text-stone-400 shrink-0" />
                    <input
                      type="text"
                      value={bookQuery}
                      onChange={(e) => setBookQuery(e.target.value)}
                      placeholder="Find book (e.g. Psalms, John)..."
                      className="w-full text-xs bg-transparent text-stone-800 dark:text-stone-200 placeholder:text-stone-400 focus:outline-none"
                      autoFocus
                    />
                    {bookQuery && (
                      <button onClick={() => setBookQuery('')} className="text-stone-400">
                        <X className="w-3.5 h-3.5" />
                      </button>
                    )}
                  </div>

                  <div className="flex-1 overflow-y-auto divide-y divide-stone-200/60 dark:divide-stone-800/60 pt-2">
                    {filteredOt.length > 0 && (
                      <div className="pb-3">
                        <div className="text-[11px] font-bold uppercase tracking-wider text-amber-800 dark:text-amber-400 mb-1 px-1">
                          Old Testament ({filteredOt.length})
                        </div>
                        <div className="grid grid-cols-2 gap-1">
                          {filteredOt.map((b) => (
                            <button
                              key={b.id}
                              onClick={() => handleBookClick(b)}
                              className={`text-left px-2 py-1.5 rounded-lg text-xs flex items-center justify-between transition cursor-pointer ${
                                b.id === currentBookId || b.name === currentBook
                                  ? 'bg-amber-100 dark:bg-amber-950/70 text-amber-900 dark:text-amber-300 font-bold'
                                  : 'text-stone-800 dark:text-stone-200 hover:bg-stone-100 dark:hover:bg-stone-800'
                              }`}
                            >
                              <span className="truncate">{b.name}</span>
                              <span className="text-[10px] text-stone-400 ml-1 shrink-0">{b.chapters}ch</span>
                            </button>
                          ))}
                        </div>
                      </div>
                    )}

                    {filteredNt.length > 0 && (
                      <div className="pt-2">
                        <div className="text-[11px] font-bold uppercase tracking-wider text-amber-800 dark:text-amber-400 mb-1 px-1">
                          New Testament ({filteredNt.length})
                        </div>
                        <div className="grid grid-cols-2 gap-1">
                          {filteredNt.map((b) => (
                            <button
                              key={b.id}
                              onClick={() => handleBookClick(b)}
                              className={`text-left px-2 py-1.5 rounded-lg text-xs flex items-center justify-between transition cursor-pointer ${
                                b.id === currentBookId || b.name === currentBook
                                  ? 'bg-amber-100 dark:bg-amber-950/70 text-amber-900 dark:text-amber-300 font-bold'
                                  : 'text-stone-800 dark:text-stone-200 hover:bg-stone-100 dark:hover:bg-stone-800'
                              }`}
                            >
                              <span className="truncate">{b.name}</span>
                              <span className="text-[10px] text-stone-400 ml-1 shrink-0">{b.chapters}ch</span>
                            </button>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>

            {/* Chapter Selector */}
            <div className="relative">
              <button
                onClick={() => {
                  setIsChapterMenuOpen(!isChapterMenuOpen);
                  setIsBookMenuOpen(false);
                }}
                className="h-8 flex items-center gap-1 px-3 text-xs font-semibold rounded-lg bg-stone-200/70 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 text-stone-800 dark:text-stone-200 transition cursor-pointer"
              >
                <span>Ch. {currentChapter}</span>
                <ChevronDown className="w-3.5 h-3.5 opacity-60" />
              </button>

              {isChapterMenuOpen && (
                <div className="fixed inset-x-3 top-28 mt-2 max-h-80 overflow-y-auto bg-white dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-xl shadow-2xl p-3 z-50 animate-fade-in">
                  <div className="text-xs font-bold text-stone-600 dark:text-stone-300 mb-2 text-center">
                    {currentBook} — Select Chapter (1 to {totalChapters})
                  </div>
                  <div className="grid grid-cols-5 gap-1.5">
                    {Array.from({ length: totalChapters }, (_, i) => i + 1).map((ch) => (
                      <button
                        key={ch}
                        onClick={() => {
                          onSelectChapter(ch);
                          setIsChapterMenuOpen(false);
                        }}
                        className={`h-9 rounded-lg text-xs font-semibold flex items-center justify-center transition cursor-pointer ${
                          ch === currentChapter
                            ? 'bg-amber-700 text-white shadow-xs font-bold'
                            : 'bg-stone-100 dark:bg-stone-800 text-stone-800 dark:text-stone-200 hover:bg-amber-100 dark:hover:bg-amber-950/40'
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
              className="h-8 w-8 flex items-center justify-center rounded-lg text-stone-700 dark:text-stone-300 hover:bg-stone-200/70 dark:hover:bg-stone-800 disabled:opacity-30 disabled:pointer-events-none transition cursor-pointer"
              title="Next Chapter"
              aria-label="Next Chapter"
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* =========================================
            DESKTOP LAYOUT (sm: and up / 640px+)
            Single clean unified row (h-16)
           ========================================= */}
        <div className="hidden sm:flex sm:items-center sm:justify-between sm:h-16 gap-2">
          {/* Brand */}
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-amber-700 to-amber-900 flex items-center justify-center text-amber-100 shadow-sm shrink-0">
              <Book className="w-4 h-4" />
            </div>
            <div className="flex items-center gap-2">
              <span className="font-cinzel font-bold text-base md:text-lg text-stone-900 dark:text-stone-100 tracking-wide whitespace-nowrap">
                The Holy Bible
              </span>
              <span className="text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 bg-amber-100 dark:bg-amber-950/60 text-amber-800 dark:text-amber-400 rounded">
                EasyEnglish
              </span>
              {!isOnline && (
                <span className="inline-flex items-center gap-1 text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 bg-amber-200/80 dark:bg-amber-950 text-amber-900 dark:text-amber-300 rounded shadow-xs" title="Offline Mode">
                  <WifiOff className="w-3 h-3 text-amber-700 dark:text-amber-400" /> Offline
                </span>
              )}
            </div>
          </div>

          {/* Central Chapter Navigation */}
          <div className="flex items-center gap-1.5">
            <button
              onClick={onPrevChapter}
              disabled={currentChapter <= 1}
              className="p-1.5 rounded-lg text-stone-600 hover:text-stone-900 dark:text-stone-400 dark:hover:text-stone-100 hover:bg-stone-200/60 dark:hover:bg-stone-800 disabled:opacity-30 disabled:pointer-events-none transition cursor-pointer"
              title="Previous Chapter"
              aria-label="Previous Chapter"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>

            {/* Desktop Book Selector */}
            <div className="relative">
              <button
                onClick={() => {
                  setIsBookMenuOpen(!isBookMenuOpen);
                  setIsChapterMenuOpen(false);
                }}
                className="flex items-center gap-1.5 px-3 py-1.5 text-xs sm:text-sm font-semibold rounded-lg bg-stone-200/60 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 text-stone-800 dark:text-stone-200 transition cursor-pointer"
              >
                <span>{currentBook}</span>
                <ChevronDown className="w-3.5 h-3.5 opacity-60" />
              </button>

              {isBookMenuOpen && (
                <div className="absolute top-full left-0 mt-2 w-80 max-h-[80vh] flex flex-col bg-white dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-xl shadow-xl p-3 z-50 animate-fade-in">
                  {/* Search input for books */}
                  <div className="pb-2 border-b border-stone-200 dark:border-stone-800 flex items-center gap-2">
                    <Search className="w-4 h-4 text-stone-400 shrink-0" />
                    <input
                      type="text"
                      value={bookQuery}
                      onChange={(e) => setBookQuery(e.target.value)}
                      placeholder="Search books (e.g., Romans, Mark)..."
                      className="w-full text-xs bg-transparent text-stone-800 dark:text-stone-200 placeholder:text-stone-400 focus:outline-none"
                      autoFocus
                    />
                    {bookQuery && (
                      <button onClick={() => setBookQuery('')} className="text-stone-400">
                        <X className="w-3.5 h-3.5" />
                      </button>
                    )}
                  </div>

                  <div className="flex-1 overflow-y-auto divide-y divide-stone-200/60 dark:divide-stone-800/60 pt-2 space-y-2">
                    {filteredOt.length > 0 && (
                      <div>
                        <div className="text-[11px] font-bold uppercase tracking-wider text-amber-800 dark:text-amber-400 mb-1 px-1">
                          Old Testament ({filteredOt.length})
                        </div>
                        <div className="grid grid-cols-2 gap-1">
                          {filteredOt.map((b) => (
                            <button
                              key={b.id}
                              onClick={() => handleBookClick(b)}
                              className={`text-left px-2 py-1 rounded-lg text-xs flex items-center justify-between transition cursor-pointer ${
                                b.id === currentBookId || b.name === currentBook
                                  ? 'bg-amber-100 dark:bg-amber-950/60 text-amber-900 dark:text-amber-300 font-bold'
                                  : 'text-stone-800 dark:text-stone-200 hover:bg-stone-100 dark:hover:bg-stone-800'
                              }`}
                            >
                              <span className="truncate">{b.name}</span>
                              <span className="text-[10px] text-stone-400 ml-1 shrink-0">{b.chapters}ch</span>
                            </button>
                          ))}
                        </div>
                      </div>
                    )}

                    {filteredNt.length > 0 && (
                      <div className="pt-2">
                        <div className="text-[11px] font-bold uppercase tracking-wider text-amber-800 dark:text-amber-400 mb-1 px-1">
                          New Testament ({filteredNt.length})
                        </div>
                        <div className="grid grid-cols-2 gap-1">
                          {filteredNt.map((b) => (
                            <button
                              key={b.id}
                              onClick={() => handleBookClick(b)}
                              className={`text-left px-2 py-1 rounded-lg text-xs flex items-center justify-between transition cursor-pointer ${
                                b.id === currentBookId || b.name === currentBook
                                  ? 'bg-amber-100 dark:bg-amber-950/60 text-amber-900 dark:text-amber-300 font-bold'
                                  : 'text-stone-800 dark:text-stone-200 hover:bg-stone-100 dark:hover:bg-stone-800'
                              }`}
                            >
                              <span className="truncate">{b.name}</span>
                              <span className="text-[10px] text-stone-400 ml-1 shrink-0">{b.chapters}ch</span>
                            </button>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>

            {/* Desktop Chapter Selector */}
            <div className="relative">
              <button
                onClick={() => {
                  setIsChapterMenuOpen(!isChapterMenuOpen);
                  setIsBookMenuOpen(false);
                }}
                className="flex items-center gap-1 px-2.5 py-1.5 text-xs sm:text-sm font-semibold rounded-lg bg-stone-200/60 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 text-stone-800 dark:text-stone-200 transition cursor-pointer"
              >
                <span>Ch. {currentChapter}</span>
                <ChevronDown className="w-3.5 h-3.5 opacity-60" />
              </button>

              {isChapterMenuOpen && (
                <div className="absolute top-full left-1/2 -translate-x-1/2 mt-2 w-72 max-h-80 overflow-y-auto bg-white dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-xl shadow-xl p-3 z-50 animate-fade-in">
                  <div className="text-xs font-bold text-stone-600 dark:text-stone-300 mb-2 text-center">
                    {currentBook} — Select Chapter (1 to {totalChapters})
                  </div>
                  <div className="grid grid-cols-5 gap-1.5">
                    {Array.from({ length: totalChapters }, (_, i) => i + 1).map((ch) => (
                      <button
                        key={ch}
                        onClick={() => {
                          onSelectChapter(ch);
                          setIsChapterMenuOpen(false);
                        }}
                        className={`h-9 rounded-lg text-xs font-semibold flex items-center justify-center transition cursor-pointer ${
                          ch === currentChapter
                            ? 'bg-amber-700 text-white shadow-xs font-bold'
                            : 'bg-stone-100 dark:bg-stone-800 text-stone-800 dark:text-stone-200 hover:bg-amber-100 dark:hover:bg-amber-950/40'
                        }`}
                      >
                        {ch}
                      </button>
                    ))}
                  </div>
                </div>
              )}
            </div>

            <button
              onClick={onNextChapter}
              disabled={currentChapter >= totalChapters}
              className="p-1.5 rounded-lg text-stone-600 hover:text-stone-900 dark:text-stone-400 dark:hover:text-stone-100 hover:bg-stone-200/60 dark:hover:bg-stone-800 disabled:opacity-30 disabled:pointer-events-none transition cursor-pointer"
              title="Next Chapter"
              aria-label="Next Chapter"
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>

          {/* Desktop Actions */}
          <div className="flex items-center gap-1.5 sm:gap-2">
            {onOpenBookReview && (
              <button
                onClick={onOpenBookReview}
                className="inline-flex items-center gap-1.5 px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-amber-100 hover:bg-amber-200 dark:bg-amber-950/70 dark:hover:bg-amber-900/60 text-amber-900 dark:text-amber-300 border border-amber-300/60 dark:border-amber-800 transition cursor-pointer"
                title="50-Question Comprehensive Book Review"
              >
                <Award className="w-3.5 h-3.5 text-amber-700 dark:text-amber-400" />
                <span>50-Q Review</span>
              </button>
            )}

            {!isInstalled ? (
              <button
                onClick={onOpenInstall}
                className="inline-flex items-center gap-1.5 px-2.5 py-1.5 text-xs font-semibold rounded-lg bg-amber-700 hover:bg-amber-800 text-white shadow-xs transition cursor-pointer"
                title="Install Holy Bible App for Offline Reading"
              >
                <Download className="w-3.5 h-3.5" />
                <span>Install</span>
              </button>
            ) : (
              <button
                onClick={onOpenInstall}
                className="inline-flex items-center gap-1 px-2 py-1.5 text-[11px] font-semibold rounded-lg text-emerald-800 dark:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-950/40 transition cursor-pointer"
                title="App is installed and running offline-ready"
              >
                <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
                <span>Offline Ready</span>
              </button>
            )}

            <button
              onClick={onOpenSearch}
              className="p-2 text-stone-600 dark:text-stone-300 hover:bg-stone-200/60 dark:hover:bg-stone-800 rounded-lg transition cursor-pointer"
              title="Search Bible (Ctrl+K)"
              aria-label="Search"
            >
              <Search className="w-4 h-4" />
            </button>

            <button
              onClick={onOpenBookmarks}
              className="relative p-2 text-stone-600 dark:text-stone-300 hover:bg-stone-200/60 dark:hover:bg-stone-800 rounded-lg transition cursor-pointer"
              title="Bookmarks and Progress"
              aria-label="Bookmarks"
            >
              <Bookmark className="w-4 h-4" />
              {bookmarkCount > 0 && (
                <span className="absolute top-1 right-1 w-2 h-2 rounded-full bg-amber-600" />
              )}
            </button>

            {/* Desktop Theme Selector Toggle */}
            <div className="flex items-center bg-stone-200/60 dark:bg-stone-800/80 rounded-lg p-0.5">
              {themes.map((t) => (
                <button
                  key={t.id}
                  onClick={() => onChangeTheme(t.id)}
                  className={`px-2 py-1 text-xs rounded-md font-medium transition cursor-pointer ${
                    theme === t.id
                      ? 'bg-white dark:bg-stone-700 text-stone-900 dark:text-stone-100 shadow-xs'
                      : 'text-stone-600 hover:text-stone-900 dark:text-stone-400 dark:hover:text-stone-200'
                  }`}
                >
                  {t.label}
                </button>
              ))}
            </div>

            {/* Desktop Font Size Toggle */}
            <div className="flex items-center bg-stone-200/60 dark:bg-stone-800/80 rounded-lg p-0.5">
              {fontSizes.map((f) => (
                <button
                  key={f.id}
                  onClick={() => onChangeFontSize(f.id)}
                  className={`px-1.5 py-1 text-[11px] rounded-md font-bold transition cursor-pointer ${
                    fontSize === f.id
                      ? 'bg-white dark:bg-stone-700 text-stone-900 dark:text-stone-100 shadow-xs'
                      : 'text-stone-600 hover:text-stone-900 dark:text-stone-400 dark:hover:text-stone-200'
                  }`}
                >
                  {f.label}
                </button>
              ))}
            </div>

            <button
              onClick={onOpenCopyright}
              className="p-2 text-stone-500 hover:text-stone-800 dark:text-stone-400 dark:hover:text-stone-200 rounded-lg transition cursor-pointer"
              title="Copyright & Permissions"
              aria-label="About"
            >
              <ShieldCheck className="w-4 h-4" />
            </button>
          </div>
        </div>

      </div>
    </header>
  );
}
