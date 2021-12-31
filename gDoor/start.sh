#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

readonly __dir="$(dirname $0)"
: "${PYTHON:=/opt/bb/bin/python3.7}"
: "${LOG_LEVEL:=INFO}"
if [[ ! -x "${PYTHON}" ]]; then
    PYTHON="$(which python3)"
fi

if [ "${ENV}" != "dev" ]; then 
    echo "Collecting / ploading static assets"
    ${PYTHON} ${__dir}/manage.py collectstatic --noinput
fi

echo "Running migrations if any required"
${PYTHON} ${__dir}/manage.py makemigrations 


echo "Running migrations if any required"
${PYTHON} ${__dir}/manage.py migrate --noinput


echo "Starting server"
${PYTHON} ${__dir}/manage.py runserver 0.0.0.0:8000
