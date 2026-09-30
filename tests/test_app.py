from fastapi.testclient import TestClient
import pytest

from app.main import app
from app.routes import ai as ai_routes
from app.services.memory_store import memory_store

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_document():
    memory_store.clear()
    yield
    memory_store.clear()


def test_dashboard_loads():
    response = client.get("/")
    assert response.status_code == 200
    assert "AI Study" in response.text


def test_upload_text_document():
    response = client.post("/upload", files={"file": ("notes.txt", b"FastAPI is a Python web framework.", "text/plain")})
    assert response.status_code == 200
    assert response.json()["document"]["word_count"] == 6
    assert memory_store.get().content == "FastAPI is a Python web framework."


def test_upload_rejects_unsupported_type():
    response = client.post("/upload", files={"file": ("program.py", b"print('no')", "text/x-python")})
    assert response.status_code == 415


def test_ai_requires_document():
    response = client.post("/summarize")
    assert response.status_code == 400
    assert "Upload a document" in response.json()["detail"]


def test_summary_returns_sanitized_html(monkeypatch):
    memory_store.set("notes.txt", "txt", "Grounded content")

    async def fake_summary():
        return "## Summary\n<script>alert(1)</script>Safe content"

    monkeypatch.setattr(ai_routes.ai_service, "summarize_document", fake_summary)
    response = client.post("/summarize")
    assert response.status_code == 200
    assert "<script>" not in response.json()["html"]
    assert "Safe content" in response.json()["html"]


def test_mcq_returns_interactive_question_data(monkeypatch):
    memory_store.set("notes.txt", "txt", "Grounded content")
    questions = [
        {
            "number": index,
            "question": f"Question {index}?",
            "options": {"A": "First", "B": "Second", "C": "Third", "D": "Fourth"},
            "correct_answer": "A",
            "explanation": "The document supports option A.",
        }
        for index in range(1, 11)
    ]

    async def fake_mcqs():
        return questions

    monkeypatch.setattr(ai_routes.ai_service, "generate_mcqs", fake_mcqs)
    response = client.post("/mcq")
    assert response.status_code == 200
    assert response.json()["total"] == 10
    assert response.json()["questions"][0]["options"]["A"] == "First"


def test_explain_validates_prompt():
    memory_store.set("notes.txt", "txt", "Grounded content")
    response = client.post("/explain", json={"prompt": "x"})
    assert response.status_code == 422
