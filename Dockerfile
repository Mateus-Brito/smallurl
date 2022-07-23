# Base Image
FROM python:3.10-slim-bullseye

# Python Interpreter Flags
ENV PYTHONUNBUFFERED 1  
ENV PYTHONDONTWRITEBYTECODE 1

# Create a user to avoid running containers as root in production
RUN addgroup --system django \
    && adduser --system --ingroup django django

# Install os-level dependencies (as root)
RUN apt-get update && apt-get install -y -q --no-install-recommends \
  # dependencies for building Python packages
  build-essential \
  # postgress client (psycopg2) dependencies
  libpq-dev \
  libgdal-dev \
  # cleaning up unused files to reduce the image size
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

ENV PATH="/home/django/.local/bin:${PATH}"

# Switch to the non-root user
USER django

# Create a directory for the source code and use it as base path
WORKDIR /home/django/code/

# Copy the python depencencies list for pip
COPY --chown=django:django ./requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=django:django . .
