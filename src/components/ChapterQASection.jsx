import React, { useState, useEffect } from 'react';
import { 
  HelpCircle, 
  CheckCircle2, 
  XCircle, 
  RotateCcw, 
  Eye, 
  EyeOff, 
  Award, 
  ArrowUp, 
  ChevronDown, 
  ChevronUp, 
  ArrowRight, 
  BookOpen, 
  Check, 
  Layers,
  Trophy
} from 'lucide-react';
import qaDataset from '../data/genesis_qa.json';

export default function ChapterQASection({ chapter = 1 }) {
  const [activeTab, setActiveTab] = useState('practice'); // 'practice' | 'study'

  // Questions for this specific chapter
  const chapterQuestions = qaDataset?.chapters?.[String(chapter)] || [];

  // Practice Mode State
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [score, setScore] = useState(0);
  const [userAnswers, setUserAnswers] = useState([]); // array of { index, selected, isCorrect }
  const [quizFinished, setQuizFinished] = useState(false);
  const [bestScore, setBestScore] = useState(null);

  // Study Mode State
  const [expandedAnswers, setExpandedAnswers] = useState({}); // { [qId]: boolean }

  // Load best score from local storage
  const loadBestScore = () => {
    try {
      const saved = JSON.parse(localStorage.getItem('holy_bible_quiz_scores') || '{}');
      setBestScore(saved[String(chapter)] || null);
    } catch {
      setBestScore(null);
    }
  };

  // Save completed quiz score to local storage
  const saveQuizScore = (finalScore) => {
    try {
      const saved = JSON.parse(localStorage.getItem('holy_bible_quiz_scores') || '{}');
      const prev = saved[String(chapter)];
      if (!prev || finalScore >= prev.score) {
        const record = {
          score: finalScore,
          total: chapterQuestions.length,
          percentage: Math.round((finalScore / chapterQuestions.length) * 100),
          updatedAt: new Date().toISOString()
        };
        saved[String(chapter)] = record;
        localStorage.setItem('holy_bible_quiz_scores', JSON.stringify(saved));
        setBestScore(record);
      }
    } catch (e) {
      console.warn('Could not save score to local storage:', e);
    }
  };

  // Reset practice state when chapter changes
  useEffect(() => {
    setCurrentIndex(0);
    setSelectedOption(null);
    setIsAnswered(false);
    setScore(0);
    setUserAnswers([]);
    setQuizFinished(false);
    setExpandedAnswers({});
    loadBestScore();
  }, [chapter]);

  if (!chapterQuestions || chapterQuestions.length === 0) {
    return null;
  }

  const currentQ = chapterQuestions[currentIndex] || chapterQuestions[0];

  // Practice Mode Handlers
  const handleSelectOption = (optIndex) => {
    if (isAnswered) return; // Prevent changing after submission
    setSelectedOption(optIndex);
    setIsAnswered(true);

    const isCorrect = optIndex === currentQ.correctAnswerIndex;
    const newScore = isCorrect ? score + 1 : score;
    if (isCorrect) {
      setScore(newScore);
    }

    setUserAnswers((prev) => [
      ...prev,
      {
        questionIndex: currentIndex,
        questionId: currentQ.id,
        selectedOption: optIndex,
        isCorrect
      }
    ]);
  };

  const handleNextQuestion = () => {
    if (currentIndex < chapterQuestions.length - 1) {
      setCurrentIndex((prev) => prev + 1);
      setSelectedOption(null);
      setIsAnswered(false);
    } else {
      setQuizFinished(true);
      saveQuizScore(score);
    }
  };

  const handleRestartQuiz = () => {
    setCurrentIndex(0);
    setSelectedOption(null);
    setIsAnswered(false);
    setScore(0);
    setUserAnswers([]);
    setQuizFinished(false);
    loadBestScore();
  };

  // Study Mode Handlers
  const toggleAnswer = (qId) => {
    setExpandedAnswers((prev) => ({
      ...prev,
      [qId]: !prev[qId]
    }));
  };

  const handleExpandAll = () => {
    const allExpanded = {};
    chapterQuestions.forEach((q) => {
      allExpanded[q.id] = true;
    });
    setExpandedAnswers(allExpanded);
  };

  const handleCollapseAll = () => {
    setExpandedAnswers({});
  };

  const areAllExpanded = chapterQuestions.every((q) => expandedAnswers[q.id]);

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <section className="mt-16 pt-10 border-t-2 border-stone-200 dark:border-stone-800 transition-colors">
      {/* Section Header */}
      <div className="text-center mb-8">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-amber-100 dark:bg-amber-950/60 text-amber-800 dark:text-amber-400 mb-2">
          <BookOpen className="w-3.5 h-3.5" />
          Interactive Bible Study
        </div>
        <h2 className="text-2xl sm:text-3xl font-cinzel font-bold text-stone-900 dark:text-stone-100 tracking-tight">
          Chapter Review — Questions and Answers
        </h2>
        <p className="mt-2 text-sm text-stone-600 dark:text-stone-400 max-w-xl mx-auto">
          Test your comprehension of Genesis Chapter {chapter} with 10 questions grounded directly in the biblical text.
        </p>

        {/* Mode Switcher Tabs */}
        <div className="inline-flex items-center p-1 mt-6 rounded-xl bg-stone-200/70 dark:bg-stone-800/80 border border-stone-300/60 dark:border-stone-700/60 shadow-inner">
          <button
            onClick={() => setActiveTab('practice')}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg text-xs sm:text-sm font-semibold transition-all cursor-pointer ${
              activeTab === 'practice'
                ? 'bg-white dark:bg-stone-900 text-amber-900 dark:text-amber-300 shadow-sm'
                : 'text-stone-600 dark:text-stone-400 hover:text-stone-900 dark:hover:text-stone-200'
            }`}
          >
            <HelpCircle className="w-4 h-4 text-amber-600 dark:text-amber-400" />
            <span>Practice Mode (Interactive Quiz)</span>
          </button>
          <button
            onClick={() => setActiveTab('study')}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg text-xs sm:text-sm font-semibold transition-all cursor-pointer ${
              activeTab === 'study'
                ? 'bg-white dark:bg-stone-900 text-amber-900 dark:text-amber-300 shadow-sm'
                : 'text-stone-600 dark:text-stone-400 hover:text-stone-900 dark:hover:text-stone-200'
            }`}
          >
            <Layers className="w-4 h-4 text-amber-600 dark:text-amber-400" />
            <span>Study Mode (All 10 Questions)</span>
          </button>
        </div>
      </div>

      {/* PRACTICE MODE */}
      {activeTab === 'practice' && (
        <div className="bg-stone-50 dark:bg-stone-900/90 border border-stone-200 dark:border-stone-800 rounded-2xl p-6 sm:p-8 shadow-sm">
          {!quizFinished ? (
            <div>
              {/* Quiz Header & Live Score Tracker */}
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-5 mb-6 border-b border-stone-200 dark:border-stone-800">
                <div className="flex items-center gap-2 flex-wrap">
                  <span className="text-xs font-bold uppercase tracking-wider text-amber-800 dark:text-amber-400 bg-amber-100 dark:bg-amber-950/70 px-2.5 py-1 rounded-md">
                    Question {currentIndex + 1} of {chapterQuestions.length}
                  </span>
                  <span className="text-xs text-stone-500 dark:text-stone-400">
                    Genesis {chapter}
                  </span>
                  {bestScore && (
                    <span className="inline-flex items-center gap-1 text-[11px] font-semibold text-amber-700 dark:text-amber-300 bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-900/40 px-2 py-0.5 rounded">
                      <Trophy className="w-3 h-3 text-amber-500" />
                      Best: {bestScore.score}/{bestScore.total}
                    </span>
                  )}
                </div>

                {/* Score Tracker & Progress Dots */}
                <div className="flex items-center gap-3">
                  <div className="flex items-center gap-1">
                    {chapterQuestions.map((_, idx) => {
                      const answerRecord = userAnswers.find((a) => a.questionIndex === idx);
                      let dotColor = 'bg-stone-300 dark:bg-stone-700';
                      if (answerRecord) {
                        dotColor = answerRecord.isCorrect ? 'bg-emerald-500' : 'bg-rose-500';
                      } else if (idx === currentIndex) {
                        dotColor = 'bg-amber-600 dark:bg-amber-400 ring-2 ring-amber-300 dark:ring-amber-900';
                      }
                      return (
                        <div
                          key={idx}
                          className={`w-2.5 h-2.5 rounded-full transition-all ${dotColor}`}
                          title={`Question ${idx + 1}`}
                        />
                      );
                    })}
                  </div>
                  <div className="text-xs font-semibold text-stone-700 dark:text-stone-300 bg-stone-200/70 dark:bg-stone-800 px-2 py-1 rounded-md">
                    Score: <strong className="text-amber-700 dark:text-amber-400">{score}</strong> / {currentIndex + (isAnswered ? 1 : 0)}
                  </div>
                </div>
              </div>

              {/* Question Text */}
              <div className="mb-6">
                <h3 className="text-lg sm:text-xl font-medium text-stone-900 dark:text-stone-100 leading-snug">
                  {currentQ.question}
                </h3>
              </div>

              {/* 4 Multiple Choice Options */}
              <div className="space-y-3 mb-6">
                {currentQ.options.map((option, optIdx) => {
                  const isSelected = selectedOption === optIdx;
                  const isCorrect = optIdx === currentQ.correctAnswerIndex;

                  let optionStyle = 'border-stone-200 dark:border-stone-800 bg-white dark:bg-stone-800/60 hover:bg-amber-50/50 dark:hover:bg-stone-800 hover:border-amber-300 dark:hover:border-stone-700 text-stone-800 dark:text-stone-200';

                  if (isAnswered) {
                    if (isCorrect) {
                      optionStyle = 'border-emerald-500 bg-emerald-50/80 dark:bg-emerald-950/40 text-emerald-950 dark:text-emerald-200 font-medium ring-1 ring-emerald-500';
                    } else if (isSelected && !isCorrect) {
                      optionStyle = 'border-rose-500 bg-rose-50/80 dark:bg-rose-950/40 text-rose-950 dark:text-rose-200 font-medium ring-1 ring-rose-500';
                    } else {
                      optionStyle = 'border-stone-200 dark:border-stone-800/80 bg-white/50 dark:bg-stone-800/30 text-stone-400 dark:text-stone-500 opacity-60';
                    }
                  }

                  const letterLabel = String.fromCharCode(65 + optIdx); // A, B, C, D

                  return (
                    <button
                      key={optIdx}
                      onClick={() => handleSelectOption(optIdx)}
                      disabled={isAnswered}
                      className={`w-full text-left p-3.5 sm:p-4 rounded-xl border transition-all flex items-start gap-3.5 cursor-pointer ${optionStyle} ${
                        isAnswered ? 'cursor-default' : ''
                      }`}
                    >
                      <span className={`w-7 h-7 rounded-lg flex items-center justify-center text-xs font-bold shrink-0 transition-colors ${
                        isAnswered && isCorrect
                          ? 'bg-emerald-600 text-white'
                          : isAnswered && isSelected && !isCorrect
                          ? 'bg-rose-600 text-white'
                          : 'bg-stone-100 dark:bg-stone-700 text-stone-700 dark:text-stone-300'
                      }`}>
                        {letterLabel}
                      </span>
                      <span className="flex-1 text-sm sm:text-base pt-0.5 leading-normal">
                        {option}
                      </span>
                      {isAnswered && isCorrect && (
                        <CheckCircle2 className="w-5 h-5 text-emerald-600 dark:text-emerald-400 shrink-0 self-center" />
                      )}
                      {isAnswered && isSelected && !isCorrect && (
                        <XCircle className="w-5 h-5 text-rose-600 dark:text-rose-400 shrink-0 self-center" />
                      )}
                    </button>
                  );
                })}
              </div>

              {/* Immediate Feedback & Scripture Explanation */}
              {isAnswered && (
                <div className={`p-4 sm:p-5 rounded-xl border mb-6 animate-fade-in ${
                  selectedOption === currentQ.correctAnswerIndex
                    ? 'bg-emerald-50/90 dark:bg-emerald-950/30 border-emerald-300 dark:border-emerald-900/60'
                    : 'bg-rose-50/90 dark:bg-rose-950/30 border-rose-300 dark:border-rose-900/60'
                }`}>
                  <div className="flex items-center justify-between gap-2 mb-2">
                    <div className="flex items-center gap-2">
                      {selectedOption === currentQ.correctAnswerIndex ? (
                        <>
                          <CheckCircle2 className="w-5 h-5 text-emerald-600 dark:text-emerald-400" />
                          <span className="font-bold text-sm sm:text-base text-emerald-900 dark:text-emerald-200">
                            Correct!
                          </span>
                        </>
                      ) : (
                        <>
                          <XCircle className="w-5 h-5 text-rose-600 dark:text-rose-400" />
                          <span className="font-bold text-sm sm:text-base text-rose-900 dark:text-rose-200">
                            Incorrect. The correct answer is: {currentQ.correctAnswer}
                          </span>
                        </>
                      )}
                    </div>
                    <span className="text-xs font-bold px-2 py-0.5 rounded bg-white/80 dark:bg-stone-900/80 text-amber-800 dark:text-amber-400 border border-stone-200 dark:border-stone-700">
                      📖 {currentQ.reference}
                    </span>
                  </div>
                  <p className="text-xs sm:text-sm text-stone-700 dark:text-stone-300 leading-relaxed font-serif pt-1">
                    {currentQ.explanation}
                  </p>
                </div>
              )}

              {/* Next Question / Finish Button */}
              {isAnswered && (
                <div className="flex justify-end pt-2">
                  <button
                    onClick={handleNextQuestion}
                    className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-amber-800 hover:bg-amber-900 dark:bg-amber-700 dark:hover:bg-amber-600 text-white font-semibold text-xs sm:text-sm shadow transition-all cursor-pointer"
                  >
                    <span>
                      {currentIndex < chapterQuestions.length - 1 ? 'Next Question' : 'View Final Results'}
                    </span>
                    <ArrowRight className="w-4 h-4" />
                  </button>
                </div>
              )}
            </div>
          ) : (
            /* Quiz Completion Results Screen */
            <div className="text-center py-6 sm:py-8 space-y-6 animate-fade-in">
              <div className="w-16 h-16 mx-auto rounded-2xl bg-amber-100 dark:bg-amber-950/70 text-amber-800 dark:text-amber-300 flex items-center justify-center shadow-inner">
                <Award className="w-8 h-8" />
              </div>

              <div>
                <h3 className="text-2xl sm:text-3xl font-cinzel font-bold text-stone-900 dark:text-stone-100">
                  Quiz Completed!
                </h3>
                <p className="text-stone-600 dark:text-stone-400 text-sm mt-1">
                  You reviewed all 10 questions for Genesis Chapter {chapter}.
                </p>
              </div>

              {/* Score Display Card */}
              <div className="inline-block p-6 rounded-2xl bg-white dark:bg-stone-800 border border-stone-200 dark:border-stone-700 shadow-sm">
                <div className="text-4xl sm:text-5xl font-extrabold text-amber-700 dark:text-amber-400">
                  {score} / 10
                </div>
                <div className="text-xs uppercase font-bold tracking-wider text-stone-500 dark:text-stone-400 mt-2">
                  {Math.round((score / 10) * 100)}% Accuracy
                </div>
                <div className="mt-3 text-xs sm:text-sm font-medium text-stone-700 dark:text-stone-300">
                  {score === 10 && "🌟 Perfect score! Outstanding knowledge of this chapter!"}
                  {score >= 8 && score < 10 && "👏 Excellent work! You have a strong grasp of Genesis " + chapter + "."}
                  {score >= 6 && score < 8 && "👍 Good effort! Review the Scripture references to master this chapter."}
                  {score < 6 && "📖 Keep reading and reflecting on God's Word. Try studying with Study Mode!"}
                </div>
                <div className="mt-2.5 pt-2 border-t border-stone-200/60 dark:border-stone-700/60 text-[11px] text-stone-500 dark:text-stone-400 flex items-center justify-center gap-1.5">
                  <Trophy className="w-3.5 h-3.5 text-amber-500 inline" />
                  <span>Saved locally to your device for offline progress tracking</span>
                </div>
              </div>

              {/* Action Buttons */}
              <div className="flex flex-wrap items-center justify-center gap-3 pt-4">
                <button
                  onClick={handleRestartQuiz}
                  className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-amber-800 hover:bg-amber-900 text-white font-semibold text-xs sm:text-sm shadow transition cursor-pointer"
                >
                  <RotateCcw className="w-4 h-4" />
                  <span>Retry Quiz</span>
                </button>
                <button
                  onClick={() => setActiveTab('study')}
                  className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-stone-200 dark:bg-stone-800 hover:bg-stone-300 dark:hover:bg-stone-700 text-stone-800 dark:text-stone-200 font-semibold text-xs sm:text-sm transition cursor-pointer"
                >
                  <Layers className="w-4 h-4 text-amber-600 dark:text-amber-400" />
                  <span>Review All in Study Mode</span>
                </button>
              </div>
            </div>
          )}
        </div>
      )}

      {/* STUDY MODE */}
      {activeTab === 'study' && (
        <div className="space-y-4">
          {/* Study Mode Controls Toolbar */}
          <div className="flex items-center justify-between gap-3 p-3 rounded-xl bg-stone-100 dark:bg-stone-800/60 border border-stone-200 dark:border-stone-800">
            <span className="text-xs font-semibold text-stone-600 dark:text-stone-400">
              Showing all 10 questions for Genesis {chapter}
            </span>
            <div className="flex items-center gap-2">
              <button
                onClick={areAllExpanded ? handleCollapseAll : handleExpandAll}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold rounded-lg bg-white dark:bg-stone-800 border border-stone-200 dark:border-stone-700 hover:bg-stone-50 dark:hover:bg-stone-700 text-stone-700 dark:text-stone-300 transition cursor-pointer shadow-xs"
              >
                {areAllExpanded ? (
                  <>
                    <EyeOff className="w-3.5 h-3.5" />
                    <span>Collapse All</span>
                  </>
                ) : (
                  <>
                    <Eye className="w-3.5 h-3.5" />
                    <span>Expand All</span>
                  </>
                )}
              </button>
            </div>
          </div>

          {/* List of 10 Study Questions */}
          <div className="space-y-4">
            {chapterQuestions.map((q, qIdx) => {
              const isExpanded = !!expandedAnswers[q.id];

              return (
                <div
                  key={q.id || qIdx}
                  className="bg-stone-50 dark:bg-stone-900/90 border border-stone-200 dark:border-stone-800 rounded-xl p-5 shadow-xs transition hover:border-amber-300 dark:hover:border-stone-700"
                >
                  {/* Question Header */}
                  <div className="flex items-start justify-between gap-3">
                    <div className="flex items-start gap-3">
                      <span className="w-7 h-7 rounded-lg bg-amber-100 dark:bg-amber-950/70 text-amber-800 dark:text-amber-400 font-bold text-xs flex items-center justify-center shrink-0 mt-0.5">
                        {qIdx + 1}
                      </span>
                      <h4 className="text-base sm:text-lg font-medium text-stone-900 dark:text-stone-100 leading-snug">
                        {q.question}
                      </h4>
                    </div>

                    <button
                      onClick={() => toggleAnswer(q.id)}
                      className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition shrink-0 cursor-pointer ${
                        isExpanded
                          ? 'bg-amber-100 dark:bg-amber-950/70 text-amber-900 dark:text-amber-300'
                          : 'bg-stone-200/70 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 text-stone-700 dark:text-stone-300'
                      }`}
                    >
                      {isExpanded ? (
                        <>
                          <span>Hide Answer</span>
                          <ChevronUp className="w-3.5 h-3.5" />
                        </>
                      ) : (
                        <>
                          <span>Show Answer</span>
                          <ChevronDown className="w-3.5 h-3.5" />
                        </>
                      )}
                    </button>
                  </div>

                  {/* Options List */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-4 ml-10">
                    {q.options.map((opt, optIdx) => {
                      const isCorrect = optIdx === q.correctAnswerIndex;
                      const letter = String.fromCharCode(65 + optIdx);
                      return (
                        <div
                          key={optIdx}
                          className={`px-3 py-2 rounded-lg text-xs sm:text-sm border flex items-center gap-2 ${
                            isExpanded && isCorrect
                              ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-400 text-emerald-950 dark:text-emerald-200 font-semibold'
                              : 'bg-white dark:bg-stone-800/40 border-stone-200 dark:border-stone-800 text-stone-700 dark:text-stone-300'
                          }`}
                        >
                          <span className={`w-5 h-5 rounded flex items-center justify-center text-[10px] font-bold ${
                            isExpanded && isCorrect
                              ? 'bg-emerald-600 text-white'
                              : 'bg-stone-100 dark:bg-stone-700 text-stone-600 dark:text-stone-300'
                          }`}>
                            {letter}
                          </span>
                          <span className="flex-1">{opt}</span>
                          {isExpanded && isCorrect && (
                            <Check className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 shrink-0" />
                          )}
                        </div>
                      );
                    })}
                  </div>

                  {/* Collapsible Answer & Scripture Reference Card */}
                  {isExpanded && (
                    <div className="mt-4 pt-4 border-t border-stone-200 dark:border-stone-800 ml-10 bg-amber-50/60 dark:bg-stone-800/50 p-4 rounded-xl border border-amber-200/60 dark:border-stone-700/60 animate-fade-in space-y-2">
                      <div className="flex flex-wrap items-center justify-between gap-2">
                        <div className="flex items-center gap-2 text-xs font-semibold text-emerald-800 dark:text-emerald-300">
                          <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                          <span>Correct Answer: {q.correctAnswer}</span>
                        </div>
                        <span className="text-[11px] font-bold px-2 py-0.5 rounded bg-white dark:bg-stone-900 text-amber-800 dark:text-amber-400 border border-stone-200 dark:border-stone-700">
                          📖 {q.reference}
                        </span>
                      </div>
                      <p className="text-xs sm:text-sm text-stone-700 dark:text-stone-300 font-serif leading-relaxed">
                        {q.explanation}
                      </p>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Back to Top Smooth Scroll */}
      <div className="mt-8 text-center">
        <button
          onClick={scrollToTop}
          className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold bg-stone-200/60 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 text-stone-700 dark:text-stone-300 transition cursor-pointer"
        >
          <ArrowUp className="w-3.5 h-3.5" />
          <span>Back to Top of Genesis {chapter}</span>
        </button>
      </div>
    </section>
  );
}
