from typing import Optional

from pydantic import BaseModel, Field, field_validator


class TodoBase(BaseModel):
    title: str = Field(min_length=1)

    @field_validator('title')
    @classmethod
    def validate_title(cls, value: str) -> str:
        trimmed = value.strip()
        if not trimmed:
            raise ValueError('할 일을 입력해 주세요.')
        return trimmed


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    completed: Optional[bool] = None


class TodoResponse(TodoBase):
    id: int
    completed: bool
