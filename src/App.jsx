import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import BibleReader from './components/BibleReader';
import SearchModal from './components/SearchModal';
import BookmarksDrawer from './components/BookmarksDrawer';
import AboutCopyrightModal from './components/AboutCopyrightModal';
import InstallAppModal from './components/InstallAppModal';
import BookReviewModal from './components/BookReviewModal';
import { CheckCircle2, WifiOff } from 'lucide-react';

import { 
  getBookMeta, 
  getAllBooks, 
  getAdjacentBooks, 
  loadBookText, 
  loadBookKjv, 
  loadBookChapterQA 
} from './services/bibleService';

export default function App() {
  // Determine initial book from URL (?book=GEN) or localStorage
  const [currentBookId, setCurrentBookId] = useState(() => {
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const bookParam = urlParams.get('book');
      if (bookParam) {
        const meta = getBookMeta(bookParam);
        if (meta) return meta.id;
      }
      const savedBook = localStorage.getItem('holy_bible_current_book');
      if (savedBook) {
        const meta = getBookMeta(savedBook);
        if (meta) return meta.id;
      }
    } catch {}
    return 'GEN';
  });

  const currentBookMeta = getBookMeta(currentBookId) || {
    id: 'GEN',
    name: 'Genesis',
    slug: 'genesis',
    chapters: 50
  };

  // Determine initial chapter from URL (?ch=1) or localStorage
  const [currentChapter, setCurrentChapter] = useState(() => {
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const chParam = parseInt(urlParams.get('ch'), 10);
      const meta = getBookMeta(urlParams.get('book') || localStorage.getItem('holy_bible_current_book') || 'GEN');
      const maxCh = meta ? meta.chapters : 50;
      if (chParam && chParam >= 1 && chParam <= maxCh) return chParam;
      const saved = localStorage.getItem('holy_bible_last_chapter');
      const savedInt = saved ? parseInt(saved, 10) : 1;
      return savedInt <= maxCh ? savedInt : 1;
    } catch {
      return 1;
    }
  });

  const [targetVerse, setTargetVerse] = useState(null);

  // Dynamic loaded book data state
  const [bookText, setBookText] = useState(null);
  const [kjvBookData, setKjvBookData] = useState(null);
  const [chapterQaData, setChapterQaData] = useState(null);
  const [isLoadingBook, setIsLoadingBook] = useState(true);

  // Persistent settings in localStorage (with query param override support)
  const [theme, setTheme] = useState(() => {
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const themeParam = urlParams.get('theme');
      if (themeParam && ['paper', 'sepia', 'dark', 'midnight'].includes(themeParam)) {
        return themeParam;
      }
    } catch {}
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
  const [isBookReviewOpen, setIsBookReviewOpen] = useState(() => {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('action') === 'review';
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

  // Load Book Content when currentBookId changes
  useEffect(() => {
    let isMounted = true;

    async function loadData() {
      setIsLoadingBook(true);
      try {
        const [textData, kjvData, qaData] = await Promise.all([
          loadBookText(currentBookId),
          loadBookKjv(currentBookId),
          loadBookChapterQA(currentBookId)
        ]);

        if (isMounted) {
          setBookText(textData);
          setKjvBookData(kjvData);
          setChapterQaData(qaData);
        }
      } catch (err) {
        console.error('Error loading book assets:', err);
      } finally {
        if (isMounted) {
          setIsLoadingBook(false);
        }
      }
    }

    loadData();

    return () => {
      isMounted = false;
    };
  }, [currentBookId]);

  // Sync currentBookId and currentChapter to localStorage and URL params
  useEffect(() => {
    localStorage.setItem('holy_bible_current_book', currentBookId);
    localStorage.setItem('holy_bible_last_chapter', String(currentChapter));

    try {
      const url = new URL(window.location.href);
      url.searchParams.set('book', currentBookId);
      url.searchParams.set('ch', String(currentChapter));
      window.history.replaceState({}, '', url.toString());
    } catch {}
  }, [currentBookId, currentChapter]);

  // Sync settings with localStorage and document styling
  useEffect(() => {
    localStorage.setItem('holy_bible_theme', theme);
    const isDark = theme === 'dark' || theme === 'midnight';
    document.documentElement.className = isDark ? 'dark' : '';
    const themeBg = {
      paper: '#fbf9f5',
      sepia: '#f4ecd8',
      dark: '#1c1917',
      midnight: '#0b0f19',
    }[theme] || '#fbf9f5';
    const themeColor = {
      paper: '#1c1917',
      sepia: '#291e10',
      dark: '#f5f5f4',
      midnight: '#f8fafc',
    }[theme] || '#1c1917';
    document.documentElement.style.backgroundColor = themeBg;
    document.body.style.backgroundColor = themeBg;
    document.body.style.color = themeColor;
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

  // Handle scroll position deep linking (e.g. ?scrollY=800)
  useEffect(() => {
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const scrollYParam = urlParams.get('scrollY');
      if (scrollYParam) {
        const offset = parseInt(scrollYParam, 10);
        if (!isNaN(offset)) {
          window.scrollTo({ top: offset, behavior: 'instant' });
        }
      }
    } catch {}
  }, [currentBookId, currentChapter]);

  // Current Chapter Data retrieval
  const currentBibleChapter = bookText?.chapters?.find((c) => c.chapter === currentChapter) || 
    bookText?.chapters?.[0] || 
    null;

  // Current Chapter QA retrieval
  const currentChapterQA = chapterQaData?.chapters?.[String(currentChapter)] || null;

  // Adjacent Books
  const adjacentBooks = getAdjacentBooks(currentBookId);

  // Navigation Handlers
  const handleSelectBook = (newBookId) => {
    const meta = getBookMeta(newBookId);
    if (meta) {
      setCurrentBookId(meta.id);
      setCurrentChapter(1);
      setTargetVerse(null);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const handleSelectChapter = (ch) => {
    const maxCh = currentBookMeta.chapters || 50;
    if (ch >= 1 && ch <= maxCh) {
      setCurrentChapter(ch);
      setTargetVerse(null);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const handlePrevChapter = () => {
    if (currentChapter > 1) {
      handleSelectChapter(currentChapter - 1);
    } else if (adjacentBooks.prev) {
      handleSelectBook(adjacentBooks.prev.id);
    }
  };

  const handleNextChapter = () => {
    const maxCh = currentBookMeta.chapters || 50;
    if (currentChapter < maxCh) {
      handleSelectChapter(currentChapter + 1);
    } else if (adjacentBooks.next) {
      handleSelectBook(adjacentBooks.next.id);
    }
  };

  const handleNextBook = () => {
    if (adjacentBooks.next) {
      handleSelectBook(adjacentBooks.next.id);
    }
  };

  const handleToggleBookmark = (ch, verseNum, text) => {
    setBookmarks((prev) => {
      const exists = prev.some((b) => (b.bookId || 'GEN') === currentBookId && b.chapter === ch && b.verse === verseNum);
      if (exists) {
        return prev.filter((b) => !((b.bookId || 'GEN') === currentBookId && b.chapter === ch && b.verse === verseNum));
      } else {
        return [
          ...prev, 
          { 
            bookId: currentBookId, 
            bookName: currentBookMeta.name, 
            chapter: ch, 
            verse: verseNum, 
            text, 
            date: new Date().toISOString() 
          }
        ];
      }
    });
  };

  const handleRemoveBookmark = (ch, verseNum, bId) => {
    const targetBookId = bId || currentBookId;
    setBookmarks((prev) => prev.filter((b) => !((b.bookId || 'GEN') === targetBookId && b.chapter === ch && b.verse === verseNum)));
  };

  const handleSetHighlight = (verseKey, color) => {
    const scopedKey = `${currentBookId}-${verseKey}`;
    setHighlights((prev) => {
      const updated = { ...prev };
      if (!color) {
        delete updated[scopedKey];
      } else {
        updated[scopedKey] = color;
      }
      return updated;
    });
  };

  const handleSelectVerseFromSearchOrBookmark = (ch, verseNum, bId) => {
    if (bId && bId !== currentBookId) {
      setCurrentBookId(bId);
    }
    setCurrentChapter(ch);
    setTargetVerse(verseNum);
  };

  // Font size classes
  const fontSizeMap = {
    small: 'text-[15px] sm:text-[16px] leading-[1.75]',
    medium: 'text-[17px] sm:text-[18px] md:text-[19px] leading-[1.8] sm:leading-[1.85]',
    large: 'text-[19px] sm:text-[21px] leading-[1.85] sm:leading-[1.9]',
    xlarge: 'text-[22px] sm:text-[24px] leading-[1.9]'
  };

  return (
    <div className={`min-h-screen theme-${theme} ${theme === 'dark' || theme === 'midnight' ? 'dark' : ''} transition-colors duration-200 flex flex-col pt-safe pb-safe pl-safe pr-safe touch-pan-y`}>
      {/* Top Navbar */}
      <Navbar
        currentBookId={currentBookId}
        currentBook={currentBookMeta.name}
        currentChapter={currentChapter}
        totalChapters={currentBookMeta.chapters}
        onSelectBook={handleSelectBook}
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
        onOpenBookReview={() => setIsBookReviewOpen(true)}
        isInstalled={isInstalled}
        isOnline={isOnline}
        bookmarkCount={bookmarks.length}
      />

      {/* Main View: Dedicated Bible Reader */}
      <main className="flex-1 w-full touch-pan-y">
        {isLoadingBook ? (
          <div className="py-24 text-center text-stone-500 font-sans">
            <div className="w-8 h-8 mx-auto mb-3 border-2 border-amber-700 border-t-transparent rounded-full animate-spin" />
            Loading {currentBookMeta.name}...
          </div>
        ) : (
          <BibleReader
            chapterData={currentBibleChapter}
            bookMeta={currentBookMeta}
            kjvBookData={kjvBookData}
            chapterQA={currentChapterQA}
            onPrevChapter={handlePrevChapter}
            onNextChapter={handleNextChapter}
            onOpenBookReview={() => setIsBookReviewOpen(true)}
            onNextBook={adjacentBooks.next ? handleNextBook : null}
            nextBookMeta={adjacentBooks.next}
            fontSizeClass={fontSizeMap[fontSize] || 'text-base'}
            bookmarks={bookmarks}
            onToggleBookmark={handleToggleBookmark}
            targetVerse={targetVerse}
            clearTargetVerse={() => setTargetVerse(null)}
            highlights={highlights}
            onSetHighlight={handleSetHighlight}
          />
        )}
      </main>

      {/* 50-Question Comprehensive Book Review Assessment Modal */}
      <BookReviewModal
        isOpen={isBookReviewOpen}
        onClose={() => setIsBookReviewOpen(false)}
        bookId={currentBookId}
        bookName={currentBookMeta.name}
      />

      {/* Modals & Overlays */}
      <SearchModal
        isOpen={isSearchOpen}
        onClose={() => setIsSearchOpen(false)}
        onSelectVerse={handleSelectVerseFromSearchOrBookmark}
        currentBookText={bookText}
        bookName={currentBookMeta.name}
        bookId={currentBookId}
      />

      <BookmarksDrawer
        isOpen={isBookmarksOpen}
        onClose={() => setIsBookmarksOpen(false)}
        bookmarks={bookmarks}
        onRemoveBookmark={handleRemoveBookmark}
        onSelectVerse={handleSelectVerseFromSearchOrBookmark}
        currentChapter={currentChapter}
        totalChapters={currentBookMeta.chapters}
        bookName={currentBookMeta.name}
        bookId={currentBookId}
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
