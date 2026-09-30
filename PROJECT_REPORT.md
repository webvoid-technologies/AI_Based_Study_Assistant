# AI-Based Study Assistant

## Complete Project Report

<div style="page-break-after: always;"></div>

## Page 1 — Title Page

**Project Title:** AI-Based Study Assistant  
**Project Type:** Final Year / Proof-of-Concept Application  
**Technology:** FastAPI, Python, Jinja2, HTML, CSS, JavaScript, and Groq API  
**Student Name:** [Student Name]  
**Roll Number:** [Roll Number]  
**Department:** [Department Name]  
**Institution:** [Institution Name]  
**Guide Name:** [Project Guide Name]  
**Academic Year:** 2026–2027  
**Date:** [Submission Date]

<div style="page-break-after: always;"></div>

## Page 2 — Certificate

This is to certify that the project report titled **AI-Based Study Assistant** has been completed by **[Student Name]**, bearing roll number **[Roll Number]**, under the guidance of **[Project Guide Name]**. The work presented in this report is an original implementation carried out as part of the academic requirements of **[Program Name]** in **[Department Name]**, **[Institution Name]**.

The project demonstrates the design and implementation of an artificial-intelligence-assisted study platform using FastAPI, Jinja2, browser-based technologies, document parsing libraries, and the Groq large language model API.

**Project Guide**  
Name: ____________________  
Signature: ________________

**Head of Department**  
Name: ____________________  
Signature: ________________

**External Examiner**  
Name: ____________________  
Signature: ________________

<div style="page-break-after: always;"></div>

## Page 3 — Declaration

I, **[Student Name]**, hereby declare that the project titled **AI-Based Study Assistant** is my original work and has been completed under the supervision of **[Project Guide Name]**. The project has not been submitted previously, either in full or in part, for the award of any degree or diploma at this or any other institution.

All external libraries, APIs, documentation, and technical resources used in the implementation have been identified and acknowledged. The source code and report represent my own understanding, design, development, integration, and testing effort.

**Place:** [Place]  
**Date:** [Date]  
**Student Signature:** ____________________  
**Student Name:** [Student Name]  
**Roll Number:** [Roll Number]

<div style="page-break-after: always;"></div>

## Page 4 — Acknowledgment

I express my sincere gratitude to **[Project Guide Name]** for continuous guidance, technical suggestions, encouragement, and review throughout the development of this project. I also thank the Head of the Department, faculty members, and laboratory staff of **[Department Name]** for providing an environment that supports practical learning and project development.

I acknowledge the maintainers and documentation teams behind FastAPI, Uvicorn, Jinja2, PyMuPDF, python-docx, python-pptx, openpyxl, Pillow, pytesseract, Groq, and the Python ecosystem. Their openly available tools made it possible to implement a complete document-processing and AI-assisted learning workflow.

Finally, I thank my classmates and family for their support and motivation during the design, implementation, debugging, testing, and documentation phases.

<div style="page-break-after: always;"></div>

## Page 5 — Abstract

Students commonly work with lecture notes, presentations, spreadsheets, scanned documents, and text files in different formats. Converting these materials into summaries, revision questions, and explanations normally requires manual effort and is time-consuming. The **AI-Based Study Assistant** addresses this problem by providing a web-based educational tool that accepts a document, extracts its text, and generates study resources using a large language model.

The application is implemented using **FastAPI** and **Jinja2**, with a browser interface built from HTML, CSS, and vanilla JavaScript. Users can upload PDF, DOCX, PPTX, XLSX, PNG, JPG, JPEG, JSON, or TXT files. Uploaded data is converted into plain text and stored only in server memory for the current session. Groq API then generates summaries, practice questions, interactive multiple-choice questions, and topic explanations grounded in the uploaded material.

The project intentionally avoids a vector database and persistent document storage. This makes the proof of concept simpler, privacy-conscious, and suitable for demonstrating document parsing, prompt engineering, REST API development, asynchronous routing, and responsive user-interface design.

<div style="page-break-after: always;"></div>

## Page 6 — Table of Contents

1. Certificate  
2. Declaration  
3. Acknowledgment  
4. Abstract  
5. Introduction  
6. Problem Statement  
7. Objectives and Scope  
8. Literature Survey  
9. Requirement Analysis  
10. Technology Selection  
11. System Architecture  
12. Module Design  
13. Document Processing  
14. AI Service and Prompt Design  
15. User Interface Design  
16. Database and Storage Design  
17. Security and Validation  
18. API Design  
19. Implementation Details  
20. Testing Strategy  
21. Results and Discussion  
22. Deployment Considerations  
23. Limitations  
24. Future Enhancements  
25. Conclusion  
26. References  
27. Appendices

<div style="page-break-after: always;"></div>

## Page 7 — List of Figures

