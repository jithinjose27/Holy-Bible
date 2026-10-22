import React, { useState, useMemo } from 'react';
import { X, Search, BookOpen, ChevronRight, Hash } from 'lucide-react';

export default function SearchModal({ 
  isOpen, 
  onClose, 
  onSelectVerse, 
  currentBookText = null,
  bookName = "Genesis",
  bookId = "GEN"
}) {
  const [searchTerm, setSearchTerm] = useState('');

  const activeBookData = currentBookText;

  const searchResults = useMemo(() => {
    const q = searchTerm.trim().toLowerCase();
    if (!q || q.length < 2) return [];

    const results = [];
    const chapters = activeBookData?.chapters || [];

    for (const ch of chapters) {
      const verses = ch.verses || [];
      for (const v of verses) {
        if (v.text && v.text.toLowerCase().includes(q)) {
          results.push({
            bookId,
            bookName,
            chapter: ch.chapter,
            verse: v.verse,
            text: v.text,
            title: ch.title,
            subtitle: ch.subtitle
          });
          if (results.length >= 60) break; // cap search results for speed
        }
      }
      if (results.length >= 60) break;
    }
    return results;
  }, [searchTerm, activeBookData, bookId, bookName]);

  if (!isOpen) return null;

  const highlightMatch = (text, term) => {
    if (!term) return text;
    const parts = text.split(new RegExp(`(${term})`, 'gi'));
    return parts.map((part, i) => 
      part.toLowerCase() === term.toLowerCase() ? (
        <mark key={i} className="bg-amber-200 dark:bg-amber-900/80 text-amber-950 dark:text-amber-100 rounded px-0.5 font-semibold">
          {part}
        </mark>
      ) : part
    );
  };

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-12 md:pt-20 p-4 bg-black/60 backdrop-blur-sm animate-fade-in">
      <div 
        className="relative w-full max-w-2xl max-h-[80vh] flex flex-col bg-stone-50 dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-2xl shadow-2xl overflow-hidden"
        role="dialog"
        aria-modal="true"
      >
        {/* Search Input Bar */}
        <div className="p-4 border-b border-stone-200 dark:border-stone-800 bg-white dark:bg-stone-900 flex items-center gap-3">
          <Search className="w-5 h-5 text-stone-400" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder={`Search ${bookName} (e.g., 'faith', 'covenant', 'glory')...`}
            className="flex-1 bg-transparent text-base text-stone-800 dark:text-stone-100 placeholder:text-stone-400 focus:outline-none"
            autoFocus
          />
          {searchTerm && (
            <button
              onClick={() => setSearchTerm('')}
              className="p-1 rounded-full text-stone-400 hover:text-stone-600 dark:hover:text-stone-200"
            >
              <X className="w-4 h-4" />
            </button>
          )}
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-stone-400 hover:text-stone-700 dark:hover:text-stone-200"
          >
            <span className="text-xs font-semibold uppercase">Close</span>
          </button>
        </div>

        {/* Results List */}
        <div className="flex-1 overflow-y-auto p-4 space-y-2">
          {searchTerm.trim().length >= 2 && searchResults.length === 0 && (
            <div className="py-12 text-center text-stone-400">
              <Search className="w-8 h-8 mx-auto mb-2 opacity-30" />
              <p className="text-sm">No matches found for "{searchTerm}" in {bookName}.</p>
            </div>
          )}

          {searchTerm.trim().length < 2 && (
            <div className="py-12 text-center text-stone-400">
              <BookOpen className="w-8 h-8 mx-auto mb-2 opacity-30" />
              <p className="text-sm">Type 2 or more characters to search {bookName} scriptures.</p>
            </div>
          )}

          {searchResults.map((res) => (
            <div
              key={`${res.chapter}-${res.verse}`}
              onClick={() => {
                onSelectVerse(res.chapter, res.verse);
                onClose();
              }}
              className="p-3.5 bg-white dark:bg-stone-800/80 hover:bg-amber-50/60 dark:hover:bg-amber-950/30 border border-stone-200 dark:border-stone-800 hover:border-amber-400 dark:hover:border-amber-600 rounded-xl cursor-pointer transition group"
            >
              <div className="flex items-center justify-between text-xs font-bold text-amber-800 dark:text-amber-400 mb-1">
                <span className="flex items-center gap-1.5">
                  <Hash className="w-3.5 h-3.5 opacity-70" /> {res.bookName} {res.chapter}:{res.verse}
                </span>
                <span className="text-[11px] font-normal text-stone-400 group-hover:text-amber-600 flex items-center gap-0.5">
                  Jump to verse <ChevronRight className="w-3 h-3" />
                </span>
              </div>
              <p className="text-xs sm:text-sm font-serif-bible text-stone-800 dark:text-stone-200 leading-relaxed">
                {highlightMatch(res.text, searchTerm)}
              </p>
            </div>
          ))}
        </div>

        {/* Footer info */}
        {searchResults.length > 0 && (
          <div className="p-3 bg-stone-100 dark:bg-stone-950 text-xs text-stone-500 text-center border-t border-stone-200 dark:border-stone-800">
            Found {searchResults.length} {searchResults.length === 1 ? 'match' : 'matches'} in {bookName}
          </div>
        )}
      </div>
    </div>
  );
}
