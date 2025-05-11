ARG PYTHON_VERSION=3.13-slim
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Cria diretórios e define /code como raiz
RUN mkdir -p /code /data
WORKDIR /code

# Instala dependências
COPY requirements.txt /code/
RUN pip install --upgrade pip \
 && pip install -r /code/requirements.txt \
 && rm -rf /root/.cache

# Copia o código e coleta estáticos
COPY . /code
RUN python manage.py collectstatic --noinput

# SQLite no volume persistente
ENV SQLITE_PATH="/data/db.sqlite3"

EXPOSE 8000

# 1 worker para evitar ‘database is locked’
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "--threads", "1", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "debug", "core.wsgi:application"]
