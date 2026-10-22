import React from 'react';

/**
 * ComicSpeechBubble Component
 * 
 * Renders authentic graphic novel speech bubbles with:
 * - Rounded white bubble with bold comic ink borders
 * - Tapered SVG pointer tails directed accurately toward the speaker
 * - Divine proclamation / Voice of God banners with golden glowing aura
 * - Thought bubbles with cloud scallops and trailing bubbles
 * - Shouting / action bubbles with jagged starburst outlines
 * - Comic Sound FX (SFX) lettering
 * - Narration boxes with dark ink border and parchment gradient
 */
export default function ComicSpeechBubble({
  bubble, // { type, text, speaker, tailDirection, position, sfx, isAdapted }
  panelRef
}) {
  const {
    type = 'speech',
    text,
    speaker,
    tailDirection = 'bottom-left',
    position = { top: '10%', left: '10%' },
    sfx,
    isAdapted = false
  } = bubble;

  // Render tail based on tailDirection
  const renderTail = () => {
    switch (tailDirection) {
      case 'bottom-left':
        return (
          <svg 
            className="absolute -bottom-3.5 left-6 w-5 h-4 pointer-events-none drop-shadow-sm" 
            viewBox="0 0 20 16"
            fill="none"
          >
            <path d="M0 0 L16 0 L3 15 Z" fill="#ffffff" stroke="#0f172a" strokeWidth="2" strokeLinejoin="round" />
            {/* Mask to bridge the bubble border */}
            <line x1="1" y1="0" x2="15" y2="0" stroke="#ffffff" strokeWidth="3" />
          </svg>
        );
      case 'bottom-right':
        return (
          <svg 
            className="absolute -bottom-3.5 right-6 w-5 h-4 pointer-events-none drop-shadow-sm" 
            viewBox="0 0 20 16"
            fill="none"
          >
            <path d="M4 0 L20 0 L17 15 Z" fill="#ffffff" stroke="#0f172a" strokeWidth="2" strokeLinejoin="round" />
            <line x1="5" y1="0" x2="19" y2="0" stroke="#ffffff" strokeWidth="3" />
          </svg>
        );
      case 'top-left':
        return (
          <svg 
            className="absolute -top-3.5 left-6 w-5 h-4 pointer-events-none drop-shadow-sm" 
            viewBox="0 0 20 16"
            fill="none"
          >
            <path d="M0 16 L16 16 L3 1 Z" fill="#ffffff" stroke="#0f172a" strokeWidth="2" strokeLinejoin="round" />
            <line x1="1" y1="16" x2="15" y2="16" stroke="#ffffff" strokeWidth="3" />
          </svg>
        );
      case 'top-right':
        return (
          <svg 
            className="absolute -top-3.5 right-6 w-5 h-4 pointer-events-none drop-shadow-sm" 
            viewBox="0 0 20 16"
            fill="none"
          >
            <path d="M4 16 L20 16 L17 1 Z" fill="#ffffff" stroke="#0f172a" strokeWidth="2" strokeLinejoin="round" />
            <line x1="5" y1="16" x2="19" y2="16" stroke="#ffffff" strokeWidth="3" />
          </svg>
        );
      case 'left':
        return (
          <svg 
            className="absolute top-4 -left-3.5 w-4 h-5 pointer-events-none drop-shadow-sm" 
            viewBox="0 0 16 20"
            fill="none"
          >
            <path d="M16 0 L16 16 L1 3 Z" fill="#ffffff" stroke="#0f172a" strokeWidth="2" strokeLinejoin="round" />
            <line x1="16" y1="1" x2="16" y2="15" stroke="#ffffff" strokeWidth="3" />
          </svg>
        );
      case 'right':
        return (
          <svg 
            className="absolute top-4 -right-3.5 w-4 h-5 pointer-events-none drop-shadow-sm" 
            viewBox="0 0 16 20"
            fill="none"
          >
            <path d="M0 0 L0 16 L15 3 Z" fill="#ffffff" stroke="#0f172a" strokeWidth="2" strokeLinejoin="round" />
            <line x1="0" y1="1" x2="0" y2="15" stroke="#ffffff" strokeWidth="3" />
          </svg>
        );
      default:
        return null;
    }
  };

  // Convert position object to inline style
  const positionStyle = {
    position: 'absolute',
    ...position,
    maxWidth: position.maxWidth || '85%'
  };

  // 1. Narration Box (Classic comic caption)
  if (type === 'narration') {
    return (
      <div 
        style={positionStyle} 
        className="z-20 bg-amber-50/95 dark:bg-stone-900/95 border-2 border-stone-900 dark:border-amber-500/60 shadow-[3px_3px_0px_rgba(0,0,0,0.85)] rounded-md px-3.5 py-2.5 backdrop-blur-xs text-xs sm:text-sm text-stone-900 dark:text-stone-100 font-serif leading-relaxed max-w-sm sm:max-w-md animate-fade-in pointer-events-auto"
      >
        <div className="flex items-center justify-between text-[10px] font-sans font-bold uppercase tracking-wider text-amber-700 dark:text-amber-400 mb-1 border-b border-amber-200/50 dark:border-stone-800 pb-0.5">
          <span>{speaker || 'Narration'}</span>
        </div>
        <p className="italic">"{text}"</p>
      </div>
    );
  }

  // 2. Divine Speech / Voice of God (Proclamation treatment with golden glowing aura)
  if (type === 'divine') {
    return (
      <div 
        style={positionStyle}
        className="z-20 bg-gradient-to-r from-amber-100/95 via-white/95 to-amber-100/95 border-2 border-amber-500 shadow-[0_0_20px_rgba(245,158,11,0.5),3px_3px_0px_rgba(15,23,42,0.9)] rounded-xl px-4 py-3 text-center max-w-sm sm:max-w-md backdrop-blur-xs animate-fade-in pointer-events-auto"
      >
        <div className="text-[10px] uppercase font-cinzel font-bold tracking-widest text-amber-800 mb-1 flex items-center justify-center gap-1.5">
          <span className="w-4 h-px bg-amber-600"></span>
          <span>Voice of the Almighty</span>
          <span className="w-4 h-px bg-amber-600"></span>
        </div>
        <p className="font-cinzel font-extrabold text-sm sm:text-base md:text-lg text-amber-950 tracking-wide leading-tight drop-shadow-xs">
          “{text}”
        </p>
        {/* Divine radiating downward beam */}
        <div className="w-1.5 h-4 bg-gradient-to-b from-amber-500 to-transparent mx-auto mt-1 rounded-full opacity-80" />
      </div>
    );
  }

  // 3. Shouting / Dramatic Action Bubble (Jagged starburst)
  if (type === 'shout') {
    return (
      <div 
        style={positionStyle}
        className="z-20 relative bg-amber-50 border-2 border-stone-900 shadow-[4px_4px_0px_#0f172a] rounded-lg px-4 py-2.5 max-w-xs sm:max-w-sm pointer-events-auto"
      >
        {speaker && (
          <div className="text-[10px] font-bold uppercase tracking-wider text-rose-700 mb-0.5">
            {speaker} {isAdapted && <span className="opacity-70 font-normal">(Adaptation)</span>}
          </div>
        )}
        <p className="font-comic text-base sm:text-lg text-stone-900 uppercase tracking-wide leading-tight">
          “{text}”
        </p>
        {renderTail()}
      </div>
    );
  }

  // 4. Thought Bubble (Scalloped cloud shape with small trailing circles)
  if (type === 'thought') {
    return (
      <div 
        style={positionStyle}
        className="z-20 relative bg-white border-2 border-stone-800 shadow-[3px_3px_0px_rgba(15,23,42,0.6)] rounded-3xl px-4 py-2.5 max-w-xs sm:max-w-sm pointer-events-auto"
      >
        {speaker && (
          <div className="text-[10px] font-medium text-stone-500 mb-0.5">
            💭 {speaker}'s thought
          </div>
        )}
        <p className="font-sans text-xs sm:text-sm text-stone-800 italic leading-snug">
          ({text})
        </p>
        {/* Trailing thought circles */}
        <div className="absolute -bottom-3 left-6 flex flex-col items-center gap-0.5">
          <div className="w-2.5 h-2.5 rounded-full bg-white border-2 border-stone-800" />
          <div className="w-1.5 h-1.5 rounded-full bg-white border border-stone-800" />
        </div>
      </div>
    );
  }

  // 5. Sound Effect (SFX) Lettering
  if (type === 'sfx') {
    return (
      <div 
        style={positionStyle}
        className="z-30 pointer-events-none select-none"
      >
        <span className="font-comic text-3xl sm:text-5xl font-extrabold tracking-widest text-amber-400 uppercase drop-shadow-[3px_3px_0px_#0f172a] transform -rotate-6 inline-block">
          {sfx || text}
        </span>
      </div>
    );
  }

  // 6. Default: Classic Comic Speech Bubble
  return (
    <div 
      style={positionStyle}
      className="z-20 relative bg-white border-2 border-stone-900 shadow-[3px_3px_0px_#0f172a] rounded-2xl px-3.5 sm:px-4 py-2 sm:py-2.5 max-w-xs sm:max-w-sm backdrop-blur-xs transition-transform hover:scale-[1.02] pointer-events-auto"
    >
      {speaker && (
        <div className="flex items-center justify-between text-[10px] font-sans font-bold uppercase tracking-wider text-purple-700 dark:text-purple-800 mb-0.5 border-b border-stone-100 pb-0.5">
          <span>{speaker}</span>
          {isAdapted && (
            <span className="text-[9px] text-stone-400 font-normal capitalize">
              (Adaptation)
            </span>
          )}
        </div>
      )}
      <p className="font-sans font-semibold text-xs sm:text-sm text-stone-900 leading-snug">
        “{text}”
      </p>
      {renderTail()}
    </div>
  );
}
