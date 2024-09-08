# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY main.py .
COPY path_bd.py .
COPY requirements.txt .
COPY create_tables.py .
COPY celery_worker.py .
COPY alembic.ini .
COPY alembic alembic
COPY documents documents

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска FastAPI сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
