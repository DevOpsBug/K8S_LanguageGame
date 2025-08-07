#!/bin/sh
exec gunicorn -w 4 -b "${BACKEND_HOST}:${BACKEND_PORT}" app:app