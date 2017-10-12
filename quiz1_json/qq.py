#!/usr/bin/env python

# helping /u/Exostin here: https://www.reddit.com/r/learnpython/comments/753eie/python_saving_variable_data_into_file/do9fid5/

import json
import string


def question(message, options, correct):
    # message - string
    # options - list
    # correct - int
    answer = 'Enter your answer: '
    optionLetters = string.ascii_lowercase[:len(options)]
    print(message)
    print(' '.join('{}: {}'.format(letter, answer)
                   for letter, answer in zip(optionLetters, options)))
    response = input(answer)
    if response == correct:
        return 1
    else:
        return 0


print('Welcome to quiz about python!')

try:
    with open('mydata.json') as f:
        data_store = json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    # if json file doesn't exist or is corrupt/blank, start fresh
    data_store = []

question_sets = [('\nQuestion 1: Who created python?',
                  ['None of Above', 'Guido van Rossum', 'Mark Zuckerberg',
                   'Aliens'], 1),
                 ('\nQuestion 2: What is the lastest version of python?',
                  ['4', '9', '2', '3'], 3),
                 ('\nQuestion 3: Where is creator of python from?',
                  ['USA', 'Mars', 'Netherland', 'Poland'], 2),
                 ('\nQuestion 4: What sites from above are written in python?',
                  ['YouTube', 'All of them', 'Google', 'Reddit'], 1),
                 ('\nQuestion 5: ', ['true', '', '', ''], 0)]

while True:
    name = input('Enter your name: ')
    score = 0
    for q in question_sets:
        score += question(*q)

    data_store.append({'Name: ': name, 'Score: ': score})
    again = input('Do you want to do next quiz? [y/n] ').lower()
    if again == 'y':
        continue
    else:
        with open('mydata.json', 'w') as f:
            json.dump(data_store, f)
        break
