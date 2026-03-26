# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy pyproject.toml and any poetry/uv config first (for caching dependencies)
COPY pyproject.toml poetry.lock* uv.lock* /app/

# Install build tools and uv
RUN apt-get update && apt-get install -y curl git build-essential && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    python3 -m pip install --upgrade pip setuptools wheel && \
    pip install "uv[all]"

# Copy the rest of the bot source code
COPY . /app

# Expose any port if needed (optional, for debugging)
EXPOSE 8080

# Set environment variables (can also be provided via docker-compose)
ENV PYTHONUNBUFFERED=1

# Run bot with uv (reads pyproject.toml)
CMD ["uv", "sync", "--no-verify", "run", "bot/bot.py"]