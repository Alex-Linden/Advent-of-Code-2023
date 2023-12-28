puzzle_input = open("day13.txt").read().split("\n")
test = open("day13t1.txt").read().split("\n")


mirror_map = []
mini = []
for row in puzzle_input:
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