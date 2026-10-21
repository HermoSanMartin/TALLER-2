from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.students.students_schemas import StudentSchema

router = APIRouter(prefix="/students", tags=["Students"])

# 1. OBTENER TODOS LOS ESTUDIANTES
@router.get("/")
def get_all_students(db: Session = Depends(get_db)):
    return db.query(StudentSchema).all()

# 2. OBTENER UN ESTUDIANTE POR ID
@router.get("/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentSchema).filter(StudentSchema.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return student

# 3. CREAR UN ESTUDIANTE
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_student(student_data: dict, db: Session = Depends(get_db)):
    new_student = StudentSchema(**student_data)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# 4. ELIMINAR UN ESTUDIANTE
@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentSchema).filter(StudentSchema.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    db.delete(student)
    db.commit()
    return None