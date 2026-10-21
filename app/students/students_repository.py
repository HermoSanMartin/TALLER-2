from sqlalchemy.orm import Session
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
