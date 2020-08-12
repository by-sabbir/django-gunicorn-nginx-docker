FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /app
