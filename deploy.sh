#!/bin/bash

cd /home/ubuntu/3tier-project

git pull origin main

source fetch-secrets.sh

docker-compose down

docker system prune -af

docker-compose up --build -d
