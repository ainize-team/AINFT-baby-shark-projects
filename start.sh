#!/bin/bash
if [[ ! -v NUMBER_OF_WORKERS ]]; then
    export NUMBER_OF_WORKERS=$(grep -c processor /proc/cpuinfo)
fi
if [[ ! -v WORKER_TIMEOUT ]]; then
    export WORKER_TIMEOUT=300
fi
gunicorn --workers ${NUMBER_OF_WORKERS} --bind 0.0.0.0:8000 --timeout ${WORKER_TIMEOUT} -k uvicorn.workers.UvicornWorker main:app