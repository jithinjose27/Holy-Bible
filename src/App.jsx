import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import BibleReader from './components/BibleReader';
import VisualStoryReader from './components/VisualStoryReader';
import SearchModal from './components/SearchModal';
import BookmarksDrawer from './components/BookmarksDrawer';
import CharacterGuideModal from './components/CharacterGuideModal';
import AboutCopyrightModal from './components/AboutCopyrightModal';

import bibleData from './data/genesis_bible_text.json';
import storyDataset from './data/genesis_story_data.json';

export default function App() {
  const [activeMode, setActiveMode] = useState('bible'); // 'bible' (default) | 'story'
  const [currentChapter, setCurrentChapter] = useState(1);
  const [targetVerse, setTargetVerse] = useState(null);

  // Persistent settings in localStorage
  const [theme, setTheme] = useState(() => {
    return localStorage.getItem('holy_bible_theme') || 'paper';
  });
  const [fontSize, setFontSize] = useState(() => {
    return localStorage.getItem('holy_bible_font_size') || 'medium';
  });
  const [bookmarks, setBookmarks] = useState(() => {
    try {
      const saved = localStorage.getItem('holy_bible_bookmarks');
      return saved ? JSON.parse(saved) : [];
    } catch {
      return [];
    }
  });

  // Modal states
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [isBookmarksOpen, setIsBookmarksOpen] = useState(false);
  const [isCharacterGuideOpen, setIsCharacterGuideOpen] = useState(false);
  const [isCopyrightOpen, setIsCopyrightOpen] = useState(false);

  // Sync settings
  useEffect(() => {
    localStorage.setItem('holy_bible_theme', theme);
    document.documentElement.className = theme === 'dark' || theme === 'midnight' ? 'dark' : '';
  }, [theme]);

  useEffect(() => {
    localStorage.setItem('holy_bible_font_size', fontSize);
  }, [fontSize]);

  useEffect(() => {
    localStorage.setItem('holy_bible_bookmarks', JSON.stringify(bookmarks));
  }, [bookmarks]);

  // Global keyboard shortcuts (Ctrl+K for search)
  useEffect(() => {
    const handleKeyDown = (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        setIsSearchOpen(true);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  // Chapter data retrieval
  const currentBibleChapter = bibleData.chapters.find((c) => c.chapter === currentChapter) || bibleData.chapters[0];
  const currentStoryChapter = storyDataset.chapters.find((c) => c.chapter === currentChapter) || storyDataset.chapters[0];

  // Handlers
  const handleSelectChapter = (ch) => {
    if (ch >= 1 && ch <= 50) {
      setCurrentChapter(ch);
      setTargetVerse(null);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const handlePrevChapter = () => {
    if (currentChapter > 1) {
      handleSelectChapter(currentChapter - 1);
    }
  };

  const handleNextChapter = () => {
    if (currentChapter < 50) {
      handleSelectChapter(currentChapter + 1);
    }
  };

  const handleOpenStoryMode = (ch) => {
    if (ch) setCurrentChapter(ch);
    setActiveMode('story');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleBackToBible = () => {
    setActiveMode('bible');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleToggleBookmark = (ch, verseNum, text) => {
    setBookmarks((prev) => {
      const exists = prev.some((b) => b.chapter === ch && b.verse === verseNum);
      if (exists) {
        return prev.filter((b) => !(b.chapter === ch && b.verse === verseNum));
      } else {
        return [...prev, { chapter: ch, verse: verseNum, text, date: new Date().toISOString() }];
      }
    });
  };

  const handleRemoveBookmark = (ch, verseNum) => {
    setBookmarks((prev) => prev.filter((b) => !(b.chapter === ch && b.verse === verseNum)));
  };

  const handleSelectVerseFromSearchOrBookmark = (ch, verseNum) => {
    setCurrentChapter(ch);
    setTargetVerse(verseNum);
    setActiveMode('bible');
  };

  // Font size classes
  const fontSizeMap = {
    small: 'text-sm sm:text-base',
    medium: 'text-base sm:text-lg',
    large: 'text-lg sm:text-xl',
    xlarge: 'text-xl sm:text-2xl'
  };

  return (
    <div className={`min-h-screen theme-${theme} transition-colors duration-200 flex flex-col`}>
      {/* Top Navbar */}
      <Navbar
        currentBook="Genesis"
        currentChapter={currentChapter}
        totalChapters={50}
        onSelectChapter={handleSelectChapter}
        onPrevChapter={handlePrevChapter}
        onNextChapter={handleNextChapter}
        theme={theme}
        onChangeTheme={setTheme}
        fontSize={fontSize}
        onChangeFontSize={setFontSize}
        onOpenSearch={() => setIsSearchOpen(true)}
        onOpenBookmarks={() => setIsBookmarksOpen(true)}
        onOpenCharacterGuide={() => setIsCharacterGuideOpen(true)}
        onOpenCopyright={() => setIsCopyrightOpen(true)}
        bookmarkCount={bookmarks.length}
        isStoryMode={activeMode === 'story'}
      />

      {/* Main View Router: Bible Reader vs Visual Story Mode */}
      <main className="flex-1">
        {activeMode === 'bible' ? (
          <BibleReader
            chapterData={currentBibleChapter}
            onOpenStoryMode={handleOpenStoryMode}
            onPrevChapter={handlePrevChapter}
            onNextChapter={handleNextChapter}
            fontSizeClass={fontSizeMap[fontSize] || 'text-base'}
            bookmarks={bookmarks}
            onToggleBookmark={handleToggleBookmark}
            targetVerse={targetVerse}
            clearTargetVerse={() => setTargetVerse(null)}
          />
        ) : (
          <VisualStoryReader
            storyData={currentStoryChapter}
            chapterNumber={currentChapter}
            onBackToBible={handleBackToBible}
            onSelectChapter={handleSelectChapter}
            onOpenCharacterGuide={() => setIsCharacterGuideOpen(true)}
            totalChapters={50}
          />
        )}
      </main>

      {/* Modals & Overlays */}
      <SearchModal
        isOpen={isSearchOpen}
        onClose={() => setIsSearchOpen(false)}
        onSelectVerse={handleSelectVerseFromSearchOrBookmark}
      />

      <BookmarksDrawer
        isOpen={isBookmarksOpen}
        onClose={() => setIsBookmarksOpen(false)}
        bookmarks={bookmarks}
        onRemoveBookmark={handleRemoveBookmark}
        onSelectVerse={handleSelectVerseFromSearchOrBookmark}
        currentChapter={currentChapter}
        totalChapters={50}
      />

      <CharacterGuideModal
        isOpen={isCharacterGuideOpen}
        onClose={() => setIsCharacterGuideOpen(false)}
        onSelectChapter={handleSelectChapter}
      />

      <AboutCopyrightModal
        isOpen={isCopyrightOpen}
        onClose={() => setIsCopyrightOpen(false)}
      />
    </div>
  );
}
