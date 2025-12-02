from fastapi import FastAPI
from app.database.database import Base, engine
from .routers import users, tasks

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routers
app.include_router(users.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "Task Manager API is running"}
