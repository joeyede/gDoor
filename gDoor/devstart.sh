#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

: "${ENV:=dev}"
readonly __dir="$(dirname $0)"
env_path="${__dir}/${ENV}.env"

if [[ ! -f "${env_path}" ]]; then
    echo "Uknown environment specified."
    echo "Available environments for \$ENV:"
    for e in ${__dir}/*.env; do
        filename=$(basename $e)
        echo -e "\t ${filename/.env/}"
    done
    echo
    exit 1
fi

echo "ENVIRONMENT IS: ${ENV}"
export ENV=${ENV}
source "${__dir}/${ENV}.env"
${__dir}/start.sh
