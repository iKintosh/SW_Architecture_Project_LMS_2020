FROM python:3.7

COPY LMS LMS
COPY migrations migrations
COPY migrations/env.py migrations/
COPY migrations/versions migrations/versions
COPY kubernetes kubernetes
COPY config.py .
COPY requirements.txt .
COPY run.py .
COPY config.py .

RUN apt-get update && apt-get install -y gcc python3-dev apt-utils
RUN pip install -r requirements.txt

ENV DATABASE_URL 'postgres://superuser:password@postgres-service:5432/postgres'
ENV FLASK_DEBUG 0
ENV FLASK_APP "run.py"
ENV PYTHONPATH '.'

RUN chmod +x run.py

EXPOSE 5000

CMD gunicorn run:app --config=config.py