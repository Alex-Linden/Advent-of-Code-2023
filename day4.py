scratch_cards = open("day4.txt").read().split('\n')

test = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]

# scratch_cards = test
x = 0

for i in range(len(scratch_cards[0])):
    if scratch_cards[0][i] == ":":
        x = i + 1

points_per_game = []
i = 0
for card in scratch_cards:
    first_match = True
    points = 0
    winning_nums, nums = card[x:].split("|")
    winning_nums, nums = winning_nums.strip().split(" "), nums.strip().split(" ")
    # print(winning_nums, nums)
    for num in nums:
        if num in winning_nums:
            if num == '':
                continue
            if first_match:
                points = 1
                first_match = False
            else:
                points *= 2
    if points > 0:
        points_per_game.append(points)
    # i += 1
    # if i == 10: break

print(sum(points_per_game))

cards_per_round = [1] * len(scratch_cards)

for idx, card in enumerate(scratch_cards):
    plays = cards_per_round[idx]
    winning_nums, nums = card[x:].split("|")
    winning_nums, nums = winning_nums.strip().split(" "), nums.strip().split(" ")
    wins = 0
    for num in nums:
        if num in winning_nums:
            if num == '':
                continue
            else:
                wins += 1
    for i in range(1, wins + 1):
        cards_per_round[idx + i] += plays

print(sum(cards_per_round), cards_per_round)


