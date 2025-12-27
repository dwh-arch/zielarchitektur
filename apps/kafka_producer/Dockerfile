FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY producer.py producer.py

ENV PYTHONUNBUFFERED=1
CMD ["python", "producer.py"]
