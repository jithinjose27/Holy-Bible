import React, { useState, useMemo } from 'react';
import { X, Search, BookOpen, ChevronRight, Hash } from 'lucide-react';
import bibleData from '../data/genesis_bible_text.json';

export default function SearchModal({ isOpen, onClose, onSelectVerse }) {
  const [searchTerm, setSearchTerm] = useState('');

  const searchResults = useMemo(() => {
    const q = searchTerm.trim().toLowerCase();
    if (!q || q.length < 2) return [];

    const results = [];
    for (const ch of bibleData.chapters) {
      for (const v of ch.verses) {
        if (v.text.toLowerCase().includes(q)) {
          results.push({
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
  }, [searchTerm]);

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
            placeholder="Search Genesis (e.g., 'light', 'covenant', 'Joseph', 'stars')..."
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
            className="px-3 py-1.5 text-xs font-semibold bg-stone-200 dark:bg-stone-800 hover:bg-stone-300 dark:hover:bg-stone-700 text-stone-700 dark:text-stone-300 rounded-lg transition"
          >
            Esc
          </button>
        </div>

        {/* Results List */}
        <div className="flex-1 overflow-y-auto p-4 divide-y divide-stone-200/60 dark:divide-stone-800/60">
          {!searchTerm.trim() ? (
            <div className="py-12 text-center text-stone-400">
              <Search className="w-10 h-10 mx-auto mb-3 opacity-30" />
              <p className="text-sm font-medium">Type a word or phrase to search all 50 chapters of Genesis.</p>
              <div className="mt-4 flex flex-wrap justify-center gap-2 text-xs">
                {['In the beginning', 'Covenant', 'Rainbow', 'Abraham', 'Isaac', 'Ladder', 'Joseph'].map((sample) => (
                  <button
                    key={sample}
                    onClick={() => setSearchTerm(sample)}
                    className="px-2.5 py-1 bg-stone-100 dark:bg-stone-800 text-stone-600 dark:text-stone-300 rounded-full hover:bg-amber-100 dark:hover:bg-amber-950/40 hover:text-amber-800 transition"
                  >
                    "{sample}"
                  </button>
                ))}
              </div>
            </div>
          ) : searchResults.length === 0 ? (
            <div className="py-12 text-center text-stone-400">
              <p className="text-sm">No matches found for "{searchTerm}".</p>
            </div>
          ) : (
            searchResults.map((res, idx) => (
              <div
                key={idx}
                onClick={() => {
                  onSelectVerse(res.chapter, res.verse);
                  onClose();
                }}
                className="py-3 px-3 hover:bg-stone-100 dark:hover:bg-stone-800/50 rounded-xl cursor-pointer transition group"
              >
                <div className="flex items-center justify-between mb-1">
                  <span className="text-xs font-bold text-amber-800 dark:text-amber-400 flex items-center gap-1.5">
                    <BookOpen className="w-3.5 h-3.5" /> Genesis {res.chapter}:{res.verse}
                  </span>
                  <span className="text-[11px] text-stone-400 flex items-center gap-1 opacity-0 group-hover:opacity-100 transition">
                    Jump to verse <ChevronRight className="w-3.5 h-3.5" />
                  </span>
                </div>
                <p className="text-sm font-serif-bible text-stone-700 dark:text-stone-300 line-clamp-2 leading-relaxed">
                  {highlightMatch(res.text, searchTerm)}
                </p>
              </div>
            ))
          )}
        </div>

        {/* Footer */}
        {searchResults.length > 0 && (
          <div className="p-3 border-t border-stone-200 dark:border-stone-800 bg-stone-100/60 dark:bg-stone-950/40 text-xs text-stone-500 text-right">
            Found {searchResults.length} {searchResults.length === 60 ? 'or more' : ''} verses
          </div>
        )}
      </div>
    </div>
  );
}
