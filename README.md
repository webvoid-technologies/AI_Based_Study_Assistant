# Webvoid AI-Based Study Assistant

<p align="center">
  <img src="https://www.webvoidtechnologies.com/webvoid_logo_tm.png" alt="Webvoid Technologies Logo" width="220">
</p>

A Webvoid Technologies FastAPI study application that extracts text from uploaded learning material and uses Groq to generate summaries, practice questions, interactive MCQs, and explanations.

## Webvoid Project Prerequisites

- Python 3.9 or later; Python 3.12+ is recommended
- pip
- A Groq API key from `https://console.groq.com/`
- Tesseract OCR for PNG, JPG, and JPEG uploads

## 1. Install Tesseract for Webvoid OCR

### macOS

```bash
/opt/homebrew/bin/brew install tesseract
```

The Webvoid configuration uses `/opt/homebrew/bin/tesseract`. For additional languages, install the language package:

```bash
/opt/homebrew/bin/brew install tesseract-lang
```

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install tesseract-ocr
```

### Windows

Install the Tesseract Windows build, then set `TESSERACT_CMD` to the installed `tesseract.exe` path.

## 2. Create the Webvoid Virtual Environment

Each Webvoid project keeps its own isolated `.venv` folder inside that project's directory. Do not share one virtual environment across projects.

From the Webvoid project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install Webvoid Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Configure Webvoid Environment Variables

```bash
cp .env.example .env
```

Edit `.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=qwen/qwen3.8-27b
TESSERACT_CMD=/opt/homebrew/bin/tesseract
```

On Windows, use a path similar to:

```env
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe
```

## 5. Run the Webvoid Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

If port `8000` is already occupied, use another port:

```bash
uvicorn app.main:app --reload --port 8001
```

Then open `http://127.0.0.1:8001`.

## 6. Run Webvoid Tests

```bash
pytest
```

## Webvoid Troubleshooting

### `GROQ_API_KEY is not configured`

Confirm `.env` exists in the Webvoid project root and contains `GROQ_API_KEY`.

### `model_not_found`

The configured model is unavailable to the Groq API key. List available models in the Groq console or set `GROQ_MODEL` to a supported model.

### `Tesseract OCR is not installed or is unavailable`

Install Tesseract and update `TESSERACT_CMD` in `.env`.

### `File is too large`

The maximum Webvoid upload size is 20 MB.

### `No readable text was found`

Use a document that contains selectable text or a clear image with readable text.

### Port already in use

```bash
lsof -ti:8000 | xargs kill -9
```

Then start the Webvoid application again.

---

**Webvoid Technologies — AI-Based Study Assistant**
