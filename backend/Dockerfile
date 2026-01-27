# --- BUILDER ---
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# --- RUNNER ---
FROM python:3.9-slim
WORKDIR /app

# Instalamos curl para healthcheck y libpq para postgres
RUN apt-get update && apt-get install -y curl libpq-dev && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local
COPY . .

# Usuario no-root por seguridad
RUN useradd -m appuser
USER appuser

# Gunicorn ejecutará la app en el puerto 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
