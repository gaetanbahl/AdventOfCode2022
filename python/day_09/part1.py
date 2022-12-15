with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [l.strip().split(" ") for l in lines]

t = [0, 0]
h = [0, 0]

visited = set()
visited.add(tuple(t))

def dist_inf(h, t):
    return max(abs(h[0]-t[0]), abs(h[1]-t[1]))

def clamp(n):
    return int(max(min(n, 1), -1))

def move(h, t, dir):

    if dir == "U":
        h[1] += 1
    elif dir == "D":
        h[1] -= 1
    elif dir == "R":
        h[0] += 1
    elif dir == "L":
        h[0] -= 1

    if dist_inf(h, t) > 1:
        t[0] += clamp(h[0] - t[0])
        t[1] += clamp(h[1] - t[1])
        visited.add(tuple(t))

    return h, t

for l in lines:
    for _ in range(int(l[1])):
        h, t = move(h, t, l[0])

print(len(visited))