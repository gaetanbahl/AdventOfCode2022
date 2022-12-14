with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

lines = [(l[:len(l)//2], l[len(l)//2:]) for l in lines]

def common(left, right):
    for c in left:
        if c in right:
            return c

total = 0

for l in lines:
    c = common(*l)
    if c == c.upper():
        total += ord(c) - 64 + 26
    else:
        total += ord(c) - 96 

print(total)