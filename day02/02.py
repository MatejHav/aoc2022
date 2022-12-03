import numpy as np

(lambda x: print(x[0], x[1]))((lambda data: (sum(map(lambda line: ord(line[1]) - 87 + [3, 0, 6][ord(line[0]) + 23 - ord(line[1])], map(lambda x: x.split(' '), data))), sum(map(lambda line: 3 * (ord(line[1]) - 88) + [1, 2, 3][ord(line[0]) + 23 - ord(line[1]) + ((90-ord(line[1])) if 90-ord(line[1]) < 2 else -1)], map(lambda x: x.split(' '), data)))))(open('02.txt').read().split('\n')))
