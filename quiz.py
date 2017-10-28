#!/usr/bin/env python
import json
import string

print('Welcome to quiz about python!')


def questionDef(message, options, correct):
    # message - string
    # options - list
    # correct - string
    answer = 'Enter your answer: '

    # Defines a, b, c option letters
    optionLetters = string.ascii_lowercase[:len(options)]

    # Prints out questions and options from question sets
    print(message)
    print(' '.join('{}: {}'.format(letter, answer)
                   for letter, answer in zip(optionLetters, options)))
    response = input(answer)
    if response.lower() == correct:
        return 1
    else:
        return 0


try:
    with open('data.json') as f:
        data_store = json.load(f)
# If json file doesn't exist or is corrupt/blank, start fresh
except (FileNotFoundError, json.decoder.JSONDecodeError):
    data_store = []

# ----------- QUESTIONS ----------- #

question_sets = [('\nQuestion 1: Who created python?',
                  ['None of these', 'Guido van Rossum', 'Mark Zuckerberg',
                   'Aliens'], 'b'),
                 ('\nQuestion 2: What is the lastest version of python?',
                  ['4', '9', '2', '3'], 'd'),
                 ('\nQuestion 3: Where is creator of python from?',
                  ['USA', 'Mars', 'Netherland', 'Poland'], 'c'),
                 ('\nQuestion 4: What sites from these are written in python?',
                  ['YouTube', 'All of them', 'Google', 'Reddit'], 'b'),
                 ('\nQuestion 5: Which of these is exponent operator?',
                  ['**', '/', '*', '%'], 'a'),
                 ("\nQuestion 6: What is n? n = '5'",
                  ['String', 'Integer', 'Float', 'Tuple'], 'a'),
                 ('\nQuestion 7: Statement using "and" operator results true if: ',
                  ['Either of the operands is true', 'Both operands are false',
                   'Both operands are true', 'First operand is true'], 'c'),
                 ('\nQuestion 8: ?',
                  ['', 'true', '', ''], 'b'),
                 ('\nQuestion 9: ?',
                  ['true', '', '', ''], 'a'),
                 ('\nQuestion 10: ?',
                  ['', '', '', 'true'], 'd')]

# -------------------------------- #

while True:
    name = input('Enter your name: ')
    score = 0

    # For each question in question sets, it calls questionDef,
    # and adds score for correct answer
    for q in question_sets:
        score += questionDef(*q)

    data_store.append({'Name: ': name, 'Score: ': score})
    again = input('Do you want to do next quiz? [y/n] ').lower()
    if again == 'y':
        continue
    else:
        # Saves data into json file
        with open('data.json', 'w') as f:
            json.dump(data_store, f, indent=2)
        break
