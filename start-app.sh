#!/bin/bash

# start the prometheus
docker-compose -f otel/docker/docker-compose.yaml up -d

source venv/bin/activate
python manage.py runserver


# open Home Page at http://127.0.0.1:8000/ 
# open Prometheus dashboard at http://127.0.0.1:9090/ 