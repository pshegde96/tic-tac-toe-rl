import os
import game_engine as ge
import numpy as np

board_init = np.zeros((3,3))
grid = ge.Grid(board_init)
player1 = ge.Player(1)
player2 = ge.Player(2)
grid.display()
game_end = 0
count = 0
while game_end ==0:
	if count%2 ==0:
		player1.player_move(grid);
		os.system('clear')
		grid.display();	
		game_end = player1.check_win(grid)		

	else:
		player2.computer_move_random(grid)
		game_end = player2.check_win(grid)
		os.system('clear')
		grid.display();	
	count += 1

