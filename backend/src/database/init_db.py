from sqlmodel import SQLModel
from .session import engine
from ..models.todo import Todo

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)