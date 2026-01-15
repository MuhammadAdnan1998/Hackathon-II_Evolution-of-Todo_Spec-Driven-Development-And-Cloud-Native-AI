import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from main import app
from src.models.todo import Todo
from src.database.session import get_session

# Create a test database in memory
@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(bind=engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

def test_create_todo(client: TestClient):
    todo_data = {
        "title": "Test todo",
        "completed": False,
        "priority": "medium",
        "tags": "test,important",
        "due_date": "2023-12-31T10:00:00"
    }
    response = client.post("/api/todos", json=todo_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test todo"
    assert data["completed"] == False
    assert data["priority"] == "medium"
    assert data["tags"] == "test,important"

def test_read_todos(client: TestClient, session: Session):
    # Create a todo first
    todo_data = {
        "title": "Test todo",
        "completed": False,
        "priority": "medium"
    }
    client.post("/api/todos", json=todo_data)

    response = client.get("/api/todos")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Test todo"

def test_read_todo(client: TestClient, session: Session):
    # Create a todo first
    todo_data = {
        "title": "Test todo",
        "completed": False,
        "priority": "medium"
    }
    response = client.post("/api/todos", json=todo_data)
    created_todo = response.json()
    todo_id = created_todo["id"]

    response = client.get(f"/api/todos/{todo_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test todo"

def test_update_todo(client: TestClient, session: Session):
    # Create a todo first
    todo_data = {
        "title": "Test todo",
        "completed": False,
        "priority": "medium"
    }
    response = client.post("/api/todos", json=todo_data)
    created_todo = response.json()
    todo_id = created_todo["id"]

    # Update the todo
    update_data = {
        "title": "Updated todo",
        "completed": True
    }
    response = client.put(f"/api/todos/{todo_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated todo"
    assert data["completed"] == True

def test_delete_todo(client: TestClient, session: Session):
    # Create a todo first
    todo_data = {
        "title": "Test todo",
        "completed": False,
        "priority": "medium"
    }
    response = client.post("/api/todos", json=todo_data)
    created_todo = response.json()
    todo_id = created_todo["id"]

    # Delete the todo
    response = client.delete(f"/api/todos/{todo_id}")
    assert response.status_code == 200

    # Verify it's deleted
    response = client.get(f"/api/todos/{todo_id}")
    assert response.status_code == 404

def test_filter_todos_by_priority(client: TestClient, session: Session):
    # Create todos with different priorities
    client.post("/api/todos", json={"title": "Low priority", "priority": "low"})
    client.post("/api/todos", json={"title": "High priority", "priority": "high"})

    # Filter by priority
    response = client.get("/api/todos?priority=high")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["priority"] == "high"
    assert data[0]["title"] == "High priority"

def test_sort_todos(client: TestClient, session: Session):
    # Create todos
    client.post("/api/todos", json={"title": "Todo 1", "priority": "high"})
    client.post("/api/todos", json={"title": "Todo 2", "priority": "low"})

    # Sort by priority
    response = client.get("/api/todos?sort_by=priority&sort_order=desc")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    # High priority should come first
    assert data[0]["priority"] == "high"