- Figure 1: High-level system architecture
- Figure 2: Application request flow
- Figure 3: Dashboard layout
- Figure 4: File-upload workflow
- Figure 5: AI request workflow
- Figure 6: Interactive MCQ workflow
- Figure 7: Responsive desktop layout
- Figure 8: Responsive mobile drawer layout
- Figure 9: Error-handling workflow
- Figure 10: In-memory document lifecycle

Final printed versions can insert actual screenshots and UML-style diagrams at the locations identified in the implementation and testing sections.

<div style="page-break-after: always;"></div>

## Page 8 — List of Tables

- Table 1: Functional requirements
- Table 2: Non-functional requirements
- Table 3: Supported input formats
- Table 4: API endpoint summary
- Table 5: Python dependencies
- Table 6: Unit and integration test cases
- Table 7: Error-handling scenarios
- Table 8: Security controls
- Table 9: Performance considerations
- Table 10: Comparison with traditional study workflows

<div style="page-break-after: always;"></div>

## Page 9 — Abbreviations

| Abbreviation | Meaning |
|---|---|
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| CSS | Cascading Style Sheets |
| DOCX | Microsoft Word Document |
| DOM | Document Object Model |
| HTML | HyperText Markup Language |
| JSON | JavaScript Object Notation |
| LLM | Large Language Model |
| MCQ | Multiple-Choice Question |
| OCR | Optical Character Recognition |
| PDF | Portable Document Format |
| POC | Proof of Concept |
| PPTX | Microsoft PowerPoint Presentation |
| RAM | Random Access Memory |
| REST | Representational State Transfer |
| TXT | Plain Text |
| UI | User Interface |
| UX | User Experience |
| XLSX | Microsoft Excel Workbook |

<div style="page-break-after: always;"></div>

## Page 10 — Chapter 1: Introduction

Digital education has increased the amount of material students must read and revise. Academic content may be distributed as slide decks, PDF handouts, Word files, spreadsheets, screenshots, or plain-text notes. Students often need summaries, question banks, and explanations while preparing for examinations.

The AI-Based Study Assistant is designed to reduce the time required to convert study material into usable revision content. It provides a single interface where a student uploads a document and then selects an AI-assisted operation. The extracted text is sent to Groq with a controlled system prompt so that generated output remains grounded in the document.

The system is intentionally implemented as a proof of concept. It demonstrates an end-to-end AI workflow without introducing a database, vector store, authentication system, or distributed infrastructure. This keeps the project focused on document parsing, API design, prompt engineering, and responsive web development.

<div style="page-break-after: always;"></div>

## Page 11 — Background and Motivation

Traditional study workflows require students to read long documents, highlight important topics, manually create questions, and search for explanations. Although general-purpose AI chat tools can help, they usually require users to copy and paste text manually. This process is inconvenient for large or formatted files and can lead to missing content.

An integrated assistant improves this workflow by accepting the source document directly. It can normalize multiple formats into text, retain that text temporarily, and apply reusable prompts for common academic tasks. Students receive consistent output without needing to design prompts themselves.

The project also demonstrates practical software-engineering concepts. File parsers isolate format-specific logic, a memory store isolates session state, an AI service isolates the language-model provider, and routes expose clear HTTP endpoints. This structure makes the system understandable and maintainable.

<div style="page-break-after: always;"></div>

## Page 12 — Problem Statement

Students need a simple way to convert study documents into summaries, questions, MCQs, and explanations. Existing workflows often require several applications: a document reader, a text extractor, an AI chat application, and a notes editor. These workflows are fragmented and may permanently upload documents to third-party systems.

The problem addressed by this project is to build a browser-based assistant that:

- Accepts common academic file formats.
- Converts them into plain text.
- Keeps extracted text only in temporary memory.
- Generates grounded study material using Groq.
- Presents results through a responsive and usable interface.
- Avoids embeddings, vector databases, and persistent storage.

The resulting system should be easy to install, easy to demonstrate, and suitable as a final-year proof of concept.

<div style="page-break-after: always;"></div>

## Page 13 — Project Objectives

The primary objectives are:

1. Build a complete FastAPI-only web application without a separate frontend framework.
2. Support PDF, DOCX, PPTX, XLSX, image, JSON, and TXT uploads.
3. Convert uploaded files into normalized plain text.
4. Store only one document in RAM for the current process.
5. Validate file extension, MIME type, file size, and empty content.
6. Generate short and detailed summaries.
7. Generate short-answer, long-answer, and viva questions.
8. Generate exactly ten interactive MCQs with answer feedback.
9. Explain a user-selected topic using only uploaded content.
10. Provide copy and TXT-download functionality.
11. Produce a responsive blue-and-white educational dashboard.
12. Keep the Groq provider isolated in a replaceable service module.

These objectives combine document engineering, web development, AI integration, and user-experience design.

<div style="page-break-after: always;"></div>

## Page 14 — Scope of the Project

The system supports one active document at a time. A new upload replaces the previous extracted text, and restarting the server clears all content. This behavior is intentional for a proof of concept and reduces privacy and persistence concerns.

