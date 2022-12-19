import networkx as nx

with open("input.txt", 'r') as f:
    lines = f.readlines()
    lines = [l.strip().split(" ") for l in lines]
    lines = [[l[1], int(l[4][5:-1]), l[9:]] for l in lines]

for l in lines:
    neighbors = []
    for n in l[2][:-1]:
        neighbors.append(n[:-1])
    neighbors.append(l[2][-1])
    l[2] = neighbors

G = nx.Graph()

for l in lines:
    G.add_node(l[0])

for l in lines:
    for n in l[2]:
        G.add_edge(l[0], n)

paths = dict(nx.all_pairs_shortest_path(G))

to_go = [l[0] for l in lines if l[1] > 0]

flow = dict()
for l in lines:
    flow[l[0]] = l[1]

total_nodes = len(to_go)

memo = dict()

def compute_remaining_pressure_released(current, minutes_left, remaining_nodes):

    if (current, minutes_left, tuple(remaining_nodes)) in memo:
        return memo[(current, minutes_left, tuple(remaining_nodes))]

    if len(remaining_nodes) == 0:
        return 0

    if minutes_left <= 2:
        return 0

    possibilities = []
    for i, n in enumerate(remaining_nodes):
        travel_time = len(paths[current][n])
        if travel_time >= minutes_left:
            continue
        ret = (minutes_left - travel_time)*flow[n] 
        ret += compute_remaining_pressure_released(n, 
                                                    minutes_left-travel_time, 
                                                    [m for m in remaining_nodes if m != n])
        possibilities.append(ret)

    if len(possibilities):
        ret = max(possibilities)
    else:
        ret = 0
    memo[(current, minutes_left, tuple(remaining_nodes))] = ret
    return ret


max_flow = compute_remaining_pressure_released('AA', 30, sorted(to_go))

print(max_flow)