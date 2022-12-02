import numpy as np

# data = open('02.txt').read().split('\n')
# data = ['A Y', 'B X', 'C Z']
# points = 0

(lambda x: print(x[0], x[1]))((lambda data: (sum(map(lambda line: ord(line[1]) - 87 + [3, 0, 6][ord(line[0]) + 23 - ord(line[1])], map(lambda x: x.split(' '), data))), sum(map(lambda line: 3 * (ord(line[1]) - 88) + [1, 2, 3][ord(line[0]) + 23 - ord(line[1]) + ((90-ord(line[1])) if 90-ord(line[1]) < 2 else -1)], map(lambda x: x.split(' '), data)))))(open('02.txt').read().split('\n')))

# for line in data:
#     line = line.split(' ')
#     points += 3 * (ord(line[1]) - 88) + [1, 2, 3][ord(line[0]) + 23 - ord(line[1]) + ((90-ord(line[1])) if 90-ord(line[1]) < 2 else -1)]
#     print(points)
    # if 'X' in s or 'Y' in s or 'Z' in s:
    #     if 'X' in s: #lose
    #         if 'A' in s:
    #             points += 3
    #         if 'B' in s:
    #             points += 1
    #         if 'C' in s:
    #             points += 2
    #     if 'Y' in s: #draw
    #         if 'A' in s:
    #             points += 1 + 3
    #         if 'B' in s:
    #             points += 2 + 3
    #         if 'C' in s:
    #             points += 3 + 3
    #     if 'Z' in s:
    #         if 'A' in s:
    #             points += 6 + 2
    #         if 'B' in s:
    #             points += 6 + 3
    #         if 'C' in s:
    #             points += 6 + 1
# print(points)
