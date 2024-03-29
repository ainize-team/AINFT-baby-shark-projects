FROM python:3.9-slim-buster

# set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    VIRTUAL_ENVIRONMENT_PATH="/app/.venv"

ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENVIRONMENT_PATH/bin:$PATH"

# Install Poetry
# https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    build-essential \
    curl \
    gcc \
    g++ \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get purge --auto-remove -y \
    build-essential
    
WORKDIR /app
COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock
RUN poetry install --only main

COPY ./src/ /app/
COPY ./data /app/data

EXPOSE 8000

COPY ./start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ./start.sh