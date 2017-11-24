def main_fill():
    import json
    import os
    # Defining dash, because in windows it is \ while in linux/mac it is /
    if os.name == 'nt':
        dash = "\\"
    else:
        dash = "/"

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
            questions_store.append({'Question': question, 'a': a,
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
