FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "app:app", "-w", "4", "-b", "0.0.0.0:80", "--timeout", "60"]