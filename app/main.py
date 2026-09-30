"""FastAPI entry point for the AI-Based Study Assistant."""

from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import ai, pages, upload

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="AI-Based Study Assistant", version="2.0.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
app.include_router(pages.router)
app.include_router(upload.router)
app.include_router(ai.router)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy", "provider": "groq"}
