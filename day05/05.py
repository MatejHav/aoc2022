all = open('05.txt').read().split('\n\n')
data = all[0].split('\n')[:-1]
rest = all[1].split('\n')

size = 9
stacks = [[] for _ in range(size)]

for line in data:
     s = line.split(' ')
     index = 0
     count = 0
     for char in s:
        if char == '':
            count += 1
        if char != '':
            val = list(char)[1]
            stacks[index].append(val)
            index += 1
            count = 0
            continue
        if count % 3 == 0:
            count = 0
            index += 1
            continue

for index in range(len(stacks)):
    stacks[index].reverse()

for instruction in rest:
    inst = instruction.split(' to ')
    temp = inst[0].split(' from ')
    inst = [int(temp[0].split(' ')[1]), int(temp[1]), int(inst[1])]
    temp = []
    for _ in range(inst[0]):
        val = stacks[inst[1]-1].pop()
        # part 1
        # stacks[inst[2]-1].append(val)
        # part 2
        temp.append(val)
    temp.reverse()
    for val in temp:
        stacks[inst[2]-1].append(val)

for stack in stacks:
    print(stack.pop(), end='')

