insts = open('10.txt').read().split('\n')

registers = {'X': 1}
ticks = 0
part_one = 0
part_two = ''

for inst in insts:
    inst = inst.split(' ')
    if inst[0] == 'noop':
        ticks += 1
    elif inst[0] == 'addx':
        if (ticks + 1 - 20) % 40 == 0:
            part_one += (ticks + 1) * registers['X']
        if (ticks + 2 - 20) % 40 == 0:
            part_one += (ticks + 2) * registers['X']
        ticks += 2
        registers['X'] += int(inst[1])
        continue
    if (ticks - 20) % 40 == 0:
        part_one += ticks * registers['X']

print(part_one)


# part 2
registers['X'] = 1

def draw(part_two):
    if abs(ticks % 40 - 1 - registers['X']) <= 1:
        part_two += '#'
    else:
        part_two += '.'
    return part_two


for inst in insts:
    inst = inst.split(' ')
    if inst[0] == 'noop':
        ticks += 1
        part_two = draw(part_two)
    elif inst[0] == 'addx':
        ticks += 1
        part_two = draw(part_two)
        if ticks % 40 == 0:
            part_two += '\n'
        ticks += 1
        part_two = draw(part_two)
        if ticks % 40 == 0:
            part_two += '\n'
        registers['X'] += int(inst[1])
        continue
    if ticks % 40 == 0:
        part_two += '\n'

print(part_two)
