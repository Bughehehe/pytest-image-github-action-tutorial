FROM python:3.12-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:0.11.14 /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

COPY . .
RUN uv sync --frozen

ENV PYTHONUNBUFFERED=1

RUN adduser --disabled-password --gecos "" appuser
USER appuser

CMD ["uv", "run", "src/pytest_tutorial/main.py"]