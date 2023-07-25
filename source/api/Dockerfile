FROM python:3.10-alpine
WORKDIR /code
COPY api/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY api/app /code/source/api/app
COPY databases.py /code/source/databases.py
CMD ["python", "source/api/app/main.py"]
