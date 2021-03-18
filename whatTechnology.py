import json
import numpy as np
import random
import pickle

answers = [
    1, 
    0.75, 
    0.5, 
    0.25, 
    0
    ]

with open('./data/questions.json', 'rb') as file:
    questions = json.load(file)

with open('./data/db.pickle', 'rb') as file:
    db = pickle.load(file)

for q in questions:
    print(questions.index(q), q)

def db_save():
    with open('data/db.pickle', 'wb') as file:
        pickle.dump(db, file, protocol=pickle.HIGHEST_PROTOCOL)
        
def questions_save():
    with open('data/questions.json', 'w') as file:
        json.dump(questions, file)

def db_add():
    name = input("Name of technology: ")
    db.append({"name": name, "answers": dict(zip(questions_so_far, answers_so_far))})
    db_save()
        
def questions_add():
    question = input("Enter question here: ")
    questions.append(question)
    questions_save()
    for tech in db:
        question_number = len(questions)-1
        print(question_number)
        ans = input(tech['name'] + ' - ' + question)
        tech['answers'][question_number] = float(ans)
        print(db)
        db_save()
    
    

def answer_question(question, answer):
    questions_so_far.append(int(question))
    answers_so_far.append(float(answer))
    probabilities = calculate_probabilites(questions_so_far, answers_so_far)
    sort = sorted(
            probabilities, key=lambda p: p['probability'], reverse=True)
    
    print("probabilities", probabilities)
    print(sort, type(sort))
    largest = sort[0]['probability']
    runner_up = sort[1]['probability']
    significant_difference = largest - runner_up > 0.3
    questions_left = list(set(list(range(len(questions)))) - set(questions_so_far))
    out_of_questions = len(questions_left) == 0
    if out_of_questions or significant_difference:
        print('\nprediction:\n'+ sort[0]['name'])
        correct = input('Was this correct? (y/n): ')
        if correct.lower() == 'n':
            new_tech_added = False
            while True:
                fix = input("""What do you want to do?
1) Add new question
2) Add new technology
3) Continue
    """)
                if fix == '1':
                    questions_add()
                elif fix == '2':
                    if new_tech_added:
                        print('Technology has already been added')
                        continue
                    db_add()
                    new_tech_added = True
                    print('Added using answers from this round')
                elif fix == '3':
                    if out_of_questions:
                        break
                    else:
                        next_question = random.choice(questions_left)
                        return next_question
                    
        return -1
    else:
        next_question = random.choice(questions_left)
        return next_question

def calculate_probabilites(questions_so_far, answers_so_far):
    probabilities = []
    for tech in db:
        probabilities.append({
            'name': tech['name'],
            'probability': calculate_tech_probability(tech, questions_so_far, answers_so_far)
        })

    return probabilities

def calculate_tech_probability(tech, questions_so_far, answers_so_far):
    # Prior
    P_tech = 1 / len(db)

    # Likelihood
    P_answers_given_tech = 1
    P_answers_given_not_tech = 1
    for question, answer in zip(questions_so_far, answers_so_far):
        P_answers_given_tech *= max(
            1 - abs(answer - tech_answer(tech, question)), 0.01)

        P_answer_not_tech = np.mean([1 - abs(answer - tech_answer(not_tech, question))
                                          for not_tech in db
                                          if not_tech['name'] != tech['name']])
        P_answers_given_not_tech *= max(P_answer_not_tech, 0.01)

    # Evidence
    P_answers = P_tech * P_answers_given_tech + \
        (1 - P_tech) * P_answers_given_not_tech

    # Bayes Theorem
    P_tech_given_answers = (
        P_answers_given_tech * P_tech) / P_answers

    return P_tech_given_answers


def tech_answer(tech, question):
    if question in tech['answers']:
        return tech['answers'][question]
    return 0.5

if __name__ == '__main__':
    print(db)
    print('answers:', answers)
    while True:
        question = 0
        questions_so_far = []
        answers_so_far = []
        while True:
            answer = input(questions[question]+ ' ')
            if float(answer) not in answers:
                print('Invalid response, must be one of 0, 0.25, 0.5, 0.75, 1')
                continue
            question = answer_question(question, float(answer))
            if question == -1:
                print('===RESTART===')
                break