import sys
from Board import Board
from Solver import Solver

# Taking in console input

argNum = len(sys.argv)

if argNum != 3:
    print("Invalid Input, number of args: ", argNum)

fileName = sys.argv[0]

# Choose if AI is player 1 or 2; Player 1 is MAX and will play Os, Player 2 is MIN and will play Xs
player = sys.argv[1]

searchmethod = sys.argv[2]



board = Board(8, 8)

solver = Solver(player, searchmethod, board)

# Information for ReadMe
# print(solver.nodesExpanded, solver.depth)