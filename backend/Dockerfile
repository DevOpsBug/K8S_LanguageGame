FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV BACKEND_HOST=127.0.0.1
ENV BACKEND_PORT=5000

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD gunicorn -w 4 -b ${BACKEND_HOST}:${BACKEND_PORT} app:app
