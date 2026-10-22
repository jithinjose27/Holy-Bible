import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import BibleReader from './components/BibleReader';
import SearchModal from './components/SearchModal';
import BookmarksDrawer from './components/BookmarksDrawer';
import AboutCopyrightModal from './components/AboutCopyrightModal';
import InstallAppModal from './components/InstallAppModal';
import { CheckCircle2, WifiOff } from 'lucide-react';

import bibleData from './data/genesis_bible_text.json';

export default function App() {
  // Restore last-read chapter from URL or localStorage
  const [currentChapter, setCurrentChapter] = useState(() => {
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const chParam = parseInt(urlParams.get('ch'), 10);
      if (chParam && chParam >= 1 && chParam <= 50) return chParam;
      const saved = localStorage.getItem('holy_bible_last_chapter');
      return saved ? parseInt(saved, 10) : 1;
    } catch {
      return 1;
    }
  });

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
  const [highlights, setHighlights] = useState(() => {
    try {
      const saved = localStorage.getItem('holy_bible_highlights');
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  // Modal states
  const [isSearchOpen, setIsSearchOpen] = useState(() => {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('action') === 'search';
  });
  const [isBookmarksOpen, setIsBookmarksOpen] = useState(() => {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('action') === 'bookmarks';
  });
  const [isCopyrightOpen, setIsCopyrightOpen] = useState(false);
  const [isInstallModalOpen, setIsInstallModalOpen] = useState(false);

  // PWA & Network States
  const [deferredPrompt, setDeferredPrompt] = useState(null);
  const [isInstalled, setIsInstalled] = useState(() => {
    if (typeof window === 'undefined') return false;
    return (
      window.matchMedia('(display-mode: standalone)').matches ||
      window.navigator.standalone === true
    );
  });
  const [isOnline, setIsOnline] = useState(() => {
    return typeof navigator !== 'undefined' ? navigator.onLine : true;
  });
  const [showInstallToast, setShowInstallToast] = useState(false);

  // Sync currentChapter to localStorage
  useEffect(() => {
    localStorage.setItem('holy_bible_last_chapter', String(currentChapter));
  }, [currentChapter]);

  // Sync settings with localStorage
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

  useEffect(() => {
    localStorage.setItem('holy_bible_highlights', JSON.stringify(highlights));
  }, [highlights]);

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

  // Online / Offline Status Listeners
  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  // PWA BeforeInstallPrompt and AppInstalled Event Handlers
  useEffect(() => {
    const handleBeforeInstall = (e) => {
      // Prevent automatic browser mini-infobar on mobile
      e.preventDefault();
      setDeferredPrompt(e);
    };

    const handleAppInstalled = () => {
      setIsInstalled(true);
      setDeferredPrompt(null);
      setShowInstallToast(true);
      const timer = setTimeout(() => setShowInstallToast(false), 5000);
      return () => clearTimeout(timer);
    };

    window.addEventListener('beforeinstallprompt', handleBeforeInstall);
    window.addEventListener('appinstalled', handleAppInstalled);

    return () => {
      window.removeEventListener('beforeinstallprompt', handleBeforeInstall);
      window.removeEventListener('appinstalled', handleAppInstalled);
    };
  }, []);

  // Chapter data retrieval
  const currentBibleChapter = bibleData.chapters.find((c) => c.chapter === currentChapter) || bibleData.chapters[0];

  // Navigation Handlers
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

  const handleSetHighlight = (verseKey, color) => {
    setHighlights((prev) => {
      const updated = { ...prev };
      if (!color) {
        delete updated[verseKey];
      } else {
        updated[verseKey] = color;
      }
      return updated;
    });
  };

  const handleSelectVerseFromSearchOrBookmark = (ch, verseNum) => {
    setCurrentChapter(ch);
    setTargetVerse(verseNum);
  };

  // Font size classes
  const fontSizeMap = {
    small: 'text-sm sm:text-base',
    medium: 'text-base sm:text-lg',
    large: 'text-lg sm:text-xl',
    xlarge: 'text-xl sm:text-2xl'
  };

  return (
    <div className={`min-h-screen theme-${theme} transition-colors duration-200 flex flex-col pt-safe pb-safe pl-safe pr-safe`}>
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
        onOpenCopyright={() => setIsCopyrightOpen(true)}
        onOpenInstall={() => setIsInstallModalOpen(true)}
        isInstalled={isInstalled}
        isOnline={isOnline}
        bookmarkCount={bookmarks.length}
      />

      {/* Main View: Dedicated Bible Reader */}
      <main className="flex-1">
        <BibleReader
          chapterData={currentBibleChapter}
          onPrevChapter={handlePrevChapter}
          onNextChapter={handleNextChapter}
          fontSizeClass={fontSizeMap[fontSize] || 'text-base'}
          bookmarks={bookmarks}
          onToggleBookmark={handleToggleBookmark}
          targetVerse={targetVerse}
          clearTargetVerse={() => setTargetVerse(null)}
          highlights={highlights}
          onSetHighlight={handleSetHighlight}
        />
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

      <AboutCopyrightModal
        isOpen={isCopyrightOpen}
        onClose={() => setIsCopyrightOpen(false)}
      />

      <InstallAppModal
        isOpen={isInstallModalOpen}
        onClose={() => setIsInstallModalOpen(false)}
        deferredPrompt={deferredPrompt}
        isInstalled={isInstalled}
        onInstallSuccess={() => {
          setIsInstalled(true);
          setShowInstallToast(true);
        }}
      />

      {/* Success Toast when App is Installed */}
      {showInstallToast && (
        <div className="fixed bottom-6 right-6 z-50 p-4 rounded-xl bg-emerald-800 text-white shadow-2xl flex items-center gap-3 animate-fade-in border border-emerald-600">
          <CheckCircle2 className="w-5 h-5 text-emerald-300 shrink-0" />
          <div className="text-xs sm:text-sm">
            <strong className="block font-semibold">Holy Bible Installed!</strong>
            You can now launch the app anytime from your home screen or desktop.
          </div>
        </div>
      )}
    </div>
  );
}
