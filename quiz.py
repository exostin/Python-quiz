#!/usr/bin/env python

# To run it on linux: 1.Open folder with this file in terminal
# 2.Make the file executable with: "chmod +x pycalc.py"
# 3.Execute with: "./pycalc.py"
# or do first step and then "phyton pycalc.py"
import string
import pickle

print('Welcome to quiz about python!', '\n')

score = 0
answer = ('Enter your answer: ')

name = input('Enter your name: ')


def question(message, options, correct):
    # message - string
    # options - list
    # correct - int
    # attempts - int

    optionLetters = string.ascii_lowercase[:len(options)]
    print(message)
    print(' '.join('{}: {}'.format(letter, answer)
                   for letter, answer in zip(optionLetters, options)))
    response = input(answer)
    if response == optionLetters[correct]:
        return True, score + 1
    else:
        return False


question1 = question('\nQuestion 1: Who created python?',
                     ['None of Above', 'Guido van Rossum', 'Mark Zuckerberg', 'Aliens'], 1)
question2 = question('\nQuestion 2: What is the lastest version of python?',
                     ['4', '9', '2', '3'], 3)
question3 = question('\nQuestion 3: Where is creator of python from?',
                     ['USA', 'Mars', 'Netherland', 'Poland'], 2)
question4 = question('\nQuestion 4: What sites from above are written in python?',
                     ['YouTube', 'All of them', 'Google', 'Reddit'], 1)
question5 = question('\nQuestion 5: ',
                     ['true', '', '', ''], 0)
question6 = question('\nQuestion 6: ',
                     ['', 'true', '', ''], 1)
question7 = question('\nQuestion 7: ',
                     ['', '', 'true', ''], 2)
question8 = question('\nQuestion 8: ',
                     ['true', '', '', ''], 0)
question9 = question('\nQuestion 9: ',
                     ['true', '', '', ''], 0)
question10 = question('\nQuestion 10: ',
                      ['', '', '', 'true'], 3)
question11 = question('\nQuestion 11: ',
                      ['', '', 'true', ''], 2)
question12 = question('\nQuestion 12: ',
                      ['', '', '', 'true'], 3)

data = {name: score}
pickle.dump(data, open("data.p", "rb"))
