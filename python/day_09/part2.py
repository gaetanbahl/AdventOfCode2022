with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [l.strip().split(" ") for l in lines]

rope = [[0, 0] for i in range(10)]

visited = set()
visited.add(tuple(rope[-1]))

def dist_inf(h, t):
    return max(abs(h[0]-t[0]), abs(h[1]-t[1]))

def clamp(n):
    return int(max(min(n, 1), -1))

def move(rope, dir):

    if dir == "U":
        rope[0][1] += 1
    elif dir == "D":
        rope[0][1] -= 1
    elif dir == "R":
        rope[0][0] += 1
    elif dir == "L":
        rope[0][0] -= 1

    for i in range(len(rope)-1):
        if dist_inf(rope[i], rope[i+1]) > 1:
            rope[i+1][0] += clamp(rope[i][0] - rope[i+1][0])
            rope[i+1][1] += clamp(rope[i][1] - rope[i+1][1])
            if i == len(rope) - 2:
                visited.add(tuple(rope[-1]))
    return rope

for l in lines:
    for _ in range(int(l[1])):
        rope = move(rope, l[0])

print(len(visited))