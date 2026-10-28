import sys, os
from pathlib import Path

# Inyección de ruta raíz
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Importaciones corregidas a tus rutas reales
from app.shared.database import Base
from app.students.students_model import *
from app.pets.pets_model import *

config = context.config

if config.config_file_name:
    fileConfig(config.config_file_name)

db_url = os.getenv("DATABASE_URL", "postgresql://hermo:taller2@localhost:5432/sistema_taller2")
config.set_main_option("sqlalchemy.url", db_url)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
