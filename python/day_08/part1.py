import numpy as np

with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [[int(t) for t in line.strip()] for line in lines]

grid = np.array(lines)

left_cum_max = np.copy(grid)
right_cum_max = np.copy(grid)
top_cum_max = np.copy(grid)
bot_cum_max = np.copy(grid)

for i in range(1, grid.shape[1]):
    left_cum_max[:, i] = np.max(np.stack([left_cum_max[:, i], left_cum_max[:, i-1]]), axis=0)

for i in range(1, grid.shape[0]):
    top_cum_max[i, :] = np.max(np.stack([top_cum_max[i, :], top_cum_max[i-1,:]]), axis=0)

for i in reversed(range(0, grid.shape[1]-1)):
    right_cum_max[:, i] = np.max(np.stack([right_cum_max[:, i], right_cum_max[:,i+1]]), axis=0)

for i in reversed(range(0, grid.shape[0]-1)):
    bot_cum_max[i, :] = np.max(np.stack([bot_cum_max[i, :], bot_cum_max[i+1, :]]), axis=0)

total = 0
for i in range(1, grid.shape[0]-1):
    for j in range(1, grid.shape[1]-1):
        if grid[i, j] > left_cum_max[i, j-1] or grid[i, j] > right_cum_max[i ,j+1] or grid[i, j] > top_cum_max[i-1,j] or grid[i, j] > bot_cum_max[i+1,j]:
            total += 1

print(total + grid.shape[0]*2 + grid.shape[1]*2 -4)
