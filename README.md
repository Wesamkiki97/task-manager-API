# Task Manager API

A small REST API for managing tasks. I built this project to practice FastAPI, PostgreSQL, SQLAlchemy, Pydantic, and basic backend project structure.

## Features

- Create a task.
- Get all tasks.
- Filter tasks by completion status.
- Get one task by ID.
- Update a task.
- Delete a task.
- Return validated responses with Pydantic.

## Tech stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn

## Project structure

```text
task-manager-API/
|-- app/
|   |-- main.py
|   |-- database.py
|   |-- init_db.py
|   |-- models.py
|   |-- schemas.py
|   |-- routes/
|   |   `-- tasks.py
|   `-- services/
|       `-- task_service.py
|-- .env.example
|-- requirements.txt
`-- README.md
```

## Setup

1. Create and activate a virtual environment.
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Create a PostgreSQL database named `task_db`.
4. Set the database connection URL.

PowerShell:

```powershell
$env:DATABASE_URL="postgresql://postgres:your_password@localhost:5432/task_db"
```

Command Prompt:

```cmd
set DATABASE_URL=postgresql://postgres:your_password@localhost:5432/task_db
```

5. Create the table:

```bash
python -m app.init_db
```

6. Run the API:

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/tasks` | Create a task |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks?completed=true` | Filter completed tasks |
| GET | `/tasks/{task_id}` | Get one task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

Example request body:

```json
{
  "title": "Learn FastAPI",
  "completed": false
}
```

## Current scope

This is a learning project focused on CRUD operations and database integration. It does not currently include authentication, automated tests, Docker, or deployment configuration.

## Author

Wesam Kiki
