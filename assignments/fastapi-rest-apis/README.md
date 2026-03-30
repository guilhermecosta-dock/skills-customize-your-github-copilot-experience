# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build scalable, efficient REST APIs using the FastAPI framework. You'll understand HTTP methods, routing, request/response handling, and data validation to create a fully functional web service.

## 📝 Tasks

### 🛠️ Create a Student Management REST API

#### Description
Develop a complete REST API for managing student records with endpoints for creating, reading, updating, and deleting student information using FastAPI and Pydantic models.

#### Requirements
Completed program should:

- Define a Pydantic model for Student with fields like id, name, email, grade, and enrollmentDate
- Implement GET endpoint to retrieve all students
- Implement GET endpoint to retrieve a specific student by ID
- Implement POST endpoint to create a new student with proper validation
- Implement PUT endpoint to update an existing student's information
- Implement DELETE endpoint to remove a student record
- Use appropriate HTTP status codes (200, 201, 404, 400) for all endpoints
- Include input validation and error handling for invalid requests

### 🛠️ Add Advanced Features

#### Description
Extend your REST API with filtering, sorting, and search capabilities to make it more functional and realistic.

#### Requirements
Completed program should:

- Add query parameters to filter students by grade or enrollment year
- Implement sorting functionality (by name, grade, or date)
- Add a search endpoint to find students by name (partial match)
- Include pagination support (limit and skip parameters)
- Document API endpoints using FastAPI's automatic documentation features
