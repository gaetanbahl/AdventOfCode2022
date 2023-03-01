import numpy as np

with open("input.txt", 'r') as f:
    lines = f.readlines()
    commands = lines[-1]
    grid = lines[:-2]

def mapping(c):
    if c == " ":
        return 0
    elif c == ".":
        return 1
    elif c == "#":
        return 2

facing = [np.array([0, 1]), np.array([1, 0]), np.array([0, -1]), np.array([-1, 0])]

curr_facing = 0

pos = np.array([0, grid[0].index(".")])

maxlen = max(map(len, grid))

grid = [[mapping(c) for c in l.strip("\n")] + [0 for _ in range(maxlen - len(l))] for l in grid]

grid = np.array(grid)

def turn(c, curr_facing):
    if c == 'R':
        curr_facing += 1
    elif c == 'L':
        curr_facing -= 1
    curr_facing %= 4
    return curr_facing


numbers = [str(n) for n in range(10)]

commands = list(commands.strip())

while len(commands):

    display = grid.copy()

    display[pos[0], pos[1]] = curr_facing + 4
    print(display)

    c = commands.pop(0)

    if c == 'R' or c == 'L':
        curr_facing = turn(c, curr_facing)
        print(c)
    else:
        l = [c]

        while len(commands) and commands[0] in numbers:
            l.append(commands.pop(0))
        
        forward = int("".join(l))
        print(forward)
        
        for _ in range(forward):
            new_pos = pos + facing[curr_facing]

            new_pos[0] = new_pos[0] % grid.shape[0]
            new_pos[1] = new_pos[1] % grid.shape[1]

            if grid[tuple(new_pos)] == 2:
                break
            elif grid[tuple(new_pos)] == 0:
                if curr_facing == 0:
                    new_pos[1] = 0
                elif curr_facing == 1:
                    new_pos[0] = 0
                elif curr_facing == 2:
                    new_pos[1] = grid.shape[1]-1
                elif curr_facing == 3:
                    new_pos[0] = grid.shape[0]-1
                while grid[tuple(new_pos)] == 0:
                    print(new_pos)
                    new_pos += facing[curr_facing]
                
                if grid[tuple(new_pos)] != 2:
                    pos = new_pos
            elif grid[tuple(new_pos)] == 1:
                pos = new_pos

print(pos)
print(1000 * (pos[0]+1) + 4 * (pos[1]+1) + curr_facing)