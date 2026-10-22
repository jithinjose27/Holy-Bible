import React from 'react';
import ComicPanel from './ComicPanel';

/**
 * ComicPageLayout Component
 * 
 * Arranges panels into authentic graphic novel layouts:
 * - Splash tiers (single wide cinematic panel)
 * - Two-panel conversational tiers (medium shots with dialogue)
 * - Three-panel action strips
 */
export default function ComicPageLayout({
  panels = [],
  layoutMode = 'comic_grid' // 'comic_grid' | 'webtoon_strip'
}) {
  if (layoutMode === 'webtoon_strip') {
    return (
      <div className="flex flex-col space-y-12 sm:space-y-16 max-w-3xl mx-auto">
        {panels.map((panel, idx) => (
          <div key={panel.panelId || idx} className="w-full">
            <ComicPanel panel={panel} index={idx} isSplash={true} />
          </div>
        ))}
      </div>
    );
  }

  // Desktop graphic novel page grid
  return (
    <div className="max-w-4xl mx-auto space-y-6 sm:space-y-8 p-3 sm:p-6 bg-stone-900/60 rounded-2xl border border-stone-800 shadow-2xl">
      {/* Tier 1: Wide Establishing Shot */}
      {panels.length > 0 && (
        <div className="w-full">
          <ComicPanel 
            panel={panels[0]} 
            index={0} 
            isSplash={true}
            aspectRatio="aspect-16/9 sm:aspect-21/9" 
          />
        </div>
      )}

      {/* Tier 2: 2-panel spread (if 3 or more panels) */}
      {panels.length >= 3 && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <ComicPanel 
            panel={panels[1]} 
            index={1} 
            aspectRatio="aspect-4/3" 
          />
          <ComicPanel 
            panel={panels[2]} 
            index={2} 
            aspectRatio="aspect-4/3" 
          />
        </div>
      )}

      {/* Remaining panels */}
      {panels.slice(panels.length >= 3 ? 3 : 1).map((panel, idx) => (
        <div key={panel.panelId || idx + 3} className="w-full">
          <ComicPanel 
            panel={panel} 
            index={idx + 3} 
            isSplash={true}
            aspectRatio="aspect-16/9" 
          />
        </div>
      ))}
    </div>
  );
}
