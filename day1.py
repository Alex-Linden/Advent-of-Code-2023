f = open('day1.txt').read().split('\n')
# f = f.strip().split('\n\n')
# f.split('\n')


test = ["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"]

num_sts = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
              }

def has_num_str(s):
    for n in num_sts.keys():
        if n in s:
            return num_sts[n]
    return False

total = 0
for row in f:
    num = ""
    l, r = 0, len(row) - 1
    while l < len(row):
        if row[l].isdigit():
            num += row[l]
            break
        n = has_num_str(row[:l+1])
        if n:
            num += n
            break
        else:
            l += 1
    while r >= 0:
        if row[r].isdigit():
            num += row[r]
            break
        n = has_num_str(row[r:])
        if n:
            num += n
            break
        else:
            r -= 1
    # print(row, num)
    total += int(num)

print(total)
# print(f[0:3])