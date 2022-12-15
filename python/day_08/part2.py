import numpy as np

with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [[int(t) for t in line.strip()] for line in lines]

grid = np.array(lines)

left_dist = np.zeros_like(grid)
right_dist = np.zeros_like(grid)
top_dist = np.zeros_like(grid)
bot_dist = np.zeros_like(grid)

for i in range(grid.shape[0]):
    indices = [0 for _ in range(10)]
    for j in range(grid.shape[1]):
        left_dist[i,j] = j - max(indices[grid[i,j]:])
        indices[grid[i,j]] = j

for i in range(grid.shape[0]):
    indices = [grid.shape[1]-1 for _ in range(10)]
    for j in reversed(range(grid.shape[1])):
        right_dist[i,j] = min(indices[grid[i,j]:]) - j 
        indices[grid[i,j]] = j  

for j in range(grid.shape[1]):
    indices = [0 for _ in range(10)]
    for i in range(grid.shape[0]):
        top_dist[i,j] = i - max(indices[grid[i,j]:])   
        indices[grid[i,j]] = i 

for j in range(grid.shape[1]):
    indices = [grid.shape[0]-1 for _ in range(10)]
    for i in reversed(range(grid.shape[0])):
        bot_dist[i,j] = min(indices[grid[i,j]:]) - i 
        indices[grid[i,j]] = i

score = left_dist * right_dist * top_dist * bot_dist
print(np.max(score))