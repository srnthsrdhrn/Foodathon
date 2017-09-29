#!/bin/sh
python manage.py migrate&&python manage.py collectstatic --noinput&&/usr/local/bin/gunicorn Foodathon.wsgi:application --reload -w 2 -b :8000

