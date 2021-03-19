from flask.cli import FlaskGroup

from project import app, db, Tech, Question


cli = FlaskGroup(app)

techs = [
    {
        'name': 'Python',
        'answers': {0: 1, 1: 1, 2: 0, 3: 1, 4: 0.0, 5: 0, 6: 0, 7: 0, 8: 1, 9: 1, 10: 0, 11: 1, 12: 1, 13: 0.5, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0}
    },
    {
        'name': 'JavaScript',
        'answers': {0: 1, 1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0.5, 9: 1, 10: 0, 11: 1, 12: 1, 13: 0.5, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0}
    },
    {
        'name': 'C',
        'answers': {0: 1.0, 12: 1.0, 11: 1.0, 3: 1.0, 7: 0.0, 10: 0.0, 5: 0.0, 6: 0.0, 9: 1.0, 2: 0.0, 4: 0.0, 13: 0.0, 1: 0.0, 8: 0.0, 14: 0.25, 15: 0.0, 16: 0.0, 17: 0.5, 18: 0.0}
    }, {'name': 'Docker', 'answers': {0: 0.0, 3: 1.0, 13: 0.0, 11: 0.5, 10: 1.0, 5: 0.0, 8: 0.5, 7: 1.0, 1: 0.5, 6: 0.0, 4: 0.0, 12: 1.0, 9: 1.0, 2: 0.75, 14: 0.25, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0}}, {'name': 'GPU', 'answers': {0: 0.0, 6: 0.0, 4: 1.0, 2: 0.0, 11: 0.5, 9: 0.0, 1: 0.5, 5: 0.25, 8: 0.5, 10: 0.0, 12: 0.0, 3: 1.0, 13: 1.0, 7: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0}}, {'name': 'CPU', 'answers': {0: 0.0, 9: 0.0, 13: 1.0, 1: 0.5, 2: 0.0, 7: 0.25, 4: 0.25, 6: 0.0, 10: 0.0, 8: 0.5, 5: 0.0, 3: 1.0, 12: 0.0, 11: 0.5, 14: 0.0, 15: 0.0, 16: 0.0, 17: 1.0, 18: 0.0}}, {'name': 'Matlab', 'answers': {0: 1.0, 8: 0.75, 13: 0.0, 6: 0.0, 10: 0.0, 9: 1.0, 11: 0.0, 12: 0.0, 2: 0.0, 4: 0.0, 7: 0.0, 1: 1.0, 5: 0.0, 3: 1.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0}}, {'name': 'R', 'answers': {0: 1.0, 1: 1.0, 7: 0.0, 11: 0.0, 2: 0.0, 3: 1.0, 4: 0.0, 5: 0.0, 6: 0.0, 8: 0.75, 9: 1.0, 10: 0.0, 12: 1.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0}}, {'name': 'Blender', 'answers': {0: 0.0, 4: 1.0, 5: 0.0, 1: 0.5, 2: 0.0, 3: 1.0, 6: 0.0, 7: 0.0, 8: 0.5, 9: 1.0, 10: 0.0, 11: 0.5, 12: 1.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0}}, {'name': 'WiFi dongle', 'answers': {0: 0.0, 4: 0.0, 9: 0.0, 1: 0.5, 2: 1.0, 3: 1.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 0.5, 10: 0.0, 11: 0.5, 12: 0.75, 13: 1.0, 14: 1.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0}}, {'name': 'Computer Mouse', 'answers': {0: 0.0, 4: 0.0, 5: 1.0, 1: 0.5, 2: 0.0, 3: 1.0, 6: 0.0, 7: 0.0, 8: 0.5, 9: 0.0, 10: 0.0, 11: 0.5, 12: 0.5, 13: 1.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.75, 18: 0.0}}, {'name': 'Keyboard', 'answers': {0: 0.0, 4: 0.0, 5: 1.0, 2: 0.0, 1: 0.5, 3: 1.0, 6: 0.0, 7: 0.0, 8: 0.5, 9: 0.0, 10: 0.0, 11: 0.5, 12: 0.5, 13: 1.0, 14: 0.0, 15: 1.0, 16: 0.0, 17: 0.75, 18: 0.0}}, {'name': 'MS Windows', 'answers': {0: 0.0, 4: 0.25, 9: 1.0, 7: 0.75, 1: 0.5, 2: 0.0, 3: 0.0, 5: 0.0, 6: 0.0, 8: 0.5, 10: 0.25, 11: 0.5, 12: 0.0, 13: 0.0, 14: 0.25, 15: 0.0, 16: 1.0, 17: 0.0, 18: 0.0}}, {'name': 'Apple OSX', 'answers': {0: 0.0, 4: 0.25, 3: 0.0, 1: 0.5, 2: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.5, 9: 1.0, 10: 0.0, 11: 0.5, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 1.0, 17: 1.0, 18: 0.0}}, {'name': 'Objective C', 'answers': {0: 1.0, 2: 0.0, 1: 0.0, 3: 0.25, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 1.0, 9: 1.0, 10: 0.0, 11: 1.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 1.0, 18: 1.0}}, {'name': 'Java', 'answers': {0: 1.0, 2: 0.0, 1: 0.0, 8: 1.0, 3: 1.0, 4: 0.0, 5: 0.0, 6: 1.0, 7: 0.75, 9: 1.0, 10: 0.0, 11: 1.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0}}, {'name': 'iPhone', 'answers': {0: 0.0, 4: 0.0, 5: 0.0, 9: 0.0, 1: 0.5, 2: 0.0, 3: 0.0, 6: 0.0, 7: 0.0, 8: 0.5, 10: 0.0, 11: 0.5, 12: 0.0, 13: 1.0, 14: 0.5, 15: 1.0, 16: 0.25, 17: 1.0, 18: 0.0}}]

questions = ["Are you searching for a programming language?", "Do you prefer softly typed programming languages?", "Is the tech web related?", "Is the tech cross platform?", "Is the tech graphics related?", "Is your technology a peripheral?", "Is your technology related to android apps?", "Does your technology relate to virtual machines?", "Is your programming language object oriented?", "Is your technology software?", "Is your technology related to software deployment (devops)?", "Does your programming language use 0 indexing?", "Is your technology and open standard / open source?", "Is your technology hardware?", "Is the technology networking related?", "Did your technology exist in an analogous form before the dawn of computers? (keyboards, clocks, fans ect)", "Is your technology an operating system?", "Does apple make a variation of your technology/are you thinking of an apple product?", "Is the technology depricated?"]


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    for tech in techs:
        db.session.add(Tech(id=tech['name'], answers=tech['answers']))
    for question in questions:
        db.session.add(Question(text=question))
    db.session.commit()


if __name__ == "__main__":
    cli()
