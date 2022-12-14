with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

lines = [(lines[n:n+3]) for n in range(0, len(lines), 3)]

def common(first, second, third):
    for c in first:
        if c in second and c in third:
            return c

total = 0

for l in lines:
    c = common(*l)
    if c == c.upper():
        total += ord(c) - 64 + 26
    else:
        total += ord(c) - 96 

print(total)