#!/bin/sh

set -e
cd core

python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module core.wsgi
