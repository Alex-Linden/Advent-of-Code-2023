puzzle_input = open("day13.txt").read().split("\n")
test = open("day13t1.txt").read().split("\n")


mirror_map = []
mini = []
for row in puzzle_input:
# for row in test:
    if row != "":
        mini.append(row)
    else:
        mirror_map.append(mini)
        mini = []
mirror_map.append(mini)

m_loc = []

def rev_string(str):
    return str[::-1]

def find_mirror_idx(matrix):
    for i in range(1, len(matrix[0])):
        row = 0
        minn = min(i, len(matrix[0]) - i)
        # print(minn)
        while row < len(matrix):
            # print(matrix[row][i-minn:i], rev_string(matrix[row][i:i+minn]))
            # print(matrix[row][:i], matrix[row][i:])
            if matrix[row][i-minn:i] != rev_string(matrix[row][i:i+minn]):
                break
            row += 1

        if row == len(matrix):
            # print("------Row = len------",i)
            # m_loc.append(row)
            return i
    return -1

for m in mirror_map:
    # print(m)
    v = find_mirror_idx(m)
    if v == -1:
        turned_m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
        v = find_mirror_idx(turned_m) * 100

    print(v)
    m_loc.append(v)
    # for i in range(1, len(m[0])):
    #     row = 0
    #     minn = min(i, len(m[0]) - i)
    #     print(minn)
    #     while row < len(m):
    #         print(m[row][i-minn:i], rev_string(m[row][i:i+minn]))
    #         # print(m[row][:i], m[row][i:])
    #         if m[row][i-minn:i] != rev_string(m[row][i:i+minn]):
    #             break
    #         row += 1

    #     if row == len(m):
    #         print("------Row = len------",i)
    #         m_loc.append(row)


print(sum(m_loc), m_loc)


# part 2
# brute force is the only idea I can come up with lets see how long it takes

m_loc2 = []
for o, m in enumerate(mirror_map):
    not_found = True
    # print(c)
    for col in range(1, len(m[0])):
        diff = 0
        l, r = col - 1, col
        while 0 <= l and r < len(m[0]):
            for row in range(len(m)):
                if m[row][l] != m[row][r]:
                    diff += 1
            l -= 1
            r += 1
            if diff > 1:
                break
        if diff == 1:
            m_loc2.append(col)
    for row in range(1, len(m)):
        diff = 0
        up, down = row - 1, row
        while 0 <= up and down < len(m):
            for col in range(len(m[0])):
                if m[up][col] != m[down][col]:
                    diff += 1
            up -= 1
            down += 1
            if diff > 1:
                break
        if diff == 1:
            m_loc2.append(row * 100)


    # for i in range(len(m)):
    #     for j in range(len(m[i])):
    #         c = m.copy()
    #         ch = "." if c[i][j] == "#" else "#"
    #         c[i] = c[i][:j] + ch + c[i][j+1:]

    #         idx = find_mirror_idx(c)
    #         # print(idx)
    #         if idx == -1 or idx == m_loc[o]:
    #             turn_c = [[c[j][i] for j in range(len(c))] for i in range(len(c[0]))]
    #             # if i == 1 and j == 4 and o == 1:
    #             #     print(turn_c)
    #             idx = find_mirror_idx(turn_c) * 100
    #             # print(idx)
    #         if o == 4:
    #             print(idx)
    #         if idx > -1 and idx != m_loc[o] and not_found:
    #             m_loc2.append(idx)
    #             not_found = False
    #             print(o)
    #             break

    #     if not not_found:
    #         break
    # if not_found:
    #     m_loc2.append(m_loc[o])

print(len(m_loc), len(m_loc2))

print("mloc2",sum(m_loc2), m_loc2)