The project includes server-rendered pages, client-side asynchronous calls, document parsing, OCR, prompt templates, response sanitization, interactive scoring, and automated API tests. It does not include user accounts, document history, collaborative workspaces, embeddings, semantic search, or database persistence.

Because the complete extracted text is appended to the request, very large documents can exceed a model's context window or token quota. For this reason, the current version is best suited to lecture notes, chapters, slides, and focused study material rather than entire books.

<div style="page-break-after: always;"></div>

## Page 15 — Expected Users and Use Cases

The primary users are students preparing for examinations, reviewing lecture material, or learning technical concepts. Teachers can also use it to generate draft quizzes and revision questions from lesson material.

Typical use cases include:

- Uploading lecture slides and generating a summary.
- Uploading a PDF chapter and producing practice questions.
- Uploading a worksheet and creating an interactive MCQ quiz.
- Uploading a technical note and requesting an explanation of one topic.
- Uploading an image containing readable printed text for OCR extraction.
- Uploading structured JSON or spreadsheet data and converting it into reviewable text.

The interface is intended to be understandable without technical training. Upload status, action labels, errors, and answer feedback are visible and direct.

<div style="page-break-after: always;"></div>

## Page 16 — Chapter 2: Literature Survey

AI-assisted learning systems have evolved from simple static content delivery to personalized and generative tools. Traditional educational software often provides fixed question banks or manually prepared summaries. Modern large language models can generate context-specific content dynamically.

Retrieval-Augmented Generation systems commonly use embeddings and a vector database to retrieve relevant passages. That architecture is appropriate for large document collections, but it introduces indexing, storage, embedding generation, and retrieval complexity. This project intentionally uses a simpler approach: the entire extracted document is included in the prompt for the current session.

This decision is appropriate for a POC because it eliminates vector-database dependencies and makes the document lifecycle transparent. It also demonstrates the trade-off between architectural simplicity and scalability.

<div style="page-break-after: always;"></div>

## Page 17 — Existing Approaches

Several approaches can answer questions or generate study material:

1. **Manual summarization:** Accurate but slow and dependent on student effort.
2. **Generic AI chat tools:** Flexible, but users must manually copy document text.
3. **Embedding-based RAG systems:** Suitable for large corpora, but require embeddings and vector storage.
4. **Static question banks:** Fast and predictable, but not personalized to a document.
5. **Integrated document assistants:** Upload a document and generate grounded outputs directly.

This project follows the fifth approach while avoiding the database complexity of a RAG system. The current document is parsed once, held in memory, and passed to Groq for each requested feature.

<div style="page-break-after: always;"></div>

## Page 18 — Comparison with RAG Architecture

A vector-based system normally divides a document into chunks, computes embeddings, stores vectors, retrieves the most relevant chunks, and sends them to an LLM. This improves scalability and allows many documents to be searched.

The implemented system does not generate embeddings or maintain a vector store. It uses direct context inclusion. This has advantages:

- No indexing time.
- No vector database installation.
- No embeddings generated or retained.
- Easier auditing because the full current document is known.
- Simpler proof-of-concept implementation.

The disadvantages are context-window limits and the absence of cross-document retrieval. For larger deployments, the AI service can later be changed to retrieval-based behavior without changing the browser-facing routes.

<div style="page-break-after: always;"></div>

## Page 19 — Relevance of Groq API

Groq provides low-latency access to hosted language models through an API compatible with chat-completion workflows. It is suitable for educational demonstrations because response time affects perceived usability, especially when users request summaries or quizzes.

The project separates Groq integration into `app/services/ai_service.py`. The service constructs messages, applies a common system prompt, sends document content, handles request errors, and normalizes structured MCQ output. Routes do not communicate with Groq directly.

This separation is important because a future implementation could replace Groq with another provider, such as OpenAI or a local model, while preserving the route and frontend contracts. Only the service implementation and configuration would need to change.

<div style="page-break-after: always;"></div>

## Page 20 — Chapter 3: Requirement Analysis

The project was designed from functional and non-functional requirements. Functional requirements describe what the application must do, while non-functional requirements describe usability, performance, privacy, security, and maintainability expectations.

A critical functional requirement is that every AI operation uses the currently uploaded document only. The system should clearly report errors when no document exists, when the file is unsupported, when parsing fails, or when the AI provider cannot complete a request.

Another important requirement is responsiveness. The interface must support desktop, tablet, and mobile screens. AI calls can take several seconds, so the interface must provide clear progress indicators and prevent duplicate submissions.

<div style="page-break-after: always;"></div>

## Page 21 — Functional Requirements

