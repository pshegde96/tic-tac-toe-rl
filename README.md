This is an implementation of the TD algorithm presented in Chapter 1 of [Sutton and Barto](https://webdocs.cs.ualberta.ca/~sutton/book/bookdraft2016sep.pdf)

###Files:
ge.py : Contains the descriptions of all the players and the game

game_with_trained_agent.py : To play game against a trained rl agent

game_trainRLAgent.py : To train 2 RL agents by playing against each other

agents/: contains files for trained agents

###Description:
####Players:
There are 3 kinds of players:
* RL agent
* Human Player
* Random Player: Picks one of the legal moves randomly

###Usage:
Run ~python game_with_trained_agent.py ~ to play with a trained RL agent
Run ~python game_trainRLAgent.py  ~ to train RL agents by playing against each other and store them in agents/ directory

Checkout the above mentioned files to checkout how to use the classes described in ge.py and use them in different ways. 
