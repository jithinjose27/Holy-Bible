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
  MessageSquare,
  ShieldCheck,
  CheckCircle
} from 'lucide-react';

export default function VisualStoryReader({
  storyData,
  chapterNumber,
  onBackToBible,
  onSelectChapter,
  onOpenCharacterGuide,
  totalChapters = 50
}) {
  const [currentPageIndex, setCurrentPageIndex] = useState(0);
  const [readingFormat, setReadingFormat] = useState('scroll'); // 'scroll' (manhwa) | 'page' (comic)
  const [immersiveTheme, setImmersiveTheme] = useState('dark'); // 'dark' | 'light' | 'midnight'

  // Scroll to top when chapter changes
  useEffect(() => {
    setCurrentPageIndex(0);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [chapterNumber]);

  // Keyboard navigation for page-by-page mode
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (readingFormat === 'page' && storyData?.pages) {
        if (e.key === 'ArrowRight' || e.key === 'PageDown') {
          if (currentPageIndex < storyData.pages.length - 1) {
            setCurrentPageIndex((prev) => prev + 1);
            window.scrollTo({ top: 0, behavior: 'smooth' });
          }
        } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
          if (currentPageIndex > 0) {
            setCurrentPageIndex((prev) => prev - 1);
            window.scrollTo({ top: 0, behavior: 'smooth' });
          }
        }
      }
      if (e.key === 'Escape') {
        onBackToBible();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [readingFormat, currentPageIndex, storyData, onBackToBible]);

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
      {/* Persistent Story Navigation Bar */}
      <header className="sticky top-0 z-40 w-full border-b border-white/10 backdrop-blur-md bg-stone-950/80 px-4 py-3">
        <div className="max-w-5xl mx-auto flex items-center justify-between gap-3">
          {/* Back to Bible Reader Button */}
          <button
            onClick={onBackToBible}
            className="flex items-center gap-2 px-3.5 py-1.5 rounded-xl bg-amber-600/20 hover:bg-amber-600/30 text-amber-300 hover:text-amber-200 border border-amber-500/30 transition text-xs sm:text-sm font-semibold cursor-pointer"
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
              <span>{storyData.totalPanels} Illustrated Scenes</span>
              {readingFormat === 'page' && (
                <>
                  <span>•</span>
                  <span>Page {currentPageIndex + 1} of {pages.length}</span>
                </>
              )}
            </div>
          </div>

          {/* Reading Format & Theme Controls */}
          <div className="flex items-center gap-1.5 sm:gap-2">
            {/* Format Toggle: Scroll vs Page */}
            <div className="flex bg-stone-900 border border-stone-800 rounded-lg p-0.5">
              <button
                onClick={() => setReadingFormat('scroll')}
                className={`p-1.5 rounded-md text-xs font-semibold flex items-center gap-1 transition ${
                  readingFormat === 'scroll'
                    ? 'bg-purple-700 text-white shadow-xs'
                    : 'text-stone-400 hover:text-stone-200'
                }`}
                title="Continuous Vertical Manhwa Scroll"
              >
                <ScrollText className="w-3.5 h-3.5" />
                <span className="hidden md:inline">Scroll</span>
              </button>
              <button
                onClick={() => setReadingFormat('page')}
                className={`p-1.5 rounded-md text-xs font-semibold flex items-center gap-1 transition ${
                  readingFormat === 'page'
                    ? 'bg-purple-700 text-white shadow-xs'
                    : 'text-stone-400 hover:text-stone-200'
                }`}
                title="Page-by-Page Comic Layout"
              >
                <Layers className="w-3.5 h-3.5" />
                <span className="hidden md:inline">Pages</span>
              </button>
            </div>

            {/* Character Guide Quick Access */}
            <button
              onClick={onOpenCharacterGuide}
              className="p-1.5 rounded-lg bg-stone-900 border border-stone-800 text-stone-300 hover:text-purple-300 transition"
              title="Character & Art Guide"
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
              title="Toggle Story Theme"
            >
              {immersiveTheme === 'light' ? <Moon className="w-4 h-4" /> : <Sun className="w-4 h-4" />}
            </button>
          </div>
        </div>

        {/* Progress Bar */}
        <div className="w-full h-1 bg-stone-800 mt-2">
          <div 
            className="h-full bg-gradient-to-r from-purple-500 via-indigo-500 to-amber-500 transition-all duration-300"
            style={{ 
              width: readingFormat === 'page' 
                ? `${((currentPageIndex + 1) / pages.length) * 100}%` 
                : '100%' 
            }}
          />
        </div>
      </header>

      {/* Main Comic / Manhwa Container */}
      <main className="max-w-4xl mx-auto px-3 sm:px-6 pt-6 sm:pt-10">
        {/* Chapter Title Card */}
        <div className="mb-8 text-center space-y-2 p-6 rounded-2xl bg-gradient-to-b from-stone-900/60 to-stone-950/80 border border-white/5 shadow-xl">
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-purple-950/80 border border-purple-500/30 text-purple-300 text-xs font-bold uppercase tracking-wider">
            <Sparkles className="w-3.5 h-3.5" /> Visual Story Mode • Genesis {storyData.chapter}
          </div>
          <h2 className="text-2xl sm:text-4xl font-cinzel font-extrabold text-stone-100 tracking-tight">
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

        {/* Panels Content Area */}
        {readingFormat === 'scroll' ? (
          /* Vertical Manhwa Continuous Strip */
          <div className="space-y-12 sm:space-y-16">
            {allPanels.map((panel, idx) => (
              <PanelItem key={panel.panelId || idx} panel={panel} index={idx} />
            ))}
          </div>
        ) : (
          /* Page-by-Page Comic Format */
          <div className="space-y-8 animate-fade-in">
            {currentPage.panels.map((panel, idx) => (
              <PanelItem key={panel.panelId || idx} panel={panel} index={idx} />
            ))}

            {/* Page Navigation Controls */}
            <div className="pt-6 border-t border-white/10 flex items-center justify-between">
              <button
                onClick={() => {
                  if (currentPageIndex > 0) {
                    setCurrentPageIndex((prev) => prev - 1);
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                  }
                }}
                disabled={currentPageIndex === 0}
                className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-stone-900 border border-stone-800 hover:bg-stone-800 disabled:opacity-30 disabled:pointer-events-none transition cursor-pointer"
              >
                <ChevronLeft className="w-4 h-4" />
                <span>Previous Page</span>
              </button>

              <div className="text-xs font-semibold text-stone-400">
                Page {currentPageIndex + 1} of {pages.length}
              </div>

              <button
                onClick={() => {
                  if (currentPageIndex < pages.length - 1) {
                    setCurrentPageIndex((prev) => prev + 1);
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                  }
                }}
                disabled={currentPageIndex >= pages.length - 1}
                className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-stone-900 border border-stone-800 hover:bg-stone-800 disabled:opacity-30 disabled:pointer-events-none transition cursor-pointer"
              >
                <span>Next Page</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        )}

        {/* Chapter Completion & Navigation Footer */}
        <div className="mt-16 pt-8 border-t border-white/10 p-6 sm:p-8 rounded-2xl bg-stone-900/50 border border-white/5 text-center space-y-4">
          <div className="inline-flex items-center justify-center p-3 rounded-full bg-amber-500/20 text-amber-400 mb-1">
            <CheckCircle className="w-8 h-8" />
          </div>
          <h3 className="text-lg sm:text-xl font-cinzel font-bold text-stone-100">
            End of Genesis {chapterNumber} Story Mode
          </h3>
          <p className="text-xs sm:text-sm text-stone-400 max-w-lg mx-auto">
            Continue reading the narrative arc or return to the complete biblical chapter text with verse-by-verse study.
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
                <span>Proceed to Genesis {chapterNumber + 1} Story</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

// Individual Panel Component with Artwork, Narration Box, Dialogue Bubbles, and Verse Badge
function PanelItem({ panel, index }) {
  const [imageLoaded, setImageLoaded] = useState(false);
  const [imageError, setImageError] = useState(false);

  return (
    <article className="relative bg-stone-900/90 dark:bg-stone-950 border-2 border-stone-800 rounded-2xl overflow-hidden shadow-2xl transition hover:border-stone-700">
      {/* Bible Reference Badge at Top of Panel */}
      <div className="absolute top-4 left-4 z-20 flex items-center gap-2">
        <span className="px-3 py-1 rounded-full bg-black/75 backdrop-blur-md border border-white/20 text-amber-300 font-bold text-xs shadow-md tracking-wider flex items-center gap-1.5">
          <BookOpen className="w-3.5 h-3.5 text-amber-400" />
          {panel.reference}
        </span>
      </div>

      {/* Panel Illustration Container */}
      <div className="relative w-full aspect-video sm:aspect-16/9 bg-stone-950 overflow-hidden">
        {/* Placeholder skeleton while loading */}
        {!imageLoaded && !imageError && (
          <div className="absolute inset-0 bg-stone-900 animate-pulse flex items-center justify-center">
            <span className="text-xs text-stone-500 font-medium tracking-wide">
              Loading panel illustration...
            </span>
          </div>
        )}

        <img
          src={panel.image}
          alt={panel.altText || `Panel scene for ${panel.reference}`}
          loading="lazy"
          onLoad={() => setImageLoaded(true)}
          onError={() => {
            setImageLoaded(true);
            setImageError(true);
          }}
          className={`w-full h-full object-cover transition-opacity duration-500 ${
            imageLoaded ? 'opacity-100 scale-100' : 'opacity-0 scale-95'
          }`}
        />

        {/* Fallback if image fails */}
        {imageError && (
          <div className="absolute inset-0 bg-gradient-to-br from-stone-900 to-stone-950 flex flex-col items-center justify-center p-6 text-center">
            <Sparkles className="w-8 h-8 text-amber-400 mb-2 opacity-50" />
            <p className="text-sm font-semibold text-stone-300">{panel.reference}</p>
            <p className="text-xs text-stone-500 mt-1 max-w-sm">{panel.altText}</p>
          </div>
        )}

        {/* Cinematic gradient overlay at bottom of image for seamless panel blending */}
        <div className="absolute inset-x-0 bottom-0 h-24 bg-gradient-to-t from-stone-950/90 to-transparent pointer-events-none" />
      </div>

      {/* Narration and Character Dialogue Area */}
      <div className="p-4 sm:p-6 space-y-4 bg-stone-950/95">
        {/* Narration Box - Clearly Distinguished from Scripture */}
        {panel.narration && (
          <div className="narration-box p-3.5 sm:p-4 rounded-xl text-xs sm:text-sm leading-relaxed">
            <div className="text-[10px] uppercase font-bold tracking-wider text-amber-500 mb-1 flex items-center gap-1.5">
              <span>📜 Narration</span>
              <span className="text-stone-400 font-normal">({panel.reference})</span>
            </div>
            <p className="font-serif italic text-stone-200">
              "{panel.narration}"
            </p>
          </div>
        )}

        {/* Character Dialogue Speech Bubbles */}
        {panel.dialogue && panel.dialogue.length > 0 && (
          <div className="space-y-3 pt-1">
            {panel.dialogue.map((dlg, dIdx) => (
              <div 
                key={dIdx}
                className="p-3.5 bg-stone-900 border border-stone-800 rounded-xl space-y-1 shadow-md hover:border-purple-500/40 transition"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-purple-400 flex items-center gap-1.5">
                    <MessageSquare className="w-3.5 h-3.5" />
                    {dlg.speaker}
                  </span>
                  {dlg.isAdapted ? (
                    <span className="text-[10px] px-1.5 py-0.5 rounded bg-stone-800 text-stone-400 border border-stone-700">
                      Creative Adaptation
                    </span>
                  ) : (
                    <span className="text-[10px] px-1.5 py-0.5 rounded bg-amber-950/60 text-amber-300 border border-amber-800/40">
                      Biblical Text
                    </span>
                  )}
                </div>
                <p className="text-xs sm:text-sm font-sans font-medium text-stone-100 leading-snug">
                  {dlg.text}
                </p>
              </div>
            ))}
          </div>
        )}
      </div>
    </article>
  );
}
