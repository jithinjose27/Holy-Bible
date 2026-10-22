import React from 'react';
import { X, Bookmark, Trash2, ArrowRight, BookOpen, Clock, CheckCircle2 } from 'lucide-react';

export default function BookmarksDrawer({ 
  isOpen, 
  onClose, 
  bookmarks = [], 
  onRemoveBookmark, 
  onSelectVerse, 
  currentChapter = 1, 
  totalChapters = 50,
  bookName = "Genesis",
  bookId = "GEN"
}) {
  if (!isOpen) return null;

  const progressPercent = Math.round((currentChapter / totalChapters) * 100);

  return (
    <div className="fixed inset-0 z-50 flex justify-end bg-black/50 backdrop-blur-xs animate-fade-in">
      <div 
        className="w-full max-w-md h-full bg-stone-50 dark:bg-stone-900 border-l border-stone-200 dark:border-stone-800 shadow-2xl flex flex-col"
        role="dialog"
      >
        {/* Header */}
        <div className="p-5 border-b border-stone-200 dark:border-stone-800 flex items-center justify-between bg-stone-100/60 dark:bg-stone-950/40">
          <div className="flex items-center gap-2.5">
            <Bookmark className="w-5 h-5 text-amber-700 dark:text-amber-400 fill-amber-700 dark:fill-amber-400" />
            <h2 className="font-cinzel font-bold text-lg text-stone-900 dark:text-stone-100">
              Bookmarks & Progress
            </h2>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-full text-stone-400 hover:text-stone-700 dark:hover:text-stone-200"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Reading Progress Card */}
        <div className="p-5 border-b border-stone-200 dark:border-stone-800 bg-amber-50/50 dark:bg-amber-950/20">
          <div className="flex items-center justify-between text-xs font-semibold text-stone-600 dark:text-stone-400 mb-2">
            <span>{bookName} Reading Progress</span>
            <span className="text-amber-800 dark:text-amber-300 font-bold">{progressPercent}%</span>
          </div>
          <div className="w-full h-2 bg-stone-200 dark:bg-stone-800 rounded-full overflow-hidden">
            <div 
              className="h-full bg-gradient-to-r from-amber-600 to-amber-500 rounded-full transition-all duration-500" 
              style={{ width: `${progressPercent}%` }}
            />
          </div>
          <p className="mt-2 text-xs text-stone-500 flex items-center gap-1.5">
            <CheckCircle2 className="w-3.5 h-3.5 text-amber-600" />
            Currently at Chapter {currentChapter} of {totalChapters}
          </p>
        </div>

        {/* Bookmarks List */}
        <div className="flex-1 overflow-y-auto p-5 space-y-3">
          <h3 className="text-xs font-bold uppercase tracking-wider text-stone-400 mb-2">
            Saved Verses ({bookmarks.length})
          </h3>

          {bookmarks.length === 0 ? (
            <div className="py-12 text-center text-stone-400">
              <Bookmark className="w-10 h-10 mx-auto mb-2 opacity-25" />
              <p className="text-sm font-medium">No saved verses yet.</p>
              <p className="text-xs text-stone-500 mt-1">
                Click on any verse number while reading to bookmark it.
              </p>
            </div>
          ) : (
            bookmarks.map((bm, idx) => (
              <div
                key={bm.id || `${bm.bookId || bookId}-${bm.chapter}-${bm.verse}-${idx}`}
                className="p-3 bg-white dark:bg-stone-800/80 border border-stone-200 dark:border-stone-700/60 rounded-xl shadow-xs hover:border-amber-400 dark:hover:border-amber-600 transition group"
              >
                <div className="flex items-center justify-between mb-1.5">
                  <span className="text-xs font-bold text-amber-800 dark:text-amber-400 flex items-center gap-1">
                    <BookOpen className="w-3.5 h-3.5" /> {bm.bookName || bookName} {bm.chapter}:{bm.verse}
                  </span>
                  <button
                    onClick={() => onRemoveBookmark(bm.chapter, bm.verse, bm.bookId || bookId)}
                    className="text-stone-300 hover:text-rose-500 p-1 transition"
                    title="Remove bookmark"
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                  </button>
                </div>
                <p className="text-xs font-serif-bible text-stone-700 dark:text-stone-300 line-clamp-3 leading-relaxed">
                  "{bm.text}"
                </p>
                <div className="mt-2 pt-2 border-t border-stone-100 dark:border-stone-700/50 flex justify-end">
                  <button
                    onClick={() => {
                      onSelectVerse(bm.chapter, bm.verse, bm.bookId || bookId);
                      onClose();
                    }}
                    className="text-xs font-medium text-amber-700 dark:text-amber-400 hover:underline flex items-center gap-1"
                  >
                    Go to verse <ArrowRight className="w-3 h-3" />
                  </button>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}
