with open("input.txt", 'r') as f:
    monkeys = f.readlines()
    monkeys = map(lambda x: x.strip().split(" "), monkeys)

monkey_dict = dict()

for m in monkeys:

    if len(m) == 2:
        monkey_dict[m[0][:-1]] = int(m[1])
    else:
        monkey_dict[m[0][:-1]] = tuple(m[1:])

def compute(name):

    if type(monkey_dict[name]) == int:
        return monkey_dict[name]
    else:
        m1 = compute(monkey_dict[name][0])
        m2 = compute(monkey_dict[name][2])

        op = monkey_dict[name][1]

        if op == "*":
            return m1 * m2
        elif op == "+":
            return m1 + m2
        elif op == "-":
            return m1 - m2
        elif op == "/":
            return m1 / m2
        else:
            print("what")

print(compute("root"))

