#!/bin/bash

if [ "$1" == "build" ]
then
    docker-compose -f docker-compose.prod.yml down -v
    cd ui
    yarn build
    rm -r ../services/web/project/static/*
    cp -rlf ./build/* ../services/web/project/static
    cd ..
    docker-compose -f docker-compose.prod.yml up --build -d
    sleep 5
    docker-compose exec -T web python manage.py create_db
    docker-compose exec -T web python manage.py seed_db
fi

if [ "$1" == "restart" ]
then
    docker-compose -f docker-compose.prod.yml up --build -d
fi

if [ "$1" == "stop" ]
then
    docker-compose down -v --remove-orphans
fi

if [ "$1" == "db" ]
then
    winpty docker-compose exec db psql --username=hello_flask --dbname=hello_flask_prod || docker-compose exec db psql --username=hello_flask --dbname=hello_flask_prod
fi

if [ "$1" == "logs" ]
then
    docker-compose logs -f
fi