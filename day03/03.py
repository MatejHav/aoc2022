import numpy as np

(lambda x: print(x[0], x[1]))((lambda data: (sum([sum([ord(char) - (96 if ord(char) >= 97 else 38) for char in rucksack[0]]) for rucksack in data]),sum([ord(char) - (96 if ord(char) >= 97 else 38) for char in [list(set(data[i][1]).intersection(set(data[i+1][1]).intersection(set(data[i+2][1]))))[0] for i in range(0, len(data), 3)]])))((lambda f: [(set(line[:len(line)//2]).intersection(set(line[len(line)//2:])), set(line)) for line in f])(open('03.txt').read().split('\n'))))
