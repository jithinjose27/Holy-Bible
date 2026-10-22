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
  Eye,
  ArrowUp
} from 'lucide-react';
import ComicPageLayout from './ComicPageLayout';

/**
 * VisualStoryReader Component
 * 
 * Delivers a complete, continuous single-page graphic novel / manhwa reading experience:
 * - The entire chapter's sequential panels appear on one continuous, vertically scrollable page.
 * - Numbered comic-page pagination within chapters is eliminated.
 * - Dynamic scroll-based reading progress indicator tracks progress through the chapter.
 * - Seamless navigation between Bible chapters at header and footer.
 */
export default function VisualStoryReader({
  storyData,
  chapterNumber,
  onBackToBible,
  onSelectChapter,
  onOpenCharacterGuide,
  totalChapters = 50
}) {
  const [readingFormat, setReadingFormat] = useState('comic'); // 'comic' (cinematic tiers) | 'webtoon' (vertical strip)
  const [immersiveTheme, setImmersiveTheme] = useState('dark'); // 'dark' | 'light' | 'midnight'
  const [isTheaterMode, setIsTheaterMode] = useState(false);
  const [scrollProgress, setScrollProgress] = useState(0);

  // Scroll to top when changing chapters
  useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
    setScrollProgress(0);
  }, [chapterNumber]);

  // Track window scroll progress for the continuous single-page chapter
  useEffect(() => {
    const handleScroll = () => {
      const totalScroll = document.documentElement.scrollHeight - window.innerHeight;
      if (totalScroll > 0) {
        const currentProgress = (window.scrollY / totalScroll) * 100;
        setScrollProgress(Math.min(100, Math.max(0, currentProgress)));
      }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Keyboard navigation & shortcuts
  useEffect(() => {
    const handleKeyDown = (e) => {
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
      if (e.key === 'j' || e.key === 'ArrowDown') {
        window.scrollBy({ top: 350, behavior: 'smooth' });
      }
      if (e.key === 'k' || e.key === 'ArrowUp') {
        window.scrollBy({ top: -350, behavior: 'smooth' });
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [onBackToBible, isTheaterMode]);

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

  // Extract all panels for this complete chapter into one sequential array
  const panels = storyData.panels || storyData.pages?.flatMap((p) => p.panels) || [];

  const themeClasses = {
    dark: 'bg-stone-950 text-stone-100 manhwa-dark',
    light: 'bg-stone-100 text-stone-900',
    midnight: 'bg-black text-stone-100'
  }[immersiveTheme];

  return (
    <div className={`min-h-screen ${themeClasses} transition-colors duration-300 pb-24`}>
      {/* Persistent Story Navigation Bar (Hidden in Theater Mode) */}
      {!isTheaterMode && (
        <header className="sticky top-0 z-40 w-full border-b border-white/10 backdrop-blur-md bg-stone-950/90 px-4 py-3 transition-all">
          <div className="max-w-6xl mx-auto flex items-center justify-between gap-3">
            {/* Back to Bible Reader Action */}
            <div className="flex items-center gap-2">
              <button
                onClick={onBackToBible}
                className="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-amber-600/20 hover:bg-amber-600/30 text-amber-300 hover:text-amber-200 border border-amber-500/30 transition text-xs sm:text-sm font-semibold cursor-pointer shadow-xs"
                title="Return to the Bible reading view"
              >
                <ArrowLeft className="w-4 h-4" />
                <span>Back to Bible</span>
              </button>

              {/* Prev Chapter Quick Jump */}
              {chapterNumber > 1 && (
                <button
                  onClick={() => onSelectChapter(chapterNumber - 1)}
                  className="p-1.5 rounded-lg bg-stone-900 border border-stone-800 text-stone-400 hover:text-white transition"
                  title={`Previous Chapter (Genesis ${chapterNumber - 1})`}
                >
                  <ChevronLeft className="w-4 h-4" />
                </button>
              )}
            </div>

            {/* Chapter Title & Complete Single-Page Indicator */}
            <div className="text-center">
              <h1 className="font-cinzel font-bold text-sm sm:text-base text-stone-100 tracking-wide line-clamp-1">
                {storyData.title}
              </h1>
              <div className="text-[11px] text-stone-400 flex items-center justify-center gap-2">
                <span className="font-semibold text-amber-400">{panels.length} Sequential Scenes</span>
                <span>•</span>
                <span className="text-stone-300">Complete Chapter (Single Page)</span>
              </div>
            </div>

            {/* Reading Format, Chapter Jump, Theater & Theme Controls */}
            <div className="flex items-center gap-1.5 sm:gap-2">
              {/* Next Chapter Quick Jump */}
              {chapterNumber < totalChapters && (
                <button
                  onClick={() => onSelectChapter(chapterNumber + 1)}
                  className="p-1.5 rounded-lg bg-stone-900 border border-stone-800 text-stone-400 hover:text-white transition"
                  title={`Next Chapter (Genesis ${chapterNumber + 1})`}
                >
                  <ChevronRight className="w-4 h-4" />
                </button>
              )}

              {/* Format Toggle: Cinematic Graphic Novel Tiers vs Vertical Webtoon Strip */}
              <div className="flex bg-stone-900 border border-stone-800 rounded-lg p-0.5">
                <button
                  onClick={() => setReadingFormat('comic')}
                  className={`p-1.5 rounded-md text-xs font-semibold flex items-center gap-1 transition cursor-pointer ${
                    readingFormat === 'comic'
                      ? 'bg-purple-700 text-white shadow-xs'
                      : 'text-stone-400 hover:text-stone-200'
                  }`}
                  title="Cinematic Graphic Novel Tiers"
                >
                  <Layers className="w-3.5 h-3.5" />
                  <span className="hidden sm:inline">Comic Tiers</span>
                </button>
                <button
                  onClick={() => setReadingFormat('webtoon')}
                  className={`p-1.5 rounded-md text-xs font-semibold flex items-center gap-1 transition cursor-pointer ${
                    readingFormat === 'webtoon'
                      ? 'bg-purple-700 text-white shadow-xs'
                      : 'text-stone-400 hover:text-stone-200'
                  }`}
                  title="Continuous Vertical Webtoon Strip"
                >
                  <ScrollText className="w-3.5 h-3.5" />
                  <span className="hidden sm:inline">Vertical Strip</span>
                </button>
              </div>

              {/* Theater Mode Toggle */}
              <button
                onClick={() => setIsTheaterMode(true)}
                className="p-1.5 rounded-lg bg-stone-900 border border-stone-800 text-stone-300 hover:text-amber-400 transition cursor-pointer"
                title="Enter Theater / Fullscreen Mode (T)"
              >
                <Maximize2 className="w-4 h-4" />
              </button>

              {/* Character Reference Sheet Quick Access */}
              <button
                onClick={onOpenCharacterGuide}
                className="p-1.5 rounded-lg bg-stone-900 border border-stone-800 text-stone-300 hover:text-purple-300 transition cursor-pointer"
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
                className="p-1.5 rounded-lg bg-stone-900 border border-stone-800 text-stone-300 hover:text-amber-300 transition cursor-pointer"
                title="Toggle Reading Theme"
              >
                {immersiveTheme === 'light' ? <Moon className="w-4 h-4" /> : <Sun className="w-4 h-4" />}
              </button>
            </div>
          </div>

          {/* Continuous Chapter Reading Progress Bar */}
          <div className="w-full h-1 bg-stone-800/80 mt-2">
            <div 
              className="h-full bg-gradient-to-r from-purple-500 via-amber-500 to-emerald-500 transition-all duration-150"
              style={{ width: `${scrollProgress}%` }}
              title={`Chapter Reading Progress: ${Math.round(scrollProgress)}%`}
            />
          </div>
        </header>
      )}

      {/* Floating Exit Button for Theater Mode */}
      {isTheaterMode && (
        <button
          onClick={() => setIsTheaterMode(false)}
          className="fixed top-4 right-4 z-50 p-2.5 rounded-full bg-black/80 hover:bg-black text-white border border-white/20 shadow-2xl transition cursor-pointer"
          title="Exit Theater Mode (Esc)"
        >
          <Minimize2 className="w-5 h-5" />
        </button>
      )}

      {/* Main Single-Page Comic Stage */}
      <main className="max-w-5xl mx-auto px-3 sm:px-6 pt-6 sm:pt-8">
        {/* Chapter Title & Visual Hook Header */}
        {!isTheaterMode && (
          <div className="mb-10 text-center space-y-2 p-6 sm:p-8 rounded-3xl bg-gradient-to-b from-stone-900/90 via-stone-900/50 to-stone-950/90 border border-white/5 shadow-2xl">
            <div className="inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full bg-purple-950/90 border border-purple-500/40 text-purple-300 text-xs font-bold uppercase tracking-wider shadow-sm">
              <Sparkles className="w-3.5 h-3.5 text-amber-300" /> Complete Chapter Adaptation • Genesis {storyData.chapter}
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
            <div className="pt-2 text-xs text-stone-500 flex items-center justify-center gap-3">
              <span>{panels.length} Illustrations in Sequence</span>
              <span>•</span>
              <span>Scroll down to experience the complete chapter</span>
            </div>
          </div>
        )}

        {/* The Entire Chapter's Panels on One Continuous Page */}
        <section aria-label={`Genesis ${chapterNumber} Illustrated Scenes`}>
          <ComicPageLayout 
            panels={panels} 
            layoutMode={readingFormat === 'comic' ? 'comic_grid' : 'webtoon_strip'} 
          />
        </section>

        {/* Chapter Completion & Navigation Footer */}
        <div className="mt-16 pt-8 border-t border-white/10 p-6 sm:p-10 rounded-3xl bg-stone-900/70 border border-white/5 text-center space-y-5">
          <div className="inline-flex items-center justify-center p-3 rounded-full bg-emerald-500/20 text-emerald-400 mb-1">
            <CheckCircle className="w-8 h-8" />
          </div>
          <h3 className="text-xl sm:text-2xl font-cinzel font-bold text-stone-100">
            Genesis Chapter {chapterNumber} Completed
          </h3>
          <p className="text-xs sm:text-sm text-stone-400 max-w-lg mx-auto">
            You have read all {panels.length} illustrated scenes of Genesis {chapterNumber}. You can proceed to the next chapter's story or study the verse text and KJV in the Bible reader.
          </p>

          <div className="flex flex-wrap items-center justify-center gap-3 pt-2">
            {chapterNumber > 1 && (
              <button
                onClick={() => onSelectChapter(chapterNumber - 1)}
                className="inline-flex items-center gap-1.5 px-4 py-2.5 rounded-xl bg-stone-800 hover:bg-stone-700 text-stone-200 font-semibold text-xs sm:text-sm border border-stone-700 shadow-md transition cursor-pointer"
              >
                <ChevronLeft className="w-4 h-4" />
                <span>Genesis {chapterNumber - 1} Story</span>
              </button>
            )}

            <button
              onClick={onBackToBible}
              className="px-5 py-2.5 rounded-xl bg-amber-700 hover:bg-amber-600 text-white font-semibold text-xs sm:text-sm shadow-md transition cursor-pointer"
            >
              Return to Genesis {chapterNumber} Bible Reader
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

          <div className="pt-4">
            <button
              onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
              className="inline-flex items-center gap-1 text-xs text-stone-500 hover:text-stone-300 transition cursor-pointer"
            >
              <ArrowUp className="w-3.5 h-3.5" />
              <span>Back to Top of Genesis {chapterNumber}</span>
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}
