with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

cycles = 1
X = 1

look = [20, 60, 100, 140, 180, 220]
total = 0

def incr_cycles():
    global cycles, total
    if cycles in look:
        total += X * cycles
    cycles += 1

for l in lines:
    if l.startswith("noop"):
        incr_cycles()
    elif l.startswith("add"):
        incr_cycles()
        incr_cycles()
        X += int(l.split(" ")[1])

print(total)
    