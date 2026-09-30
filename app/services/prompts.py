"""Prompt templates shared by all Groq study features."""

COMMON_SYSTEM_PROMPT = """You are an AI Study Assistant.
Rules:
- Answer only using uploaded document content.
- Use simple English.
- Use headings and bullet points.
- If content is unavailable, clearly mention it.
- Do not invent information outside the document.
- Return clean Markdown without code fences.
"""

SUMMARY_PROMPT = """Create all of the following sections:
## Short Summary
## Detailed Summary
## Key Takeaways
## Important Topics
"""

PRACTICE_PROMPT = """Create exactly:
- 5 short-answer questions
- 3 long-answer questions
- 2 viva questions
Group them under clear headings and label every question Easy, Medium, or Hard.
"""

MCQ_PROMPT = """Create exactly 10 multiple-choice questions.
Return only a valid JSON object with this structure, without Markdown or code fences:
{
  "questions": [
    {
      "question": "Question text?",
      "options": {"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"},
      "correct_answer": "A",
      "explanation": "Short explanation"
    }
  ]
}
Every question must have exactly four options and one correct answer letter.
"""

EXPLAIN_PROMPT = """Explain the requested topic using only the document. Return:
## Explanation
## Real-world Example
## Simple Analogy
If an analogy is not applicable, say so clearly.
"""
