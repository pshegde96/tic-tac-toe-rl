import ge
import numpy as np
import pickle

#Load the value function from the trained RL agent
with open('agents/rl_player2_50000.pkl') as f:
    val_fn = pickle.load(f)

player2 = ge.RLPlayer(2)
player1 = ge.HumanPlayer(1)
player2.value_fn = val_fn #Set the val function to that of the trained agent
player2.mode = 'test' #Set the mode such that no exploratory moves are made

gameplay = ge.GamePlay(player1,player2)
gameplay.play()

