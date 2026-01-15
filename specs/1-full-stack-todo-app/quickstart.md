# Quickstart Guide: Full-Stack Todo Web Application

## Prerequisites

- Node.js 18+ for Next.js frontend
- Python 3.11+ for FastAPI backend
- Access to Neon PostgreSQL database
- Git for version control

## Local Development Setup

### 1. Clone and Branch
```bash
git clone <repository-url>
git checkout phase-2
```

### 2. Backend Setup (FastAPI)
```bash
# Navigate to backend directory (will be created)
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn sqlmodel python-dotenv psycopg2-binary

# Create .env file with database configuration
echo "DATABASE_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require" > .env

# Run the backend
uvicorn main:app --reload
```

### 3. Frontend Setup (Next.js)
```bash
# Navigate to frontend directory (will be created)
cd frontend

# Install dependencies
npm install
# or
yarn install

# Create .env.local file
echo "NEXT_PUBLIC_API_BASE_URL=http://localhost:8000" > .env.local

# Run the frontend
npm run dev
# or
yarn dev
```

## Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://username:password@ep-xxxxx.us-east-1.aws.neon.tech/dbname?sslmode=require
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

## Running the Application

1. Start the backend server: `uvicorn main:app --reload`
2. Start the frontend server: `npm run dev`
3. Access the application at `http://localhost:3000`

## Database Migrations

When you make changes to the data model:

```bash
# Run from backend directory
python -m alembic revision --autogenerate -m "Description of changes"
python -m alembic upgrade head
```

## Testing the API

Test the API endpoints directly:

- `GET /api/todos` - List all todos
- `POST /api/todos` - Create a new todo
- `GET /api/todos/{id}` - Get specific todo
- `PUT /api/todos/{id}` - Update a todo
- `DELETE /api/todos/{id}` - Delete a todo

Example curl command:
```bash
curl -X POST http://localhost:8000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Test todo", "priority": "medium"}'
```

## Deployment Notes

- The backend should be deployed to a service that supports Python applications
- The frontend should be deployed to a service that supports Next.js applications
- Ensure environment variables are properly configured in the deployment environment
- Database connection strings should be secured and not hardcoded