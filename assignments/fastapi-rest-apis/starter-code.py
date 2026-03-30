from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

# Define the Student model
class Student(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    grade: str
    enrollmentDate: datetime

# In-memory database (for demonstration purposes)
students_db = []

# TODO: Implement GET endpoint to retrieve all students
@app.get("/students")
async def get_students():
    pass

# TODO: Implement GET endpoint to retrieve a specific student by ID
@app.get("/students/{student_id}")
async def get_student(student_id: int):
    pass

# TODO: Implement POST endpoint to create a new student
@app.post("/students")
async def create_student(student: Student):
    pass

# TODO: Implement PUT endpoint to update a student
@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    pass

# TODO: Implement DELETE endpoint to remove a student
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    pass

# Optional: Implement filtering endpoint
@app.get("/students/filter/by-grade")
async def filter_by_grade(grade: str):
    pass

# TODO: Run the app with: uvicorn starter-code:app --reload