| ID | Requirement |
|---|---|
| FR-01 | Render a Jinja dashboard at `/`. |
| FR-02 | Accept PDF, DOCX, PPTX, XLSX, PNG, JPG, JPEG, JSON, and TXT. |
| FR-03 | Reject unsupported or mismatched file types. |
| FR-04 | Reject files larger than 20 MB. |
| FR-05 | Extract normalized plain text from supported files. |
| FR-06 | Store filename, type, content, timestamp, word count, and character count in RAM. |
| FR-07 | Replace the existing document when a new file is uploaded. |
| FR-08 | Generate a structured summary through `/summarize`. |
| FR-09 | Generate practice questions through `/practice`. |
| FR-10 | Generate exactly ten MCQs through `/mcq`. |
| FR-11 | Explain a supplied topic through `/explain`. |
| FR-12 | Display and score selected MCQ options in the browser. |
| FR-13 | Provide copy and TXT-download actions. |

<div style="page-break-after: always;"></div>

## Page 22 — Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR-01 | Use asynchronous FastAPI endpoints where appropriate. |
| NFR-02 | Keep the UI responsive on desktop and mobile. |
| NFR-03 | Display progress during uploads and AI requests. |
| NFR-04 | Sanitize filenames and generated HTML. |
| NFR-05 | Avoid document persistence and embeddings. |
| NFR-06 | Return friendly error messages. |
| NFR-07 | Isolate provider logic for maintainability. |
| NFR-08 | Use modular routes and services. |
| NFR-09 | Support automated testing with FastAPI TestClient. |
| NFR-10 | Keep uploaded data limited to one process and session. |

These requirements prioritize clarity and privacy while still providing a complete end-to-end educational workflow.

<div style="page-break-after: always;"></div>

## Page 23 — Input Requirements

The upload subsystem accepts eight extension families. Each extension is mapped to a parser and an allowed MIME type set. This protects against a file being renamed to a supported extension while declaring an unrelated content type.

| Format | Extensions | Extraction Method |
|---|---|---|
| PDF | `.pdf` | PyMuPDF page text extraction |
| Word | `.docx` | Paragraph and table text extraction |
| PowerPoint | `.pptx` | Slide and text-box extraction |
| Excel | `.xlsx` | Sheet and row conversion |
| Images | `.png`, `.jpg`, `.jpeg` | Pillow preprocessing and Tesseract OCR |
| JSON | `.json` | Pretty-printed structured text |
| Text | `.txt` | Direct UTF-8 reading |

The maximum file size is 20 MB. Empty files and files that produce no text are rejected.

<div style="page-break-after: always;"></div>

## Page 24 — Output Requirements

Each AI feature produces a different output contract:

- **Summary:** short summary, detailed summary, key takeaways, and important topics.
- **Practice:** five short-answer questions, three long-answer questions, and two viva questions with difficulty labels.
- **MCQ:** exactly ten questions, each with four options, a correct answer, and an explanation.
- **Explanation:** explanation, real-world example, and analogy where applicable.

Markdown-based results are converted to HTML and sanitized before being inserted into the page. MCQs use structured JSON so the frontend can attach click behavior, answer styling, explanations, progress, and scoring.

<div style="page-break-after: always;"></div>

## Page 25 — Technology Selection

FastAPI was selected because it provides a concise routing model, asynchronous support, automatic request validation through Pydantic, and convenient integration with Jinja2 and static files. Uvicorn provides the ASGI server.

Jinja2, HTML5, CSS3, and vanilla JavaScript provide the interface without requiring a separate React build pipeline. This reduces project complexity and allows the application to be demonstrated with a single Python process.

Document processing uses PyMuPDF, python-docx, python-pptx, openpyxl, Pillow, and pytesseract. These libraries are established and cover the required formats. Groq is used as the only AI provider in the current implementation.

<div style="page-break-after: always;"></div>

## Page 26 — Dependency Summary

| Dependency | Purpose |
|---|---|
| FastAPI | Web framework and API routing |
| Uvicorn | ASGI server |
| Jinja2 | Server-side templates |
| python-multipart | Multipart file uploads |
| Groq Python SDK | LLM API client |
| PyMuPDF | PDF text extraction |
| python-docx | DOCX paragraphs and tables |
| python-pptx | PPTX slide text |
| openpyxl | XLSX sheet processing |
| Pillow | Image loading and preprocessing |
| pytesseract | OCR interface |
| Markdown | Markdown-to-HTML conversion |
| Bleach | Generated HTML sanitization |
| pytest/httpx | Automated testing |

This dependency set supports the required POC while avoiding vector database packages.

<div style="page-break-after: always;"></div>

## Page 27 — Chapter 4: System Architecture

The application follows a layered design:

1. **Presentation layer:** Jinja templates, CSS, and JavaScript.
2. **Route layer:** FastAPI endpoints for pages, uploads, and AI features.
3. **Service layer:** file parsing, memory storage, prompts, and Groq calls.
4. **External services:** Groq API and the local Tesseract executable.

The browser submits a file to `/upload`. The route validates and stores it temporarily, sends the temporary path to the parser, stores extracted content in `MemoryStore`, and deletes the temporary file. Later AI requests read only the in-memory content.

This architecture is intentionally compact. It avoids unnecessary infrastructure while keeping separate concerns in separate modules.

<div style="page-break-after: always;"></div>

## Page 28 — High-Level Request Flow

