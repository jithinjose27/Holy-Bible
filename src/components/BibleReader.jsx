import React, { useState, useEffect, useRef } from 'react';
import { 
  Sparkles, 
  ChevronLeft, 
  ChevronRight, 
  Bookmark, 
  Share2, 
  ExternalLink, 
  Info,
  Check,
  Plus,
  Minus,
  BookOpen,
  ChevronDown,
  ChevronUp
} from 'lucide-react';
import kjvData from '../data/genesis_kjv_text.json';

export default function BibleReader({
  chapterData,
  onOpenStoryMode,
  onPrevChapter,
  onNextChapter,
  fontSizeClass = "text-base",
  bookmarks = [],
  onToggleBookmark,
  targetVerse = null,
  clearTargetVerse,
  highlights = {}, // { "ch-v": "yellow" | "green" | "blue" | "rose" | "purple" }
  onSetHighlight
}) {
  const verseRefs = useRef({});
  const [copiedVerse, setCopiedVerse] = useState(null);
  const [expandedVerses, setExpandedVerses] = useState({}); // { [verseNum]: boolean }
  const [showOverview, setShowOverview] = useState(false);

  // Reset expanded verses when changing chapter
  useEffect(() => {
    setExpandedVerses({});
  }, [chapterData?.chapter]);

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
      <div className="py-24 text-center text-stone-500 font-sans">
        Loading chapter text...
      </div>
    );
  }

  const isVerseBookmarked = (verseNum) => {
    return bookmarks.some(
      (b) => b.chapter === chapterData.chapter && b.verse === verseNum
    );
  };

  const toggleVerseExpand = (vNum) => {
    setExpandedVerses((prev) => ({
      ...prev,
      [vNum]: !prev[vNum]
    }));
  };

  // Retrieve exact KJV text for Genesis {chapter}:{verse} from WordProject dataset
  const getKjvVerseText = (chapterNum, verseNum) => {
    const chKey = String(chapterNum);
    const vKey = String(verseNum);
    return kjvData.chapters?.[chKey]?.[vKey] || null;
  };

  const handleCopyKjvVerse = (verseNum, text) => {
    const quote = `Genesis ${chapterData.chapter}:${verseNum} – “${text}” (King James Version - KJV, WordProject)`;
    navigator.clipboard?.writeText(quote);
    setCopiedVerse(`kjv-${verseNum}`);
    setTimeout(() => setCopiedVerse(null), 2500);
  };

  // Highlight color map
  const highlightClasses = {
    yellow: 'bg-amber-200/60 dark:bg-amber-900/40 rounded px-1',
    green: 'bg-emerald-200/60 dark:bg-emerald-900/40 rounded px-1',
    blue: 'bg-sky-200/60 dark:bg-sky-900/40 rounded px-1',
    rose: 'bg-rose-200/60 dark:bg-rose-900/40 rounded px-1',
    purple: 'bg-purple-200/60 dark:bg-purple-900/40 rounded px-1'
  };

  return (
    <article className="max-w-3xl mx-auto px-4 sm:px-6 py-8 md:py-12 transition-colors">
      {/* Chapter Header Banner */}
      <div className="pb-8 mb-8 border-b border-stone-200 dark:border-stone-800">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <div className="text-xs uppercase font-bold tracking-widest text-amber-700 dark:text-amber-400 mb-1">
              The Book of Genesis
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

          {/* Dedicated "Read as Comic" Action Button */}
          <div className="flex items-center gap-2">
            <button
              onClick={() => onOpenStoryMode(chapterData.chapter)}
              className="group relative inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-gradient-to-r from-purple-700 via-indigo-700 to-amber-700 hover:from-purple-800 hover:to-amber-800 text-white font-medium text-xs sm:text-sm shadow-md hover:shadow-lg transition-all transform hover:-translate-y-0.5 active:translate-y-0 cursor-pointer"
              title="Open photorealistic comic / manhwa story mode for Genesis"
            >
              <Sparkles className="w-4 h-4 text-amber-300 group-hover:rotate-12 transition-transform" />
              <span className="font-semibold tracking-wide">🎨 Read as Comic</span>
            </button>
          </div>
        </div>

        {/* Chapter Overview Card (Collapsible) */}
        <div className="mt-6 p-4 rounded-xl bg-amber-50/70 dark:bg-stone-900/80 border border-amber-200/60 dark:border-stone-800 transition">
          <div 
            onClick={() => setShowOverview(!showOverview)}
            className="flex items-center justify-between cursor-pointer select-none text-xs font-bold uppercase tracking-wider text-amber-800 dark:text-amber-400"
          >
            <span className="flex items-center gap-1.5">
              <BookOpen className="w-4 h-4 text-amber-700 dark:text-amber-400" />
              Chapter {chapterData.chapter} Overview & Historical Setting
            </span>
            <button className="text-stone-500 hover:text-stone-800 dark:hover:text-stone-200">
              {showOverview ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
            </button>
          </div>

          {showOverview && (
            <div className="mt-2.5 pt-2 border-t border-amber-200/50 dark:border-stone-800/80 text-xs sm:text-sm text-stone-700 dark:text-stone-300 font-serif leading-relaxed space-y-1.5">
              <p>
                <strong className="font-sans font-semibold text-stone-900 dark:text-stone-100">Summary: </strong>
                {chapterData.subtitle || `The narrative of Genesis Chapter ${chapterData.chapter}`}. Contains {chapterData.totalVerses} verses divided into {chapterData.sections.length} thematic sections.
              </p>
              <p className="text-xs text-stone-500 dark:text-stone-400 font-sans">
                💡 <strong className="font-semibold text-stone-700 dark:text-stone-300">Feature: </strong> 
                Click the <Plus className="w-3 h-3 inline text-amber-700 dark:text-amber-400 font-bold" /> icon beside any verse number to reveal the corresponding <strong>King James Version (KJV)</strong> text from WordProject.
              </p>
            </div>
          )}
        </div>

        {/* Translation Attribution Bar */}
        <div className="mt-4 pt-3 border-t border-stone-100 dark:border-stone-800/60 flex items-center justify-between text-xs text-stone-500 dark:text-stone-400">
          <div className="flex items-center gap-2">
            <span>Main Translation: EasyEnglish Bible</span>
            <span>•</span>
            <span>Expandable: King James Version (KJV)</span>
          </div>
          <a
            href={chapterData.sourceUrl || `https://www.easyenglish.bible/bible/easy/genesis/${chapterData.chapter}/`}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1 text-stone-500 hover:text-amber-800 dark:hover:text-amber-400 transition"
          >
            <span>EasyEnglish.bible</span>
            <ExternalLink className="w-3 h-3" />
          </a>
        </div>
      </div>

      {/* Main Scripture Text Body with Collapsible KJV Verse Controls */}
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
                <div key={pIdx} className="space-y-2">
                  <p className="leading-loose tracking-normal text-justify sm:text-left">
                    {paragraph.map((verseItem, vIdx) => {
                      const vNum = verseItem.verse;
                      const isBookmarked = isVerseBookmarked(vNum);
                      const isTarget = targetVerse === vNum;
                      const isExpanded = !!expandedVerses[vNum];
                      const hlColor = highlights?.[`${chapterData.chapter}-${vNum}`];

                      return (
                        <span
                          key={vIdx}
                          ref={(el) => {
                            if (el && vNum) verseRefs.current[vNum] = el;
                          }}
                          className={`inline transition-colors duration-300 ${
                            isTarget
                              ? 'bg-amber-200/90 dark:bg-amber-900/60 ring-2 ring-amber-400 font-medium'
                              : hlColor
                              ? highlightClasses[hlColor] || ''
                              : isBookmarked
                              ? 'bg-amber-50 dark:bg-amber-950/40 text-stone-900 dark:text-stone-100'
                              : ''
                          }`}
                        >
                          {/* Verse Number & Collapsible KJV Control */}
                          {!verseItem.isContinuation && (
                            <span className="inline-flex items-center gap-0.5 select-none align-baseline mr-1.5">
                              {/* Clickable Verse Number (Bookmark Toggle) */}
                              <button
                                onClick={() => onToggleBookmark(chapterData.chapter, vNum, verseItem.text)}
                                title={`Click to bookmark Genesis ${chapterData.chapter}:${vNum}`}
                                className={`text-[0.68em] font-sans font-bold px-1 py-0.2 rounded transition cursor-pointer ${
                                  isBookmarked
                                    ? 'bg-amber-700 text-white shadow-xs'
                                    : 'text-amber-700 dark:text-amber-400 hover:bg-amber-100 dark:hover:bg-amber-950/60'
                                }`}
                              >
                                {vNum}
                              </button>

                              {/* Unobtrusive Collapsible KJV Control Icon */}
                              <button
                                onClick={() => toggleVerseExpand(vNum)}
                                aria-label={isExpanded ? `Hide KJV text for Genesis ${chapterData.chapter}:${vNum}` : `Show KJV text for Genesis ${chapterData.chapter}:${vNum}`}
                                title={isExpanded ? "Hide King James Version text" : "Click to view exact King James Version (KJV) verse text from WordProject"}
                                className={`p-0.5 rounded transition cursor-pointer text-stone-400 hover:text-amber-800 dark:hover:text-amber-300 ${
                                  isExpanded ? 'text-amber-800 dark:text-amber-300 bg-amber-200/70 dark:bg-amber-950 font-bold' : 'hover:bg-stone-200/60 dark:hover:bg-stone-800'
                                }`}
                              >
                                {isExpanded ? (
                                  <Minus className="w-3 h-3" />
                                ) : (
                                  <Plus className="w-3 h-3" />
                                )}
                              </button>
                            </span>
                          )}

                          {/* Verse Text in Main Translation (EasyEnglish) */}
                          <span>{verseItem.text} </span>
                        </span>
                      );
                    })}
                  </p>

                  {/* Inline Expandable King James Version (KJV) Sections */}
                  {paragraph.map((verseItem) => {
                    const vNum = verseItem.verse;
                    const isExpanded = expandedVerses[vNum];
                    if (!isExpanded) return null;

                    const kjvVerseText = getKjvVerseText(chapterData.chapter, vNum);
                    const hlKey = `${chapterData.chapter}-${vNum}`;
                    const currentHl = highlights?.[hlKey];

                    return (
                      <div 
                        key={`expand-${vNum}`}
                        className="my-3 p-4 bg-amber-50/95 dark:bg-stone-900 border-l-4 border-amber-600 rounded-r-xl shadow-md space-y-3 font-sans text-xs sm:text-sm animate-fade-in"
                      >
                        {/* Header clearly labeling translation as King James Version (KJV) */}
                        <div className="flex items-center justify-between border-b border-amber-200/60 dark:border-stone-800 pb-2">
                          <div className="flex items-center gap-2">
                            <BookOpen className="w-4 h-4 text-amber-700 dark:text-amber-400" />
                            <span className="font-bold text-amber-950 dark:text-amber-300">
                              King James Version (KJV) • Genesis {chapterData.chapter}:{vNum}
                            </span>
                          </div>
                          <div className="flex items-center gap-2">
                            <a
                              href={`https://www.wordproject.org/bibles/kj/01/${chapterData.chapter}.htm`}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="text-[11px] text-amber-700 dark:text-amber-400 hover:underline flex items-center gap-1 font-medium"
                            >
                              <span>WordProject source</span>
                              <ExternalLink className="w-3 h-3" />
                            </a>
                            <button
                              onClick={() => toggleVerseExpand(vNum)}
                              className="text-xs text-stone-400 hover:text-stone-700 dark:hover:text-stone-200 ml-2"
                              aria-label={`Collapse Genesis ${chapterData.chapter}:${vNum}`}
                            >
                              Collapse
                            </button>
                          </div>
                        </div>

                        {/* Exact KJV Scripture Text from WordProject */}
                        <div className="p-3.5 bg-white dark:bg-stone-950 rounded-lg border border-amber-200/50 dark:border-stone-800">
                          {kjvVerseText ? (
                            <p className="font-serif italic text-stone-900 dark:text-stone-100 leading-relaxed text-sm sm:text-base">
                              “{kjvVerseText}”
                            </p>
                          ) : (
                            <p className="text-xs text-rose-500 italic">
                              KJV verse text is currently unavailable for Genesis {chapterData.chapter}:{vNum}.
                            </p>
                          )}
                        </div>

                        {/* Translation Contrast & Copy Citation */}
                        <div className="flex flex-wrap items-center justify-between gap-3 pt-1 text-xs">
                          {/* Color Highlighter Palette */}
                          <div className="flex items-center gap-1.5">
                            <span className="text-stone-500 font-medium">Highlight:</span>
                            {['yellow', 'green', 'blue', 'rose', 'purple'].map((color) => (
                              <button
                                key={color}
                                onClick={() => onSetHighlight && onSetHighlight(hlKey, currentHl === color ? null : color)}
                                className={`w-5 h-5 rounded-full border border-black/20 transition ${
                                  color === 'yellow' ? 'bg-amber-300' :
                                  color === 'green' ? 'bg-emerald-400' :
                                  color === 'blue' ? 'bg-sky-400' :
                                  color === 'rose' ? 'bg-rose-400' : 'bg-purple-400'
                                } ${currentHl === color ? 'ring-2 ring-stone-900 dark:ring-white scale-110' : 'hover:scale-105'}`}
                                title={`Highlight ${color}`}
                              />
                            ))}
                            {currentHl && (
                              <button
                                onClick={() => onSetHighlight && onSetHighlight(hlKey, null)}
                                className="text-[10px] text-stone-400 hover:text-stone-600 ml-1 underline"
                              >
                                Clear
                              </button>
                            )}
                          </div>

                          {/* Copy KJV Citation Action */}
                          {kjvVerseText && (
                            <button
                              onClick={() => handleCopyKjvVerse(vNum, kjvVerseText)}
                              className="inline-flex items-center gap-1 px-2.5 py-1 rounded bg-stone-200/80 dark:bg-stone-800 hover:bg-stone-300 text-stone-700 dark:text-stone-300 transition font-medium"
                            >
                              {copiedVerse === `kjv-${vNum}` ? (
                                <>
                                  <Check className="w-3.5 h-3.5 text-emerald-600" />
                                  <span>Copied KJV!</span>
                                </>
                              ) : (
                                <>
                                  <Share2 className="w-3.5 h-3.5" />
                                  <span>Copy KJV</span>
                                </>
                              )}
                            </button>
                          )}
                        </div>
                      </div>
                    );
                  })}
                </div>
              ))}
            </div>
          </section>
        ))}
      </div>

      {/* Chapter Footnotes section at bottom */}
      {chapterData.footnotes && chapterData.footnotes.length > 0 && (
        <div className="mt-12 p-5 bg-stone-100/70 dark:bg-stone-900/60 border border-stone-200 dark:border-stone-800 rounded-xl space-y-2 text-xs text-stone-600 dark:text-stone-400 font-sans">
          <div className="font-bold text-stone-800 dark:text-stone-200 flex items-center gap-1.5 uppercase tracking-wider text-[11px]">
            <Info className="w-3.5 h-3.5 text-amber-700 dark:text-amber-400" /> Complete Chapter Study Notes
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
          className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-semibold bg-stone-200/60 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 disabled:opacity-30 disabled:pointer-events-none transition cursor-pointer"
        >
          <ChevronLeft className="w-4 h-4" />
          <span>Genesis {chapterData.chapter - 1}</span>
        </button>

        {/* Read as Comic CTA at bottom */}
        <button
          onClick={() => onOpenStoryMode(chapterData.chapter)}
          className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold text-purple-700 dark:text-purple-300 hover:bg-purple-100 dark:hover:bg-purple-950/40 border border-purple-200 dark:border-purple-900/50 transition cursor-pointer"
        >
          <Sparkles className="w-4 h-4 text-amber-500" />
          <span>Read Ch. {chapterData.chapter} as Comic</span>
        </button>

        <button
          onClick={onNextChapter}
          disabled={chapterData.chapter >= 50}
          className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-semibold bg-stone-200/60 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 disabled:opacity-30 disabled:pointer-events-none transition cursor-pointer"
        >
          <span>Genesis {chapterData.chapter + 1}</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>

      {/* Translation & Attribution Notice */}
      <footer className="mt-8 text-center text-xs text-stone-500 dark:text-stone-400 space-y-1">
        <p>Main Scripture quotations are from the EasyEnglish Bible Copyright © MissionAssist 2018, 2024. Used by permission.</p>
        <p className="text-[11px] text-stone-400">Expandable verses are from the King James Version (KJV) sourced from WordProject (wordproject.org).</p>
      </footer>
    </article>
  );
}
