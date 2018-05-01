def main_read():
    import json
    import string
    from operator import itemgetter
    # Defining characters for exit variable
    possibleCharacters = string.ascii_lowercase + \
        string.digits + string.ascii_uppercase + ' .,!?;:'

    # Opens file data_scores
    with open('data_scores.json', 'r') as f:
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
