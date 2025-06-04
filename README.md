# fastapi-projects


This is a beginner-friendly FastAPI project for managing tasks (CRUD operations).

## Features
- Create, Read, Update, Delete tasks
- Mark tasks as completed
- SQLite database using SQLAlchemy
- Auto-generated OpenAPI documentation

## How to Run

1. Clone the repository:
```bash
git clone <your-repo-url>
cd task_manager
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn app.main:app --reload
```

4. Open your browser at `http://127.0.0.1:8000/docs`
