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
    global humn  

    if type(monkey_dict[name]) == int:
        if name == "humn":
            return humn

        return monkey_dict[name]
    else:
        m1 = compute(monkey_dict[name][0])
        m2 = compute(monkey_dict[name][2])

        if name == "root":
            print("output", m1, m2)
            if m1 == m2:
                print("FOUND ANSWER", humn)
                exit()
            return m1, m2

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

lr = 0.0001
humn = 1000000000000
while True:

    humn = humn - 1
    prev, m2 = compute("root")

    humn = humn + 2
    after, m2 = compute("root")
    humn = humn - 1 + (prev - after) * (prev - m2) * lr
    print("input", int(humn))