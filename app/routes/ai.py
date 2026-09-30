"""Document-grounded AI feature routes."""

import bleach
import markdown
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.services import ai_service
from app.services.ai_service import AIServiceError, NoDocumentError

router = APIRouter()
ALLOWED_TAGS = set(bleach.sanitizer.ALLOWED_TAGS) | {"h1", "h2", "h3", "h4", "p", "pre", "br", "hr"}


class ExplainRequest(BaseModel):
    prompt: str = Field(min_length=2, max_length=500)


def render_result(content: str) -> dict[str, str]:
    html = markdown.markdown(content, extensions=["extra", "sane_lists"])
    return {"content": content, "html": bleach.clean(html, tags=ALLOWED_TAGS, strip=True)}


async def execute(action) -> dict[str, str]:
    try:
        return render_result(await action())
    except NoDocumentError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except AIServiceError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc


@router.post("/summarize")
async def summarize() -> dict[str, str]:
    return await execute(ai_service.summarize_document)


@router.post("/practice")
async def practice() -> dict[str, str]:
    return await execute(ai_service.generate_practice_questions)


@router.post("/mcq")
async def mcq() -> dict[str, object]:
    try:
        questions = await ai_service.generate_mcqs()
        return {"questions": questions, "total": len(questions)}
    except NoDocumentError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except AIServiceError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc


@router.post("/explain")
async def explain(payload: ExplainRequest) -> dict[str, str]:
    return await execute(lambda: ai_service.explain_topic(payload.prompt))
