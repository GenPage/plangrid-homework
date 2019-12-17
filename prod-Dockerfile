FROM python:3-slim

LABEL maintainer="dylandcpage@gmail.com"
LABEL description="Plangrid homework flask app"

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /requirements.txt && \
    rm -f /requirements.txt

COPY app.py /app.py

ENV LOGLEVEL INFO

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 --workers 2 --log-level $LOGLEVEL app:app"]