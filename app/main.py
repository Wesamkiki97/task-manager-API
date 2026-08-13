from fastapi import FastAPI

from app.routes import tasks


app = FastAPI(title="Task Manager API")
app.include_router(tasks.router)


@app.get("/")
def home():
    return {"message": "Task Manager API is running"}




