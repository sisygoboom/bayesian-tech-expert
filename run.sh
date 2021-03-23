docker-compose -f docker-compose.prod.yml down -v
cd ui
yarn build
rm -r ../services/web/project/static/*
cp -rlf ./build/* ../services/web/project/static
cd ..
docker-compose -f docker-compose.prod.yml up --build -d
sleep 5
alias docker-compose="winpty docker-compose"
docker-compose exec web python manage.py create_db
docker-compose exec web python manage.py seed_db