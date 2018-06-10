def main_quiz():
    import json
    from os import path.join
    from operator import itemgetter
    from random import shuffle

    # Prints out questions and options from question sets
    def Def_Question(message, a, b, c, d, correct):
        # Prints question
        print('\n> ' + message)

        # Prints possible answers
        print('\na: {} \nb: {} \nc: {} \nd: {}'.format(a, b, c, d))

        # Checks if the answer is correct, and then gives points accordingly
        response = input('Enter your answer: ')
        return response.lower() == correct

    # Chooses which language to initialize
    while True:
        language = input('Choose language [en/pl]: ').lower()
        if language == 'en':
            with open(os.path.join('question_sets', 'questions_en.json'), 'r') as f:
                questionsets = json.load(f)
            questiondict = []
            break
        elif language == 'pl':
            with open(os.path.join('question_sets', 'questions_pl.json'), 'r') as f:
                questionsets = json.load(f)
            questiondict = []
            break
    #   elif language == 'enter abbreviation of your questionset here':
    #       with open('question_sets{}your question set name here.json'.format(dash), 'r') as f:
    #           questionsets = json.load(f)
    #           questiondict = []
    #       break
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

        # For each question in question sets, it calls Def_Question,
        # and adds score for correct answer
        for q in questiondict:
            score += Def_Question(*q)

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
