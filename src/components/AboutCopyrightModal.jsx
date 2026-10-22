import React from 'react';
import { X, ExternalLink, ShieldCheck, BookOpen, HelpCircle, Heart } from 'lucide-react';

export default function AboutCopyrightModal({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fade-in">
      <div 
        className="relative w-full max-w-2xl max-h-[90vh] overflow-y-auto bg-stone-50 dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-2xl shadow-2xl p-6 md:p-8 text-stone-800 dark:text-stone-200"
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
      >
        <button
          onClick={onClose}
          className="absolute top-5 right-5 p-2 rounded-full text-stone-400 hover:text-stone-700 dark:hover:text-stone-200 hover:bg-stone-200 dark:hover:bg-stone-800 transition"
          aria-label="Close dialog"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="flex items-center gap-3 mb-6">
          <div className="p-3 bg-amber-100 dark:bg-amber-950/60 text-amber-800 dark:text-amber-400 rounded-xl">
            <ShieldCheck className="w-6 h-6" />
          </div>
          <div>
            <h2 id="modal-title" className="text-xl md:text-2xl font-cinzel font-bold text-stone-900 dark:text-stone-100">
              Bible Translations & Copyright Notice
            </h2>
            <p className="text-xs text-stone-500 dark:text-stone-400">EasyEnglish Bible & King James Version (KJV)</p>
          </div>
        </div>

        <div className="space-y-5 text-sm leading-relaxed">
          {/* Main EasyEnglish Bible Attribution */}
          <div className="p-4 bg-amber-50/80 dark:bg-amber-950/30 border border-amber-200/80 dark:border-amber-900/40 rounded-xl">
            <h3 className="font-semibold text-amber-900 dark:text-amber-300 mb-1 flex items-center gap-2">
              <BookOpen className="w-4 h-4" /> Main Translation: EasyEnglish Bible
            </h3>
            <p className="font-serif italic text-stone-800 dark:text-stone-200 text-xs sm:text-sm">
              “Scripture quotations are from the EasyEnglish Bible Copyright © MissionAssist 2018, 2024 – UK Charitable Incorporated Organisation 1162807. Used by permission. All rights reserved.”
            </p>
            <div className="mt-3 pt-3 border-t border-amber-200/60 dark:border-amber-900/30 flex items-center justify-between text-xs">
              <span className="text-stone-500 dark:text-stone-400">Publisher: MissionAssist UK Charity</span>
              <a 
                href="https://www.easyenglish.bible/bible/easy/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="inline-flex items-center gap-1 font-medium text-amber-700 dark:text-amber-400 hover:underline"
              >
                Visit EasyEnglish.bible <ExternalLink className="w-3.5 h-3.5" />
              </a>
            </div>
          </div>

          {/* King James Version (KJV) via WordProject Attribution */}
          <div className="p-4 bg-stone-100/80 dark:bg-stone-800/60 border border-stone-200 dark:border-stone-700/60 rounded-xl">
            <h3 className="font-semibold text-stone-900 dark:text-stone-100 mb-1 flex items-center gap-2">
              <BookOpen className="w-4 h-4 text-amber-600" /> Expandable Translation: King James Version (KJV)
            </h3>
            <p className="font-serif italic text-stone-700 dark:text-stone-300 text-xs sm:text-sm">
              The King James Version (KJV) text revealed via the [+] verse control is sourced from WordProject (wordproject.org). This historic English translation allows readers to compare verses side-by-side with the modern EasyEnglish text.
            </p>
            <div className="mt-3 pt-3 border-t border-stone-200/60 dark:border-stone-700/40 flex items-center justify-between text-xs">
              <span className="text-stone-500 dark:text-stone-400">Reference: WordProject Public Repository</span>
              <a 
                href="https://www.wordproject.org/bibles/kj/01/1.htm" 
                target="_blank" 
                rel="noopener noreferrer"
                className="inline-flex items-center gap-1 font-medium text-amber-700 dark:text-amber-400 hover:underline"
              >
                Visit WordProject.org <ExternalLink className="w-3.5 h-3.5" />
              </a>
            </div>
          </div>

          <div>
            <h4 className="font-semibold text-stone-900 dark:text-stone-100 mb-1 flex items-center gap-2">
              <HelpCircle className="w-4 h-4 text-amber-700 dark:text-amber-400" /> Chapter Review — Questions & Answers
            </h4>
            <p className="text-stone-600 dark:text-stone-400 text-xs sm:text-sm">
              Each chapter of Genesis includes 10 review questions grounded directly in Scripture. Readers can test their understanding interactively through Practice Mode (instant feedback, live scoring, and explanations) or examine the full study guide with collapsible answers and verse references in Study Mode.
            </p>
          </div>

          <div className="p-3.5 bg-stone-100/70 dark:bg-stone-800/50 border border-stone-200 dark:border-stone-700/60 rounded-xl text-xs space-y-1">
            <h4 className="font-semibold text-stone-800 dark:text-stone-200">
              Offline Capability & Local Device Privacy
            </h4>
            <p className="text-stone-600 dark:text-stone-400 leading-relaxed">
              All 50 chapters of Genesis and all 500 review questions are pre-bundled and cached locally on your device via the Progressive Web App Service Worker. Reading progress, bookmarks, verse highlights, and quiz scores are stored strictly in your device's browser local storage and never transmitted to external cloud servers. Progress is maintained locally on each device.
            </p>
          </div>

          <div className="pt-4 border-t border-stone-200 dark:border-stone-800 text-xs text-stone-500 flex items-center justify-between">
            <span>Holy Bible Reader • Version 3.5 (Cross-Platform PWA & Offline Study)</span>
            <span className="flex items-center gap-1">Crafted with reverence <Heart className="w-3.5 h-3.5 text-rose-500 fill-rose-500 inline" /></span>
          </div>
        </div>
      </div>
    </div>
  );
}
