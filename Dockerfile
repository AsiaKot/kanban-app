FROM python:3.9-slim

WORKDIR /kanban

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
