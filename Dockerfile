FROM python:3.13-slim

WORKDIR /app

# Instalar uv oficial
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copiar archivos de configuración y dependencias primero
COPY pyproject.toml uv.lock ./

# Instalar dependencias globalmente en el sistema de forma directa
RUN uv pip install --system --no-cache .

# Copiar el resto del código del proyecto
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]