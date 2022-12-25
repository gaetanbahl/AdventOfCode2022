with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [tuple([int(c) for c in l.strip().split(",")]) for l in lines]


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
    

total_surface = 0

added_points = set()

for p in lines:

    surface_removed = sum([isnextto(p, p2) for p2 in added_points])
    total_surface += 6 - 2*surface_removed
    added_points.add(p)

print(total_surface)