#!/bin/bash

alembic upgrade head
gunicorn main:app --workers 4 --workers-class uvicorn.workers.UvicornWorkers --bind=0.0.0.0:8000
apt-get update && apt-get install -y tesseract-ocr
