import sys
import webbrowser
import os
import json
from operator import itemgetter
import string

# Defining dash, because in windows it is \ while in linux/mac it is /
if os.name == 'nt':
    dash = "\\"
else:
    dash = "/"
# ----- QUIZ ----- #


def main_quiz():

    def questionDef(message, a, b, c, d, correct):
        answer = 'Enter your answer: '

        # Prints out questions and options from question sets
        print('\n> ' + message)
        print('\na: {} \nb: {} \nc: {} \nd: {}'.format(a, b, c, d))
        response = input(answer)
        if response.lower() == correct:
            return 1
        else:
            return 0

    # Defining IDEs for extra question
    ides = ['atom', 'vim', 'codeblocks', 'visualstudiocode',
            'codelite', 'dialogblocks', 'eclipse', 'netbeans',
            'komodo', 'aptanastudio', 'geany', 'shiftedit',
            'squad', 'visualstudio', 'monodevelop', 'pycharm',
            'kate', 'gedit', 'sublimetext', 'vscode', 'visualstudio'
            'what am i even doing here ;_;', 'vs', 'idle']

    print('Welcome to quiz about python!')

    # Chooses which language to initialize
    while True:
        language = input('Choose language [en/pl]: ').lower()
        if language == 'en':
            with open('question_sets{}questions_en.json'.format(dash), 'r') as f:
                questionsets = json.load(f)
            questiondict = []
            break
        elif language == 'pl':
            with open('question_sets{}questions_pl.json'.format(dash), 'r') as f:
                questionsets = json.load(f)
            questiondict = []
            break
    #   elif language == 'enter abbreviation of your questionset here':
    #       with open('question_sets{}your question set name here.json'.format(dash), 'r') as f:
    #           questionsets = json.load(f)
    #           questiondict = []
    #       break
        else:
            print('This language isn\'t currently supported. Try again.')
            continue

    try:
        with open('data.json') as f:
            data_store = json.load(f)
    # If json file doesn't exist or is corrupt/blank, start fresh
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data_store = []

    for item in questionsets:
        question = item['Question']
        a = item['a']
        b = item['b']
        c = item['c']
        d = item['d']
        answer = item['answer']
        questiondict.append((question, a, b, c, d, answer))

    # Quiz loop
    while True:
        name = input('Enter your name: ')
        score = 0

        # For each question in question sets, it calls questionDef,
        # and adds score for correct answer
        for q in questiondict:
            score += questionDef(*q)
        print('\n(-1 point if your answer is wrong in extra question)')
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

# ----- QUIZ ----- #

# ----- READ ----- #


def main_read():
    # Defining characters for exit variable
    possibleCharacters = string.ascii_lowercase + \
        string.digits + string.ascii_uppercase + ' .,!?;:'

    # Opens file with data
    with open('data.json', 'r') as f:
        data = json.load(f)
    scores = []  # Create temporary score variable

    # Appends Name and Score value to temporary score variable
    for item in data:
        temp_name = item['Name: ']
        temp_score = item['Score: ']
        scores.append((temp_name, temp_score))

    # Prints out scores sorted in descending order
    for name, score in sorted(scores, key=itemgetter(1), reverse=True):
        print('{}: {}'.format(name, score))

    # Need this, because program automatically ends in windows, when opened.
    exit = input('Enter anything to end. ')
    if exit in possibleCharacters:
        pass
    else:
        pass

# ----- READ ----- #


# ----- FILL ----- #


def main_fill():

    # Defining possible answers.
    p_answers = ['a', 'b', 'c', 'd']
    while True:
        quest_number = 0
        questionset = input('Enter your questionset name: ')
        file = "question_sets{}{}.json".format(dash, questionset)
        fptr = open(file, "w")
        # Open questionset file
        try:
            with open('questions_sets{}{}.json'.format(dash, questionset)) as f:
                questions_store = json.load(f)
        # If json file doesn't exist or is corrupt/blank, start fresh
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            questions_store = []
        while True:
            try:
                how_many_q = int(input('How many questions do you want? '))
            except ValueError:
                print('Only numbers. Try again')
                continue
            else:
                break
        while True:
            quest_number += 1
            question = input('Enter your question: ')
            a = input('Enter option a: ')
            b = input('Enter option b: ')
            c = input('Enter option c: ')
            d = input('Enter option d: ')
            while True:
                answer = input('Enter correct answer: [a/b/c/d] \n').lower()
                if answer in p_answers:
                    break
                else:
                    print('You can select only a/b/c/d for answer.')
                    continue
            # Append question set data.
            questions_store.append({'question': question, 'a': a,
                                    'b': b, 'c': c, 'd': d, 'answer': answer})
            if quest_number == how_many_q:
                break
            else:
                continue
        # Saves data into json file
        with open('question_sets/{}.json'.format(questionset), 'w') as f:
            json.dump(questions_store, f, indent=2)
        again = input('Do you want to make next questionset? [y/n] ').lower()
        if again == 'y':
            continue
        else:
            break

# ----- FILL ----- #


# ----- CORE ----- #

try:
    while True:
        print('''Quiz (q) - take the quiz
Read (r) - read scores from quiz
Fill (f) - make your own question set for quiz
GitHub (git) - Launches this project link in your default browser
Nevermind (nvm) - Exit''')
        while True:
            choice = input('Enter your choice: ').lower()
            if choice == 'q':
                main_quiz()
                break
            elif choice == 'r':
                main_read()
                break
            elif choice == 'f':
                main_fill()
                break
            elif choice == "git":
                webbrowser.open("https://github.com/exostin/Python-quiz")
                break
            elif choice == 'nvm':
                sys.exit(0)
            else:
                print("Wrong input! Try again.")
                continue
        again = input('Do you want to do something more? [y/n] ').lower()
        if again == 'y':
            continue
        else:
            break
except KeyboardInterrupt:
    print("Shutdown requested...exiting")

# ----- CORE ------ #
