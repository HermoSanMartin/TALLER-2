from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.shared.database import Base

class PetModel(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    student = relationship("StudentModel", back_populates="pets")