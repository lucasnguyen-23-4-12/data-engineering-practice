FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install requests beautifulsoup4 psycopg2-binary

CMD ["python", "main.py"]