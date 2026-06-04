FROM python:3.12-slim

WORKDIR /app

# Установка зависимостей (если есть requirements.txt)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY data/ ./data/

ENTRYPOINT ["python", "src/main.py"]
CMD ["--input", "data/sample_input.json"]
