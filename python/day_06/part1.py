with open("input.txt", 'r') as f:
    line = f.readlines()[0].strip()

for i in range(len(line)-4):
    if len(set(line[i:(i+4)])) == 4:
        print(i + 4)
        break