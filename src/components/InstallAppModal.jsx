import React, { useState, useEffect } from 'react';
import { 
  X, 
  Download, 
  Smartphone, 
  Monitor, 
  CheckCircle2, 
  Share2, 
  PlusSquare, 
  Wifi, 
  WifiOff, 
  ShieldCheck, 
  Zap,
  BookOpen
} from 'lucide-react';

export default function InstallAppModal({
  isOpen,
  onClose,
  deferredPrompt,
  onInstallSuccess,
  isInstalled
}) {
  const [platform, setPlatform] = useState('unknown'); // 'ios' | 'android' | 'windows' | 'mac' | 'linux' | 'desktop'
  const [isInstalling, setIsInstalling] = useState(false);

  useEffect(() => {
    const userAgent = window.navigator.userAgent.toLowerCase();
    const isIOSDevice = /iphone|ipad|ipod/.test(userAgent) || 
      (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    const isAndroidDevice = /android/.test(userAgent);
    const isWindowsDevice = /windows/.test(userAgent);
    const isMacDevice = /macintosh|mac os x/.test(userAgent) && !isIOSDevice;
    const isLinuxDevice = /linux/.test(userAgent) && !isAndroidDevice;

    if (isIOSDevice) {
      setPlatform('ios');
    } else if (isAndroidDevice) {
      setPlatform('android');
    } else if (isWindowsDevice) {
      setPlatform('windows');
    } else if (isMacDevice) {
      setPlatform('mac');
    } else if (isLinuxDevice) {
      setPlatform('linux');
    } else {
      setPlatform('desktop');
    }
  }, []);

  if (!isOpen) return null;

  const handleNativeInstall = async () => {
    if (!deferredPrompt) return;
    setIsInstalling(true);
    try {
      await deferredPrompt.prompt();
      const choiceResult = await deferredPrompt.userChoice;
      if (choiceResult.outcome === 'accepted') {
        if (onInstallSuccess) onInstallSuccess();
        onClose();
      }
    } catch (err) {
      console.warn('[PWA] Installation prompt error:', err);
    } finally {
      setIsInstalling(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fade-in">
      <div 
        className="relative w-full max-w-lg max-h-[90vh] overflow-y-auto bg-stone-50 dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-2xl shadow-2xl p-6 sm:p-7 text-stone-800 dark:text-stone-200"
        role="dialog"
        aria-modal="true"
        aria-labelledby="install-modal-title"
      >
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-2 rounded-full text-stone-400 hover:text-stone-700 dark:hover:text-stone-200 hover:bg-stone-200/60 dark:hover:bg-stone-800 transition"
          aria-label="Close installation dialog"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Modal Header */}
        <div className="flex items-center gap-3.5 mb-5">
          <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-amber-700 to-amber-950 flex items-center justify-center text-amber-100 shadow-md shrink-0 border border-amber-600/30">
            <BookOpen className="w-6 h-6" />
          </div>
          <div>
            <h2 id="install-modal-title" className="text-xl font-cinzel font-bold text-stone-900 dark:text-stone-100">
              Install The Holy Bible
            </h2>
            <p className="text-xs text-stone-500 dark:text-stone-400">
              Cross-Platform Progressive Web App (PWA)
            </p>
          </div>
        </div>

        {/* If already installed */}
        {isInstalled ? (
          <div className="p-4 bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-300 dark:border-emerald-800 rounded-xl mb-5 flex items-start gap-3">
            <CheckCircle2 className="w-5 h-5 text-emerald-600 dark:text-emerald-400 shrink-0 mt-0.5" />
            <div className="text-xs sm:text-sm text-emerald-950 dark:text-emerald-200">
              <strong className="block font-semibold mb-0.5">App is already installed!</strong>
              You are running the Holy Bible in standalone mode. All 50 chapters and 500 review questions are saved locally on your device for offline reading.
            </div>
          </div>
        ) : (
          <>
            {/* Native Install Prompt Available (Android / Chrome / Edge / Windows / Linux) */}
            {deferredPrompt ? (
              <div className="mb-6 p-4 bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-900/40 rounded-xl text-center space-y-3">
                <p className="text-xs sm:text-sm text-stone-700 dark:text-stone-300">
                  Click below to install the Holy Bible directly to your device home screen or application launcher.
                </p>
                <button
                  onClick={handleNativeInstall}
                  disabled={isInstalling}
                  className="w-full inline-flex items-center justify-center gap-2 py-3 px-5 rounded-xl bg-gradient-to-r from-amber-700 to-amber-900 hover:from-amber-800 hover:to-amber-950 text-white font-semibold text-sm shadow-md hover:shadow-lg transition cursor-pointer"
                >
                  <Download className="w-4 h-4" />
                  <span>{isInstalling ? 'Installing...' : 'Install Holy Bible Now'}</span>
                </button>
              </div>
            ) : platform === 'ios' ? (
              /* iOS Safari Step-by-Step Instructions */
              <div className="mb-6 p-4 sm:p-5 bg-amber-50/80 dark:bg-amber-950/20 border border-amber-200/80 dark:border-amber-900/40 rounded-xl space-y-3">
                <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-amber-800 dark:text-amber-400">
                  <Smartphone className="w-4 h-4" /> iOS (iPhone & iPad) Setup
                </div>
                <p className="text-xs sm:text-sm text-stone-700 dark:text-stone-300">
                  Safari on iOS does not support one-click web prompts. Follow these 3 simple steps to install:
                </p>
                <ol className="space-y-2 text-xs sm:text-sm text-stone-800 dark:text-stone-200 pt-1">
                  <li className="flex items-center gap-2.5">
                    <span className="w-5 h-5 rounded-full bg-amber-700 text-white text-[11px] font-bold flex items-center justify-center shrink-0">1</span>
                    <span>Tap the <strong>Share</strong> button <Share2 className="w-3.5 h-3.5 inline text-amber-700 dark:text-amber-400" /> at the bottom of Safari.</span>
                  </li>
                  <li className="flex items-center gap-2.5">
                    <span className="w-5 h-5 rounded-full bg-amber-700 text-white text-[11px] font-bold flex items-center justify-center shrink-0">2</span>
                    <span>Scroll down and select <strong>"Add to Home Screen"</strong> <PlusSquare className="w-3.5 h-3.5 inline text-amber-700 dark:text-amber-400" />.</span>
                  </li>
                  <li className="flex items-center gap-2.5">
                    <span className="w-5 h-5 rounded-full bg-amber-700 text-white text-[11px] font-bold flex items-center justify-center shrink-0">3</span>
                    <span>Tap <strong>Add</strong> in the top-right corner. The Holy Bible icon will appear on your home screen!</span>
                  </li>
                </ol>
              </div>
            ) : (
              /* Desktop (Chrome / Edge / Firefox / Linux / Windows manual) */
              <div className="mb-6 p-4 bg-stone-100 dark:bg-stone-800/60 border border-stone-200 dark:border-stone-700 rounded-xl space-y-2 text-xs sm:text-sm">
                <div className="font-semibold text-stone-900 dark:text-stone-100 flex items-center gap-2">
                  <Monitor className="w-4 h-4 text-amber-600" />
                  Desktop Installation Instructions
                </div>
                <p className="text-stone-600 dark:text-stone-400">
                  To install in <strong>Chrome, Edge, or Brave</strong>: Click the <strong>Install</strong> icon <Download className="w-3.5 h-3.5 inline text-amber-600" /> on the right side of your browser's address bar.
                </p>
                <p className="text-stone-600 dark:text-stone-400">
                  To use in <strong>Firefox or other browsers</strong>: Bookmark this page (<kbd className="px-1 py-0.5 rounded bg-stone-200 dark:bg-stone-700 font-mono text-[10px]">Ctrl+D</kbd> or <kbd className="px-1 py-0.5 rounded bg-stone-200 dark:bg-stone-700 font-mono text-[10px]">⌘+D</kbd>) for instant access anytime.
                </p>
              </div>
            )}
          </>
        )}

        {/* Benefits List */}
        <div className="border-t border-stone-200 dark:border-stone-800 pt-4 space-y-2.5">
          <div className="text-xs font-bold uppercase tracking-wider text-stone-400 dark:text-stone-500 mb-1">
            Why Install the App?
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-stone-600 dark:text-stone-300">
            <div className="flex items-start gap-2">
              <WifiOff className="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0 mt-0.5" />
              <span><strong>100% Offline</strong>: All 50 chapters & 500 quiz questions work without internet.</span>
            </div>
            <div className="flex items-start gap-2">
              <Zap className="w-4 h-4 text-amber-600 dark:text-amber-400 shrink-0 mt-0.5" />
              <span><strong>Instant Launch</strong>: Opens in a clean standalone window without browser clutter.</span>
            </div>
            <div className="flex items-start gap-2">
              <ShieldCheck className="w-4 h-4 text-blue-600 dark:text-blue-400 shrink-0 mt-0.5" />
              <span><strong>Local Privacy</strong>: Bookmarks, highlights, and quiz scores stay on your device.</span>
            </div>
            <div className="flex items-start gap-2">
              <Smartphone className="w-4 h-4 text-purple-600 dark:text-purple-400 shrink-0 mt-0.5" />
              <span><strong>Multi-Device</strong>: Runs smoothly on Android, iPhone, iPad, Windows, and Linux.</span>
            </div>
          </div>
        </div>

        {/* Close Button */}
        <div className="mt-6 pt-4 border-t border-stone-200 dark:border-stone-800 text-right">
          <button
            onClick={onClose}
            className="px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-stone-200/80 dark:bg-stone-800 hover:bg-stone-300 dark:hover:bg-stone-700 text-stone-800 dark:text-stone-200 transition cursor-pointer"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}
