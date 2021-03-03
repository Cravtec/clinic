# build django project on lightweight alpine linux and python 3.8 
FROM python:3.8

LABEL maintainer="Mateusz Mielniczuk" \
        name="Django clinic" \
        version="0.1"

# send python output into terminal(to see django logs)
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# update and install required packages
RUN apt-get -y update \
    && apt-get -y upgrade \
    && python3 -m pip install --upgrade pip \
    && pip install django~=3.0.8 \
    && django-admin.py startproject clinic

WORKDIR /app/clinic

RUN python3 manage.py migrate auth \
    && mv db.sqlite3 clinic_db.sqlite3

COPY . /app

RUN pip install -r requirements.txt \
    && python3 manage.py migrate \
    && python3 manage.py loaddata fixtures.json
