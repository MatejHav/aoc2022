import numpy as np

data = open('06.txt').read().strip()
# data = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

solve = lambda i: (i+4 if len(set(data[i:i+4])) == 4 else '', i+14 if len(set(data[i:i+14])) == 14 else '')
res = np.array([solve(i) for i in range(len(data)) if solve(i) != ('', '')])
print(res[res[:,0] != ''][0][0], res[res[:,1] != ''][0][1])