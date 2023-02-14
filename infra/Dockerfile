FROM python:3.10-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN apt-get update && \
    apt-get -y install gcc && \
    pip install pip --upgrade && \
    pip install -r requirements.txt && \
    apt-get -y autoremove gcc && \
    apt-get clean

COPY . .