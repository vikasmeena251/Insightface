# 🧠 Face Similarity Checker – Code Editor Rules

## Project Context

A lightweight web app built using Python, Streamlit, and InsightFace to visually compare two faces and show a similarity score.

---

## Code Style and Structure

- Use descriptive, consistent variable names (`img1`, `face_app`, `similarity_score`)
- Write modular Python functions for reusable logic
- Avoid deeply nested code; prefer readability
- Use virtual environments for isolated setups
- Follow a clean folder layout (`components/`, `utils/`, etc.)

---

## Naming Conventions

- `snake_case` for variables and function names
- `PascalCase` for class names (if ever used)
- `UPPER_CASE` for constants
- Keep filenames lowercase with underscores (e.g., `face_utils.py`)

---

## Commit Guidelines

- Prefix with intent:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `refactor:` for code restructuring
  - `docs:` for README or usage updates
- Keep messages short and meaningful

---

## Deployment & Maintenance

- Target minimal footprint for deployment
- Make sure to test with small & large images
- Streamlit deploy options: Streamlit Cloud, Render, or custom VPS
- Keep `requirements.txt` lean and tested

---

## Author Notes

If adapting this into a larger platform, structure for scale:
- Add `core/`, `services/`, `components/`
- Refactor model loading and embedding to `utils/` or `lib/`
- Log errors and edge cases for image upload or model failure
