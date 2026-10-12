# Fencing101

A Python-powered beginner fencing website with a responsive English interface.

## Run locally

Requires Python 3. No third-party dependencies or build tools are needed.

From this folder, run:

```sh
python3 app.py
```

Open http://127.0.0.1:8765/ in your browser. Press Ctrl+C to stop.

If that port is busy:

```sh
python3 app.py --port 8000
```

## Files

- `app.py`: Python HTTP server, page routing, and `/health` endpoint.
- `index.html`: page content, responsive styling, illustrations, and interactive checklist.

The Python server serves only defined routes, rather than exposing the folder. It is intended for local use.

## Content

Weapon comparisons, basic rules, footwork, equipment, a glossary, FAQs, and a first-lesson checklist. References link to USA Fencing. Explanations are simplified; follow your coach and current competition rules.
