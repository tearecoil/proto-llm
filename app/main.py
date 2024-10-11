from typing import Union
from fastapi import FastAPI

from app.db import get_db_connection
from app.student import Student, StudentCreate
from http.client import HTTPException

app = FastAPI(title="Prototype LLM")

@app.get("/")
def read_root():
    return{"Hello":"World"}

@app.get("/items/{items_id}")
def read_items(item_id: int, q: Union[str, None] = None):
    return{"item_id": item_id, "q": q}

@app.get("/status")
async def status():
    return{"message":"Connected"}

#testing
@app.post("/student")
def create_student(student: StudentCreate):
    conn, cursor = get_db_connection()
    try:
        cursor.execute("INSERT STUDENT INFO (first_name, last_name)", 
                       (student.first_name, student.last_name))
        new_student = cursor.fetchone()
        conn.commit()
        cursor.close()
    except Exception as error:
        conn.close()
        raise HTTPException(status_code = 500, detail=str(e))
    conn.close()
    if new_student:
        return Student(**new_student)
    raise HTTPException(status_code = 400, detail="Error creating students")