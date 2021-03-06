# Bayesian tech expert
A bayes theorem based expert system that can guess a technology (could be hardware or software) based on your answers to questions.

## Requirements
- Docker (you can use `./install-docker.sh` or visit the docker website for binaries)
- docker-compose 
- yarn (only required if building ui)
- node (only required if building ui)

## Useage
### Quickstart
- `chmod +x run.sh`
- `./run.sh build`
- Navigate to [localhost](http://localhost) in your browser.

**If run.sh fails or you are unable to run it, you must follow the following manual steps:**
- *`docker-compose -f docker-compose.prod.yml up --build -d` in the projects root directory*
- *`docker-compose exec web python manage.py create_db` then `docker-compose exec web python manage.py seed_db` to initialise and populate the DB*

**If you can't get the docker version to work at all, there is a text-based version available by running `whatTechnology.py`**

Make sure that:
- All requirements listed above are installed and up to date
- Docker service is running
- If on linux, that the shell scripts are being run with root privelages
- If on linux, that the shell scripts have execution premissions (`chmod +x`)
- No other programs are running on port 80

### Accessing the DB

To ssh into the db container execute:
`./run.sh db`

### Rebuild and restart containers without deleting db changes (static files won't be updated)
`./run.sh restart`

### Stop containers and remove volumes (deletes db changes)
`./run.sh stop`

### View logs
`./run.sh logs`

### Build project
`./run.sh build`

### Build project and UI from source
`./run.sh build -ui`

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
