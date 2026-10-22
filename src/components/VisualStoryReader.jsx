import React, { useState, useEffect } from 'react';
import { 
  ArrowLeft, 
  ChevronLeft, 
  ChevronRight, 
  BookOpen, 
  Sparkles, 
  Layers, 
  ScrollText, 
  Maximize2, 
  Minimize2, 
  Moon, 
  Sun,
  Users,
  Compass,
  CheckCircle,
  Eye
} from 'lucide-react';
import ComicPageLayout from './ComicPageLayout';

export default function VisualStoryReader({
  storyData,
  chapterNumber,
  onBackToBible,
  onSelectChapter,
  onOpenCharacterGuide,
  totalChapters = 50
}) {
  const [currentPageIndex, setCurrentPageIndex] = useState(0);
  const [readingFormat, setReadingFormat] = useState('comic'); // 'comic' (graphic novel pages) | 'webtoon' (vertical strip)
  const [immersiveTheme, setImmersiveTheme] = useState('dark'); // 'dark' | 'light' | 'midnight'
  const [isTheaterMode, setIsTheaterMode] = useState(false);

  // Scroll to top when chapter or page changes
  useEffect(() => {
    setCurrentPageIndex(0);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [chapterNumber]);

  // Keyboard navigation for graphic novel page mode
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (readingFormat === 'comic' && storyData?.pages) {
        if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {
          if (currentPageIndex < storyData.pages.length - 1) {
            e.preventDefault();
            setCurrentPageIndex((prev) => prev + 1);
            window.scrollTo({ top: 0, behavior: 'smooth' });
          }
        } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
          if (currentPageIndex > 0) {
            e.preventDefault();
            setCurrentPageIndex((prev) => prev - 1);
            window.scrollTo({ top: 0, behavior: 'smooth' });
          }
        }
      }
      if (e.key === 'Escape') {
        if (isTheaterMode) {
          setIsTheaterMode(false);
        } else {
          onBackToBible();
        }
      }
      if (e.key.toLowerCase() === 't') {
        setIsTheaterMode((prev) => !prev);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [readingFormat, currentPageIndex, storyData, onBackToBible, isTheaterMode]);

  if (!storyData) {
    return (
      <div className="min-h-screen flex items-center justify-center p-6 bg-stone-900 text-stone-200">
        <div className="text-center space-y-4">
          <p className="text-lg">Preparing visual story mode for Genesis {chapterNumber}...</p>
          <button
            onClick={onBackToBible}
            className="px-4 py-2 bg-amber-700 text-white rounded-xl hover:bg-amber-600 transition"
          >
            Return to Bible
          </button>
        </div>
      </div>
    );
  }

  const pages = storyData.pages || [];
  const currentPage = pages[currentPageIndex] || { panels: [] };
  const allPanels = pages.flatMap((p) => p.panels);

  const themeClasses = {
    dark: 'bg-stone-950 text-stone-100 manhwa-dark',
    light: 'bg-stone-100 text-stone-900',
    midnight: 'bg-black text-stone-100'
  }[immersiveTheme];

  return (
    <div className={`min-h-screen ${themeClasses} transition-colors duration-300 pb-24`}>
      {/* Persistent Story Navigation Bar (Hidden in Theater Mode) */}
      {!isTheaterMode && (
        <header className="sticky top-0 z-40 w-full border-b border-white/10 backdrop-blur-md bg-stone-950/85 px-4 py-3 transition-all">
          <div className="max-w-6xl mx-auto flex items-center justify-between gap-3">
            {/* Back to Bible Reader Action */}
            <button
              onClick={onBackToBible}
              className="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-amber-600/20 hover:bg-amber-600/30 text-amber-300 hover:text-amber-200 border border-amber-500/30 transition text-xs sm:text-sm font-semibold cursor-pointer shadow-xs"
              title="Return to the Bible reading view"
            >
              <ArrowLeft className="w-4 h-4" />
              <span>Back to Bible</span>
            </button>

            {/* Chapter Title & Page Indicator */}
            <div className="text-center">
              <h1 className="font-cinzel font-bold text-sm sm:text-base text-stone-100 tracking-wide line-clamp-1">
                {storyData.title}
              </h1>
              <div className="text-[11px] text-stone-400 flex items-center justify-center gap-2">
                <span>{storyData.totalPanels} Comic Panels</span>
                {readingFormat === 'comic' && (
                  <>
                    <span>•</span>
                    <span className="font-semibold text-amber-400">Page {currentPageIndex + 1} of {pages.length}</span>
                  </>
                )}
              </div>
            </div>

            {/* Reading Format, Theater & Theme Controls */}
            <div className="flex items-center gap-1.5 sm:gap-2">
              {/* Format Toggle: Comic Pages vs Webtoon Strip */}
              <div className="flex bg-stone-900 border border-stone-800 rounded-lg p-0.5">
                <button
                  onClick={() => setReadingFormat('comic')}
                  className={`p-1.5 rounded-md text-xs font-semibold flex items-center gap-1 transition ${
                    readingFormat === 'comic'
                      ? 'bg-purple-700 text-white shadow-xs'
                      : 'text-stone-400 hover:text-stone-200'
                  }`}
                  title="Comic Book Pages Mode"
                >
                  <Layers className="w-3.5 h-3.5" />
                  <span className="hidden sm:inline">Pages</span>
                </button>
                <button
                  onClick={() => setReadingFormat('webtoon')}
                  className={`p-1.5 rounded-md text-xs font-semibold flex items-center gap-1 transition ${
                    readingFormat === 'webtoon'
                      ? 'bg-purple-700 text-white shadow-xs'
                      : 'text-stone-400 hover:text-stone-200'
                  }`}
                  title="Continuous Vertical Webtoon Strip"
                >
                  <ScrollText className="w-3.5 h-3.5" />
                  <span className="hidden sm:inline">Webtoon</span>
                </button>
              </div>

              {/* Theater Mode Toggle */}
              <button
                onClick={() => setIsTheaterMode(true)}
                className="p-1.5 rounded-lg bg-stone-900 border border-stone-800 text-stone-300 hover:text-amber-400 transition"
                title="Enter Theater / Fullscreen Mode (T)"
              >
                <Maximize2 className="w-4 h-4" />
              </button>

              {/* Character Reference Sheet Quick Access */}
              <button
                onClick={onOpenCharacterGuide}
                className="p-1.5 rounded-lg bg-stone-900 border border-stone-800 text-stone-300 hover:text-purple-300 transition"
                title="Character Continuity & Visual Guide"
              >
                <Users className="w-4 h-4 text-purple-400" />
              </button>

              {/* Theme Toggle */}
              <button
                onClick={() => {
                  setImmersiveTheme(
                    immersiveTheme === 'dark' ? 'midnight' : immersiveTheme === 'midnight' ? 'light' : 'dark'
                  );
                }}
                className="p-1.5 rounded-lg bg-stone-900 border border-stone-800 text-stone-300 hover:text-amber-300 transition"
                title="Toggle Reading Theme"
              >
                {immersiveTheme === 'light' ? <Moon className="w-4 h-4" /> : <Sun className="w-4 h-4" />}
              </button>
            </div>
          </div>

          {/* Progress Indicator Line */}
          <div className="w-full h-1 bg-stone-800/80 mt-2">
            <div 
              className="h-full bg-gradient-to-r from-purple-500 via-amber-500 to-indigo-500 transition-all duration-300"
              style={{ 
                width: readingFormat === 'comic' 
                  ? `${((currentPageIndex + 1) / pages.length) * 100}%` 
                  : '100%' 
              }}
            />
          </div>
        </header>
      )}

      {/* Floating Exit Button for Theater Mode */}
      {isTheaterMode && (
        <button
          onClick={() => setIsTheaterMode(false)}
          className="fixed top-4 right-4 z-50 p-2.5 rounded-full bg-black/80 hover:bg-black text-white border border-white/20 shadow-2xl transition"
          title="Exit Theater Mode (Esc)"
        >
          <Minimize2 className="w-5 h-5" />
        </button>
      )}

      {/* Main Comic Reader Stage */}
      <main className="max-w-5xl mx-auto px-3 sm:px-6 pt-6 sm:pt-8">
        {/* Chapter Title & Visual Hook */}
        {!isTheaterMode && (
          <div className="mb-8 text-center space-y-2 p-6 rounded-2xl bg-gradient-to-b from-stone-900/80 via-stone-900/40 to-stone-950/90 border border-white/5 shadow-xl">
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-purple-950/90 border border-purple-500/40 text-purple-300 text-xs font-bold uppercase tracking-wider shadow-sm">
              <Sparkles className="w-3.5 h-3.5 text-amber-300" /> Graphic Novel Adaptation • Genesis {storyData.chapter}
            </div>
            <h2 className="text-2xl sm:text-4xl md:text-5xl font-cinzel font-black text-stone-100 tracking-tight">
              {storyData.title}
            </h2>
            {storyData.subtitle && (
              <p className="text-sm sm:text-base text-amber-300/90 font-serif italic max-w-xl mx-auto">
                "{storyData.subtitle}"
              </p>
            )}
            {storyData.synopsis && (
              <p className="text-xs sm:text-sm text-stone-400 max-w-2xl mx-auto leading-relaxed pt-1">
                {storyData.synopsis}
              </p>
            )}
          </div>
        )}

        {/* Content Layout: Comic Grid (Pages) vs Webtoon Strip */}
        {readingFormat === 'comic' ? (
          <div className="space-y-6">
            <ComicPageLayout 
              panels={currentPage.panels} 
              layoutMode="comic_grid" 
            />

            {/* Graphic Novel Page Turner Bar */}
            <div className="pt-6 border-t border-white/10 flex items-center justify-between">
              <button
                onClick={() => {
                  if (currentPageIndex > 0) {
                    setCurrentPageIndex((prev) => prev - 1);
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                  }
                }}
                disabled={currentPageIndex === 0}
                className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-stone-900 border border-stone-800 hover:bg-stone-800 disabled:opacity-30 disabled:pointer-events-none transition cursor-pointer shadow-md"
              >
                <ChevronLeft className="w-4 h-4" />
                <span>Previous Page</span>
              </button>

              {/* Page Pill Indicators */}
              <div className="flex items-center gap-1.5">
                {pages.map((_, idx) => (
                  <button
                    key={idx}
                    onClick={() => {
                      setCurrentPageIndex(idx);
                      window.scrollTo({ top: 0, behavior: 'smooth' });
                    }}
                    className={`w-7 h-7 rounded-lg text-xs font-bold transition ${
                      idx === currentPageIndex
                        ? 'bg-amber-500 text-stone-950 font-black shadow-md scale-105'
                        : 'bg-stone-900 border border-stone-800 text-stone-400 hover:text-white'
                    }`}
                  >
                    {idx + 1}
                  </button>
                ))}
              </div>

              <button
                onClick={() => {
                  if (currentPageIndex < pages.length - 1) {
                    setCurrentPageIndex((prev) => prev + 1);
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                  }
                }}
                disabled={currentPageIndex >= pages.length - 1}
                className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-stone-900 border border-stone-800 hover:bg-stone-800 disabled:opacity-30 disabled:pointer-events-none transition cursor-pointer shadow-md"
              >
                <span>Next Page</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        ) : (
          /* Webtoon Strip Mode */
          <ComicPageLayout 
            panels={allPanels} 
            layoutMode="webtoon_strip" 
          />
        )}

        {/* Chapter Completion & Navigation Footer */}
        <div className="mt-16 pt-8 border-t border-white/10 p-6 sm:p-8 rounded-2xl bg-stone-900/60 border border-white/5 text-center space-y-4">
          <div className="inline-flex items-center justify-center p-3 rounded-full bg-amber-500/20 text-amber-400 mb-1">
            <CheckCircle className="w-8 h-8" />
          </div>
          <h3 className="text-lg sm:text-xl font-cinzel font-bold text-stone-100">
            Genesis {chapterNumber} Graphic Novel Completed
          </h3>
          <p className="text-xs sm:text-sm text-stone-400 max-w-lg mx-auto">
            Proceed to the next chapter's comic adaptation or return to the Bible reader to explore verse study notes and original text.
          </p>

          <div className="flex flex-wrap items-center justify-center gap-3 pt-2">
            <button
              onClick={onBackToBible}
              className="px-5 py-2.5 rounded-xl bg-amber-700 hover:bg-amber-600 text-white font-semibold text-xs sm:text-sm shadow-md transition cursor-pointer"
            >
              Return to Genesis {chapterNumber} Bible Text
            </button>

            {chapterNumber < totalChapters && (
              <button
                onClick={() => onSelectChapter(chapterNumber + 1)}
                className="inline-flex items-center gap-1.5 px-5 py-2.5 rounded-xl bg-purple-700 hover:bg-purple-600 text-white font-semibold text-xs sm:text-sm shadow-md transition cursor-pointer"
              >
                <span>Read Genesis {chapterNumber + 1} Story</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}
