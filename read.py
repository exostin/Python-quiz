#!/usr/bin/env python
import json
from operator import itemgetter
with open('data.json', 'r') as f:
    data = json.load(f)
scores = []
for item in data:
    temp_name = item['Name: ']
    temp_score = item['Score: ']
    scores.append((temp_name, temp_score))

for name, score in sorted(scores, key=itemgetter(1), reverse=True):
    print('{}: {}'.format(name, score))
