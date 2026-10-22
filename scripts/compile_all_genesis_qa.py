#!/usr/bin/env python3
import json
import os
import sys

# Add scripts directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from build_qa_part1 import get_chapters_1_to_10
from build_qa_part2 import get_chapters_11_to_20
from build_qa_part3 import get_chapters_21_to_30
from build_qa_part4 import get_chapters_31_to_40
from build_qa_part5 import get_chapters_41_to_50

def main():
    raw_chapters = {}
    
    print("Collecting Q&A chapters 1-10...")
    raw_chapters.update(get_chapters_1_to_10())
    
    print("Collecting Q&A chapters 11-20...")
    raw_chapters.update(get_chapters_11_to_20())
    
    print("Collecting Q&A chapters 21-30...")
    raw_chapters.update(get_chapters_21_to_30())
    
    print("Collecting Q&A chapters 31-40...")
    raw_chapters.update(get_chapters_31_to_40())
    
    print("Collecting Q&A chapters 41-50...")
    raw_chapters.update(get_chapters_41_to_50())
    
    # Normalize keys to strings
    all_chapters = {str(k): v for k, v in raw_chapters.items()}
    
    # Validation
    total_chapters = len(all_chapters)
    total_questions = 0
    errors = []
    
    print(f"\nValidating {total_chapters} chapters...")
    for ch_num in range(1, 51):
        ch_key = str(ch_num)
        if ch_key not in all_chapters:
            errors.append(f"Missing chapter {ch_key}!")
            continue
        
        q_list = all_chapters[ch_key]
        if len(q_list) != 10:
            errors.append(f"Chapter {ch_key} has {len(q_list)} questions, expected 10!")
        
        total_questions += len(q_list)
        for idx, q in enumerate(q_list):
            q_id = q.get("id")
            question_text = q.get("question")
            options = q.get("options", [])
            correct_idx = q.get("correctAnswerIndex")
            correct_ans = q.get("correctAnswer")
            ref = q.get("reference")
            exp = q.get("explanation")
            
            if not question_text:
                errors.append(f"Ch {ch_key} Q {idx+1} is missing question text")
            if len(options) != 4:
                errors.append(f"Ch {ch_key} Q {idx+1} has {len(options)} options, expected 4")
            if correct_idx is None or correct_idx < 0 or correct_idx >= 4:
                errors.append(f"Ch {ch_key} Q {idx+1} invalid correctAnswerIndex: {correct_idx}")
            elif options[correct_idx] != correct_ans:
                errors.append(f"Ch {ch_key} Q {idx+1} correctAnswer '{correct_ans}' does not match option[{correct_idx}] '{options[correct_idx]}'")
            if not ref:
                errors.append(f"Ch {ch_key} Q {idx+1} missing reference")
            if not exp:
                errors.append(f"Ch {ch_key} Q {idx+1} missing explanation")

    if errors:
        print(f"Validation failed with {len(errors)} errors:")
        for err in errors[:20]:
            print(" - ", err)
        if len(errors) > 20:
            print(f"... and {len(errors) - 20} more errors.")
        sys.exit(1)
        
    print(f"Validation successful! Total chapters: {total_chapters}, total questions: {total_questions}")
    
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "data", "genesis_qa.json")
    output_path = os.path.abspath(output_path)
    
    payload = {
        "book": "Genesis",
        "totalChapters": total_chapters,
        "totalQuestions": total_questions,
        "questionsPerChapter": 10,
        "chapters": all_chapters
    }
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        
    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"Successfully wrote {output_path} ({file_size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
