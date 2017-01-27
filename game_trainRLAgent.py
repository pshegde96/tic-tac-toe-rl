import os
import ge
import numpy as np
import pickle

#Setup the players
player1 = ge.RLPlayer(1)
player2 = ge.RLPlayer(2)
number_of_games =50000
gameplay = ge.GamePlay(player1,player2,no_of_games=number_of_games)#Setup the game
gameplay.play()#Play the game
#Save the trained agents
player1.save('agents/rl_player1_'+str(number_of_games)+'.pkl') 
player2.save('agents/rl_player2_'+str(number_of_games)+'.pkl')
player1.mode = 'test' #Set the mode to test so that no exploratory moves are made
playerhuman = ge.HumanPlayer(2)
gameplay2 = ge.GamePlay(player1,playerhuman)
gameplay2.play()
