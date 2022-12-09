import numpy as np

data_copy = np.array(list(map(lambda c: [int(char) for char in list(c)], open('08.txt').read().split('\n'))))
data = data_copy.copy()

top = np.ones(data.shape, dtype=np.bool_)
for row in range(data.shape[0]-1):
    for col in range(data.shape[1]):
        top[row+1][col] = 0 if data[row][col] >= data[row+1][col] else 1
        data[row+1][col] = max(data[row][col], data[row+1][col])

data = data_copy.copy()
right = np.ones(data.shape, dtype=np.bool_)
for col in range(data.shape[1]-1):
    for row in range(data.shape[0]):
        right[row][col+1] = 0 if data[row][col] >= data[row][col+1] else 1
        data[row][col+1] = max(data[row][col], data[row][col+1])

data = data_copy.copy()
bottom = np.ones(data.shape, dtype=np.bool_)
for row in range(data.shape[0]-1, 0, -1):
    for col in range(data.shape[1]):
        bottom[row-1][col] = 0 if data[row][col] >= data[row-1][col] else 1
        data[row-1][col] = max(data[row][col], data[row-1][col])

data = data_copy.copy()
left = np.ones(data.shape, dtype=np.bool_)
for col in range(data.shape[1]-1, 0, -1):
    for row in range(data.shape[0]):
        left[row][col-1] = 0 if data[row][col] >= data[row][col-1] else 1
        data[row][col-1] = max(data[row][col], data[row][col-1])

#part 1
print(np.bitwise_or(np.bitwise_or(top, right), np.bitwise_or(bottom, left)).sum())

# part 2
data = data_copy.copy()
def check(row, col, data):
    left = [0]
    for i in range(col-1, -1, -1):
        left.append(data[row][i])
        if left[-1] >= data[row][col]:
            break

    right = [0]
    for i in range(col+1, data.shape[1]):
        right.append(data[row][i])
        if right[-1] >= data[row][col]:
            break

    up = [0]
    for i in range(row-1, -1, -1):
        up.append(data[i][col])
        if up[-1] >= data[row][col]:
            break

    down = [0]
    for i in range(row+1, data.shape[0]):
        down.append(data[i][col])
        if down[-1] >= data[row][col]:
            break

    val = (len(left)-1) * (len(right)-1) * (len(up)-1) * (len(down)-1)
    print((row, col), left, right, up, down, val, data[row][col])
    return val

best = 0
a = None
for row in range(data.shape[0]):
    for col in range(data.shape[1]):
        c = check(row, col, data)
        if c > best:
            best = c
            a = (row, col)
print(best, a)
