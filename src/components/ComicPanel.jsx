import React, { useState } from 'react';
import { BookOpen, Sparkles, ZoomIn, X } from 'lucide-react';
import ComicSpeechBubble from './ComicSpeechBubble';

export default function ComicPanel({
  panel,
  index,
  aspectRatio = 'aspect-16/9',
  isSplash = false,
  onInspectImage
}) {
  const [imageLoaded, setImageLoaded] = useState(false);
  const [imageError, setImageError] = useState(false);
  const [isZoomed, setIsZoomed] = useState(false);

  // Collect all bubbles for this panel
  const bubbles = panel.bubbles || [];

  return (
    <div className={`relative group ${isSplash ? 'col-span-full' : ''}`}>
      {/* Comic Panel Frame with authentic ink border and drop shadow */}
      <div className="relative bg-stone-950 border-3 border-stone-900 rounded-xl overflow-hidden shadow-[4px_6px_0px_rgba(0,0,0,0.85)] hover:shadow-[6px_8px_0px_rgba(0,0,0,0.9)] transition-all duration-300">
        
        {/* Top-Left Scripture Verse Range Badge */}
        <div className="absolute top-3 left-3 z-30 pointer-events-auto">
          <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-stone-900/90 border border-amber-500/40 text-amber-300 font-sans font-bold text-xs shadow-md tracking-wide backdrop-blur-xs">
            <BookOpen className="w-3.5 h-3.5 text-amber-400" />
            <span>{panel.reference}</span>
          </div>
        </div>

        {/* Top-Right Zoom Button */}
        <button
          onClick={() => setIsZoomed(true)}
          className="absolute top-3 right-3 z-30 p-1.5 rounded-md bg-stone-900/80 hover:bg-stone-800 text-stone-300 hover:text-white border border-stone-700 opacity-0 group-hover:opacity-100 transition shadow-sm cursor-pointer"
          title="Zoom Panel Image"
        >
          <ZoomIn className="w-3.5 h-3.5" />
        </button>

        {/* Panel Artwork Container */}
        <div className={`relative w-full ${panel.aspectRatio || aspectRatio} bg-stone-900 overflow-hidden`}>
          {/* Skeleton loader */}
          {!imageLoaded && !imageError && (
            <div className="absolute inset-0 bg-stone-900 animate-pulse flex items-center justify-center">
              <span className="text-xs text-stone-500 font-medium tracking-wide">
                Illustrating scene...
              </span>
            </div>
          )}

          {/* Panel Illustration */}
          <img
            src={panel.image}
            alt={panel.altText || `Comic scene for ${panel.reference}`}
            loading="lazy"
            onLoad={() => setImageLoaded(true)}
            onError={() => {
              setImageLoaded(true);
              setImageError(true);
            }}
            className={`w-full h-full object-cover transition-transform duration-700 group-hover:scale-[1.02] ${
              imageLoaded ? 'opacity-100' : 'opacity-0'
            }`}
          />

          {/* Fallback Graphic if Image Missing */}
          {imageError && (
            <div className="absolute inset-0 bg-gradient-to-br from-stone-900 to-stone-950 flex flex-col items-center justify-center p-6 text-center">
              <Sparkles className="w-8 h-8 text-amber-400 mb-2 opacity-40" />
              <p className="text-sm font-semibold text-stone-300">{panel.reference}</p>
              <p className="text-xs text-stone-500 mt-1 max-w-sm">{panel.altText}</p>
            </div>
          )}

          {/* Vignette border shading for comic ink aesthetic */}
          <div className="absolute inset-0 pointer-events-none ring-1 ring-inset ring-black/40 shadow-[inset_0_0_40px_rgba(0,0,0,0.5)]" />
        </div>

        {/* IN-PANEL SPEECH BUBBLE & NARRATION OVERLAY LAYER */}
        <div className="absolute inset-0 pointer-events-none p-3 sm:p-5 overflow-hidden">
          {bubbles.map((b, bIdx) => (
            <ComicSpeechBubble key={bIdx} bubble={b} />
          ))}

          {/* Fallback: If no structured bubbles array, render default narration/dialogue if available */}
          {bubbles.length === 0 && panel.narration && (
            <ComicSpeechBubble
              bubble={{
                type: 'narration',
                text: panel.narration,
                speaker: 'Narration',
                position: { bottom: '12px', left: '12px', right: '12px', maxWidth: '95%' }
              }}
            />
          )}

          {bubbles.length === 0 && panel.dialogue && panel.dialogue.map((dlg, dIdx) => (
            <ComicSpeechBubble
              key={`dlg-${dIdx}`}
              bubble={{
                type: dlg.speaker?.includes('Almighty') || dlg.speaker?.includes('Lord') ? 'divine' : 'speech',
                text: dlg.text.replace(/^[‘“'"]+|[’”'"]+$/g, ''),
                speaker: dlg.speaker,
                isAdapted: dlg.isAdapted,
                tailDirection: dIdx % 2 === 0 ? 'bottom-left' : 'bottom-right',
                position: { 
                  top: `${16 + dIdx * 32}%`, 
                  right: dIdx % 2 === 0 ? '16px' : 'auto',
                  left: dIdx % 2 === 0 ? 'auto' : '16px' 
                }
              }}
            />
          ))}
        </div>
      </div>

      {/* Fullscreen Zoom Modal */}
      {isZoomed && (
        <div 
          onClick={() => setIsZoomed(false)}
          className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/90 backdrop-blur-md animate-fade-in"
        >
          <div className="relative max-w-6xl max-h-[92vh] overflow-hidden rounded-xl border border-stone-800 bg-stone-950">
            <button
              onClick={() => setIsZoomed(false)}
              className="absolute top-4 right-4 z-50 p-2 rounded-full bg-black/70 text-white hover:bg-black transition"
            >
              <X className="w-6 h-6" />
            </button>
            <img
              src={panel.image}
              alt={panel.altText}
              className="w-full h-full object-contain max-h-[85vh]"
            />
            <div className="p-4 bg-stone-900/90 text-stone-200 text-sm border-t border-stone-800 flex items-center justify-between">
              <span className="font-bold text-amber-400">{panel.reference}</span>
              <span className="text-xs text-stone-400">{panel.altText}</span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
