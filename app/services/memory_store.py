"""Thread-safe, in-memory storage for the current uploaded document."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from threading import RLock


@dataclass(frozen=True)
class StoredDocument:
    filename: str
    filetype: str
    content: str
    uploaded_at: str
    word_count: int
    character_count: int


class MemoryStore:
    """Keep one document in RAM; a new upload replaces the previous one."""

    def __init__(self) -> None:
        self._document: StoredDocument | None = None
        self._lock = RLock()

    def set(self, filename: str, filetype: str, content: str) -> StoredDocument:
        document = StoredDocument(
            filename=filename,
            filetype=filetype,
            content=content,
            uploaded_at=datetime.now(timezone.utc).isoformat(),
            word_count=len(content.split()),
            character_count=len(content),
        )
        with self._lock:
            self._document = document
        return document

    def get(self) -> StoredDocument | None:
        with self._lock:
            return self._document

    def metadata(self) -> dict[str, str | int] | None:
        document = self.get()
        if document is None:
            return None
        data = asdict(document)
        data.pop("content")
        return data

    def clear(self) -> None:
        with self._lock:
            self._document = None


memory_store = MemoryStore()
