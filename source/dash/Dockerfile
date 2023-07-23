FROM python:3.10-alpine
WORKDIR /code
COPY dash/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY dash/app /code/app
CMD gunicorn -b 0.0.0.0:8080 app.app:server