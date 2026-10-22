import React, { useEffect, useRef } from 'react';
import { 
  Sparkles, 
  ChevronLeft, 
  ChevronRight, 
  Bookmark, 
  Share2, 
  ExternalLink, 
  Info,
  Check
} from 'lucide-react';

export default function BibleReader({
  chapterData,
  onOpenStoryMode,
  onPrevChapter,
  onNextChapter,
  fontSizeClass = "text-base",
  bookmarks = [],
  onToggleBookmark,
  targetVerse = null,
  clearTargetVerse
}) {
  const verseRefs = useRef({});
  const [copiedVerse, setCopiedVerse] = React.useState(null);

  // Auto scroll to target verse when jumped from search or bookmarks
  useEffect(() => {
    if (targetVerse && verseRefs.current[targetVerse]) {
      setTimeout(() => {
        verseRefs.current[targetVerse]?.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }, 100);
      const timer = setTimeout(() => {
        if (clearTargetVerse) clearTargetVerse();
      }, 3000);
      return () => clearTimeout(timer);
    }
  }, [targetVerse, chapterData]);

  if (!chapterData) {
    return (
      <div className="py-24 text-center text-stone-500">
        Loading chapter text...
      </div>
    );
  }

  const isVerseBookmarked = (verseNum) => {
    return bookmarks.some(
      (b) => b.chapter === chapterData.chapter && b.verse === verseNum
    );
  };

  const handleCopyVerse = (verseNum, text) => {
    const quote = `Genesis ${chapterData.chapter}:${verseNum} – "${text}" (EasyEnglish Bible)`;
    navigator.clipboard?.writeText(quote);
    setCopiedVerse(verseNum);
    setTimeout(() => setCopiedVerse(null), 2000);
  };

  return (
    <article className="max-w-3xl mx-auto px-4 sm:px-6 py-8 md:py-12 transition-colors">
      {/* Chapter Header Banner */}
      <div className="pb-8 mb-8 border-b border-stone-200 dark:border-stone-800">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <div className="text-xs uppercase font-bold tracking-widest text-amber-700 dark:text-amber-400 mb-1">
              Book of Genesis
            </div>
            <h1 className="text-3xl sm:text-4xl md:text-5xl font-cinzel font-bold text-stone-900 dark:text-stone-50 tracking-tight">
              {chapterData.title}
            </h1>
            {chapterData.subtitle && (
              <p className="mt-1.5 text-base sm:text-lg text-stone-600 dark:text-stone-300 font-serif italic">
                {chapterData.subtitle}
              </p>
            )}
          </div>

          {/* Dedicated "Read as Story" Action Button */}
          <div className="flex items-center gap-2">
            <button
              onClick={() => onOpenStoryMode(chapterData.chapter)}
              className="group relative inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-gradient-to-r from-purple-700 via-indigo-700 to-amber-700 hover:from-purple-800 hover:to-amber-800 text-white font-medium text-xs sm:text-sm shadow-md hover:shadow-lg transition-all transform hover:-translate-y-0.5 active:translate-y-0 cursor-pointer"
              title="Open full-colour illustrated manhwa story mode for this chapter"
            >
              <Sparkles className="w-4 h-4 text-amber-300 group-hover:rotate-12 transition-transform" />
              <span className="font-semibold tracking-wide">🎨 Read as Story</span>
            </button>
          </div>
        </div>

        {/* Official Source & Metadata Bar */}
        <div className="mt-4 pt-3 border-t border-stone-100 dark:border-stone-800/60 flex items-center justify-between text-xs text-stone-500 dark:text-stone-400">
          <div className="flex items-center gap-3">
            <span>Translation: EasyEnglish Bible</span>
            <span className="hidden sm:inline">•</span>
            <span className="hidden sm:inline">{chapterData.totalVerses} Verses</span>
          </div>
          <a
            href={chapterData.sourceUrl || `https://www.easyenglish.bible/bible/easy/genesis/${chapterData.chapter}/`}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1 text-stone-500 hover:text-amber-800 dark:hover:text-amber-400 transition"
          >
            <span>EasyEnglish.bible source</span>
            <ExternalLink className="w-3 h-3" />
          </a>
        </div>
      </div>

      {/* Main Scripture Text Body */}
      <div className={`space-y-6 font-serif-bible ${fontSizeClass} leading-relaxed text-stone-800 dark:text-stone-200`}>
        {chapterData.sections.map((section, sIdx) => (
          <section key={sIdx} className="space-y-4">
            {section.heading && (
              <h2 className="text-xl sm:text-2xl font-cinzel font-semibold text-stone-900 dark:text-stone-100 pt-4 pb-1 border-b border-stone-200/50 dark:border-stone-800/50">
                {section.heading}
              </h2>
            )}

            <div className="space-y-3">
              {section.items.map((paragraph, pIdx) => (
                <p key={pIdx} className="leading-loose tracking-normal text-justify sm:text-left">
                  {paragraph.map((verseItem, vIdx) => {
                    const vNum = verseItem.verse;
                    const bookmarked = isVerseBookmarked(vNum);
                    const isTarget = targetVerse === vNum;

                    return (
                      <span
                        key={vIdx}
                        ref={(el) => {
                          if (el && vNum) verseRefs.current[vNum] = el;
                        }}
                        className={`inline transition-colors duration-300 rounded px-1 -mx-1 ${
                          isTarget
                            ? 'bg-amber-200/90 dark:bg-amber-900/60 ring-2 ring-amber-400 font-medium'
                            : bookmarked
                            ? 'bg-amber-50 dark:bg-amber-950/40 text-stone-900 dark:text-stone-100'
                            : ''
                        }`}
                      >
                        {/* Verse Number Indicator */}
                        {!verseItem.isContinuation && (
                          <span
                            onClick={() => onToggleBookmark(chapterData.chapter, vNum, verseItem.text)}
                            title={`Click to bookmark Genesis ${chapterData.chapter}:${vNum}`}
                            className={`inline-flex items-center select-none cursor-pointer align-super text-[0.68em] font-sans font-bold mr-1.5 px-1 py-0.2 rounded transition ${
                              bookmarked
                                ? 'bg-amber-700 text-white shadow-xs'
                                : 'text-amber-700 dark:text-amber-400 hover:bg-amber-100 dark:hover:bg-amber-950/60'
                            }`}
                          >
                            {vNum}
                          </span>
                        )}
                        <span>{verseItem.text} </span>
                      </span>
                    );
                  })}
                </p>
              ))}
            </div>
          </section>
        ))}
      </div>

      {/* Chapter Footnotes / Study Notes if present */}
      {chapterData.footnotes && chapterData.footnotes.length > 0 && (
        <div className="mt-12 p-5 bg-stone-100/70 dark:bg-stone-900/60 border border-stone-200 dark:border-stone-800 rounded-xl space-y-2 text-xs text-stone-600 dark:text-stone-400 font-sans">
          <div className="font-bold text-stone-800 dark:text-stone-200 flex items-center gap-1.5 uppercase tracking-wider text-[11px]">
            <Info className="w-3.5 h-3.5 text-amber-700 dark:text-amber-400" /> Study Notes & Explanations
          </div>
          <div className="divide-y divide-stone-200/60 dark:divide-stone-800/60 pt-1">
            {chapterData.footnotes.map((fn, idx) => (
              <div key={idx} className="py-1.5 flex gap-2">
                <span className="font-semibold text-amber-800 dark:text-amber-400 shrink-0">
                  {fn.ref || `Note ${idx + 1}`}:
                </span>
                <span>{fn.text}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Bottom Chapter Navigation Bar */}
      <div className="mt-12 pt-6 border-t border-stone-200 dark:border-stone-800 flex items-center justify-between">
        <button
          onClick={onPrevChapter}
          disabled={chapterData.chapter <= 1}
          className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-semibold bg-stone-200/60 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 disabled:opacity-30 disabled:pointer-events-none transition"
        >
          <ChevronLeft className="w-4 h-4" />
          <span>Genesis {chapterData.chapter - 1}</span>
        </button>

        {/* Read as Story CTA at bottom */}
        <button
          onClick={() => onOpenStoryMode(chapterData.chapter)}
          className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-semibold text-purple-700 dark:text-purple-300 hover:bg-purple-100 dark:hover:bg-purple-950/40 border border-purple-200 dark:border-purple-900/50 transition"
        >
          <Sparkles className="w-4 h-4" />
          <span>Read Ch. {chapterData.chapter} as Story</span>
        </button>

        <button
          onClick={onNextChapter}
          disabled={chapterData.chapter >= 50}
          className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-semibold bg-stone-200/60 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 disabled:opacity-30 disabled:pointer-events-none transition"
        >
          <span>Genesis {chapterData.chapter + 1}</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>

      {/* Official EasyEnglish Notice */}
      <footer className="mt-8 text-center text-xs text-stone-500 dark:text-stone-400">
        <p>Scripture quotations are from the EasyEnglish Bible Copyright © MissionAssist 2018, 2024. Used by permission.</p>
      </footer>
    </article>
  );
}
