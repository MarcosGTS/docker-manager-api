#!/bin/sh

set -e

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Adicione a linha abaixo para executar as migrações
echo "Applying migrations..."
python manage.py migrate --no-input

exec "$@"