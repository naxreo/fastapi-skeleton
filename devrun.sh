#!/bin/bash
## python:3.10-bullseye
IMAGE="python:3.10-bullseye"

docker run -itd --name fastapi -v $(pwd -P):/app -p 8000:8000 ${IMAGE} bash
if [[ $? == 0 ]]; then
    docker exec -it fastapi bash
else
    docker stop fastapi
    docker rm fastapi
fi

