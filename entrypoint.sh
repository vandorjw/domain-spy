#!/bin/bash
set -e
cmd="$@"

source /app/.venv/bin/activate

if [ -z "$DATABASE_URL" ]; then
    export DATABASE_URL=postgres://postgres:postgres@postgres:5432/postgres
fi

function postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect("$DATABASE_URL")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable -- sleeping..."
  sleep 1
done

>&2 echo "Postgres is up -- continuing..."

# -z tests for empty, if TRUE, $cmd is empty
if [ -z $cmd ]; then
  python manage.py migrate --no-input
  python manage.py collectstatic --no-input
  gunicorn --config=gunicorn.py config.wsgi
else
  >&2 echo "Running command passed (by the compose file)"
  if [ "$cmd" == "migrate" ]
  then
    python manage.py migrate --no-input
  elif [ "$cmd" == "collectstatic" ]
  then
    python manage.py collectstatic --no-input
  else
    exec $cmd
  fi
fi
