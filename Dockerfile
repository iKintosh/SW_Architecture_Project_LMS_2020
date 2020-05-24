FROM python:3.7

COPY LMS ./LMS
COPY migrations ./migrations
COPY config.py .
COPY requirements.txt .
COPY run.py .

RUN apt-get update && apt-get install -y gcc python3-dev
RUN pip install -r requirements.txt

ENV DATABASE_URL postgresql://superuser:password@db/postgres
ENV FLASK_DEBUG 0
ENV FLASK_APP "run.py"
ENV JWT_SECRET_KEY "you-will-never-guess"

CMD flask run --host 0.0.0.0