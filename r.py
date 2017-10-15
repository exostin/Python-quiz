#!/usr/bin/env python
import json
from pprint import pprint
with open('data.json', 'r') as f:
    data = json.load(f)
pprint(data)
