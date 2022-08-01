FROM python:3.8.13-slim-buster

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./src /app/
COPY ./data /app/data

EXPOSE 8000

# gunicorn --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker main:app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "300", "-k", "uvicorn.workers.UvicornWorker", "main:app"]