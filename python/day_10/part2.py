with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

cycles = 1
X = 1

look = [20, 60, 100, 140, 180, 220]
total = 0

crt_pos = 1

def draw():
    global crt_pos
    if crt_pos % 40 <= X + 2 and crt_pos % 40 >= X :
        print("#", end="")
    else:
        print(".", end="")
    if crt_pos % 40 == 0:
        print()
    crt_pos += 1

def incr_cycles():
    global cycles, total
    if cycles in look:
        total += X * cycles
    cycles += 1
    draw()

for l in lines:
    if l.startswith("noop"):
        incr_cycles()
    elif l.startswith("add"):
        incr_cycles()
        incr_cycles()
        X += int(l.split(" ")[1])
print()