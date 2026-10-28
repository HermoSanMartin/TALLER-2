<<<<<<< HEAD
FROM python:3.13-slim

WORKDIR /app

# Instalar uv oficial
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copiar archivos de configuración y dependencias primero
COPY pyproject.toml uv.lock ./

# Instalar dependencias globalmente en el sistema de forma directa
RUN uv pip install --system --no-cache .

# Copiar el resto del código del proyecto
=======
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt-get/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock* ./
RUN uv sync --no-cache

>>>>>>> main
COPY . .

EXPOSE 8000

<<<<<<< HEAD
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> main
