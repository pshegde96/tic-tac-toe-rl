import os
import ge
import numpy as np

player1 = ge.HumanPlayer(1)
player2 = ge.RLPlayer(2)
number_of_games = 1
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

