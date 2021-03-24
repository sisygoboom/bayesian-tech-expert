# Bayesian tech expert
A bayes theorem based expert system that can guess a technology (could be hardware or software) based on your answers to questions.

## Requirements
- Docker
- yarn

## Useage
### Quickstart
- `chmod +x run.sh`
- `./run.sh build`
- Navigate to [localhost](http://localhost) in your browser.
- Think of a technology and the beyesian tech expert will attempt to guess what it is by asking questions.
- If the expert gets it wrong, you may add additional questions, add a new technology or restart the game.

*If run.sh fails or you are unable to run it, you must follow the following manual steps:*
- *(optional) `yarn build` in the /ui directory, then copy files in /ui/build to /services/web/project/static*
- *`docker-compose -f docker-compose.prod.yml up --build -d` in the projects root directory*
- *`docker-compose exec web python manage.py create_db` then `docker-compose exec web python manage.py seed_db` to initialise and populate the DB*

### Accessing the DB

To ssh into the db container execute:
`./run.sh db`
or
`docker-compose exec db psql --username=hello_flask --dbname=hello_flask_prod`

Once in, `\c` to connect.

`\dt` to list tables.

Write regular SQL to view rows.

`\q` to quit.

### Rebuild and restart containers without deleting db changes (static files won't be updated)
`./run.sh restart`

### Stop containers and remove volumes (deletes db changes)
`./run.sh stop`

### View logs
`./run.sh logs`

## More info

Currently the prepared db includes (but is not limited to):
- JavaScript
- WiFi dongle
- Python
- C
- Matlab
- R
- Objective C
- Java
- Docker
- GPU
- CPU
- Blender
- Computer Mouse
- Keyboard
- MS Windows
- Apple OSX
- iPhone

The prepared questions currently include (but are not limited to):
- Are you searching for a programming language?
- Do you prefer softly typed programming languages?
- Is the tech web related?
- Is the tech cross platform?
- Is the tech graphics related?
- Is your technology a peripheral?
- Is your technology related to android apps?
- Does your technology relate to virtual machines?
- Is your programming language object oriented?
- Is your technology software?
- Is your technology related to software deployment (devops)?
- Does your programming language use 0 indexing?
- Is your technology and open standard / open source?
- Is your technology hardware?
- Is the technology networking related?
- Did your technology exist in an analogous form before the dawn of computers? (keyboards, clocks, fans ect)
- Is your technology an operating system?
- Does apple make a variation of your technology/are you thinking of an apple product?
- Is the technology depricated?