```text
Browser
  |
  |-- Upload file --> /upload
  |                    |
  |                    +--> Validate filename, MIME type, and size
  |                    +--> Save temporary file
  |                    +--> FileParser.extract_text()
  |                    +--> MemoryStore.set()
  |                    +--> Delete temporary file
  |
  |-- Select action --> /summarize, /practice, /mcq, /explain
                          |
                          +--> MemoryStore.get()
                          +--> Build common prompt + document text
                          +--> Groq chat completion
                          +--> Sanitize or normalize response
                          +--> Render in dashboard
```

The document remains only in server process memory and disappears on restart or replacement.

<div style="page-break-after: always;"></div>

## Page 29 — Module Design

The root `app/` package is organized as follows:

```text
app/
├── main.py
├── routes/
│   ├── pages.py
│   ├── upload.py
│   └── ai.py
├── services/
│   ├── file_parser.py
│   ├── memory_store.py
│   ├── prompts.py
│   └── ai_service.py
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── result.html
│   └── partials/
├── static/
│   ├── css/style.css
│   ├── js/app.js
│   └── icons/
└── uploads/
```

Routes handle HTTP details. Services contain document, storage, prompt, and AI logic. Templates define page structure, while static assets provide styling and interactivity.

<div style="page-break-after: always;"></div>

## Page 30 — Application Entry Point

`app/main.py` initializes the FastAPI application, loads environment variables, mounts static files, and includes the page, upload, and AI routers. It also exposes `/health`, which reports the service status and AI provider name.

The application can be started using:

```bash
uvicorn app.main:app --reload
```

Because document content is stored in process memory, the proof of concept should run as a single worker. Multiple workers would maintain separate memory stores, causing inconsistent document availability between requests.

<div style="page-break-after: always;"></div>

## Page 31 — Upload Module

The upload route sanitizes the filename, checks the extension, verifies the declared MIME type, limits the request to 20 MB, and rejects empty files. Content is written to an operating-system temporary file because parsing libraries expect a file path.

After extraction, the temporary file is deleted in a `finally` block. This ensures cleanup even when parsing fails. The extracted content is then stored in memory and metadata is returned to the browser.

The upload route deliberately does not execute uploaded content. Office files are opened as data by parsing libraries, and image files are passed only to OCR.

<div style="page-break-after: always;"></div>

## Page 32 — File Parser Design

`FileParser` maps extensions to parser methods. Each parser returns a plain string, which is stripped and checked for non-empty content.

- PDF text is appended page by page.
- DOCX paragraphs and table rows are combined.
- PPTX slides and text-bearing shapes are extracted.
- XLSX rows are converted into readable label-value sentences.
- Images are converted to grayscale, contrast-enhanced, and OCR processed.
- JSON is pretty-printed.
- TXT is read as UTF-8 text.

A dedicated `FileParsingError` converts parser failures into user-friendly HTTP errors without exposing internal implementation details.

<div style="page-break-after: always;"></div>

## Page 33 — Memory Store Design

`MemoryStore` stores one `StoredDocument` object containing:

- filename
- file type
- extracted text
- upload timestamp
- word count
- character count

A reentrant lock protects reads and writes if concurrent requests access the store. `metadata()` returns document information without exposing the full extracted content.

The store has `set()`, `get()`, `metadata()`, and `clear()` methods. It does not write to disk or a database. A restart clears content automatically, and a new upload replaces the old document.

<div style="page-break-after: always;"></div>

## Page 34 — Prompt Design

All features share a common system prompt requiring the model to:

- Answer only from uploaded document content.
- Use simple English.
- Use headings and bullet points.
- State clearly if content is unavailable.
- Avoid inventing information outside the document.
- Return clean output without code fences unless JSON is explicitly requested.

Feature-specific prompts describe the required sections or JSON schema. Prompt centralization in `prompts.py` makes prompt behavior easier to review and modify.

The MCQ prompt requests a strict JSON object with a `questions` array. This enables deterministic browser rendering rather than relying on fragile Markdown parsing.

<div style="page-break-after: always;"></div>

## Page 35 — AI Service Design

`GroqAIService` creates requests using the current in-memory document and the shared prompt. It supports four public operations:

- `summarize_document()`
- `generate_practice_questions()`
- `generate_mcqs()`
- `explain_topic(user_prompt)`

The service checks for a document and API key before sending a request. Provider exceptions are wrapped in `AIServiceError` so routes can return a controlled 503 response. Missing documents produce a 400 response.

For MCQs, JSON mode is requested and the result is validated for exactly ten questions, four options, a valid answer letter, and an explanation.

<div style="page-break-after: always;"></div>

## Page 36 — MCQ Response Normalization

The expected MCQ structure is:

```json
{
  "questions": [
    {
      "number": 1,
      "question": "Question text?",
      "options": {
        "A": "First option",
        "B": "Second option",
        "C": "Third option",
        "D": "Fourth option"
      },
      "correct_answer": "A",
      "explanation": "Why the answer is correct"
    }
  ],
  "total": 10
}
```

