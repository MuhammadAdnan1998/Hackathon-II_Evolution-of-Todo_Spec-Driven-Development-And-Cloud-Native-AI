# Research Findings: Full-Stack Todo Web Application

## Database Schema Details

### Decision: SQLModel Todo Entity Schema
```python
from sqlmodel import SQLModel, Field, Column
from typing import Optional, List
from datetime import datetime
import enum

class PriorityEnum(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(min_length=1, max_length=255)
    completed: bool = Field(default=False)
    priority: PriorityEnum = Field(default=PriorityEnum.MEDIUM)
    tags: Optional[str] = Field(default=None)  # JSON string representation
    due_date: Optional[datetime] = Field(default=None)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=False)
```

### Rationale:
This schema design follows SQLModel best practices and includes all required fields from the specification. It uses proper type hints and validation constraints.

### Alternatives Considered:
- Using a separate Tags table with many-to-many relationship (more normalized but complex)
- Using a dedicated JSON column for tags (better for complex tag structures)

## API Endpoint Definitions

### Decision: RESTful API Endpoints
```
GET    /api/todos          # List all todos with optional filters
POST   /api/todos          # Create a new todo
GET    /api/todos/{id}     # Get a specific todo
PUT    /api/todos/{id}     # Update a specific todo
DELETE /api/todos/{id}     # Delete a specific todo
```

### Rationale:
Standard REST patterns provide predictable and scalable API design. These endpoints cover all required CRUD operations from the functional requirements.

### Request/Response Formats:
- Create/Update: JSON with {title, completed, priority, tags, due_date}
- Response: Full todo object with ID and timestamps
- Error responses: Standard format with message and status code

### Alternatives Considered:
- GraphQL API (more flexible but adds complexity)
- Different URL patterns (non-standard REST)

## Frontend Component Architecture

### Decision: Component Structure
- `pages/index.tsx`: Main dashboard with todo list and filter controls
- `components/TodoList.tsx`: Displays todos with sorting/filtering
- `components/TodoForm.tsx`: Form for creating/editing todos
- `components/TodoItem.tsx`: Individual todo display with action buttons
- `services/api.ts`: API client for backend communication

### Rationale:
This structure follows Next.js best practices and provides clear separation of concerns. Components are reusable and maintainable.

### Alternatives Considered:
- Single-page app with client-side routing (less SEO-friendly)
- Different component organization patterns (would complicate maintenance)

## Neon DB Configuration

### Decision: Environment Variables and Connection String
```
DATABASE_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require
```

### Rationale:
Neon provides standard PostgreSQL connection strings that work directly with SQLModel. The sslmode=require ensures secure connections.

### Configuration Details:
- Connection pooling settings managed by Neon
- Environment variables stored in .env.local for local development
- Separate configurations for development and production

### Alternatives Considered:
- Direct connection without Neon's serverless features (loses scalability benefits)
- Different environment variable naming schemes (less conventional)

## Next.js and FastAPI Integration

### Decision: API Communication Pattern
- Frontend makes HTTP requests to backend API endpoints
- Backend serves API responses in JSON format
- CORS configured to allow frontend domain access

### Rationale:
Standard HTTP communication is reliable, well-documented, and works across different deployment scenarios.

### Implementation Approach:
- Use fetch API or axios for HTTP requests
- Handle loading states and error responses appropriately
- Implement retry logic for failed requests

### Alternatives Considered:
- WebSocket connections (unnecessary complexity for basic CRUD)
- Server-side rendering with data fetching (would couple frontend and backend too tightly)