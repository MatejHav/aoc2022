data = open('11.txt').read().split('\n\n')

monkeys = []

# part 2
common_divisor = 1


class Monkey():
    def __init__(self, items, operation_str, divisible, true, false):
        self.items = items
        self.operation = lambda old: eval(operation_str)
        self.test = lambda n: true if n % divisible == 0 else false
        self.inspections = 0

    def add(self, item):
        self.items.append(item)

    def round(self):
        to_remove = []
        for index, item in enumerate(self.items):
            #part 1
            #self.items[index] = self.operation(item) // 3
            #part 2
            self.items[index] = self.operation(item) % common_divisor
            self.inspections += 1
            next_monkey = self.test(self.items[index])
            monkeys[next_monkey].add(self.items[index])
            to_remove.append(index)
        to_remove.reverse()
        for index in to_remove:
            self.items.pop(index)


for monkey in data:
    lines = monkey.split('\n')
    items = list(map(int, lines[1].split(':')[1].split(', ')))
    operation_str = lines[2].split('=')[1].strip()
    divisible = int(lines[3].split(' ')[-1])
    common_divisor *= divisible
    true = int(lines[4].split(' ')[-1])
    false = int(lines[5].split(' ')[-1])
    monkeys.append(Monkey(items, operation_str, divisible, true, false))

# part 1 and 2
for round in range(10000):
    print(f'########### {round} ###########')
    for monkey in monkeys:
        print(monkey.items)
        monkey.round()

sort = sorted(monkeys, key=lambda monkey: monkey.inspections, reverse=True)
print(sort[0].inspections * sort[1].inspections)
