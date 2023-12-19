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
        count = list(eval(count))
        return [springs, count]

    def find_possible_arrangements(self, spring, count):
        print(spring, count)
        # base case
        if len(count) == 0 and spring:
            return 1
        elif len(count) > 0 and not spring:
            return 0
        total = 0
        i = 0
        while i < len(spring):
            if spring[i] == "?" and (i == 0 or spring[i-1] != "#") and spring[i + 1] != "#":
                j = i + 1
                while j < len(spring) and j <= i + count[0]:
                    if spring[j] in "?#":
                        j += 1
                    else:
                        break
                total += self.find_possible_arrangements(spring[j:], count[1:])
            elif spring[i] == "#":
                j = i + 1
                while j < len(spring) and j <= i + count[0]:
                    if spring[j] in "?#":
                        j += 1
                    else:
                        break
                total += self.find_possible_arrangements(spring[j:], count[1:])
        return total

    def count_each_row(self):
        count_per_row = []
        for row in self.record:
            spring, count = self.parse_row(row)
            # print(spring, count)
            count = self.find_possible_arrangements(spring, count)
            count_per_row.append(count)
        return count_per_row

test1 = Spring(test)

print(test1.count_each_row())





