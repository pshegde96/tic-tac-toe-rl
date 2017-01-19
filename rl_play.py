import numpy as np
import game_engine as ge

grid = ge.Grid()
rlp = ge.rl_player(1)

rlp.player_move(grid)
print grid.squares
