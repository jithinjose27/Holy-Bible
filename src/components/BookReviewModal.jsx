import React, { useState, useEffect } from 'react';
import { 
  X, 
  Award, 
  CheckCircle2, 
  XCircle, 
  RotateCcw, 
  Eye, 
  EyeOff, 
  BookOpen, 
  ChevronRight, 
  ChevronLeft, 
  Trophy, 
  Layers, 
  Sparkles,
  HelpCircle,
  Check
} from 'lucide-react';
import { loadBookReviewQA } from '../services/bibleService';

export default function BookReviewModal({
  isOpen,
  onClose,
  bookId = 'GEN',
  bookName = 'Genesis'
}) {
  const [activeTab, setActiveTab] = useState('practice'); // 'practice' | 'study'
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);

  // Practice Mode State
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [score, setScore] = useState(0);
  const [userAnswers, setUserAnswers] = useState([]); // array of { index, selected, isCorrect }
  const [quizFinished, setQuizFinished] = useState(false);
  const [bestScore, setBestScore] = useState(null);

  // Study Mode State
  const [expandedAnswers, setExpandedAnswers] = useState({});

  // Load questions whenever bookId changes or modal opens
  useEffect(() => {
    if (!isOpen || !bookId) return;

    let isMounted = true;
    setLoading(true);

    loadBookReviewQA(bookId).then((data) => {
      if (!isMounted) return;
      if (data && data.questions && data.questions.length > 0) {
        setQuestions(data.questions);
      } else {
        setQuestions([]);
      }
      setLoading(false);
      resetQuiz();
      loadSavedScore();
    });

    return () => {
      isMounted = false;
    };
  }, [isOpen, bookId]);

  const loadSavedScore = () => {
    try {
      const saved = JSON.parse(localStorage.getItem('holy_bible_book_scores') || '{}');
      setBestScore(saved[bookId] || null);
    } catch {
      setBestScore(null);
    }
  };

  const saveBookScore = (finalScore, total) => {
    try {
      const saved = JSON.parse(localStorage.getItem('holy_bible_book_scores') || '{}');
      const prev = saved[bookId];
      if (!prev || finalScore >= prev.score) {
        const record = {
          score: finalScore,
          total: total,
          percentage: Math.round((finalScore / total) * 100),
          updatedAt: new Date().toISOString()
        };
        saved[bookId] = record;
        localStorage.setItem('holy_bible_book_scores', JSON.stringify(saved));
        setBestScore(record);
      }
    } catch (e) {
      console.error('Error saving book review score:', e);
    }
  };

  const resetQuiz = () => {
    setCurrentIndex(0);
    setSelectedOption(null);
    setIsAnswered(false);
    setScore(0);
    setUserAnswers([]);
    setQuizFinished(false);
  };

  if (!isOpen) return null;

  const currentQ = questions[currentIndex];
  const totalQuestions = questions.length;
  const progressPercent = totalQuestions > 0 ? Math.round(((currentIndex + (isAnswered ? 1 : 0)) / totalQuestions) * 100) : 0;

  const handleSelectOption = (idx) => {
    if (isAnswered || !currentQ) return;
    setSelectedOption(idx);
    setIsAnswered(true);

    const isCorrect = idx === currentQ.correctAnswerIndex;
    if (isCorrect) {
      setScore((prev) => prev + 1);
    }

    setUserAnswers((prev) => [
      ...prev,
      {
        questionIndex: currentIndex,
        question: currentQ.question,
        selectedOption: idx,
        correctIndex: currentQ.correctAnswerIndex,
        isCorrect
      }
    ]);
  };

  const handleNext = () => {
    if (currentIndex < totalQuestions - 1) {
      setCurrentIndex((prev) => prev + 1);
      setSelectedOption(null);
      setIsAnswered(false);
    } else {
      setQuizFinished(true);
      saveBookScore(score, totalQuestions);
    }
  };

  const toggleStudyAnswer = (qId) => {
    setExpandedAnswers((prev) => ({
      ...prev,
      [qId]: !prev[qId]
    }));
  };

  const toggleAllStudyAnswers = () => {
    const allExpanded = questions.every((q) => expandedAnswers[q.id]);
    const newState = {};
    if (!allExpanded) {
      questions.forEach((q) => {
        newState[q.id] = true;
      });
    }
    setExpandedAnswers(newState);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/70 backdrop-blur-sm animate-fade-in">
      <div 
        className="relative w-full max-w-4xl max-h-[90vh] flex flex-col bg-stone-50 dark:bg-stone-900 border border-stone-200 dark:border-stone-800 rounded-2xl shadow-2xl overflow-hidden text-stone-900 dark:text-stone-100"
        role="dialog"
        aria-modal="true"
      >
        {/* Header */}
        <div className="p-4 sm:p-5 border-b border-stone-200 dark:border-stone-800 bg-white dark:bg-stone-900 flex items-center justify-between gap-3 shrink-0">
          <div className="flex items-center gap-2.5 min-w-0">
            <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-amber-700 to-amber-900 flex items-center justify-center text-amber-100 shadow-sm shrink-0">
              <Trophy className="w-5 h-5" />
            </div>
            <div className="min-w-0">
              <div className="flex items-center gap-2">
                <h2 className="font-cinzel font-bold text-base sm:text-lg truncate">
                  The Book of {bookName} — Comprehensive Review
                </h2>
                <span className="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 bg-amber-100 dark:bg-amber-950/70 text-amber-800 dark:text-amber-400 rounded-full shrink-0">
                  50 Questions
                </span>
              </div>
              <p className="text-xs text-stone-500 dark:text-stone-400 truncate">
                Mastery assessment covering all major chapters, themes, covenants, and events
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 rounded-xl text-stone-400 hover:text-stone-700 dark:hover:text-stone-200 hover:bg-stone-100 dark:hover:bg-stone-800 transition cursor-pointer shrink-0"
            aria-label="Close Assessment"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Tab Controls: Practice Mode vs Study Mode */}
        <div className="px-4 sm:px-6 pt-3 pb-2 border-b border-stone-200/80 dark:border-stone-800 flex items-center justify-between bg-stone-100/50 dark:bg-stone-950/30 shrink-0">
          <div className="flex items-center gap-2">
            <button
              onClick={() => setActiveTab('practice')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
                activeTab === 'practice'
                  ? 'bg-amber-700 text-white shadow-xs'
                  : 'text-stone-600 dark:text-stone-400 hover:bg-stone-200/60 dark:hover:bg-stone-800'
              }`}
            >
              <Award className="w-3.5 h-3.5" />
              <span>Practice Mode</span>
            </button>

            <button
              onClick={() => setActiveTab('study')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
                activeTab === 'study'
                  ? 'bg-amber-700 text-white shadow-xs'
                  : 'text-stone-600 dark:text-stone-400 hover:bg-stone-200/60 dark:hover:bg-stone-800'
              }`}
            >
              <Layers className="w-3.5 h-3.5" />
              <span>Study Mode (All 50)</span>
            </button>
          </div>

          {bestScore && (
            <div className="text-xs font-semibold text-amber-800 dark:text-amber-400 flex items-center gap-1">
              <Trophy className="w-3.5 h-3.5" />
              <span>Best: {bestScore.score}/{bestScore.total} ({bestScore.percentage}%)</span>
            </div>
          )}
        </div>

        {/* Main Content Area */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 touch-pan-y">
          {loading ? (
            <div className="py-20 text-center text-stone-500 font-sans">
              <div className="w-8 h-8 mx-auto mb-3 border-2 border-amber-700 border-t-transparent rounded-full animate-spin" />
              Loading 50 Comprehensive Questions for {bookName}...
            </div>
          ) : questions.length === 0 ? (
            <div className="py-20 text-center text-stone-500 font-sans">
              No review questions currently found for {bookName}.
            </div>
          ) : activeTab === 'practice' ? (
            /* =========================================
               PRACTICE MODE
               ========================================= */
            quizFinished ? (
              <div className="max-w-xl mx-auto py-6 sm:py-8 text-center space-y-6">
                <div className="w-20 h-20 mx-auto rounded-2xl bg-amber-100 dark:bg-amber-950/60 text-amber-800 dark:text-amber-400 flex items-center justify-center shadow-lg border border-amber-200 dark:border-amber-900">
                  <Trophy className="w-10 h-10" />
                </div>

                <div>
                  <h3 className="text-2xl sm:text-3xl font-cinzel font-bold text-stone-900 dark:text-stone-100">
                    Assessment Complete!
                  </h3>
                  <p className="mt-1 text-sm text-stone-600 dark:text-stone-400">
                    You have finished all 50 questions for the Book of {bookName}.
                  </p>
                </div>

                {/* Score Banner */}
                <div className="p-6 rounded-2xl bg-amber-50 dark:bg-stone-900 border border-amber-200 dark:border-stone-800 text-center">
                  <div className="text-4xl sm:text-5xl font-black text-amber-800 dark:text-amber-400 font-cinzel">
                    {score} <span className="text-2xl text-stone-400 font-sans">/ {totalQuestions}</span>
                  </div>
                  <div className="mt-2 text-sm font-bold uppercase tracking-wider text-stone-700 dark:text-stone-300">
                    Score: {Math.round((score / totalQuestions) * 100)}%
                  </div>
                  <p className="mt-2 text-xs text-stone-500">
                    {score >= 45 
                      ? '🌟 Outstanding! Biblical Scholar level mastery.' 
                      : score >= 38 
                      ? '✨ Great job! Excellent knowledge of this book.' 
                      : score >= 30 
                      ? '📖 Good effort! Review the study mode to deepen your grasp.' 
                      : '🌱 Keep studying! Re-read the chapters and try again.'}
                  </p>
                </div>

                <div className="flex flex-wrap items-center justify-center gap-3 pt-2">
                  <button
                    onClick={resetQuiz}
                    className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold bg-amber-700 hover:bg-amber-800 text-white shadow-sm transition cursor-pointer"
                  >
                    <RotateCcw className="w-4 h-4" />
                    <span>Retake Assessment</span>
                  </button>
                  <button
                    onClick={() => setActiveTab('study')}
                    className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold bg-stone-200/80 dark:bg-stone-800 hover:bg-stone-300 dark:hover:bg-stone-700 text-stone-800 dark:text-stone-200 transition cursor-pointer"
                  >
                    <BookOpen className="w-4 h-4" />
                    <span>Review All Answers</span>
                  </button>
                </div>
              </div>
            ) : (
              <div className="max-w-2xl mx-auto space-y-5">
                {/* Progress Bar & Header */}
                <div className="space-y-1.5">
                  <div className="flex items-center justify-between text-xs font-bold text-stone-600 dark:text-stone-400">
                    <span>Question {currentIndex + 1} of {totalQuestions}</span>
                    <span className="text-amber-800 dark:text-amber-400">{progressPercent}% Completed</span>
                  </div>
                  <div className="w-full h-2 bg-stone-200 dark:bg-stone-800 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-amber-700 rounded-full transition-all duration-300" 
                      style={{ width: `${((currentIndex + (isAnswered ? 1 : 0)) / totalQuestions) * 100}%` }}
                    />
                  </div>
                </div>

                {/* Question Card */}
                <div className="p-5 sm:p-6 rounded-2xl bg-white dark:bg-stone-900 border border-stone-200 dark:border-stone-800 shadow-sm space-y-4">
                  <div className="flex items-start gap-2.5">
                    <span className="text-xs font-bold px-2 py-1 rounded bg-amber-100 dark:bg-amber-950/70 text-amber-800 dark:text-amber-400 shrink-0">
                      Q{currentIndex + 1}
                    </span>
                    <h3 className="font-cinzel font-bold text-base sm:text-lg text-stone-900 dark:text-stone-100 leading-snug">
                      {currentQ.question}
                    </h3>
                  </div>

                  {/* Options */}
                  <div className="space-y-2 pt-2">
                    {currentQ.options.map((opt, oIdx) => {
                      let btnStyle = "border-stone-200 dark:border-stone-800 hover:border-amber-500 bg-stone-50/60 dark:bg-stone-950/40 text-stone-800 dark:text-stone-200";

                      if (isAnswered) {
                        if (oIdx === currentQ.correctAnswerIndex) {
                          btnStyle = "border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-900 dark:text-emerald-200 font-semibold";
                        } else if (oIdx === selectedOption) {
                          btnStyle = "border-rose-500 bg-rose-50 dark:bg-rose-950/40 text-rose-900 dark:text-rose-200";
                        } else {
                          btnStyle = "border-stone-200 dark:border-stone-800 opacity-50 bg-transparent text-stone-500";
                        }
                      }

                      return (
                        <button
                          key={oIdx}
                          onClick={() => handleSelectOption(oIdx)}
                          disabled={isAnswered}
                          className={`w-full text-left p-3.5 rounded-xl border text-xs sm:text-sm flex items-center justify-between gap-3 transition cursor-pointer ${btnStyle}`}
                        >
                          <div className="flex items-center gap-3">
                            <span className="w-6 h-6 rounded-lg bg-stone-200/70 dark:bg-stone-800 flex items-center justify-center text-xs font-bold text-stone-700 dark:text-stone-300 shrink-0">
                              {String.fromCharCode(65 + oIdx)}
                            </span>
                            <span>{opt}</span>
                          </div>

                          {isAnswered && (
                            <div>
                              {oIdx === currentQ.correctAnswerIndex && (
                                <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0" />
                              )}
                              {oIdx === selectedOption && oIdx !== currentQ.correctAnswerIndex && (
                                <XCircle className="w-5 h-5 text-rose-600 shrink-0" />
                              )}
                            </div>
                          )}
                        </button>
                      );
                    })}
                  </div>

                  {/* Immediate Explanation Card */}
                  {isAnswered && (
                    <div className="mt-4 p-4 rounded-xl bg-amber-50/70 dark:bg-amber-950/20 border border-amber-200 dark:border-amber-900/60 text-xs sm:text-sm animate-fade-in space-y-2">
                      <div className="flex items-center justify-between">
                        <span className="font-bold text-amber-900 dark:text-amber-300 flex items-center gap-1.5">
                          <BookOpen className="w-4 h-4 text-amber-700 dark:text-amber-400" />
                          Biblical Context & Reference
                        </span>
                        <span className="font-semibold text-xs text-stone-500">
                          {currentQ.reference}
                        </span>
                      </div>
                      <p className="text-stone-700 dark:text-stone-300 font-serif leading-relaxed">
                        {currentQ.explanation}
                      </p>
                    </div>
                  )}

                  {/* Navigation controls */}
                  <div className="pt-3 border-t border-stone-200 dark:border-stone-800 flex items-center justify-between">
                    <button
                      onClick={() => {
                        if (currentIndex > 0) {
                          setCurrentIndex(prev => prev - 1);
                          setSelectedOption(null);
                          setIsAnswered(false);
                        }
                      }}
                      disabled={currentIndex === 0}
                      className="inline-flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-semibold text-stone-600 dark:text-stone-400 hover:bg-stone-200/60 dark:hover:bg-stone-800 disabled:opacity-30 disabled:pointer-events-none transition cursor-pointer"
                    >
                      <ChevronLeft className="w-4 h-4" />
                      <span>Previous</span>
                    </button>

                    <button
                      onClick={handleNext}
                      disabled={!isAnswered}
                      className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-bold bg-amber-700 hover:bg-amber-800 text-white shadow-xs disabled:opacity-40 disabled:pointer-events-none transition cursor-pointer"
                    >
                      <span>{currentIndex === totalQuestions - 1 ? 'Finish Assessment' : 'Next Question'}</span>
                      <ChevronRight className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              </div>
            )
          ) : (
            /* =========================================
               STUDY MODE
               ========================================= */
            <div className="space-y-4">
              <div className="flex items-center justify-between pb-2 border-b border-stone-200 dark:border-stone-800">
                <span className="text-xs text-stone-500">
                  Showing all {questions.length} questions for comprehensive study
                </span>
                <button
                  onClick={toggleAllStudyAnswers}
                  className="text-xs font-semibold text-amber-800 dark:text-amber-400 hover:underline flex items-center gap-1 cursor-pointer"
                >
                  <Eye className="w-3.5 h-3.5" />
                  <span>Toggle All Answers</span>
                </button>
              </div>

              <div className="space-y-3">
                {questions.map((q, idx) => {
                  const isExpanded = !!expandedAnswers[q.id];

                  return (
                    <div 
                      key={q.id || idx}
                      className="p-4 rounded-xl bg-white dark:bg-stone-900 border border-stone-200 dark:border-stone-800 space-y-2.5 transition"
                    >
                      <div className="flex items-start justify-between gap-3">
                        <div className="flex items-start gap-2 min-w-0">
                          <span className="text-xs font-bold px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950/70 text-amber-800 dark:text-amber-400 shrink-0">
                            Q{idx + 1}
                          </span>
                          <span className="font-cinzel font-semibold text-sm sm:text-base text-stone-900 dark:text-stone-100">
                            {q.question}
                          </span>
                        </div>
                        <button
                          onClick={() => toggleStudyAnswer(q.id)}
                          className="p-1 rounded-lg text-stone-400 hover:text-stone-700 dark:hover:text-stone-200 hover:bg-stone-100 dark:hover:bg-stone-800 transition cursor-pointer shrink-0"
                          title="Toggle Answer"
                        >
                          {isExpanded ? <EyeOff className="w-4 h-4 text-amber-700" /> : <Eye className="w-4 h-4" />}
                        </button>
                      </div>

                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-1.5 pt-1 text-xs">
                        {q.options.map((opt, oIdx) => {
                          const isCorrect = oIdx === q.correctAnswerIndex;
                          return (
                            <div
                              key={oIdx}
                              className={`p-2 rounded-lg border flex items-center gap-2 ${
                                isExpanded && isCorrect
                                  ? 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/30 text-emerald-900 dark:text-emerald-200 font-bold'
                                  : 'border-stone-200 dark:border-stone-800 bg-stone-50/50 dark:bg-stone-950/30 text-stone-700 dark:text-stone-300'
                              }`}
                            >
                              <span className="w-5 h-5 rounded bg-stone-200/60 dark:bg-stone-800 flex items-center justify-center text-[10px] font-bold text-stone-600 dark:text-stone-400 shrink-0">
                                {String.fromCharCode(65 + oIdx)}
                              </span>
                              <span className="truncate">{opt}</span>
                              {isExpanded && isCorrect && (
                                <Check className="w-3.5 h-3.5 text-emerald-600 ml-auto shrink-0" />
                              )}
                            </div>
                          );
                        })}
                      </div>

                      {isExpanded && (
                        <div className="mt-2 p-3 rounded-lg bg-amber-50/70 dark:bg-amber-950/20 border border-amber-200/70 dark:border-amber-900/50 text-xs text-stone-700 dark:text-stone-300 font-serif leading-relaxed animate-fade-in">
                          <div className="font-sans font-bold text-amber-900 dark:text-amber-400 mb-1 flex items-center justify-between">
                            <span>Scripture Reference: {q.reference}</span>
                            <span className="text-emerald-700 dark:text-emerald-400 font-bold">Answer: {q.correctAnswer}</span>
                          </div>
                          <p>{q.explanation}</p>
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
