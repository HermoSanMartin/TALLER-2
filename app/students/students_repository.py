<<<<<<< HEAD
﻿from sqlalchemy.orm import Session
from app.students.students_model import StudentModel
from app.students.students_schemas import StudentCreate

class StudentsRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_all(self):
        return self.db.query(StudentModel).all()

    def find_by_id(self, student_id: int):
        return self.db.query(StudentModel).filter(StudentModel.id == student_id).first()

    def save(self, student_data: StudentCreate):
        db_student = StudentModel(name=student_data.name, username=student_data.username, email=student_data.email)
        self.db.add(db_student)
        self.db.commit()
        self.db.refresh(db_student)
        return db_student

    def delete(self, student_id: int):
        db_student = self.find_by_id(student_id)
        if db_student:
            self.db.delete(db_student)
            self.db.commit()
        return db_student
=======
from app.shared.in_memory_store import InMemoryStore
from app.students.students_schemas import Student


class StudentsRepository:
    def __init__(self) -> None:
        self._store: InMemoryStore[Student] = InMemoryStore()

    def find_all(self) -> list[Student]:
        return self._store.find_all()

    def find_by_id(self, student_id: str) -> Student | None:
        return self._store.get(student_id)

    def find_by_email(self, email: str) -> Student | None:
        matches = self._store.find_by(lambda student: student.email == email)
        return matches[0] if matches else None

    def find_by_username(self, username: str) -> Student | None:
        matches = self._store.find_by(lambda student: student.username == username)
        return matches[0] if matches else None

    def save(self, student: Student) -> Student:
        self._store.set(student)
        return student

    def delete(self, student_id: str) -> None:
        self._store.delete(student_id)
>>>>>>> main