The service accepts option dictionaries or lists and normalizes them into A–D mappings. It validates that every required field exists and that the correct answer is one of the four letters.

<div style="page-break-after: always;"></div>

## Page 37 — User Interface Structure

The dashboard uses a fixed sidebar on desktop, a compact sidebar on tablet, and a slide-in drawer on mobile. The main content contains:

- Upload card
- Document metadata card
- Four action cards
- Topic explanation form
- Result card

The visual design uses a blue-and-white educational theme, translucent cards, soft shadows, gradients, rounded corners, and responsive spacing. Upload feedback includes drag highlighting, a progress bar, filename status, and toast notifications.

Results are displayed below the action area and can be copied or downloaded as TXT.

<div style="page-break-after: always;"></div>

## Page 38 — Loading and Interaction Design

AI operations may take several seconds. To improve perceived performance, the interface uses:

- Action-specific loading titles.
- Rotating progress messages.
- Animated loading dots.
- Skeleton result lines.
- Spinner on the active action card.
- Disabled duplicate actions.
- Friendly error panels with retry.

For MCQs, the browser displays a sticky score panel, progress bar, question-number badge, and answer status. Selecting an option disables that question's options, marks the selected answer, highlights the correct answer, and reveals the explanation.

<div style="page-break-after: always;"></div>

## Page 39 — Interactive MCQ Behavior

The frontend maps the structured API response into DOM elements. Each question card contains four option buttons. When an option is selected:

1. The card is marked answered.
2. All options for that question are disabled.
3. The selected option is styled green if correct.
4. The selected option is styled red if incorrect.
5. The correct option is highlighted in all cases.
6. The explanation is shown.
7. The score and progress values are updated.

After ten answers, the score panel displays final marks and percentage and exposes a retake button. Copy and download actions use a plain-text representation generated from the structured response.

<div style="page-break-after: always;"></div>

## Page 40 — API Design

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Dashboard page |
| GET | `/health` | Application and provider status |
| POST | `/upload` | Validate, extract, and store document text |
| GET | `/document` | Current document metadata |
| POST | `/summarize` | Generate summary |
| POST | `/practice` | Generate practice questions |
| POST | `/mcq` | Generate structured MCQs |
| POST | `/explain` | Explain a supplied topic |

Routes return JSON for API operations and HTML for the dashboard. Validation errors use appropriate HTTP status codes, including 400, 413, 415, 422, and 503.

<div style="page-break-after: always;"></div>

## Page 41 — Upload API Contract

A successful upload returns:

```json
{
  "message": "Document uploaded and processed successfully.",
  "document": {
    "filename": "notes.pdf",
    "filetype": "pdf",
    "uploaded_at": "2026-09-27T10:00:00+00:00",
    "word_count": 1200,
    "character_count": 8200
  }
}
```

Failures return an object with a `detail` property. Example:

```json
{"detail": "Unsupported format. Upload PDF, DOCX, PPTX, XLSX, PNG, JPG, JPEG, JSON, or TXT."}
```

The frontend reads `detail` and displays it as a toast or error panel.

<div style="page-break-after: always;"></div>

## Page 42 — Summary and Practice Contracts

Summary and practice routes return rendered and raw content:

```json
{
  "content": "## Short Summary\n...",
  "html": "<h2>Short Summary</h2>..."
}
```

Markdown is converted using Python-Markdown and sanitized using Bleach. Sanitization prevents generated script tags or unsafe HTML from being inserted into the dashboard.

The frontend inserts only the sanitized `html` value for display while retaining `content` for copy and download operations. This balances formatting quality with output safety.

<div style="page-break-after: always;"></div>

## Page 43 — MCQ API Contract

The `/mcq` endpoint returns a structured object rather than Markdown:

```json
{
  "questions": [
    {
      "number": 1,
      "question": "What is an embedded system?",
      "options": {
        "A": "A general-purpose computer",
        "B": "A dedicated-function computer",
        "C": "A database server",
        "D": "A text editor"
      },
      "correct_answer": "B",
      "explanation": "The document defines it as dedicated-function hardware."
    }
  ],
  "total": 10
}
```

This contract allows the browser to implement immediate answer checking, visual feedback, explanation display, live progress, final marks, and quiz retake behavior.

<div style="page-break-after: always;"></div>

## Page 44 — Explain API Contract

The explanation endpoint accepts:

```json
{"prompt": "Explain inheritance"}
```

It returns sanitized HTML and source Markdown:

```json
{
  "content": "## Explanation\n...",
  "html": "<h2>Explanation</h2>..."
}
```

The user prompt is constrained to between two and five hundred characters. The backend combines the supplied topic, shared system prompt, and current document content. The requested output includes an explanation, a real-world example, and a simple analogy if applicable.

<div style="page-break-after: always;"></div>

## Page 45 — Error Handling Design

The application handles these cases explicitly:

