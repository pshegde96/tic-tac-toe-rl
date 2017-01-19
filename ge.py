import numpy as np
import os,itertools

winning = np.array([[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]);

#Class to describe the 3x3 grid
class Grid:
	#used to initialise the grid
	def __init__(self):
		sqa = np.zeros((3,3));
		self.squares = sqa;

	#Displays the grid
	def display(self):
		for row in range(0,3):
			line = str();
			for col in range(0,3):
				line = line + str(self.squares[row,col]) + "\t";
			print line;

# This class encapsulates the human player and a computer player that plays at random
class Player:
	#Used to initialise a player with his ID
	def __init__(self,pid):
		self.playerid = pid;
                self.playertype = 'notrl'

	#Check if a player has won the game
	def CheckWin(self,grid):
		#Reshape the grid to a 1D array for easier computation
		sq = grid.squares.reshape(1,9)[0];
		#Check which squares have been marked by the player
		marked = np.where(sq==self.playerid)[0];
		#flag = 1 will mean the player has won
		flag = 0;
		#Check for the presence of winning squares
		for lci in range(0,8):
			count = 0;
			for lcj in range(0,3):
				if winning[lci,lcj] in marked:
					count += 1;
			if count >= 3 :
				flag = 1;
				break;
		if flag == 1:
			string = "Player " + str(self.playerid) + " wins!!!";
			print string;
			return 1;
		else:
			return 0;
	
	def CheckDraw(self,grid):
		sq = grid.squares.reshape(9)
		empty = np.where(sq==0)[0]
		if not list(empty):
			return 1
			print "Game ends in draw"
		else:
			return 0
				
class HumanPlayer(Player):

	#Accept a move from the player and make the move
	def PlayerMove(self,grid):
		correct_move = 0;
		while correct_move == 0:
			string = "Move by Player " + str(self.playerid) + " : ";
			print string;
			inp_r = input("Row :");
			inp_c = input("Column :");
			if grid.squares[inp_r,inp_c] == 0:
				grid.squares[inp_r,inp_c] = self.playerid;
				correct_move = 1;
			else:
				print "Incorrect move \n Please try again";
		
		
class RandomPlayer(Player):


	def PlayerMove(self,grid):
		board = grid.squares.reshape(9)
		empty_pos = np.where(board==0)
		move = np.random.choice(empty_pos[0])
		row = int(move)/3
		col = move%3
		grid.squares[row,col] = self.playerid


class RLPlayer(Player):

	def __init__(self,pid,eps=0.1,alpha=0.1):
		self.playerid = pid;
		self.eps = eps
		self.alpha = alpha
                self.playertype = 'rl'
		if pid == 1:
			self.opponentid = 2
		else:
			self.opponentid = 1

		#Maintain a list of all possible board configurations
		possible_configs_itertools = itertools.product([0,1,2],repeat=9)
		board_posns = list()
		value_fn = list()
		for config in possible_configs_itertools:
			board_posns.append(list(config))
			value_fn.append(0.5)



		#Set all the winning moves prob to 1 and losing moves prob to 0
		count = 0
		for board_posn in board_posns:
			player_posn = np.where(np.array(board_posn) == self.playerid)[0]
			opp_posn = np.where(np.array(board_posn) == self.opponentid)[0]
			for win_move in winning:
				if set(win_move).issubset(set(player_posn)):
					value_fn[count] = 1.0
				if set(win_move).issubset(set(opp_posn)):
					value_fn[count] = 0.0
			count += 1		

		self.board_posns = board_posns
		self.value_fn = value_fn
                self.newboardposn = self.board_posns.index([0]*9) #Set the board posn as the initial posn of the board, used later in TD update

	def PlayerMove(self,grid,mode = 'train'):	
		
		board = grid.squares.reshape(9)
		empty_pos = np.where(board==0)[0]
		explore_or_exploit = np.random.choice(2,p = [self.eps,1-self.eps])
		
		if explore_or_exploit == 0: #explore
			move = np.random.choice(empty_pos.shape[0])
			#update probabilities
			#board_new = board.copy()
			#board_new[move] = self.playerid
			#oldposn = self.board_posns.index(list(board))
			#newposn = self.board_posns.index(list(board_new))
                        #Get the board positions to perform TD update
                        self.oldboardposn = self.newboardposn
                        self.newboardposn = self.board_posns.index(list(board))
			# TD update
			self.value_fn[oldposn] = self.value_fn[self.oldboardposn]*(1-self.alpha) + self.value_fn[self.newboardposn]*self.alpha

		else: #exploit
			move_probs = np.zeros(9) 
			#Go over all possible moves and find the value_fn of new move
			for move_possible in empty_pos:
				board_possible = board.copy()
				board_possible[move_possible] = self.playerid
				possibleposn = self.board_posns.index(list(board_possible))
				move_probs[move_possible] = self.value_fn[possibleposn]
			#Choose move greedily
			move = np.argmax(np.array(move_probs))
			board_new = board.copy()
			board_new[move] = self.playerid
			oldposn = self.board_posns.index(list(board))
			newposn = self.board_posns.index(list(board_new))
			# TD update
			self.value_fn[oldposn] = self.value_fn[oldposn]*(1-self.alpha) + self.value_fn[newposn]*self.alpha

		row = int(move)/3
		col = move%3
		grid.squares[row,col] = self.playerid
		
class GamePlay:
    def __init__(self,player1,player2,no_of_games=1,display=False):
        self.player1 = player1
        self.player2 = player2
        self.no_of_games = no_of_games
        self.display = display

    def play(self):
        for _ in range(self.no_of_games):
            game_end = 0
            count = 0
            grid = Grid()
            while True:
                if count%2 == 0:
                    self.player1.PlayerMove(grid)
                    game_end = self.player1.CheckWin(grid)
                    if game_end == 1:
                        #if self.player1.playertype == 'rl':
                        #    player1.TDupdate()
                        break
                    game_end = self.player1.CheckDraw(grid)
                    if game_end == 1:
                       # if self.player1.playertype == 'rl':
                       #     player1.TDupdate()
                        break
            
                else:
                    self.player2.PlayerMove(grid)
                    game_end = self.player2.CheckWin(grid)
                    if game_end == 1:
                        #if self.player1.playertype == 'rl':
                        #    player1.TDupdate()
                        break
                    game_end = self.player2.CheckDraw(grid)
                    if game_end == 1:
                        #if self.player1.playertype == 'rl':
                        #    player1.TDupdate()
                        break
