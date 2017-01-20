import ge
import numpy as np
import pickle

with open('agents/rl_player2_50000.pkl') as f:
    val_fn = pickle.load(f)

player1 = ge.RLPlayer(2)
player2 = ge.HumanPlayer(1)
player1.value_fn = val_fn
player1.mode = 'test'

gameplay = ge.GamePlay(player2,player1)
gameplay.play()

