from collections import defaultdict
puzzle_input = open("day5.txt").read().split('\n')

test = open("day5test.txt").read().split('\n')

# farm_almanac = test
farm_almanac = puzzle_input

seeds = farm_almanac[0].split(" ")[1:]

seeds2 = [int(seed) for seed in seeds]
seeds = [[int(seed)] for seed in seeds]
# print(seeds)


start_soil = farm_almanac.index("seed-to-soil map:") + 1
end_soil = farm_almanac[start_soil:].index("") + 1
# print(start_soil, end_soil + 3)

# print(farm_almanac[start_soil:end_soil + 3])
def find_next_spot(start, range_map):
    nxt = start
    for row in range_map:
        row = [int(num) for num in row.split(" ")]
        n, cur, r = row
        diff = n - cur
        if cur <= nxt <= cur + r -1:
            return nxt + diff
    return nxt

for seed in seeds:
    i = 2
    while i < len(farm_almanac):
        start, end = i + 1, i + 1
        while farm_almanac[end] != "":
            end += 1
        nxt = find_next_spot(seed[-1], farm_almanac[start:end])
        seed.append(nxt)
        i = end + 1

out = seeds[-1][-1]
for seed in seeds:
    out = min(out, seed[-1])
print("part 1=", out)

pt2_seeds = {}
for i in range(0, len(seeds2), 2):
    key = seeds2[i]
    val = seeds2[i+1]
    pt2_seeds[key] = val

print(pt2_seeds)

def find_next_spot_pt2(start, rnge,  range_map):
    # if rnge < 1: print(start, rnge)
    nxt = start
    closest_nxt = float("inf")
    found = False
    out = []
    for row in range_map:
        row = [int(num) for num in row.split(" ")]
        n, cur, r = row
        diff = n - cur
        top = cur + r -1
        if cur <= nxt <= top:
            # print("if cur <= nxt <= top:")
            found = True
            new_start = nxt + diff
            # print("line 67=", "top=",top, nxt + rnge)
            # print("newstart", new_start)
            if top + diff + 1 >= new_start + rnge:
                return [[new_start, rnge]]
            else:
                new_rnge = top - start
                # print("line 75=", top, start )
                return [[new_start, new_rnge]] + find_next_spot_pt2(top +1, rnge-new_rnge, range_map )
        elif nxt < cur < nxt + rnge:
            closest_nxt = min(closest_nxt, cur)
    if not found and closest_nxt - nxt < rnge:
        # print("line 80=", closest_nxt, rnge + nxt - closest_nxt)
        return [[nxt, closest_nxt - nxt]] + find_next_spot_pt2(closest_nxt, rnge + nxt - closest_nxt, range_map)
    else:
        return [[nxt, rnge]]

pt2_min_seed = float("inf")
for seed, rnge in pt2_seeds.items():
    # create cur level que => list [{min-sed-val:range}]
    # for seed-range in que test against map
    # find next spot for seed
    # check if range for next is greater than cur range
    # if cur range is greater
    # adjust next seed range
    # find top of next range
    # if not in range adjust
    cur_lvl = [[seed, rnge]]
    # print(cur_lvl)
    next_lvl = []
    i = 2
    while i < len(farm_almanac):
        start, end = i + 1, i + 1
        while farm_almanac[end] != "":
            end += 1
        for sprd in cur_lvl:
            # print(sprd)
            s, r = sprd[0], sprd[1]
            next_lvl += find_next_spot_pt2(s, r, farm_almanac[start:end])
        cur_lvl = next_lvl
        # print(cur_lvl)
        next_lvl = []
        i = end + 1


    for sd in cur_lvl:
        pt2_min_seed = min(pt2_min_seed, sd[0])


print("part2=", pt2_min_seed)

# def map_next()