#!/bin/bash

if [ "$1" == "setup" ]
then
    npm install --global yarn
    chmod +x ./services/web/entrypoint.sh
    chmod +x ./services/web/entrypoint.prod.sh
    cd ui
    yarn install
    
fi

if [ "$1" == "build" ]
then
    docker-compose -f docker-compose.prod.yml down -v
    cd ui
    yarn build
    cp -rlf ./build/* ../services/web/project/static
    cd ..
    docker-compose -f docker-compose.prod.yml up --build -d
    sleep 6
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