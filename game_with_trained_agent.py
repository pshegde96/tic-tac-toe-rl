import ge
import numpy as np
import pickle


player2 = ge.RLPlayer(2)
player1 = ge.HumanPlayer(1)
player2.load('agents/rl_player2_50000.pkl') #Load a pretrained RL agent
player2.mode = 'test' #Set the mode such that no exploratory moves are made

gameplay = ge.GamePlay(player1,player2)
gameplay.play()

