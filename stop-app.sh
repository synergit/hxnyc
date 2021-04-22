#!/bin/bash

# stop and remove resources
docker-compose -f otel/docker/docker-compose.yaml down

deactivate
# open Home Page at http://127.0.0.1:8000/ 
# open Prometheus dashboard at http://127.0.0.1:9090/ 