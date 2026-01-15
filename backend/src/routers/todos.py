from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List, Optional
from ..database.session import get_session
from ..models.todo import Todo, TodoCreate, TodoUpdate
from ..services.todo_service import (
    create_todo,
    get_todo_by_id,
    get_todos,
    update_todo,
    delete_todo
)

router = APIRouter(prefix="/api/todos", tags=["todos"])

@router.get("/", response_model=List[Todo])
def read_todos(
    completed: Optional[bool] = None,
    priority: Optional[str] = None,
    search: Optional[str] = None,
    tags: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: Optional[str] = None,
    limit: int = 100,
    offset: int = 0,
    session: Session = Depends(get_session)
):
    """
    Retrieve a list of todos with optional filtering and sorting
    """
    todos = get_todos(
        session=session,
        completed=completed,
        priority=priority,
        search=search,
        tags=tags,
        sort_by=sort_by,
        sort_order=sort_order,
        limit=limit,
        offset=offset
    )
    return todos

@router.post("/", response_model=Todo)
def create_new_todo(
    todo: TodoCreate,
    session: Session = Depends(get_session)
):
    """
    Create a new todo item
    """
    return create_todo(session=session, todo=todo)

@router.get("/{todo_id}", response_model=Todo)
def read_todo(
    todo_id: int,
    session: Session = Depends(get_session)
):
    """
    Retrieve a specific todo by ID
    """
    db_todo = get_todo_by_id(session=session, todo_id=todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.put("/{todo_id}", response_model=Todo)
def update_existing_todo(
    todo_id: int,
    todo_update: TodoUpdate,
    session: Session = Depends(get_session)
):
    """
    Update an existing todo item
    """
    db_todo = update_todo(session=session, todo_id=todo_id, todo_update=todo_update)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.delete("/{todo_id}")
def delete_existing_todo(
    todo_id: int,
    session: Session = Depends(get_session)
):
    """
    Delete an existing todo item
    """
    success = delete_todo(session=session, todo_id=todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}