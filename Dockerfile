FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir numpy scipy pydantic fastapi uvicorn

COPY . .

ENTRYPOINT ["python", "src/main.py"]