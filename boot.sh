#!/bin/bash
#source "$(pipenv --venv)/bin/activate"
#pipenv shell
while true; do
  if flask db upgrade; then
    break
  fi
  echo "Upgrade command failed, retrying in 5 secs ..."
  sleep 5
done
flask translate compile
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app
