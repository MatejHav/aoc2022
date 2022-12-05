import numpy as np
from collections import defaultdict

data = open('04.txt').read().split('\n')

union = dict()
pairs = 0
overlap = 0

for index, line in enumerate(data):
    first = line.split(',')[0].split('-')
    sec = line.split(',')[1].split('-')
    first = set(range(int(first[0]), int(first[1])+1))
    sec = set(range(int(sec[0]), int(sec[1])+1))
    if len(first.intersection(sec)) == len(first) or len(first.intersection(sec)) == len(sec):
        pairs += 1
    if len(first.intersection(sec)) >0:
        overlap += 1

print(pairs, overlap)