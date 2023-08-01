FROM python:3.10-buster
ENV API_HOST="localhost"
ENV API_PORT="8000"
WORKDIR /code
COPY api/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
     &&  pip install --no-cache-dir -r requirements.txt
COPY api/app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
