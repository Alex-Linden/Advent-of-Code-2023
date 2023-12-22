from functools import cache

puzzle_input = open("day12.txt").read().split("\n")
test = open("day12t1.txt").read().split("\n")


class Spring:
    def __init__(self, record):
        self.record = record

    def parse_row(self, row):
        """take a string and split into 2 parts
        part 1 spring: string map of possible alignment of springs
        part2 list of ints"""
        springs, count = row.split(" ")
        count = eval(count)
        return [springs, count]

    @cache
    def find_possible_arrangements(self, spring, count, continuous=0):
        # print(spring, count)
        # base case
        if not spring:
            return not count and not continuous
        total = 0
        q = ".#" if spring[0] == "?" else spring[0]
        for c in q:
            if c == "#":
                total += self.find_possible_arrangements(
                    spring[1:], count, continuous + 1
                )
            else:
                if continuous:
                    if count and count[0] == continuous:
                        total += self.find_possible_arrangements(spring[1:], count[1:])
                else:
                    total += self.find_possible_arrangements(spring[1:], count)
        return total

    def count_each_row(self):
        count_per_row = []
        for row in self.record:
            spring, count = self.parse_row(row)
            # print(spring, count)
            count = self.find_possible_arrangements(spring + ".", count)
            count_per_row.append(count)
        return count_per_row

    def count_each_row_pt2(self):
        p2_count = 0
        for row in self.record:
            spring, count = self.parse_row(row)
            spring = (spring + "?") * 5
            # print(spring, count)
            count = count * 5
            p2_count += self.find_possible_arrangements(spring[:-1] + ".", count)
        return p2_count


test1 = Spring(test)
pz = Spring(puzzle_input)

print(sum(test1.count_each_row()))
print(sum(pz.count_each_row()))

print("part2", test1.count_each_row_pt2())
print("part2 pz", pz.count_each_row_pt2())
