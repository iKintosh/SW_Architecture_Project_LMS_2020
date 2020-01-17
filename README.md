# LMS

![LICENSE][license-image]
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/iKintosh/Tink2020_LMS/?ref=repository-badge)

## Installation
To run the app make sure you have docker installed.

run
```bash
~/Tink2020_LMS/>: docker-compose up
```

Also we highly recommend to create venv for python and install requirements 
```bash
pip install -r requirements.txt
```  

Now create .env file in Tink2020_LMS:

```.env
DATABASE_URL=postgresql://postgres:@<URL_TO_DATABASE>:54320/postgres
FLASK_DEBUG=0
FLASK_APP=run.py
JWT_SECRET_KEY=<SECRET KEY>
```
URL_TO_DATABASE is usually ```localhost```

If you create DB for the first time run:
```bash
flask db upgrade

python -m LMS.test.db_filling
```

Then run:
```bash
flask run
```

If everything's fine you'll see:

```bash
* Serving Flask app "run.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

## Documentation
Is available at `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/swagger.json`

## Authors
Andrey Alekseev, Karina Chilova

[license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
