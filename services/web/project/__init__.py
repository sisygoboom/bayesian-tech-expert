from flask import Flask, jsonify, send_from_directory, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from sqlalchemy.dialects import postgresql
import numpy as np
import random

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('answers')
parser.add_argument('questions_so_far', type=int, default=[], action='append')
parser.add_argument('answers_so_far', type=float, default=[], action='append')


class Tech(db.Model):
    __tablename__ = "tech"

    id = db.Column(db.String(128), primary_key=True)
    answers = db.Column(postgresql.JSONB(), unique=False, nullable=False)

    def __init__(self, id, answers):
        self.id = id
        self.answers = answers


class Question(db.Model):
    __tablename__ = "question"

    id = db.Column(db.Integer(), db.Sequence('question_incrementer', start=0, minvalue=0), primary_key=True)
    text = db.Column(db.String(512), unique=True, nullable=False)

    def __init__(self, text):
        self.text = text


class Answer(Resource):
    def post(self):
        args = parser.parse_args()
        questions_so_far = args['questions_so_far']
        answers_so_far = args['answers_so_far']

        if not answers_so_far:
            start_question = random.choice([9, 0])
            question = Question.query.get(start_question)
            return {'question': question.text, 'question_id': start_question}
        techs = []
        for tech in Tech.query.all():
            techs.append({'name': tech.id, 'answers': tech.answers})

        questions_left = [question.id for question in
                          db.session.query(Question.id).filter(Question.id.notin_(questions_so_far))]

        probabilities = self.calculate_probabilites(questions_so_far, answers_so_far, techs)
        sort = sorted(probabilities, key=lambda p: p['probability'], reverse=True)
        largest = sort[0]['probability']
        runner_up = sort[1]['probability']
        significant_difference = largest - runner_up > 0.3
        out_of_questions = len(questions_left) == 0
        if out_of_questions or significant_difference:
            return {'prediction': sort[0]['name']}

        question_id = self.get_next_question(sort, questions_left, techs)
        question = Question.query.get(int(question_id))
        return {'question': question.text, 'question_id': question.id, 'probabilities': probabilities}

    def calculate_probabilites(self, questions_so_far, answers_so_far, db):
        probabilities = []
        for tech in db:
            probabilities.append({
                'name': tech['name'],
                'probability': self.calculate_tech_probability(tech, questions_so_far, answers_so_far, db)
            })

        return probabilities

    def calculate_tech_probability(self, tech, questions_so_far, answers_so_far, db):
        # Prior
        P_tech = 1 / len(db)

        # Likelihood
        P_answers_given_tech = 1
        P_answers_given_not_tech = 1
        for question, answer in zip(questions_so_far, answers_so_far):
            P_answers_given_tech *= max(
                1 - abs(answer - self.tech_answer(tech, question)), 0.01)

            P_answer_not_tech = np.mean([1 - abs(answer - self.tech_answer(not_tech, question))
                                         for not_tech in db
                                         if not_tech['name'] != tech['name']])
            P_answers_given_not_tech *= max(P_answer_not_tech, 0.01)

        # Evidence
        P_answers = P_tech * P_answers_given_tech + (1 - P_tech) * P_answers_given_not_tech

        # Bayes Theorem
        P_tech_given_answers = (P_answers_given_tech * P_tech) / P_answers

        return P_tech_given_answers

    def tech_answer(self, tech, question):
        if str(question) in tech['answers']:
            return tech['answers'][str(question)]
        return 0.5

    def get_next_question(self, sort, questions_left, db):
        largest = sort[0]['name']
        runner_up = sort[1]['name']
        for i in db:
            if i['name'] == largest:
                largest_answers = i['answers']
            if i['name'] == runner_up:
                runner_up_answers = i['answers']
        difference = {'index': -1, 'diff': 0}
        for q in questions_left:
            q = str(q)
            if q not in largest_answers:
                largest_answers[q] = 0.5
            if q not in runner_up_answers:
                runner_up_answers[q] = 0.5
            diff = abs(largest_answers[q] - runner_up_answers[q])
            if diff > difference['diff']:
                difference = {'index': q, 'diff': diff}

        if difference['index'] == -1:
            return random.choice(questions_left)

        return difference['index']


api.add_resource(Answer, '/api/answer')
