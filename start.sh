#!/bin/bash

cd restaurants
python manage.py makemigrations api
python manage.py migrate api
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000
