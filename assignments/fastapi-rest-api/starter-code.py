from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task Management API")

# TODO: Define your Task model using Pydantic BaseModel
# Include fields: id, title, description, completed

# In-memory storage for tasks
tasks = []

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to Task Management API"}


# TODO: Implement POST /tasks endpoint to create a new task


# TODO: Implement GET /tasks endpoint to get all tasks


# TODO: Implement GET /tasks/{task_id} endpoint to get a specific task


# TODO: Implement PUT /tasks/{task_id} endpoint to update a task


# TODO: Implement DELETE /tasks/{task_id} endpoint to delete a task


# To run this application:
# 1. Install dependencies: pip install -r requirements.txt
# 2. Run the server: uvicorn starter-code:app --reload
# 3. Visit http://localhost:8000/docs for interactive API documentation
