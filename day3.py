import pdb
from collections import defaultdict
grid = open('day3.txt').read().split("\n")

# move through grid. When a num is found
# find perminiter of num island
# if any adjacent spaces have a symbol (not . 0-9)
# then that is a valid part and we will add to part counter

test = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
]
# grid =  test

row_max, col_max = len(grid), len(grid[0])

gears = defaultdict(list)

def find_edges(x,y):
    res = ""
    cords = []
    while x < col_max and grid[y][x].isdigit():
        res += grid[y][x]
        # print(res)
        cords.append((y, x))
        x += 1

    return (int(res), cords)

def touches_symbol(cords, part_num):
    for cord in cords:
        y, x = cord
        # if y == 29: breakpoint()
        perminiter = [(y, x+1), (y, x-1), (y+1, x), (y-1, x),
                    (y+1, x+1), (y-1, x-1), (y+1, x-1), (y-1, x+1)]
        symbols = "1234567890."
        for spot in perminiter:
            r, c = spot
            if 0 <= r < row_max and 0 <= c < col_max and grid[r][c] not in symbols:
                if grid[r][c] == "*":
                    gears[(r, c)].append(part_num)
                return True

    return False

valid_parts = []
all_parts = []
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char.isdigit() and (x == 0 or grid[y][x-1].isdigit() == False):
            part_num, cords = find_edges(x, y)
            if touches_symbol(cords, part_num):
                valid_parts.append(part_num)
            all_parts.append(part_num)

# for row in range(len(grid)):
#     col = 0
#     idx = 0
#     while col < len(grid[row]):
#         if grid[row][col].isdigit():
#             print(all_parts[idx], grid[row][col])
#             if str(all_parts[idx])[0] != grid[row][col]:
#                 print("error", row, col)
#             while grid[row][col].isdigit():
#                 col += 1
#             idx += 1
#         else:
#             col += 1


        #         sam = True
        # else:
        #     print(char, y, x)

print(sum(valid_parts))
# print(all_parts)
# print(gears)

pt = 0
for parts in gears.values():
    if len(parts) == 2:
        pt += (parts[0] * parts[1])

print(pt)
# f = 0
# print("t", (grid[29][f].isdigit() and (f == 0 or grid[29][f-1].isdigit() == False)))



# import sys
# import re
# from collections import defaultdict
# D = open("day3.txt").read().strip()
# lines = D.split('\n')
# G = [[c for c in line] for line in lines]
# R = len(G)
# C = len(G[0])

# p1 = 0
# nums = defaultdict(list)
# for r in range(len(G)):
#   gears = set() # positions of '*' characters next to the current number
#   n = 0
#   has_part = False
#   for c in range(len(G[r])+1):
#     if c<C and G[r][c].isdigit():
#       n = n*10+int(G[r][c])
#       for rr in [-1,0,1]:
#         for cc in [-1,0,1]:
#           if 0<=r+rr<R and 0<=c+cc<C:
#             ch = G[r+rr][c+cc]
#             if not ch.isdigit() and ch != '.':
#               has_part = True
#             if ch=='*':
#               gears.add((r+rr, c+cc))
#     elif n>0:
#       for gear in gears:
#         nums[gear].append(n)
#       if has_part:
#         p1 += n
#       n = 0
#       has_part = False
#       gears = set()

# print(p1)