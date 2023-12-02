
moves = open('day2.txt').read().split('\n')

sample_moves = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

passed =[]
max_count = {"red":12, "blue":14, "green":13 }
pt2_min_sum =[]

for i, game in enumerate(moves):
    game = game.split(": ")
    # print(game)
    playable = True
    pt2_count = {"red":0, "blue":0, "green":0}
    for plays in game[1].split("; "):
        count = {}
        for play in plays.split(", "):
            play = play.split(" ")
            count[play[1]] = count.get(play[1], 0) + int(play[0])
            if count[play[1]] > max_count[play[1]]:
                playable = False
        for color, ct in count.items():
            pt2_count[color] = max(pt2_count[color], ct)

    if playable: passed.append(i+1)
    min_prod = 1
    for count in pt2_count.values():
        min_prod *= count
    pt2_min_sum.append(min_prod)


print(sum(passed))
print(sum(pt2_min_sum))
