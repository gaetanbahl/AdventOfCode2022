import re
from tqdm import tqdm
from functools import reduce

with open("input.txt", 'r') as f:
    lines = f.readlines()
    numbers = list(map(lambda x: [int(x) for x in re.findall(r"\d+", x)], lines))[:3]

memo = dict()

def quality_level(blueprint, ore, clay, obs, geode, ore_r, clay_r, obs_r, geode_r, remaining):

    global maximum

    if remaining == 0:
        return geode

    if (ore, clay, obs, geode, ore_r, clay_r, obs_r, geode_r, remaining) in memo:
        #print("memo hit")
        return memo[ore, clay, obs, geode, ore_r, clay_r, obs_r, geode_r, remaining]

    build_flag = 0

    upper_bound = geode + geode_r * remaining + sum([i for i in range(remaining)])

    if upper_bound < maximum:
        return 0

    poss = []
    # build a geode robot
    if ore >= blueprint[5] and obs >= blueprint[6]:
        ret = quality_level(blueprint, 
                                  ore-blueprint[5]+ore_r,
                                  clay+clay_r,
                                  obs-blueprint[6]+obs_r,
                                  geode+geode_r,
                                  ore_r,
                                  clay_r,
                                  obs_r,
                                  geode_r+1,
                                  remaining-1)
        memo[ore, clay, obs, geode, ore_r, clay_r, obs_r, geode_r, remaining] = ret
        return ret
        
    # build an ore robot
    if ore >= blueprint[1]:
        poss.append(quality_level(blueprint, 
                                  ore-blueprint[1]+ore_r,
                                  clay+clay_r,
                                  obs+obs_r,
                                  geode+geode_r,
                                  ore_r+1,
                                  clay_r,
                                  obs_r,
                                  geode_r,
                                  remaining-1))
        build_flag += 1
    # build a clay robot
    if ore >= blueprint[2]:
        poss.append(quality_level(blueprint, 
                                  ore-blueprint[2]+ore_r,
                                  clay+clay_r,
                                  obs+obs_r,
                                  geode+geode_r,
                                  ore_r,
                                  clay_r+1,
                                  obs_r,
                                  geode_r,
                                  remaining-1))
        build_flag += 1
    # build an obsidian robot
    if ore >= blueprint[3] and clay >= blueprint[4]:
        poss.append(quality_level(blueprint, 
                                  ore-blueprint[3]+ore_r,
                                  clay-blueprint[4]+clay_r,
                                  obs+obs_r,
                                  geode+geode_r,
                                  ore_r,
                                  clay_r,
                                  obs_r+1,
                                  geode_r,
                                  remaining-1))
        build_flag += 1

    # build nothing
    if build_flag < 3:
        poss.append(quality_level(blueprint, 
                                ore+ore_r,
                                clay+clay_r,
                                obs+obs_r,
                                geode+geode_r,
                                ore_r,
                                clay_r,
                                obs_r,
                                geode_r,
                                remaining-1))

    ret = max(poss)

    memo[ore, clay, obs, geode, ore_r, clay_r, obs_r, geode_r, remaining] = ret

    if ret > maximum:
        maximum = ret

    return ret

q_levels = []

for i, blueprint in enumerate(tqdm(numbers)):
    memo = dict()
    maximum = 0
    q = quality_level(blueprint, 0, 0, 0, 0, 1, 0, 0, 0, 32)
    q_levels.append(q)
    print(q)

print(reduce(lambda x, y: x*y, q_levels))
