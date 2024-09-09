# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем файлы проекта в контейнер
COPY main.py .
#COPY path_bd.py .
COPY requirements.txt .
COPY create_tables.py .
COPY celery_worker.py .
COPY alembic.ini .
COPY alembic alembic
COPY documents documents
COPY docker docker

RUN chmod a+x docker/*.sh



# Команда для запуска FastAPI сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
