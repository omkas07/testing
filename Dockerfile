FROM python:3.11-slim

WORKDIR /usr/src/app

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-interaction

COPY . .

CMD ["uvicorn", "src.testing.main:app", "--host", "0.0.0.0", "--port", "8000"]
