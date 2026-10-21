from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.shared.database import Base

class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    
    pets = relationship("PetModel", back_populates="student", cascade="all, delete-orphan")