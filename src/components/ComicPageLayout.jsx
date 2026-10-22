import React from 'react';
import ComicPanel from './ComicPanel';

/**
 * ComicPageLayout Component
 * 
 * Arranges the complete chapter's sequential panels into an authentic, continuous graphic novel layout:
 * - Dynamic splash panels for wide establishing shots & divine proclamations
 * - Two-panel conversational & interaction tiers for character dialogues
 * - Responsive vertical strip for webtoon / mobile reading
 * 
 * All panels appear on one continuous, vertically scrollable chapter page.
 */
export default function ComicPageLayout({
  panels = [],
  layoutMode = 'comic_grid' // 'comic_grid' | 'webtoon_strip'
}) {
  if (!panels || panels.length === 0) {
    return (
      <div className="py-16 text-center text-stone-500 font-sans">
        No scenes available for this chapter.
      </div>
    );
  }

  // 1. Continuous Vertical Webtoon Strip Mode
  if (layoutMode === 'webtoon_strip') {
    return (
      <div className="flex flex-col space-y-10 sm:space-y-14 max-w-3xl mx-auto">
        {panels.map((panel, idx) => (
          <div key={panel.panelId || panel.id || idx} className="w-full">
            <ComicPanel 
              panel={panel} 
              index={idx} 
              isSplash={true} 
              aspectRatio={panel.aspectRatio || "aspect-16/9"} 
            />
          </div>
        ))}
      </div>
    );
  }

  // 2. Cinematic Comic Grid Layout (Continuous Graphic Novel Tiers)
  // Group panels rhythmically: Splash (1), Paired (2), Splash (1), Paired (2)...
  const renderTieredPanels = () => {
    const tiers = [];
    let i = 0;

    while (i < panels.length) {
      const pCurrent = panels[i];
      const isDivine = pCurrent.bubbles?.some(b => b.type === 'divine');
      const isExplicitSplash = pCurrent.isSplash || pCurrent.aspectRatio === 'aspect-21/9' || i === 0;

      // Single full-width splash panel for opening, divine proclamations, or odd remaining
      if (isExplicitSplash || isDivine || i === panels.length - 1) {
        tiers.push(
          <div key={`tier-${i}`} className="w-full">
            <ComicPanel 
              panel={pCurrent} 
              index={i} 
              isSplash={true}
              aspectRatio={i === 0 ? "aspect-16/9 sm:aspect-21/9" : (pCurrent.aspectRatio || "aspect-16/9")} 
            />
          </div>
        );
        i += 1;
      } else {
        // Paired two-column tier for character interactions / conversations
        const pNext = panels[i + 1];
        tiers.push(
          <div key={`tier-${i}-${i+1}`} className="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8 items-stretch">
            <div className="w-full">
              <ComicPanel 
                panel={pCurrent} 
                index={i} 
                aspectRatio="aspect-4/3 sm:aspect-16/10" 
              />
            </div>
            <div className="w-full">
              <ComicPanel 
                panel={pNext} 
                index={i + 1} 
                aspectRatio="aspect-4/3 sm:aspect-16/10" 
              />
            </div>
          </div>
        );
        i += 2;
      }
    }
    return tiers;
  };

  return (
    <div className="max-w-5xl mx-auto space-y-8 sm:space-y-12 p-3 sm:p-8 bg-stone-900/60 rounded-3xl border border-stone-800 shadow-2xl">
      {renderTieredPanels()}
    </div>
  );
}
