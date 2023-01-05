FROM python:3.9-slim

WORKDIR /selfexclusion

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn -w 4 -bind 127.0.0.1:5000 wsgi:app