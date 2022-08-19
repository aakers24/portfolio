import copy
from Board import Board


class Solver:
    def __init__(self, player, searchmethod, board):
        self.player = player
        self.searchmethod = searchmethod
        self.board = board
        
        self.nodesExpanded = 0

        self.depth = 3 # Depth of depth-limited search

        return self.solve(player, searchmethod, board)

    def solve(self, player, searchmethod, board):
        if player == "1":
            print("Player 1: AI\nPlayer 2: Human")
        else:
            print("Player 1: Human\nPlayer 2: AI")
        
        if searchmethod == "MM":
            return self.minimax(player, board)
        else:
            return self.ABPruningMinimax(player, board)



    def minimax(self, player, board):

        gameover = False
        currentBoard = board

        while gameover == False:

            currentTree = Board.minimaxTree(copy.deepcopy(currentBoard), player, self.depth, self)

            # Choose a move based on the minimax utility value
            # &
            # make the move by updating the current board

            bestMove = 1
            bestMoveVal = 0

            if type(currentTree[1]) == Board:
                for i in range(len(currentTree)):
                    if i != 0:
                        if abs(currentTree[i].utility) > abs(bestMoveVal):
                            bestMoveVal = currentTree[i].utility
                            bestMove = i
                currentBoard = currentTree[bestMove]
            else:
                for i in range(len(currentTree)):
                    if i != 0:
                        if abs(currentTree[i][0].utility) > abs(bestMoveVal):
                            bestMoveVal = currentTree[i][0].utility
                            bestMove = i
                currentBoard = currentTree[bestMove][0]



            # Display the AI's move
            thisMoveRow = currentBoard.moveCoords[0] + 1
            thisMoveCol = currentBoard.moveCoords[1] + 1
            thisMove = (thisMoveRow, thisMoveCol)
            print("AI's move(row/col):", thisMove)

            currentBoard.printBoard()

            # Check if the game is over
            if currentBoard.remainingMoves() == 0:
                gameover = True
                print("AI Wins!")
                continue



            # Human's turn

            validIn = False
            while validIn == False:

                userIn = input("Type your move(row/col): ")
                userIn = userIn.strip(" \n").split("/")

                # Was user input formatted properly?
                if(len(userIn) != 2):
                    print("Invalid user input.")
                    continue
                else:
                    validIn = True
                
                try:
                    userRow = int(userIn[0]) - 1
                    userCol = int(userIn[1]) - 1
                except:
                    print("Invalid user input. Please make sure you're typing integers and try again.")
                    validIn = False
                    continue

                # Was user input a valid move for the current board state?
                try:
                    if currentBoard.board[userRow][userCol] != "-":
                        print("Invalid move attempted.")
                        validIn = False
                        continue
                except:
                    print("Invalid user input. Please make sure your inputs are within the dimensions of the board.")
                    validIn = False
                    continue

            currentBoard = currentBoard.makeMove(userRow, userCol, Board.swapPlayer(player))

            currentBoard.printBoard()

            # Check if the game is over
            if currentBoard.remainingMoves() == 0:
                gameover = True
                print("Human Wins!")

            # repeat

    def ABPruningMinimax(self, player, board):

        alpha = -1024
        beta = 1024
        
        gameover = False
        currentBoard = board

        while gameover == False:

            currentTree = Board.ABTree(copy.deepcopy(currentBoard), player, self.depth, alpha, beta, self)

            # Choose a move based on the minimax utility value
            # &
            # make the move by updating the current board

            bestMove = 1
            bestMoveVal = 0

            if type(currentTree[1]) == Board:
                for i in range(len(currentTree)):
                    if i != 0:
                        if abs(currentTree[i].utility) > abs(bestMoveVal):
                            bestMoveVal = currentTree[i].utility
                            bestMove = i
                currentBoard = currentTree[bestMove]
            else:
                for i in range(len(currentTree)):
                    if i != 0:
                        if abs(currentTree[i][0].utility) > abs(bestMoveVal):
                            bestMoveVal = currentTree[i][0].utility
                            bestMove = i
                currentBoard = currentTree[bestMove][0]



            # Display the AI's move
            thisMoveRow = currentBoard.moveCoords[0] + 1
            thisMoveCol = currentBoard.moveCoords[1] + 1
            thisMove = (thisMoveRow, thisMoveCol)
            print("AI's move(row/col):", thisMove)

            currentBoard.printBoard()

            # Check if the game is over
            if currentBoard.remainingMoves() == 0:
                gameover = True
                print("AI Wins!")
                continue



            # Human's turn

            validIn = False
            while validIn == False:

                userIn = input("Type your move(row/col): ")
                userIn = userIn.strip(" \n").split("/")

                # Was user input formatted properly?
                if(len(userIn) != 2):
                    print("Invalid user input.")
                    continue
                else:
                    validIn = True
                
                try:
                    userRow = int(userIn[0]) - 1
                    userCol = int(userIn[1]) - 1
                except:
                    print("Invalid user input. Please make sure you're typing integers and try again.")
                    validIn = False
                    continue

                # Was user input a valid move for the current board state?
                try:
                    if currentBoard.board[userRow][userCol] != "-":
                        print("Invalid move attempted.")
                        validIn = False
                        continue
                except:
                    print("Invalid user input. Please make sure your inputs are within the dimensions of the board.")
                    validIn = False
                    continue

            currentBoard = currentBoard.makeMove(userRow, userCol, Board.swapPlayer(player))

            currentBoard.printBoard()

            # Check if the game is over
            if currentBoard.remainingMoves() == 0:
                gameover = True
                print("Human Wins!")

            # repeat