#!/usr/bin/env python
import json
import time
from operator import itemgetter

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
time.sleep(360)
