import React from 'react';
import { X, ExternalLink, ShieldCheck, BookOpen, Sparkles, Heart } from 'lucide-react';

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
              Bible Text & Copyright Notice
            </h2>
            <p className="text-xs text-stone-500 dark:text-stone-400">EasyEnglish Bible Translation & Visual Adaptation</p>
          </div>
        </div>

        <div className="space-y-5 text-sm leading-relaxed">
          <div className="p-4 bg-amber-50/80 dark:bg-amber-950/30 border border-amber-200/80 dark:border-amber-900/40 rounded-xl">
            <h3 className="font-semibold text-amber-900 dark:text-amber-300 mb-1 flex items-center gap-2">
              <BookOpen className="w-4 h-4" /> Official Scripture Attribution
            </h3>
            <p className="font-serif italic text-stone-800 dark:text-stone-200">
              “Scripture quotations are from the EasyEnglish Bible Copyright © MissionAssist 2018, 2024 – UK Charitable Incorporated Organisation 1162807. Used by permission. All rights reserved.”
            </p>
            <div className="mt-3 pt-3 border-t border-amber-200/60 dark:border-amber-900/30 flex items-center justify-between text-xs">
              <span className="text-stone-500 dark:text-stone-400">Source: MissionAssist Charity</span>
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

          <div>
            <h4 className="font-semibold text-stone-900 dark:text-stone-100 mb-1">About the EasyEnglish Bible</h4>
            <p className="text-stone-600 dark:text-stone-400">
              The EasyEnglish Bible is produced by MissionAssist in the United Kingdom. It is translated from the original biblical languages into clear, modern English using a carefully chosen vocabulary of around 1,200 words, making it accessible to international readers, English learners, and families.
            </p>
          </div>

          <div>
            <h4 className="font-semibold text-stone-900 dark:text-stone-100 mb-1 flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-purple-600 dark:text-purple-400" /> Visual Story Mode & Creative Adaptation
            </h4>
            <p className="text-stone-600 dark:text-stone-400">
              The Visual Story Mode is a creative sequential comic/manhwa accompaniment designed to assist readers in visualizing the historical context and narrative drama of Scripture. In Visual Story Mode:
            </p>
            <ul className="mt-2 space-y-1.5 list-disc list-inside text-stone-600 dark:text-stone-400">
              <li>Original Scripture verses are cited explicitly for every scene.</li>
              <li>Supplemental narration is framed in distinct narration boxes to explain flow.</li>
              <li>Direct quotes from Scripture are rendered as biblical statements, while supplemental dialogue is explicitly tagged as creative adaptation.</li>
              <li>The normal Bible reading mode preserves the unadulterated EasyEnglish Bible text without any artistic intrusion.</li>
            </ul>
          </div>

          <div className="pt-4 border-t border-stone-200 dark:border-stone-800 text-xs text-stone-500 flex items-center justify-between">
            <span>Holy Bible Reader • Version 1.0</span>
            <span className="flex items-center gap-1">Crafted with reverence <Heart className="w-3.5 h-3.5 text-rose-500 fill-rose-500 inline" /></span>
          </div>
        </div>
      </div>
    </div>
  );
}
