from sqlmodel import SQLModel, Field, Column
from typing import Optional
from datetime import datetime
import enum

class PriorityEnum(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TodoBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    completed: bool = Field(default=False)
    priority: PriorityEnum = Field(default=PriorityEnum.MEDIUM)
    tags: Optional[str] = Field(default=None)  # JSON string representation
    due_date: Optional[datetime] = Field(default=None)

class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class TodoCreate(TodoBase):
    pass

class TodoUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    completed: Optional[bool] = None
    priority: Optional[PriorityEnum] = None
    tags: Optional[str] = None
    due_date: Optional[datetime] = None

class TodoSearch(SQLModel):
    completed: Optional[bool] = None
    priority: Optional[str] = None
    search: Optional[str] = None
    tags: Optional[str] = None  # For tag filtering