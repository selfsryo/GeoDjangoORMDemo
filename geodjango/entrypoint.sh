#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python3.8 manage.py flush --no-input
python3.8 manage.py makemigrations
python3.8 manage.py migrate
exec "$@"
