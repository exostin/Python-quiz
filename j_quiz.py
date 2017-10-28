#!/usr/bin/env python
import json
from operator import itemgetter
# import random

print('Welcome to quiz about python!')
while True:
    language = input('Choose language: en/pl: ').lower()
    if language == 'en':
        with open('questions_en.json', 'r') as f:
            quest = json.load(f)
        questions = []
        break
    elif language == 'pl':
        with open('questions_pl.json', 'r') as f:
            quest = json.load(f)
        questions = []
        break
    else:
        print('This language isn\'t currently supported. Try again.')
        continue
for item in quest:
    temp_question = item['question']
    temp_a = item['a']
    temp_b = item['b']
    temp_c = item['c']
    questions.append((temp_question, temp_a, temp_b, temp_c))

# Prints out questions sorted in descending order
for question, a, b, c in sorted(questions, key=itemgetter(1)):
    print('{}: \n{}: \n{}: \n{}: '.format(question, a, b, c))

try:
    with open('data.json') as f:
        data_store = json.load(f)
# If json file doesn't exist or is corrupt/blank, start fresh
except (FileNotFoundError, json.decoder.JSONDecodeError):
    data_store = []

while True:
    name = input('Enter your name: ')
    score = 0
    data_store.append({'Name: ': name, 'Score: ': score})
    again = input('Do you want to do next quiz? [y/n] ').lower()
    if again == 'y':
        continue
    else:
        # Saves data into json file
        with open('data.json', 'w') as f:
            json.dump(data_store, f, indent=2)
        break
