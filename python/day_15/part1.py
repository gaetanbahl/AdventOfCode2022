with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [l.split(" ") for l in lines]
    lines = [(int(l[2][2:-1]),int(l[3][2:-1]),int(l[-2][2:-1]),int(l[-1][2:-1])) for l in lines]

def manhattan(l):
    return abs(l[2] - l[0]) + abs(l[3] - l[1])

row_of_interest = 2000000

xmin = min(lines, key=lambda x : (x[0] - manhattan(x)))
xmax = max(lines, key=lambda x : (x[0] + manhattan(x)))

print(xmin[0] - manhattan(xmin), xmax[0] + manhattan(xmax))

line = set()

for l in lines:
    distance_b_s = manhattan(l)

    distance_to_line = abs(row_of_interest - l[1])

    if distance_to_line <= distance_b_s:
        xmin = l[0] - (distance_b_s - distance_to_line)
        xmax = l[0] + (distance_b_s - distance_to_line)

        for i in range(xmin, xmax+1):
            line.add(i)
    
        if l[3] == row_of_interest:
            line.remove(l[2])

        if l[1] == row_of_interest:
            line.remove(l[0])

# print(line)
print(len(line))