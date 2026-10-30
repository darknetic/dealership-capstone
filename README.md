# Car Dealership Review Capstone

A starter Django REST + React application for the dealership review capstone.

## Quick start (backend)
```bash
cd server
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```
Backend: http://127.0.0.1:8000/

## Demo API endpoints
- `GET /api/dealers/`
- `GET /api/dealers/<id>/`
- `GET /api/dealers/<id>/reviews/`
- `GET /api/dealers/state/<state>/`
- `GET /api/carmakes/`
- `POST /api/analyze/` with JSON `{"review": "Fantastic services"}`
- `POST /api/register/`
- `POST /api/login/` (Django session login; include cookies for subsequent requests)
- `POST /api/logout/`

Use `python manage.py seed_demo` to load sample dealers, makes, models, and reviews.

## Frontend
```bash
cd server/frontend
npm install
npm run dev
```
The Vite dev server proxies `/api` to Django. Set `VITE_API_BASE` if your backend is hosted elsewhere.

## Important
This is a working starter scaffold, not a guarantee of full rubric compliance. Course-provided starter code, exact endpoint names, IBM service credentials, deployment platform settings, and required screenshots may differ. Replace demo data and configure deployment secrets before submission. Capture genuine screenshots and save genuine command outputs; do not fabricate evidence.
