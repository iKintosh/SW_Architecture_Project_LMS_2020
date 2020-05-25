# LMS

![LICENSE][license-image]
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/iKintosh/Tink2020_LMS/?ref=repository-badge)

## Installation

To run the app make sure you have docker installed.

Simply run

```bash
~/Tink2020_LMS/>: docker-compose up
```

Now create .env file in Tink2020_LMS:

```.env
DATABASE_URL=postgresql://postgres:@db/postgres
FLASK_DEBUG=0
FLASK_APP=run.py
JWT_SECRET_KEY=<SECRET KEY>
```

If you create DB for the first time run:

```bash
flask db upgrade

python -m LMS.test.db_filling
```

## Documentation

Is available as swagger web-page

## Authors

Andrey Alekseev (docker, kubernetes), Karina Chilova (PostgresSQL)

[license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
