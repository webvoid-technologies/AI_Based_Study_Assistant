"""Groq-only AI provider for document-grounded study tools."""

from __future__ import annotations

import json
import os

from groq import AsyncGroq

from app.services.memory_store import memory_store
from app.services.prompts import COMMON_SYSTEM_PROMPT, EXPLAIN_PROMPT, MCQ_PROMPT, PRACTICE_PROMPT, SUMMARY_PROMPT


class AIServiceError(RuntimeError):
    """Raised when Groq cannot complete a study request."""


class NoDocumentError(AIServiceError):
    """Raised when an AI feature is requested before an upload."""


class GroqAIService:
    def __init__(self) -> None:
        self.model = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")

    async def _complete(self, instruction: str, user_prompt: str | None = None, json_response: bool = False) -> str:
        document = memory_store.get()
        if document is None:
            raise NoDocumentError("Upload a document before using an AI feature.")

        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise AIServiceError("GROQ_API_KEY is not configured on the server.")

        request = instruction
        if user_prompt:
            request += f"\n\nUser Prompt:\n{user_prompt.strip()}"
        request += f"\n\nDocument Content:\n{document.content}"

        parameters = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": COMMON_SYSTEM_PROMPT},
                {"role": "user", "content": request},
            ],
            "temperature": 0.3,
            "max_tokens": 4096,
        }
        if json_response:
            parameters["response_format"] = {"type": "json_object"}

        try:
            response = await AsyncGroq(api_key=api_key, timeout=45).chat.completions.create(**parameters)
        except Exception as exc:
            raise AIServiceError("Groq could not complete the request. Please try again.") from exc

        content = response.choices[0].message.content
        if not content:
            raise AIServiceError("Groq returned an empty response. Please try again.")
        return content

    async def summarize_document(self) -> str:
        return await self._complete(SUMMARY_PROMPT)

    async def generate_practice_questions(self) -> str:
        return await self._complete(PRACTICE_PROMPT)

    async def generate_mcqs(self) -> list[dict[str, object]]:
        content = await self._complete(MCQ_PROMPT, json_response=True)
        return self._parse_mcqs(content)

    @staticmethod
    def _parse_mcqs(content: str) -> list[dict[str, object]]:
        cleaned = content.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.strip("`")
            if cleaned.startswith("json"):
                cleaned = cleaned[4:]
        try:
            payload = json.loads(cleaned.strip())
        except json.JSONDecodeError as exc:
            raise AIServiceError("Groq returned MCQs in an unreadable format. Please try again.") from exc

        questions = payload.get("questions") if isinstance(payload, dict) else payload
        if not isinstance(questions, list) or len(questions) != 10:
            raise AIServiceError("Groq did not return exactly 10 MCQs. Please try again.")

        normalized = []
        letters = ["A", "B", "C", "D"]
        for index, item in enumerate(questions, start=1):
            if not isinstance(item, dict):
                raise AIServiceError("Groq returned an invalid MCQ format. Please try again.")
            raw_options = item.get("options")
            if isinstance(raw_options, list):
                options = dict(zip(letters, raw_options))
            elif isinstance(raw_options, dict):
                options = {letter: raw_options.get(letter) for letter in letters}
            else:
                options = {}
            raw_correct = str(item.get("correct_answer", "")).strip()
            correct = raw_correct.upper() if raw_correct.upper() in letters else next(
                (letter for letter, option in options.items() if str(option).strip().lower() == raw_correct.lower()),
                "",
            )
            question = str(item.get("question", "")).strip()
            if not question or correct not in letters or any(not isinstance(value, str) or not value.strip() for value in options.values()):
                raise AIServiceError("Groq returned an incomplete MCQ. Please try again.")
            normalized.append({
                "number": index,
                "question": question,
                "options": options,
                "correct_answer": correct,
                "explanation": str(item.get("explanation", "")).strip(),
            })
        return normalized

    async def explain_topic(self, user_prompt: str) -> str:
        return await self._complete(EXPLAIN_PROMPT, user_prompt)


_service = GroqAIService()


async def summarize_document() -> str:
    return await _service.summarize_document()


async def generate_practice_questions() -> str:
    return await _service.generate_practice_questions()


async def generate_mcqs() -> list[dict[str, object]]:
    return await _service.generate_mcqs()


async def explain_topic(user_prompt: str) -> str:
    return await _service.explain_topic(user_prompt)
