"""Secure upload and document-information routes."""

from __future__ import annotations

import re
import tempfile
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.services.file_parser import FileParsingError, file_parser
from app.services.memory_store import memory_store

router = APIRouter()
MAX_FILE_SIZE = 20 * 1024 * 1024
MIME_TYPES = {
    ".pdf": {"application/pdf"},
    ".docx": {"application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/zip"},
    ".pptx": {"application/vnd.openxmlformats-officedocument.presentationml.presentation", "application/zip"},
    ".xlsx": {"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/zip"},
    ".png": {"image/png"},
    ".jpg": {"image/jpeg"},
    ".jpeg": {"image/jpeg"},
    ".json": {"application/json", "text/json", "text/plain"},
    ".txt": {"text/plain", "application/octet-stream"},
}


def sanitize_filename(filename: str) -> str:
    name = Path(filename).name
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", name)
    return safe[:180] or "document"


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)) -> dict:
    filename = sanitize_filename(file.filename or "")
    extension = Path(filename).suffix.lower()
    if extension not in file_parser.supported_extensions:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="Unsupported format. Upload PDF, DOCX, PPTX, XLSX, PNG, JPG, JPEG, JSON, or TXT.")
    if file.content_type not in MIME_TYPES[extension]:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="The file content type does not match its extension.")

    data = await file.read(MAX_FILE_SIZE + 1)
    await file.close()
    if len(data) > MAX_FILE_SIZE:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="File is too large. Maximum size is 20 MB.")
    if not data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The uploaded file is empty.")

    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(suffix=extension, delete=False) as temporary_file:
            temporary_file.write(data)
            temporary_path = Path(temporary_file.name)
        content = file_parser.extract_text(temporary_path)
        document = memory_store.set(filename, extension.lstrip("."), content)
    except FileParsingError as exc:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)) from exc
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)

    return {"message": "Document uploaded and processed successfully.", "document": memory_store.metadata()}


@router.get("/document")
async def document_info() -> dict:
    return {"document": memory_store.metadata()}
