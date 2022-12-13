from functools import cmp_to_key

data = open('13.txt').read().split('\n\n')


def check(v1, v2):
    if type(v1) == int and type(v1) == type(v2):
        if v1 == v2:
            return None
        return v1 < v2
    if type(v1) == list and type(v1) == type(v2):
        if len(v1) == 0 and len(v2) > 0:
            return True
        if len(v1) == 0 and len(v2) == 0:
            return None
        if len(v1) > 0 and len(v2) == 0:
            return False
        first = check(v1[0], v2[0])
        if first is not None:
            return first
        return check(v1[1:], v2[1:])
    if type(v1) == int and type(v2) == list:
        return check([v1], v2)
    if type(v1) == list and type(v2) == int:
        return check(v1, [v2])
    return False

# part 1
res = 0
p = []
for index, packets in enumerate(data):
    s = packets.split('\n')
    v1 = eval(s[0])
    v2 = eval(s[1])
    p.append(v1)
    p.append(v2)
    if check(v1, v2):
        res += index+1

print('part1:', res)

# part 2

a = [[2]]
b = [[6]]
p.append(a)
p.append(b)

def compare(v1, v2):
    val = check(v1, v2)
    if val is None:
        return 0
    return 1 if val else -1

sort = sorted(p, key = cmp_to_key(compare), reverse=True)
print('part2:', (sort.index(a)+1) * (sort.index(b)+1))