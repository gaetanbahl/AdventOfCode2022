with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [l.strip().split(",") for l in lines]
    lines = [ [tuple(s.split("-")) for s in l] for l in lines ]

total = 0
for s1, s2 in lines:
    s11, s12, s21, s22 = int(s1[0]), int(s1[1]), int(s2[0]), int(s2[1])
    if (s11 >= s21 and s12 <= s22) or (s21 >= s11 and s22 <= s12):
        total += 1

print(total)