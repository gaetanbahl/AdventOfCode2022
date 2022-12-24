from itertools import cycle
# import numpy as np
# import matplotlib.pyplot as plt
# import random
from tqdm import tqdm

with open("input.txt", 'r') as f:
    line = f.readlines()[0]

line = [ 1 if x == '>' else -1 for x in line.strip()]

floor = 0
width = 7
n_blocks = 1000000000000
grid = dict()

shapes = []
shapes.append([(0,0), (1,0), (2,0), (3,0) ]) # horizontal line
shapes.append([(1,0), (0,1), (1,1), (2,1), (1,2)]) # +
shapes.append([(0,0), (1,0), (2,0), (2,1), (2,2)]) # reverse L
shapes.append([(0,0), (0,1), (0,2), (0,3)]) # vertical line
shapes.append([(0,0), (1,0), (0,1), (1,1)]) # square


def spawn(block, floor):
    b = [(x+2,y+floor+4) for x,y in block]
    return b

def push(block, dir):
    b = [(x+dir,y) for x,y in block]
    return b

def fall(block):
    b = [(x,y-1) for x,y in block]
    return b

def check(block, grid):
    for p in block:
        if p in grid:
            return True
        if p[0] < 0:
            return True
        if p[0] > width - 1:
            return True
        if p[1] <= 0:
            return True
    
    return False

def write(block, grid):
    for p in block:
        grid[p] = "#"


def write_numpy(block, array):
    color = random.randint(60, 255)
    for p in block:
        array[(p[1], p[0])] = color

def height(grid):
    return max(grid, key=lambda x : x[1])

moves = cycle(line)

# array = np.zeros((4000, 7))

history = []

for i in tqdm(range(n_blocks)):
    
    block = shapes[i%len(shapes)].copy()
    block = spawn(block, floor)

    while True:
        move = next(moves)

        prev = block.copy()
        block = push(block, move)
        if check(block, grid):
            block = prev
        prev = block.copy()
        block = fall(block)
        if check(block, grid):
            block = prev
            break

    write(block, grid)
    # write_numpy(block, array)
    history.append(height(grid)[1] - floor)
    floor = height(grid)[1]

    if i > 10000:

        for ind in range(i):
            for l in range(1000,(len(history) - ind)//2):

                sums = [sum(history[ind+j*l:(ind+(j+1)*l)]) for j in range(5)]

                if len(set(sums)) == 1:

                    print("Found cycle length", l, "starting index", ind)

                    estimate = sum(history[:ind]) + ((n_blocks-ind) // l) * sum(history[ind:ind+l]) + sum(history[ind:((n_blocks-ind) % l)+ind])
                    
                    print("estimated height", estimate) 
                    exit()
