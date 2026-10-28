from typing import Optional
from sqlalchemy.orm import Session
from app.students.students_model import StudentModel

class StudentsRepository:
    def __init__(self, db: Optional[Session] = None):
        self.db = db

    def find_all(self, db: Optional[Session] = None):
        session = db or self.db
        return session.query(StudentModel).all()

    def find_by_id(self, student_id: int, db: Optional[Session] = None):
        session = db or self.db
        return session.query(StudentModel).filter(StudentModel.id == student_id).first()

    def save(self, student_data, db: Optional[Session] = None):
        session = db or self.db
        db_student = StudentModel(
            name=student_data.name,
            username=student_data.username,
            email=student_data.email
        )
        session.add(db_student)
        session.commit()
        session.refresh(db_student)
        return db_student

    def delete(self, student_id: int, db: Optional[Session] = None):
        session = db or self.db
        db_student = self.find_by_id(student_id, session)
        if db_student:
            session.delete(db_student)
            session.commit()
            return True
        return False
