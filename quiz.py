#!/usr/bin/env python

# To run it on linux: 1.Open folder with this file in terminal
# 2.Make the file executable with: "chmod +x pycalc.py"
# 3.Execute with: "./pycalc.py"
# or do first step and then "phyton pycalc.py"
import string

print('Welcome to quiz about python!', '\n')

attempts = 2
answer = ('Enter your answer: ')
again = ('Incorrect! Try again.''\n')
no_attempts = ('Incorrect! You ran out of your attempts.', '\n')


def question(message, options, correct, attempts=attempts):
    # message - string
    # options - list
    # correct - int
    # attempts - int

    optionLetters = string.ascii_lowercase[:len(options)]
    print(message)
    print(' '.join('{}: {}'.format(letter, answer)
                   for letter, answer in zip(optionLetters, options)))
    while attempts > 0:
        response = input(answer)
        if response == optionLetters[correct]:
            return True
        else:
            attempts -= 1
            print(again)

    print(no_attempts)
    return False


# idk why but the answer is always +1 of what I typed in
question1 = question('Question 1: ',
                     ['', 'true', '', ''], 1)
question2 = question('Question 2: ',
                     ['', '', '', 'true'], 3)
question3 = question('Question 3: ',
                     ['', '', 'true', ''], 2)
question4 = question('Question 4: ',
                     ['', 'true', '', ''], 1)
question5 = question('Question 5: ',
                     ['true', '', '', ''], 0)
question6 = question('Question 6: ',
                     ['', 'true', '', ''], 1)
question7 = question('Question 7: ',
                     ['', '', 'true', ''], 2)
question8 = question('Question 8: ',
                     ['true', '', '', ''], 0)
question9 = question('Question 9: ',
                     ['true', '', '', ''], 0)
question10 = question('Question 10: ',
                      ['', '', '', 'true'], 3)
question11 = question('Question 11: ',
                      ['', '', 'true', ''], 2)
question12 = question('Question 12: ',
                      ['', '', '', 'true'], 3)
