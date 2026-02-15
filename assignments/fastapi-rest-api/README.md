# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, fast REST APIs using FastAPI framework. You'll create a complete API with endpoints for data operations, request validation, and automatic interactive documentation.

## 📝 Tasks

### 🛠️ Set Up FastAPI Project

#### Description
Initialize your FastAPI project and create a simple "Hello World" API endpoint to verify your setup is working correctly.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn server dependencies
- Create a basic FastAPI application instance
- Implement a GET endpoint at `/` that returns a welcome message
- Run the development server and test the endpoint
- Access the automatic interactive API documentation at `/docs`


### 🛠️ Create a Task Management API

#### Description
Build a RESTful API for managing a simple task list. Implement CRUD operations (Create, Read, Update, Delete) for tasks.

#### Requirements
Completed program should:

- Define a Task model with id, title, description, and completed status
- Implement POST `/tasks` endpoint to create new tasks
- Implement GET `/tasks` endpoint to retrieve all tasks
- Implement GET `/tasks/{task_id}` endpoint to retrieve a specific task
- Implement PUT `/tasks/{task_id}` endpoint to update a task
- Implement DELETE `/tasks/{task_id}` endpoint to delete a task
- Use proper HTTP status codes for responses
- Include request validation using Pydantic models


### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance your API with robust data validation and proper error handling to make it production-ready.

#### Requirements
Completed program should:

- Validate task data with appropriate field types and constraints
- Return meaningful error messages for invalid requests
- Handle cases where a requested task doesn't exist (404 errors)
- Implement input validation for task titles (minimum length, required fields)
- Test all endpoints with both valid and invalid data
