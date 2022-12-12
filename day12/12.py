from queue import PriorityQueue
from time import time
data = open('12.txt').read().split('\n')

start = None
end = None
grid = []

possible_start = []

for index, line in enumerate(data):
    if 'S' in line:
        start = (index, line.index('S'))
    if 'E' in line:
        end = (index, line.index('E'))
    for j, char in enumerate(list(line)):
        if char == 'a':
            possible_start.append((index, j))
    grid.append(list(line))

def check(pos, next_pos):
    if grid[pos[0]][pos[1]] == 'S' or grid[next_pos[0]][next_pos[1]] == 'E':
        return (grid[pos[0]][pos[1]] == 'z' and grid[next_pos[0]][next_pos[1]] == 'E')\
           or (grid[pos[0]][pos[1]] == 'S' and grid[next_pos[0]][next_pos[1]] == 'a')
    return ord(grid[pos[0]][pos[1]]) - ord(grid[next_pos[0]][next_pos[1]]) >= -1

def heuristic(pos):
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

time_start = time()

visited = dict()
pq = PriorityQueue()
pq.put((0, 0, start))
n, m = len(grid), len(grid[0])

while not pq.empty():
    h, distance, pos = pq.get()
    if pos in visited and distance >= visited[pos]:
        continue
    if pos == end:
        print(f'Part 1: {distance}')
        break
    visited[pos] = distance
    # for row in range(n):
    #     for col in range(m):
    #         if (row, col) == pos:
    #             print('\033[92mX\033[0m', end='')
    #         elif (row, col) in visited:
    #             print(f'\033[96m{grid[row][col]}\033[0m', end='')
    #         else:
    #             print(grid[row][col], end='')
    #     print()
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_pos = (max(0, min(n-1, pos[0]+dy)), max(0, min(m-1, pos[1]+dx)))
        if next_pos not in visited and check(pos, next_pos):
            pq.put((distance+heuristic(next_pos)+1, distance+1, next_pos))

# Part 2

best = 394
for start in possible_start:
    visited = dict()
    pq = PriorityQueue()
    pq.put((0, 0, start))
    n, m = len(grid), len(grid[0])

    while not pq.empty():
        h, distance, pos = pq.get()
        if pos in visited and distance >= visited[pos]:
            continue
        if pos == end:
            best = min(distance, best)
            break
        visited[pos] = distance
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_pos = (max(0, min(n-1, pos[0]+dy)), max(0, min(m-1, pos[1]+dx)))
            if next_pos not in visited and check(pos, next_pos):
                pq.put((distance+heuristic(next_pos)+1, distance+1, next_pos))

print(f'Part 2: {best}')
print(f'Time: {time() - time_start}s')