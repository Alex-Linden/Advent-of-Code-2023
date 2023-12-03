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
# grid = test

row_max, col_max = len(grid), len(grid[0])

def find_edges(x,y):
    res = ""
    cords = []
    while x < col_max and grid[y][x].isdigit():
        res += grid[y][x]
        # print(res)
        cords.append((y, x))
        x += 1

    return (int(res), cords)

def touches_symbol(cords):
    for cord in cords:
        y, x = cord
        perminiter = [(y, x+1), (y, x-1), (y+1, x), (y-1, x),
                    (y+1, x+1), (y-1, x-1), (y+1, x-1), (y-1, x+1)]
        symbols = "1234567890."
        for spot in perminiter:
            r, c = spot
            if 0 <= r < row_max and 0 <= c < col_max and grid[r][c] not in symbols:
                return True

    return False

valid_parts = []
all_parts = []
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char.isdigit() and (grid[y][x-1].isdigit() == False):
            part_num, cords = find_edges(x, y)
            if touches_symbol(cords):
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






