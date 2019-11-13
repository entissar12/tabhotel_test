#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


python /app/manage.py collectstatic --noinput
python /app/manage.py migrate
python /app/manage.py runserver 0.0.0.0:5000
