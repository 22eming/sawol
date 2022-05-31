# import numpy as np
game_cnt = int(input())

# game = ((np.array(list(map(int, input().split())))) % 2 == 1).sum()

game = 0

for i in list(map(int, input().split())):
	if i % 2:
		game += 1

if game == game_cnt / 2:
	print("tie")
else:
	print(max(game, game_cnt - game))