
with open("input.txt", 'r') as f:
    lines = f.readlines()
    points = set([tuple([int(c) for c in l.strip().split(",")]) for l in lines])


def isnextto(p1, p2):
    if p1[0] == p2[0] and p1[1] == p2[1]:
        if p1[2] == p2[2] + 1 or p1[2] == p2[2] - 1:
            return True
    if p1[2] == p2[2] and p1[1] == p2[1]:
        if p1[0] == p2[0] + 1 or p1[0] == p2[0] - 1:
            return True
    if p1[0] == p2[0] and p1[2] == p2[2]:
        if p1[1] == p2[1] + 1 or p1[1] == p2[1] - 1:
            return True
    return False


def neighbors(p):
    n = []
    n.append((p[0]+1, p[1]  , p[2]))
    n.append((p[0]-1, p[1]  , p[2]))
    n.append((p[0]  , p[1]-1, p[2]))
    n.append((p[0]  , p[1]+1, p[2]))
    n.append((p[0]  , p[1]  , p[2]+1))
    n.append((p[0]  , p[1]  , p[2]-1))
    return n


def is_in_bounds(p, bounds):
    if p[0] >= bounds[0] and p[0] <= bounds[1] and p[1] >= bounds[2] and p[1] <= bounds[3] and p[2] >= bounds[4] and p[2] <= bounds[5]:
        return True
    else:
        return False


max0 = max(points, key=lambda x: x[0])[0]
min0 = min(points, key=lambda x: x[0])[0]
max1 = max(points, key=lambda x: x[1])[1]
min1 = min(points, key=lambda x: x[1])[1]
max2 = max(points, key=lambda x: x[2])[2]
min2 = min(points, key=lambda x: x[2])[2]

bounds = (min0-1, max0+1, min1-1, max1+1, min2-1, max2+1)

starting_point = (min0, min1, min2)

steam = set()
queue = [starting_point]

total_surface = 0

while len(queue):
    curr = queue.pop(0)

    if not is_in_bounds(curr, bounds):
        continue

    if curr in points:
        continue

    if curr in steam:
        continue

    steam.add(curr)

    neighs = neighbors(curr)

    for n in neighs:
        if n in points:
            total_surface += 1

    queue += neighs

print(total_surface)