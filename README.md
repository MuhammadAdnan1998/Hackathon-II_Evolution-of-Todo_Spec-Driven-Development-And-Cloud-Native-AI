# Full-Stack Todo Web Application - Phase II

This project represents Phase II of the Todo application evolution, transforming from a console app to a full-stack web application using Next.js, FastAPI, and SQLModel with Neon DB.

## Tech Stack

- **Frontend**: Next.js 14+ with TypeScript
- **Backend**: FastAPI 0.100+ with Python 3.11+
- **Database**: SQLModel with Neon PostgreSQL database
- **API Communication**: REST API with JSON payload
- **Environment Management**: Environment variables via .env files

## Features

- Create, read, update, and delete todos
- Filter todos by completion status, priority, and tags
- Sort todos by priority, due date, and creation date
- Search todos by title
- Responsive UI that works on desktop and mobile devices
- User-friendly error handling and notifications

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your database configuration:
```bash
DATABASE_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Run the backend server:
```bash
python main.py
```

The backend will be available at `http://localhost:8000`.

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env.local` file:
```bash
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

4. Run the frontend development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`.

## API Endpoints

- `GET /api/todos` - List all todos with optional filters
- `POST /api/todos` - Create a new todo
- `GET /api/todos/{id}` - Get a specific todo
- `PUT /api/todos/{id}` - Update a specific todo
- `DELETE /api/todos/{id}` - Delete a specific todo

## Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

## Development

### Backend Development
The backend uses FastAPI which provides automatic API documentation at `/docs` when running in development mode.

### Frontend Development
The frontend uses Next.js with hot reloading for a smooth development experience.

## Testing

Backend tests can be run using pytest:
```bash
cd backend
python -m pytest tests/
```

## Deployment

### Backend Deployment
The backend can be deployed to any platform that supports Python applications (e.g., Heroku, AWS, Google Cloud).

### Frontend Deployment
The frontend can be deployed to any platform that supports Next.js applications (e.g., Vercel, Netlify, AWS Amplify).

## Milestone: Phase II

This implementation represents Milestone Phase II of the Todo application evolution, featuring a complete full-stack web application with all core functionality implemented.