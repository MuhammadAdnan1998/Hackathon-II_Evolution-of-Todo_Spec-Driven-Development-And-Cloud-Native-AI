from sqlmodel import Session, select
from sqlalchemy import desc, asc
from ..models.todo import Todo, TodoCreate, TodoUpdate
from typing import List, Optional
from datetime import datetime

def create_todo(session: Session, todo: TodoCreate) -> Todo:
    db_todo = Todo(**todo.model_dump())
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

def get_todo_by_id(session: Session, todo_id: int) -> Optional[Todo]:
    return session.get(Todo, todo_id)

def get_todos(
    session: Session,
    completed: Optional[bool] = None,
    priority: Optional[str] = None,
    search: Optional[str] = None,
    tags: Optional[str] = None,  # For tag filtering
    sort_by: Optional[str] = None,  # 'priority', 'due_date', 'created_at'
    sort_order: Optional[str] = None,  # 'asc' or 'desc'
    limit: int = 100,
    offset: int = 0
) -> List[Todo]:
    query = select(Todo)

    if completed is not None:
        query = query.where(Todo.completed == completed)

    if priority is not None:
        query = query.where(Todo.priority == priority)

    if search is not None:
        query = query.where(Todo.title.contains(search))

    # Filter by tags if provided
    if tags is not None:
        if tags.strip():  # Only filter if tags parameter is not empty
            # This checks if the tags field contains the specified tag (case-insensitive)
            # In a real application, you might want to implement more sophisticated tag matching
            query = query.where(Todo.tags.contains(tags.strip()))
        else:  # If tags is provided but empty, match records with any tags
            query = query.where(Todo.tags.is_not(None))

    # Apply sorting
    if sort_by:
        if sort_by == 'priority':
            if sort_order == 'desc':
                query = query.order_by(desc(Todo.priority))
            else:
                query = query.order_by(asc(Todo.priority))
        elif sort_by == 'due_date':
            if sort_order == 'desc':
                query = query.order_by(desc(Todo.due_date))
            else:
                query = query.order_by(asc(Todo.due_date))
        elif sort_by == 'created_at':
            if sort_order == 'desc':
                query = query.order_by(desc(Todo.created_at))
            else:
                query = query.order_by(asc(Todo.created_at))

    query = query.offset(offset).limit(limit)

    return session.execute(query).all()

def update_todo(session: Session, todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        return None

    update_data = todo_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)

    db_todo.updated_at = datetime.utcnow()

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

def delete_todo(session: Session, todo_id: int) -> bool:
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        return False

    session.delete(db_todo)
    session.commit()
    return True