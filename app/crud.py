from sqlalchemy.orm import Session
from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate


def get_todos(db: Session, status: str = "all"):
    query = db.query(Todo)
    if status == "active":
        query = query.filter(Todo.completed.is_(False))
    elif status == "completed":
        query = query.filter(Todo.completed.is_(True))
    return query.order_by(Todo.id.asc()).all()


def create_todo(db: Session, todo_in: TodoCreate):
    title = todo_in.title.strip()
    if not title:
        raise ValueError('할 일을 입력해 주세요.')
    todo = Todo(title=title, completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def toggle_todo(db: Session, todo_id: int, payload: TodoUpdate):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        return None
    if payload.completed is not None:
        todo.completed = payload.completed
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        return None
    db.delete(todo)
    db.commit()
    return todo
