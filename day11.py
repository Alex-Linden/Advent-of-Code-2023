puzzle_input = open("day11.txt").read().split("\n")
test = open("day11t1.txt").read().split("\n")

star_map = puzzle_input
# star_map = test
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
        star_map.insert(i+1, "."*len(star_map[0]))
        i+=1
    i+=1

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
        turned_star_map.insert(j+1, new_row)
        j+=1
    j+=1
# print("######")
# print(len(turned_star_map), "x", len(turned_star_map[0]))
# for row in turned_star_map:
#     print("".join(row))

galaxies = []

for y, row in enumerate(turned_star_map):
    for x, ch in enumerate(row):
        if ch == "#":
            galaxies.append((y, x))


# print(galaxies)

total = 0

for i in range(len(galaxies)):
    y1, x1 = galaxies[i]
    for j in range(i+1, len(galaxies)):
        y2, x2 = galaxies[j]
        total += abs(y1-y2) + abs(x1-x2)

print(total)
