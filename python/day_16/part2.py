import networkx as nx
from tqdm import tqdm

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

def compute_remaining_pressure_released(current_me, current_elefant, minutes_left, remaining_travel_time_me, remaining_travel_time_elefant, remaining_nodes):

    if (current_me, current_elefant, minutes_left, remaining_travel_time_me, remaining_travel_time_elefant, tuple(remaining_nodes)) in memo:
        return memo[(current_me, current_elefant, minutes_left, remaining_travel_time_me, remaining_travel_time_elefant, tuple(remaining_nodes))]
    if (current_elefant, current_me, minutes_left, remaining_travel_time_elefant, remaining_travel_time_me, tuple(remaining_nodes)) in memo:
        return memo[(current_elefant, current_me, minutes_left, remaining_travel_time_elefant, remaining_travel_time_me, tuple(remaining_nodes))]

    if len(remaining_nodes) == 0:
        return 0

    if minutes_left <= 0:
        return 0

    possibilities = []

    # I am not travelling and the elefant is traveling
    # I have to make a decision
    if not remaining_travel_time_me and remaining_travel_time_elefant:

        # choose what I do
        for n in tqdm(remaining_nodes, position=len(remaining_nodes), leave=False) if len(remaining_nodes) > 11 else remaining_nodes:
            travel_time = len(paths[current_me][n])
            if travel_time <= minutes_left:
                ret = (minutes_left - travel_time)*flow[n] 
            else:
                ret = 0
            time_skip = min(remaining_travel_time_elefant, travel_time)
            ret += compute_remaining_pressure_released(n, current_elefant, 
                                                        minutes_left-time_skip,
                                                        travel_time-time_skip,
                                                        remaining_travel_time_elefant-time_skip,
                                                        [p for p in remaining_nodes if n != p])
            possibilities.append(ret)

    # I am traveling but not the elefant
    # elefant has to make a decision
    elif remaining_travel_time_me and not remaining_travel_time_elefant:

        # choose what elefant does
        for n in tqdm(remaining_nodes, position=len(remaining_nodes), leave=False) if len(remaining_nodes) > 11 else remaining_nodes:
            travel_time = len(paths[current_elefant][n])
            if travel_time <= minutes_left:
                ret = (minutes_left - travel_time)*flow[n] 
            else:
                ret = 0
            time_skip = min(remaining_travel_time_me, travel_time)
            ret += compute_remaining_pressure_released(current_me, n, 
                                                        minutes_left-time_skip,
                                                        remaining_travel_time_me-time_skip,
                                                        travel_time-time_skip,
                                                        [p for p in remaining_nodes if n != p])
            possibilities.append(ret)
    
    # we are both traveling
    elif remaining_travel_time_elefant and remaining_travel_time_me:
        time_skip = min(remaining_travel_time_me, remaining_travel_time_elefant)
        return compute_remaining_pressure_released(current_me, current_elefant, 
                                                    minutes_left-time_skip,
                                                    remaining_travel_time_me-time_skip,
                                                    remaining_travel_time_elefant-time_skip,
                                                    remaining_nodes)

    # we both have to make a decision
    elif not remaining_travel_time_elefant and not remaining_travel_time_me:  

        # problem is symmetric, I can choose first 
        for n in tqdm(remaining_nodes, position=len(remaining_nodes), leave=False)  if len(remaining_nodes) > 11 else remaining_nodes:
            remaining_nodes_after_1st = [p for p in remaining_nodes if n != p]

            # choose what elefant does
            for m in tqdm(remaining_nodes_after_1st, position=len(remaining_nodes_after_1st), leave=False) if len(remaining_nodes_after_1st) > 11 else remaining_nodes_after_1st:

                travel_time_me = len(paths[current_me][n])
                travel_time_elefant = len(paths[current_elefant][m])
                ret = 0 
                if travel_time_me <= minutes_left:
                    ret += (minutes_left - travel_time_me)*flow[n] 
                if travel_time_elefant <= minutes_left:
                    ret += (minutes_left - travel_time_elefant)*flow[m] 
                time_skip = min(travel_time_elefant, travel_time_me)
                ret += compute_remaining_pressure_released(n, m,
                                                            minutes_left-time_skip,
                                                            travel_time_me-time_skip,
                                                            travel_time_elefant-time_skip, 
                                                            [p for p in remaining_nodes if m != p and n != p])
                possibilities.append(ret)

    if len(possibilities):
        ret = max(possibilities)
    else:
        ret = 0
    
    memo[(current_me, current_elefant, minutes_left, remaining_travel_time_me, remaining_travel_time_elefant, tuple(remaining_nodes))] = ret
    return ret


max_flow = compute_remaining_pressure_released('AA', 'AA', 26, 0, 0, sorted(to_go))
print()
print(max_flow)