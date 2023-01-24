# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /site

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /site/
RUN pip install -r requirements.txt

COPY . /site/


