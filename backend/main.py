from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database.init_db import create_db_and_tables
from src.routers import todos
from src.utils.error_handlers import general_exception_handler

app = FastAPI(title="Todo API", version="1.0.0")

# Include routers
app.include_router(todos.router)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add exception handlers
app.add_exception_handler(Exception, general_exception_handler)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)