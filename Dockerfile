FROM python:3.12

ENV PYTHONWRITEBYTCODE 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app/