FROM tiangolo/meinheld-gunicorn-flask:python3.8

RUN pip install --upgrade pip && \
    pip install --no-cache-dir prometheus-flask-exporter

COPY ./app /app
