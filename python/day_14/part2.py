import numpy as np
import matplotlib.pyplot as plt

with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [l.strip().split(" -> ") for l in lines]

coordinates = []
for l in lines:
    coordinates.append([tuple([int(n) for n in p.split(",")]) for p in l])
        
cave = dict()

def draw(start, end, cave):
    si = min(start[0], end[0])
    ei = max(start[0], end[0])
    sj = min(start[1], end[1])
    ej = max(start[1], end[1])

    for i in range(si, ei+1):
        for j in range(sj, ej+1):
            cave[(j, i)] = "#"

for l in coordinates:
    for i in range(len(l)-1):
        draw(l[i], l[i+1], cave)

max_depth = max(cave, key=lambda x : x[0])
print(max_depth)

start_sand = (0, 500)

for i in range(100000000000000):

    sand = list(start_sand)
    if start_sand in cave:
        break
    while True:
        if not (sand[0]+1, sand[1]) in cave:
            sand[0] += 1
        elif not (sand[0]+1, sand[1]-1) in cave:
            sand[0] += 1
            sand[1] -= 1
        elif not (sand[0]+1, sand[1]+1) in cave:
            sand[0] += 1
            sand[1] += 1
        else:
            cave[tuple(sand)] = "o"
            break

        if sand[0] > max_depth[0]:
            cave[tuple(sand)] = "o"
            break

print(i)

cave_np = np.zeros((1000,1000))

for p in cave:
    if cave[p] == 'o':
        cave_np[p[0], p[1]] = 1
    if cave[p] == '#':
        cave_np[p[0], p[1]] = 2

# plt.imshow(cave_np)
# plt.show()

print(np.sum(cave_np == 1))