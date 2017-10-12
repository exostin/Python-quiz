#!/usr/bin/env python

# To run it on linux: 1.Open folder with this file in terminal
# 2.Make the file executable with: "chmod +x pycalc.py"
# 3.Execute with: "./pycalc.py"
# or do first step and then "phyton pycalc.py"
print('Welcome to quiz about python!', '\n')
score = 0
while True:
    name = input('Enter your name: ')

    def question(question, rightAnswer):
        global point
        answer = input(question)
        if answer == (rightAnswer):
            point = point + 1
            return True
        else:
            return False
    question("What is love? ", "baby don't hurt me")  # question(<"question">,answer

    again = input('Do you want to do next quiz? [y/n] ').lower()
    if again == 'y':
        continue
    else:
        break
