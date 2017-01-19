import os
import ge
import numpy as np
import pickle

player1 = ge.RLPlayer(1)
player2 = ge.RLPlayer(2)
number_of_games = 5000
gameplay = ge.GamePlay(player1,player2,no_of_games=number_of_games)
gameplay.play()
with open('rl_player1.pkl','w') as f:
    pickle.dump([player1.value_fn],f)
with open('rl_player2.pkl','w') as f:
    pickle.dump([player2.value_fn],f)

playerhuman = ge.HumanPlayer(2)
gameplay2 = ge.GamePlay(player1,playerhuman)
gameplay2.play()
'''
for game_no in range(number_of_games):
	print game_no
	grid = ge.Grid()
	game_end = 0
	count = 0
	while True:
		if count%2 ==0:
			player1.PlayerMove(grid);
			game_end = player1.CheckWin(grid)	
			if game_end == 1:
				break
			game_end = player1.CheckDraw(grid)
			if game_end == 1:
				break

		else:
			player2.PlayerMove(grid)
			game_end = player2.CheckWin(grid)
			if game_end == 1:
				break
			game_end = player1.CheckDraw(grid)
			if game_end == 1:
				break
		count += 1
'''
