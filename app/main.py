import os
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import Base, SessionLocal, engine, get_db
from app.models import Todo
from app.schemas import TodoCreate, TodoResponse, TodoUpdate
from app.crud import create_todo, delete_todo, get_todos, toggle_todo

APP_TITLE = os.getenv("APP_TITLE", "오늘의 할 일")

app = FastAPI(title=APP_TITLE)
Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="todo-app/static"), name="static")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"app_title": APP_TITLE})


@app.get("/api/todos", response_model=list[TodoResponse])
def read_todos(status: str = "all", db: Session = Depends(get_db)):
    if status not in {"all", "active", "completed"}:
        raise HTTPException(status_code=422, detail="invalid status")
    return get_todos(db, status=status)


@app.post("/api/todos", response_model=TodoResponse, status_code=201)
def create_todo_api(todo_in: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo_in)


@app.patch("/api/todos/{todo_id}", response_model=TodoResponse)
def update_todo_api(todo_id: int, payload: TodoUpdate, db: Session = Depends(get_db)):
    todo = toggle_todo(db, todo_id, payload)
    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    return todo


@app.delete("/api/todos/{todo_id}", status_code=204)
def delete_todo_api(todo_id: int, db: Session = Depends(get_db)):
    todo = delete_todo(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    return None
