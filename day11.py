puzzle_input = open("day11.txt").read().split("\n")
test = open("day11t1.txt").read().split("\n")

# star_map = puzzle_input.copy()
star_map = test.copy()
# print(len(star_map), "x", len(star_map[0]))

# for row in star_map:
#     print(row)
#
# turned_star_map = [
#     [star_map[j][i] for j in range(len(star_map))] for i in range(len(star_map[0]))
# ]

# print("######")


# for row in turned_star_map:
#     print("".join(row))

i = 0
while i < len(star_map):
    if star_map[i].find("#") == -1:
        star_map.insert(i + 1, "." * len(star_map[0]))
        i += 1
    i += 1

# print(len(star_map), "x", len(star_map[0]))
# for row in star_map:
#     print(row)


turned_star_map = [
    [star_map[j][i] for j in range(len(star_map))] for i in range(len(star_map[0]))
]
# print("######")
# print(len(turned_star_map), "x", len(turned_star_map[0]))
# for row in turned_star_map:
#     row = "".join(row)
#     print(row)


j = 0
while j < len(turned_star_map):
    if "#" not in turned_star_map[j]:
        new_row = turned_star_map[j].copy()
        turned_star_map.insert(j + 1, new_row)
        j += 1
    j += 1
# print("######")
print(len(turned_star_map), "x", len(turned_star_map[0]))
# for row in turned_star_map:
#     print("".join(row))
turned_star_map = [
    [turned_star_map[j][i] for j in range(len(turned_star_map))]
    for i in range(len(turned_star_map[0]))
]
galaxies = []

for y, row in enumerate(turned_star_map):
    for x, ch in enumerate(row):
        if ch == "#":
            galaxies.append((y, x))


# print(galaxies)

total = 0

for i in range(len(galaxies)):
    y1, x1 = galaxies[i]
    for j in range(i + 1, len(galaxies)):
        y2, x2 = galaxies[j]
        total += abs(y1 - y2) + abs(x1 - x2)

print(total)


star_map_older = puzzle_input
# star_map_older = test

new_idx_row = []
# for rown in star_map_older:
#     print(rown)
# TODO: need to fix index so starts at 0 for row and col
for i in range(len(star_map_older)):
    if i == 0:
        new_idx_row.append(0)
    elif star_map_older[i].find("#") == -1:
        new_idx_row.append(new_idx_row[-1] + 1000000)
    else:
        new_idx_row.append(new_idx_row[-1] + 1)
# print(new_idx_row)
new_idx_col = []
for col in range(len(star_map_older[0])):
    seen = False
    for row in range(len(star_map_older)):
        # print(row, col)
        # print(star_map_older[row][col])
        if star_map_older[row][col] == "#":
            seen = True
            break
    if col == 0:
        new_idx_col.append(0)
    elif seen:
        new_idx_col.append(new_idx_col[-1] + 1)
    else:
        new_idx_col.append(new_idx_col[-1] + 1000000)
# print(new_idx_col)
older_galaxies = []

for y, row in enumerate(star_map_older):
    for x, ch in enumerate(row):
        if ch == "#":
            older_galaxies.append((new_idx_row[y], new_idx_col[x]))

# print(galaxies)
# print(older_galaxies)
pt2_total = 0

for i in range(len(older_galaxies)):
    y1, x1 = older_galaxies[i]
    for j in range(i + 1, len(older_galaxies)):
        y2, x2 = older_galaxies[j]
        pt2_total += abs(y1 - y2) + abs(x1 - x2)

print("part2=", pt2_total)
