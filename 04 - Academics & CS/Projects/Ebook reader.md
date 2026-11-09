---
course: "Projects"
tags:
  - course/projects
up: "[[Projects]]"
---

### Stack (recommended)
- **UI shell:**  
  - **Option A (Python-native):** PySide6/PyQt6 (native widgets, one-language stack).  
  - **Option B (Hybrid, more modern UI):** Electron or Tauri UI + Python backend (FastAPI) for AI tasks. Given Python preference, start with **PySide6** to ship faster; you can swap the UI later if needed.
- **EPUB rendering:** `epub.js` inside a webview (for nicer layout) or Python EPUB parsing (`ebooklib`) + display HTML in a Qt WebEngine view.
- **Local LLM (text → image prompt):** **Ollama** (run models locally; call via HTTP). Models: LLaMA 3.1 8B Instruct, Mistral 7B Instruct, Phi-3 Mini.
- **Local image generation:** Python + **Diffusers** (SD 1.5 for lighter VRAM, SDXL if hardware allows) behind a tiny **FastAPI** endpoint. (You can also point to Automatic1111/ComfyUI API if already running.)
- **Cloud image option:** One provider to start—**OpenAI DALL·E 3** or **Stability AI**. User supplies API key in settings.
- **Storage/config/cache:** **SQLite** (via `sqlite3` or `SQLModel/SQLAlchemy`) for settings, page→image cache, and service toggles.

### High-level architecture
- **UI process (PySide6)**  
  - Two-page view: left = EPUB page, right = generated image.  
  - Buttons: next/prev page, regenerate image, toggle local/cloud, settings dialog.  
  - Communicates with a **local Python service** (could be in-process or a small FastAPI running locally).
- **Local service layer (FastAPI, can run as thread or subprocess)**  
  - Endpoints:  
    - `POST /prompt` → calls local LLM via Ollama with page text, returns image prompt.  
    - `POST /image/local` → uses Diffusers pipeline (or forwards to A1111/ComfyUI).  
    - `POST /image/cloud` → calls chosen cloud provider with API key.  
    - Future: `/translate`, `/summarize`, etc. (same input signature `{bookId, location, text}`).

### Suggested folder structure
- `app/`
  - `ui/` (PySide6 windows/views, webview for EPUB, two-page layout)
  - `services/`
    - `epub_loader.py` (ebooklib utilities, extract page HTML/text)
    - `prompt_service.py` (calls Ollama)
    - `image_service.py` (local Diffusers + cloud adapters)
    - `translate_service.py` (future)
  - `api/` (FastAPI routers wrapping services)
  - `config/` (SQLite helpers, config models)
  - `assets/` (icons, styles)
- `main.py` (starts UI and spins up FastAPI in background)

### Phase roadmap (practical)
**Week 1: Setup & basic reader**
- Learn/refresh PySide6 basics: windows, layouts, signals/slots, embedding a webview (Qt WebEngineView) for HTML.
- Parse EPUB with `ebooklib`; render chapter/page HTML in the webview.
- Build two-page layout (split view); right pane placeholder.

**Week 2: Navigation & state**
- Implement spine/chapter navigation and “current page” state.
- Add settings storage (SQLite or JSON) for user prefs (font size, theme, model choices).
- Ensure you can extract **plain text** for the current page (strip HTML) to feed the LLM.

**Week 3: Local LLM integration**
- Install **Ollama**; pull a small model (e.g., `phi3` or `llama3.1:8b`).
- Write `prompt_service.py`:
  - Prompt template: “Summarize this page in 1–2 sentences, then give a single, vivid image prompt. Output only the image prompt.”
  - Call Ollama HTTP; parse response.
- Wire UI button “Generate prompt” and display the prompt for debugging.

**Weeks 4–5: Local image generation**
- Set up **Diffusers** (Python): start with SD 1.5, CPU or CUDA if available.
- Create `image_service.py` with a simple pipeline (respect width/height/seed).
- Expose `POST /image/local` via FastAPI; return base64 or file path.
- In UI, call endpoint, show the image on the right pane.
- Add caching: store page→image path in SQLite; reuse unless “Regenerate” pressed.

**Week 6: Cloud image option**
- Add provider (OpenAI DALL·E 3 or Stability):
  - Settings: API key, model, style preset.
  - Endpoint `POST /image/cloud` selects provider based on config.
- UI toggle for local vs cloud.

**Week 7: Polish and modularity**
- Refactor services behind interfaces so adding `/translate` or `/summarize` reuses the same pattern.
- Add minimal diagnostics screen: model reachability (Ollama up? Diffusers ready? API key valid?).

**Later (optional)**
- Translation: start with a cloud API (DeepL/Google) for speed; later add local (NLLB, M2M100 with CTranslate2).
- Summaries/notes: reuse the same local LLM.
- Packaging: use PyInstaller or Briefcase to bundle the app; test on Windows/macOS/Linux.

### Key concepts to learn (ordered)
1. **PySide6**: layouts, signals, webview (Qt WebEngine), file dialogs.
2. **EPUB handling**: `ebooklib`, HTML extraction, pagination strategies.
3. **FastAPI** basics: routes, Pydantic models, running inside the app process (uvicorn in a thread) or as a subprocess.
4. **Calling local LLMs**: Ollama HTTP API, prompt design.
5. **Diffusers**: loading SD 1.5, safety checker off/on, seeds, sizing; basic CUDA setup.
6. **Cloud APIs**: auth with API keys, error handling, rate limits.
7. **Persistence**: SQLite for settings/cache; simple migrations.
8. **Packaging**: PyInstaller/Briefcase; handling model downloads/cache directories.

### Practical tips
- Start with **local only** (prompt + SD 1.5) before cloud to reduce moving parts.
- Keep the **service API stable**: `{ text, style, seed, width, height, provider }` for images; `{ text }` for prompt.
- Cache aggressively: once an image is generated for a page, reuse until the user changes model/style or clicks regenerate.
- For responsiveness: run generation calls off the UI thread (threads or background workers).
- Use **logging + a small diagnostics panel** early; it saves time debugging GPU/driver/API issues.

If you want, I can draft a minimal `FastAPI` + PySide6 skeleton with one endpoint (`/prompt`) and the two-pane UI to get you started.

<!-- connections:start -->
---
> [!abstract] 🔗 Connections
> **Up:** [[Projects]] · **Map:** [[MOC]]
> **Prev:** [[04 - Academics & CS/Projects/Calibre Book reader|Calibre Book reader]] · **Next:** [[04 - Academics & CS/Projects/Library Pass System|Library Pass System]]
> **Related:** [[AI & ML Roadmap]] · [[Career]] · [[Data Structures]]
<!-- connections:end -->
