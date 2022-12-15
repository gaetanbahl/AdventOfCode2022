stacks = [[] for i in range(9)]

with open("input.txt", 'r') as f:
    lines = f.readlines()

letter_indices = [1 + 4*i for i in range(9)]

for l in reversed(lines[:8]):
    for i in range(9):
        letter = l[letter_indices[i]]
        if letter != " ":
            stacks[i].append(letter)

moves = []
for l in lines[10:]:
    l = l.split(" ")
    moves.append((int(l[1]), int(l[3]), int(l[5])))

for m in moves:
    tmp_stack = []
    for i in range(m[0]):
        tmp_stack.append(stacks[m[1]-1].pop())
    stacks[m[2]-1] += reversed(tmp_stack)


for s in stacks:
    print(s[-1], end="")

print()