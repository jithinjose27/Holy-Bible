import React, { useState } from 'react';
import { X, Users, Compass, Sparkles, BookOpen } from 'lucide-react';
import characterData from '../data/character_reference_sheet.json';

export default function CharacterGuideModal({ isOpen, onClose, onSelectChapter }) {
  const [activeTab, setActiveTab] = useState('characters'); // 'characters' | 'environments'

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fade-in">
      <div 
        className="relative w-full max-w-4xl max-h-[90vh] flex flex-col bg-stone-50 dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-2xl shadow-2xl overflow-hidden text-stone-800 dark:text-stone-200"
        role="dialog"
        aria-modal="true"
        aria-labelledby="char-guide-title"
      >
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-stone-200 dark:border-stone-800 bg-stone-100/70 dark:bg-stone-950/40">
          <div className="flex items-center gap-3">
            <div className="p-3 bg-purple-100 dark:bg-purple-950/60 text-purple-700 dark:text-purple-300 rounded-xl">
              <Sparkles className="w-6 h-6" />
            </div>
            <div>
              <h2 id="char-guide-title" className="text-xl md:text-2xl font-cinzel font-bold text-stone-900 dark:text-stone-100">
                Visual Art Direction & Character Guide
              </h2>
              <p className="text-xs text-stone-500 dark:text-stone-400">
                Character continuity, cultural setting, and biblical art motifs
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-2 rounded-full text-stone-400 hover:text-stone-700 dark:hover:text-stone-200 hover:bg-stone-200 dark:hover:bg-stone-800 transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Tab Bar */}
        <div className="flex border-b border-stone-200 dark:border-stone-800 bg-stone-100/40 dark:bg-stone-950/20 px-6">
          <button
            onClick={() => setActiveTab('characters')}
            className={`flex items-center gap-2 py-3 px-4 text-sm font-medium border-b-2 transition ${
              activeTab === 'characters'
                ? 'border-purple-600 text-purple-700 dark:text-purple-400'
                : 'border-transparent text-stone-500 hover:text-stone-700 dark:hover:text-stone-300'
            }`}
          >
            <Users className="w-4 h-4" /> Recurring Characters ({characterData.characters.length})
          </button>
          <button
            onClick={() => setActiveTab('environments')}
            className={`flex items-center gap-2 py-3 px-4 text-sm font-medium border-b-2 transition ${
              activeTab === 'environments'
                ? 'border-purple-600 text-purple-700 dark:text-purple-400'
                : 'border-transparent text-stone-500 hover:text-stone-700 dark:hover:text-stone-300'
            }`}
          >
            <Compass className="w-4 h-4" /> Biblical Landscapes ({characterData.environments.length})
          </button>
        </div>

        {/* Content Body */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6">
          {activeTab === 'characters' ? (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {characterData.characters.map((char, idx) => (
                <div 
                  key={idx}
                  className="p-4 bg-white dark:bg-stone-800/70 border border-stone-200 dark:border-stone-700/60 rounded-xl shadow-sm hover:shadow-md transition"
                >
                  <div className="flex items-start justify-between mb-2">
                    <div>
                      <h3 className="font-bold text-stone-900 dark:text-stone-100 text-base flex items-center gap-2">
                        {char.name}
                      </h3>
                      <span className="text-xs font-medium text-purple-600 dark:text-purple-400">
                        {char.role}
                      </span>
                    </div>
                    {/* Color Swatches */}
                    <div className="flex items-center gap-1.5 pt-1">
                      {char.colorMotifs.map((color, cIdx) => (
                        <span 
                          key={cIdx} 
                          className="w-3.5 h-3.5 rounded-full border border-black/10 dark:border-white/10 shadow-xs" 
                          style={{ backgroundColor: color }}
                          title={`Motif color ${color}`}
                        />
                      ))}
                    </div>
                  </div>

                  <p className="text-xs text-stone-600 dark:text-stone-300 leading-relaxed mb-3">
                    {char.visualFeatures}
                  </p>

                  <div className="pt-2 border-t border-stone-100 dark:border-stone-700/50 flex flex-wrap items-center gap-1.5 text-xs text-stone-500">
                    <span className="font-semibold text-stone-700 dark:text-stone-300">Chapters:</span>
                    {char.keyChapters.map((ch) => (
                      <button
                        key={ch}
                        onClick={() => {
                          onClose();
                          if (onSelectChapter) onSelectChapter(ch);
                        }}
                        className="px-2 py-0.5 bg-stone-100 dark:bg-stone-700 hover:bg-purple-100 dark:hover:bg-purple-900/40 text-stone-700 dark:text-stone-200 hover:text-purple-700 dark:hover:text-purple-300 rounded font-medium transition"
                      >
                        Gen {ch}
                      </button>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="space-y-4">
              {characterData.environments.map((env, idx) => (
                <div 
                  key={idx}
                  className="p-5 bg-white dark:bg-stone-800/70 border border-stone-200 dark:border-stone-700/60 rounded-xl"
                >
                  <h3 className="font-bold text-base text-stone-900 dark:text-stone-100 mb-1">
                    {env.name}
                  </h3>
                  <div className="text-xs text-purple-600 dark:text-purple-400 font-medium mb-2">
                    Palette: {env.palette}
                  </div>
                  {env.features && (
                    <p className="text-xs text-stone-600 dark:text-stone-300">
                      <span className="font-semibold text-stone-700 dark:text-stone-200">Key Visual Motifs: </span> 
                      {env.features}
                    </p>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="p-4 border-t border-stone-200 dark:border-stone-800 bg-stone-100/50 dark:bg-stone-950/40 text-xs text-stone-500 flex items-center justify-between">
          <span>Artistic Philosophy: Historical reverence, rich atmospheric lighting, and visual continuity</span>
          <button 
            onClick={onClose}
            className="px-4 py-1.5 bg-stone-800 text-white dark:bg-stone-200 dark:text-stone-900 font-medium rounded-lg hover:opacity-90 transition"
          >
            Close Guide
          </button>
        </div>
      </div>
    </div>
  );
}
