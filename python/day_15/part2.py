
from tqdm import tqdm

with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [l.split(" ") for l in lines]
    lines = [(int(l[2][2:-1]),int(l[3][2:-1]),int(l[-2][2:-1]),int(l[-1][2:-1])) for l in lines]

def manhattan(l):
    return abs(l[2] - l[0]) + abs(l[3] - l[1])


xmin = min(lines, key=lambda x : (x[0] - manhattan(x)))
xmax = max(lines, key=lambda x : (x[0] + manhattan(x)))

line = set()

boundsmin = 0
boundsmax = 4000000

flag = False
for l in tqdm(lines):
    distance_b_s = manhattan(l) +1

    points_around = list()

    for i in range(0, distance_b_s+1):
        points_around.append((l[0]+distance_b_s-i, l[1]-i ))
        points_around.append((l[0]+distance_b_s-i, l[1]+i ))
        points_around.append((l[0]-distance_b_s+i, l[1]+i ))
        points_around.append((l[0]-distance_b_s+i, l[1]-i ))

    for p in points_around:
        if p[0] < boundsmin or p[0] > boundsmax or p[1] < boundsmin or p[1] > boundsmax:
            continue

        flag = False
        for s in lines:
            if manhattan((p[0], p[1], s[0], s[1])) <= manhattan(s):
                flag = True
                break
        
        if not flag:
            print("found", p)
            break
    if not flag:
        break