- No uploaded document.
- Unsupported extension.
- MIME type mismatch.
- File larger than 20 MB.
- Empty file.
- Empty extracted text.
- Corrupt document.
- OCR engine unavailable.
- OCR failure.
- Missing Groq key.
- Unsupported Groq model.
- Groq timeout or service error.
- Invalid or incomplete MCQ JSON.
- Invalid explanation prompt.

Errors are translated into friendly client-visible messages. Detailed exception text is not returned to the browser unnecessarily, reducing accidental exposure of internals.

<div style="page-break-after: always;"></div>

## Page 46 — Security Design

The project implements several security controls:

- Filename sanitization removes path components and unsafe characters.
- Temporary files use generated names and are deleted after parsing.
- Extensions and declared MIME types are checked.
- File size is limited to 20 MB.
- Uploaded content is never executed.
- AI-generated HTML is sanitized before display.
- MCQ content is inserted through DOM `textContent`, not raw HTML.
- The Groq API key is loaded from `.env` rather than committed to code.
- `.env` file permissions are restricted on the development machine.

These controls are suitable for a proof of concept, but a production system would require authentication, rate limiting, malware scanning, logging, and stronger deployment controls.

<div style="page-break-after: always;"></div>

## Page 47 — Privacy and Data Lifecycle

The application does not create a document database. The temporary upload exists only long enough for a parser to read it. Extracted text is held in a process-level object and is not written back to disk.

The lifecycle is:

1. Browser uploads a file.
2. Server validates it.
3. Temporary file is created.
4. Text is extracted.
5. Temporary file is deleted.
6. Extracted text is stored in memory.
7. AI features use the stored text.
8. A new upload replaces the stored document.
9. Server restart clears it.

This simple lifecycle supports a clear privacy story for the POC.

<div style="page-break-after: always;"></div>

## Page 48 — Chapter 5: Implementation Environment

The implementation uses a local Python virtual environment. Dependencies are pinned in `requirements.txt` for repeatable installation. Environment variables are stored in `.env` and loaded using `python-dotenv`.

The current environment includes:

- Python virtual environment `.venv`
- Groq Python SDK
- FastAPI and Uvicorn
- Tesseract OCR installed through Homebrew
- Static files served by FastAPI
- Test suite run through pytest

The application is launched from the repository root so `app` can be imported as a package.

<div style="page-break-after: always;"></div>

## Page 49 — Template Implementation

`index.html` provides the shared document shell, stylesheet, toast region, and JavaScript reference. `dashboard.html` extends it and defines the complete application layout.

Template inheritance keeps common elements in one file. A separate `result.html` and partial template are present for reusable result rendering, although the primary workflow dynamically injects results into the dashboard.

Static assets are versioned with a query string to ensure browsers receive updated JavaScript and CSS after UI changes. This prevents an older cached script from rendering the previous non-interactive MCQ result.

<div style="page-break-after: always;"></div>

## Page 50 — JavaScript Implementation

`app/static/js/app.js` implements the client workflow without a JavaScript framework. It uses `XMLHttpRequest` for upload progress and `fetch` for AI actions.

Important responsibilities include:

- Drag-and-drop file selection.
- Upload progress and status text.
- Document metadata updates.
- Action-specific loading messages.
- Duplicate-request prevention.
- API error display and retry.
- Structured MCQ rendering.
- Answer checking and final scoring.
- Clipboard copy and TXT download.
- Mobile drawer control.
- Current document restoration after page refresh while the server process remains active.

All user-visible MCQ values are inserted safely using DOM text APIs.

<div style="page-break-after: always;"></div>

## Page 51 — CSS Implementation

`app/static/css/style.css` implements the visual system using CSS custom properties, responsive grid layouts, media queries, gradients, and transitions.

Major components include:

- Sidebar and mobile drawer
- Glassmorphism cards
- Drag-and-drop zone
- Document statistics
- Action cards
- Loading orbs and skeletons
- Result prose
- MCQ score panel
- Answer states
- Error panel
- Toast notifications
- Responsive breakpoints at tablet and mobile widths

Correct answers use green styling, incorrect selected answers use red styling, and the correct option remains highlighted even after an incorrect choice.

<div style="page-break-after: always;"></div>

## Page 52 — Document Extraction Details

PDF extraction iterates through every page and appends page text. DOCX extraction collects paragraphs and table rows. PPTX extraction walks through slides and shapes that expose text. XLSX extraction reads each worksheet, treats the first row as headers, and combines cells into readable sentences.

For OCR, an image is loaded by Pillow, converted to grayscale, contrast-normalized, and passed to Tesseract. The implementation detects `TESSERACT_CMD`, `PATH`, and common Homebrew locations.

Each extraction path returns one normalized string. A parser error produces a clear message and prevents incomplete or misleading content from reaching the AI service.

<div style="page-break-after: always;"></div>

## Page 53 — AI Request Construction

Every AI request combines:

1. The common system prompt.
2. A feature-specific instruction.
3. An optional user topic.
4. The complete extracted document text.

