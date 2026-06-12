FROM python:3.11-slim AS builder

WORKDIR /usr/src/app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create true && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-root --no-interaction --no-ansi
    

FROM python:3.11-slim AS runner

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/.venv /usr/src/app/.venv

COPY . .

ENV PATH="/usr/src/app/.venv/bin:$PATH"

CMD ["uvicorn", "src.testing.main:app", "--host", "0.0.0.0", "--port", "8000"]
