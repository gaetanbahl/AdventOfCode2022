import numpy as np

with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

shape = (len(lines), len(lines[0]))

array = np.zeros(shape)
start = [0,0]
end = [0,0]

for i,l in enumerate(lines):
    for j,c in enumerate(l):
        array[i, j] = ord(c) - 97
        if c == "S":
            start = (i,j)
        elif c == 'E':
            end = (i,j)

print("starting pos:", start)
print("end pos:", end)

array[start[0], start[1]] = 0
array[end[0], end[1]] = 25

def possibilities(i,j,array):
    poss = []
    if j > 0:
        if array[i, j-1] - array[i, j] <= 1:
            poss.append((i, j-1))
    if i > 0:
        if array[i-1, j] - array[i, j] <= 1:
            poss.append((i-1, j))
    if j < array.shape[1] - 1:
        if array[i, j+1] - array[i, j] <= 1:
            poss.append((i, j+1))
    if i < array.shape[0] - 1:
        if array[i+1, j] - array[i, j] <= 1:
            poss.append((i+1, j))

    return poss

lengths = np.zeros(shape) + np.inf
lengths[start[0], start[1]] = 0

stack = [start]
visited = set()

while len(stack):
    curr = stack.pop(0)
    dist = lengths[curr[0], curr[1]]
    visited.add(curr)
    if curr == end:
        print("reached end")
        print(dist)
    candidates = [p for p in possibilities(curr[0], curr[1], array) if p not in visited]
    for c in candidates:
        lengths[c[0], c[1]] = min(dist+1, lengths[c[0], c[1]])
        if not c in stack:
            stack.append(c)
    stack = sorted(stack, key=lambda x : lengths[x[0], x[1]])

print(lengths[end[0], end[1]])