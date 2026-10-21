import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

# Obtener credenciales con valores por defecto
USER = os.getenv("POSTGRES_USER", "postgres")
PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
DB = os.getenv("POSTGRES_DB", "postgres")

# URL explícita usando el driver psycopg2
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@localhost:5432/{DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Generador de sesiones de base de datos para los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()