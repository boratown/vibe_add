import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import List

APP_TITLE = os.getenv("APP_TITLE", "오늘의 할 일")

app = FastAPI(title=APP_TITLE)
templates = Jinja2Templates(directory="todo-app/templates")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={"detail": exc.errors()})


todos: List[dict] = []
_next_id = 1


class TodoCreate(BaseModel):
    title: str = Field(min_length=1)


class TodoUpdate(BaseModel):
    completed: bool


class TodoOut(BaseModel):
    id: int
    title: str
    completed: bool


def _normalize_title(title: str) -> str:
    normalized = title.strip()
    if not normalized:
        raise HTTPException(status_code=422, detail="할 일을 입력해 주세요.")
    return normalized


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"app_title": APP_TITLE},
    )


@app.get("/api/todos", response_model=List[TodoOut])
async def get_todos() -> List[TodoOut]:
    return todos


@app.post("/api/todos", response_model=TodoOut, status_code=201)
async def create_todo(todo: TodoCreate) -> TodoOut:
    global _next_id
    normalized_title = _normalize_title(todo.title)
    new_todo = {"id": _next_id, "title": normalized_title, "completed": False}
    todos.append(new_todo)
    _next_id += 1
    return new_todo


@app.get("/api/todos/{todo_id}", response_model=TodoOut)
async def get_todo(todo_id: int) -> TodoOut:
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.patch("/api/todos/{todo_id}", response_model=TodoOut)
async def update_todo(todo_id: int, payload: TodoUpdate) -> TodoOut:
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = payload.completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/api/todos/{todo_id}", status_code=204)
async def delete_todo(todo_id: int) -> None:
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(index)
            return
    raise HTTPException(status_code=404, detail="Todo not found")
