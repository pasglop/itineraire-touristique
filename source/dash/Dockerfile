FROM python:3.10-buster
WORKDIR /code
COPY dash/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
     &&  pip install --no-cache-dir -r requirements.txt
COPY dash/app /code/app
CMD ["python", "app/app.py"]