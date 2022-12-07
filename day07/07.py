import numpy as np

data = open('07.txt').read().split('\n')

outdir = {}
stack = []
curr = outdir

for line in data:
    s = line.split(' ')
    if s[0] == '$':
        if s[1] == 'ls':
            continue
        elif s[1] == 'cd':
            if s[2] == '/':
                curr = outdir
                stack = []
            elif s[2] == '..':
                curr = stack.pop()
            else:
                name = s[2]
                if name not in curr:
                    curr[name] = dict()
                stack.append(curr)
                curr = curr[name]
        else:
            continue
    else:
        if s[0] == 'dir':
            curr[s[1]] = dict()
        else:
            curr[s[1]] = int(s[0])

directories = []

def dfs(curr):
    if type(curr) is int:
        return curr
    res = 0
    for key in curr:
        a = dfs(curr[key])
        res += a
    directories.append(res)
    return res

# Part 1
dfs(outdir)
directories = np.array(directories)
print(np.sum(directories[directories <= 100000]))

# Part 2
available = 70000000 - np.max(directories)
needed = 30000000 - available
print(np.min(directories[directories >= needed]))