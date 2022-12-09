import numpy as np

tail = [0, 0]
head = [0, 0]
visited = set()


def update(head, tail):
    if abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 1:
        return
    if head[0] - tail[0] > 1 and abs(head[1] - tail[1]) == 0:
        tail[0] += 1
        return
    if head[0] - tail[0] < -1 and abs(head[1] - tail[1]) == 0:
        tail[0] -= 1
        return
    if head[1] - tail[1] > 1 and abs(head[0] - tail[0]) == 0:
        tail[1] += 1
        return
    if head[1] - tail[1] < -1 and abs(head[0] - tail[0]) == 0:
        tail[1] -= 1
        return
    # Diagonal
    if head[0] - tail[0] > 1 and head[1] - tail[1] >= 1:
        tail[0] += 1
        tail[1] += 1
        return
    if head[0] - tail[0] < -1 and head[1] - tail[1] >= 1:
        tail[0] -= 1
        tail[1] += 1
        return
    if head[0] - tail[0] > 1 and head[1] - tail[1] <= -1:
        tail[0] += 1
        tail[1] -= 1
        return
    if head[0] - tail[0] < -1 and head[1] - tail[1] <= -1:
        tail[0] -= 1
        tail[1] -= 1
        return

    if head[1] - tail[1] > 1 and head[0] - tail[0] >= 1:
        tail[1] += 1
        tail[0] += 1
        return
    if head[1] - tail[1] < -1 and head[0] - tail[0] >= 1:
        tail[1] -= 1
        tail[0] += 1
        return
    if head[1] - tail[1] > 1 and head[0] - tail[0] <= -1:
        tail[1] += 1
        tail[0] -= 1
        return
    if head[1] - tail[1] < -1 and head[0] - tail[0] <= -1:
        tail[1] -= 1
        tail[0] -= 1
        return

data = open('09.txt').read().split('\n')

tails = [[0, 0] for _ in range(9)]

for inst in data:
    d = inst.split(' ')[0]
    num = int(inst.split(' ')[1])
    for _ in range(num):
        visited.add(tuple(tails[-1]))
        if d == 'R':
            head[0] += 1
        elif d == 'L':
            head[0] -= 1
        elif d == 'U':
            head[1] += 1
        elif d == 'D':
            head[1] -= 1
        # part 1
        # update(head, tail)
        # part 2
        update(head, tails[0])
        for i in range(1, 9):
            update(tails[i - 1], tails[i])
        # print(visited)
        # for y in range(15, -15, -1):
        #     for x in range(-15, 15):
        #         if [x,y] == head:
        #             print('H', end='')
        #         elif [x, y] in tails:
        #             print(f'{tails.index([x,y])+1}', end='')
        #         else:
        #             print('.', end='')
        #     print()
    visited.add(tuple(tails[-1]))

# part 1 and 2
print(len(visited))
# temp = list(visited)
# max_x = max(temp, key=lambda x: x[0])[0]
# min_x = min(temp, key=lambda x: x[0])[0]
# max_y = max(temp, key=lambda x: x[1])[1]
# min_y = min(temp, key=lambda x: x[1])[1]
# print(visited)
# for y in range(max_y, min_y-1, -1):
#     for x in range(min_x, max_x):
#         if (x, y) in visited:
#             print('#', end='')
#         else:
#             print('.', end='')
#     print()