This approach ensures all features share the same grounding rules. The service uses a low temperature to reduce randomness and improve consistency for educational output.

MCQ generation uses JSON response mode and result normalization. The frontend is therefore not dependent on regular expressions or Markdown parsing to identify options and answers.

<div style="page-break-after: always;"></div>

## Page 54 — Groq Model Configuration

The selected model is configured through `GROQ_MODEL`. The project previously used `llama-3.3-70b-versatile`, but the Groq account reported that the model was unavailable. A supported model was selected after querying the account's model list.

Model availability and rate limits can vary by account and Groq service tier. A ten-question MCQ response requires enough completion tokens. If a model's output-token quota is too small, Groq may reject the request or return truncated JSON. The service reports this as a friendly provider error.

A production version could implement model fallback or request a lower-verbosity MCQ format while preserving all required fields.

<div style="page-break-after: always;"></div>

## Page 55 — Chapter 6: Testing Strategy

Testing focuses on the reliable parts of the system that do not require live Groq calls. FastAPI TestClient exercises routes, upload validation, in-memory state, sanitized output, and structured MCQ contracts. Groq behavior is monkeypatched in tests so tests are deterministic and do not consume API quota.

Manual verification is still used for real parsing, OCR, and Groq calls. For example, a generated image containing readable text was uploaded through the API and successfully extracted by Tesseract.

The combination of automated tests and manual provider checks gives reasonable confidence for a proof of concept.

<div style="page-break-after: always;"></div>

## Page 56 — Automated Test Cases

| Test | Expected Result |
|---|---|
| Dashboard load | HTTP 200 and rendered page |
| TXT upload | Text extracted and metadata returned |
| Unsupported extension | HTTP 415 |
| AI request without document | HTTP 400 |
| Summary output | HTML sanitized |
| MCQ route | Structured questions and total returned |
| Invalid explain prompt | HTTP 422 |

The tests also clear the memory store before and after each case to prevent state leakage.

The verified suite contains seven passing tests. Provider calls are isolated and mocked, so test results do not depend on network availability or Groq quota.

<div style="page-break-after: always;"></div>

## Page 57 — Manual Test Results

Manual checks confirmed:

- The FastAPI application starts under Uvicorn.
- `/health` returns a healthy Groq provider status.
- The dashboard renders successfully.
- A TXT document uploads and is counted correctly.
- Groq model availability can be queried through the API.
- A supported model returns a successful explanation.
- Tesseract extracts text from a generated PNG.
- An image upload returns document metadata.
- A real MCQ request returns ten structured questions.
- Browser assets are served with updated cache-version parameters.

These checks cover startup, parsing, provider connectivity, response shape, and frontend asset delivery.

<div style="page-break-after: always;"></div>

## Page 58 — Results and Discussion

The application successfully converts supported study files into temporary text and provides four AI study tools through one dashboard. The summary and practice features return formatted Markdown rendered as safe HTML. The MCQ feature uses structured JSON to support immediate scoring. The explanation feature accepts a student-entered topic.

User experience was improved by adding loading states, progress text, skeletons, toasts, retry controls, and disabled actions. These details are important because AI requests have variable latency.

The project demonstrates that a useful proof of concept can be built without a database or embeddings. However, large document support would require a more scalable retrieval design.

<div style="page-break-after: always;"></div>

## Page 59 — Limitations

The current system has known limitations:

- Only one document is active at a time.
- Restarting the server clears the document.
- Multiple Uvicorn workers do not share memory.
- Very large documents may exceed context or token limits.
- OCR accuracy depends on image quality and installed Tesseract languages.
- The selected Groq model must be available to the API key.
- Generated questions should be reviewed before formal assessment.
- There is no authentication, authorization, or rate limiting.
- There is no persistent history or document library.
- The MCQ score is not stored after page reload.
- The report screenshots must be captured separately for a printed submission.

<div style="page-break-after: always;"></div>

## Page 60 — Conclusion, Future Work, and References

### Conclusion

The AI-Based Study Assistant demonstrates a complete FastAPI document-to-learning workflow. It accepts common file formats, extracts readable text, stores it temporarily, and uses Groq to produce summaries, questions, scored MCQs, and explanations. The system is modular, responsive, and suitable for a final-year proof of concept.

### Future Enhancements

- User authentication and saved study sessions
- Multiple simultaneous documents
- Optional persistent document history
- Retrieval-based context selection for large files
- Export results to PDF or DOCX
- Flashcards and spaced repetition
- Quiz timer and question navigation
- Multi-language OCR
- Accessibility improvements
- Production logging, rate limits, and monitoring

### References

- FastAPI documentation: `https://fastapi.tiangolo.com/`
- Groq documentation: `https://console.groq.com/docs`
- PyMuPDF documentation
- python-docx documentation
- python-pptx documentation
- openpyxl documentation
- Tesseract OCR documentation
- Jinja2 documentation
- OWASP file-upload guidance
