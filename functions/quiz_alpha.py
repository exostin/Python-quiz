def main_quiz():
    import os
    import json
    from operator import itemgetter
    from random import shuffle

    # Defining dash, because in windows it is \ while in linux/mac it is /
    if os.name == 'nt':
        dash = "\\"
    else:
        dash = "/"

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
            'kate', 'gedit', 'sublimetext', 'vscode', 'visualstudio',
            'co ja tutaj robie', 'vs', 'idle', 'vscodeinsiders',
            'visualstudiocodeinsiders', '02112003', 'neovim', 'jetbrains',
            'n++', 'notepad++', 'emacs']

    # Opens config file, and creates temporary variable to store data from it
    with open('config.json', 'r') as c:
        config = json.load(c)
    qs_name = []
    qs_abbreviation = []
    qs_abbreviations = []

    # Assigns info from config file to configs variable (C stands for config, qs stands for question set)
    for item in config:
        C_questionsetname = item['questionset: ']
        C_abbreviation = item['abbreviation: ']
        qs_name = C_questionsetname
        qs_abbreviation = C_abbreviation
        qs_abbreviations.append((C_abbreviation))
        with open('question_sets{}{}.json'.format(dash, qs_name), 'r') as f:
            questionsets = json.load(f)
        questiondict = []

    # Chooses which question set (QS) to initialize
    while True:
        QSinitialize = input('Choose your quiz abbreviation: {} '.format(
            qs_abbreviations)).lower()
        if QSinitialize in qs_abbreviations:
            with open('question_sets{}{}.json'.format(dash, qs_name), 'r') as f:
                questionsets = json.load(f)
            questiondict = []
            break
        else:
            print('Sorry, I don\'t have such quiz in my database. Try again.')
            continue

    try:
        with open('data_scores.json') as f:
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
        shuffle(questiondict)
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
                'Enter name of one of popular IDEs. (without spaces, ex. thisissuperide)\n').lower()
            if ide_extra in ides:
                score += 2
            else:
                score -= 1

        data_store.append({'Name: ': name, 'Score: ': score})
        again = input('Do you want to do next quiz? [y/n] ').lower()
        if again == 'y':
            os.system('cls')
            continue
        else:
            # Saves data into json file
            with open('data_scores.json', 'w') as f:
                json.dump(data_store, f, indent=2)
            break
