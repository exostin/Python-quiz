#!/usr/bin/env python
import json
import string

print('Welcome to quiz about python!')
# Defining IDEs for extra question
ides = ['atom', 'vim', 'codeblocks', 'visualstudiocode',
        'codelite', 'dialogblocks', 'eclipse', 'netbeans',
        'komodo', 'aptanastudio', 'geany', 'shiftedit',
        'squad', 'visualstudio', 'monodevelop', 'pycharm',
        'kate', 'gedit', 'sublimetext', 'vscode', 'fuckyou',
        'what am I even doing here ;_;']


def questionDef(message, options, correct):
    # message - string
    # options - list
    # correct - string
    answer = 'Enter your answer: '

    # Defines a, b, c option letters
    optionLetters = string.ascii_lowercase[:len(options)]

    # Prints out questions and options from question sets
    print(message)
    print(' '.join('\n{}: {}'.format(letter, answer)
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
                 ('\nQuestion 8: What is symbol for writing a comment in Python?',
                  ['//', '#', '/*', '~'], 'b'),
                 ('\nQuestion 9: What is the difference between == and =?',
                  ['== compares whether two things are equal and = assigns a value to a variable',
                   '== assigns a value to a variable and = compares whether two things are equal',
                   'both == and = can be used interchangeably',
                   'both == and = only assign values to variables'], 'a'),
                 ('\nQuestion 10: What do boolean operators return?',
                  ['Float', 'String', 'Integers', 'True/False'], 'd')]

# -------------------------------- #

while True:
    name = input('Enter your name: ')
    score = 0

    # For each question in question sets, it calls questionDef,
    # and adds score for correct answer
    for q in question_sets:
        score += questionDef(*q)

    print('\n(-1 point if your answer is wrong)')
    extra = input("Do you want extra question? [y/n] ")
    if extra == 'y':
        ide_extra = input(
            'Enter name of one of popular IDEs. (without spaces,  pure string)\n').lower()
        if ide_extra in ides:
            score += 1
        else:
            score -= 1
    data_store.append({'Name: ': name, 'Score: ': score})
    again = input('Do you want to do next quiz? [y/n] ').lower()
    if again == 'y':
        continue
    else:
        # Saves data into json file
        with open('data.json', 'w') as f:
            json.dump(data_store, f, indent=2)
        break
