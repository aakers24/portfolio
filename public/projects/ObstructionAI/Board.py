import copy

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.utility = 0
        self.moveCoords = (-1, -1)
        self.alpha = -1024
        self.beta = 1024
        self.board = Board.newBoard(rows, cols)

    def newBoard(rows, cols):
        board = []

        for i in range(rows):
            board.append([])
            for j in range(cols):
                board[i].append("-")

        return board

    def printBoard(self):
        for i in range(self.cols + 1):
            print(i, end = "    ")
        print()
        for i in range(len(self.board)):
            print(i + 1, end = " ")
            print(self.board[i])

    def remainingMoves(self):
        openCount = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == "-":
                    openCount += 1
        
        return openCount

    def heuristic(self, player):

        boardSize = self.rows*self.cols

        # Util value = all spaces - available spaces
        util = boardSize - self.remainingMoves()

        # If player is min then util should be negative
        if player != "1":
            util = util * -1

        # Return value based on which player's turn it is - player 1 is max, player 2 is min
        return util



    def makeMove(self, row, col, player):
        if player == "1":
            moveChar = "O"
        else:
            moveChar = "X"

        # If the move is valid, change that square to your piece and then block applicable squares surrounding it
        if self.board[row][col] != "-":
            print("Invalid Move")
        else:
            self.board[row][col] = moveChar

            # Block Square Above and Left
            if row - 1 >= 0 and col - 1 >= 0:
                if self.board[row - 1][col - 1] == "-":
                    self.board[row - 1][col - 1] = "/"

            # Block Square Above
            if row - 1 >= 0:
                if self.board[row - 1][col] == "-":
                    self.board[row - 1][col] = "/"

            # Block Square Above and Right
            if row - 1 >= 0 and col + 1 < self.cols:
                if self.board[row - 1][col + 1] == "-":
                    self.board[row - 1][col + 1] = "/"
            
            # Block Square Left
            if col - 1 >= 0:
                if self.board[row][col - 1] == "-":
                    self.board[row][col - 1] = "/"

            # Block Square Right
            if col + 1 < self.cols:
                if self.board[row][col + 1] == "-":
                    self.board[row][col + 1] = "/"

            # Block Square Below and Left
            if row + 1 < self.rows and col - 1 >= 0:
                if self.board[row + 1][col - 1] == "-":
                    self.board[row + 1][col - 1] = "/"

            # Block Square Below
            if row + 1 < self.rows:
                if self.board[row + 1][col] == "-":
                    self.board[row + 1][col] = "/"

            # Block Square Below and Right
            if row + 1 < self.rows and col + 1 < self.cols:
                if self.board[row + 1][col + 1] == "-":
                    self.board[row + 1][col + 1] = "/"

            self.moveCoords = (row, col)

        return self



    def swapPlayer(player):
        if player == "1":
            player = "2"
        else:
            player = "1"
        
        return player



    def minimaxTree(self, player, depth, solver):

        thisList = []

        thisList.append(copy.deepcopy(self))

        # Make every possible move and append them to thisList
        # Recursive Cases
        if depth > 1:

            # For every open space
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.board[i][j] == "-":

                        # Make that move and calculate it's utility value from it's children
                        temp = copy.deepcopy(self).makeMove(i, j, player)
                        tempTree = temp.minimaxTree(Board.swapPlayer(player), depth - 1, solver)

                        # Add this tree to the list as a child node/state
                        thisList.append(tempTree)

                        solver.nodesExpanded = solver.nodesExpanded + 1

                        # Calculate the utility value of this(the parent) node from its children
                        if player == "1":
                            tempUtil = -1024
                        else:
                            tempUtil = 1024

                        # When depth == 2 the accessing is different because it's a list of nodes/boards and not a list of lists yet
                        if depth == 2:
                            if len(tempTree) == 1:
                                if player == "1" and tempTree[0].utility > tempUtil: 
                                    tempUtil = tempTree[0].utility / 2
                                elif player != "1" and tempTree[0].utility < tempUtil:
                                    tempUtil = tempTree[0].utility / 2
                            else:
                                for n in range(len(tempTree)):
                                    if n != 0:
                                        if player == "1" and tempTree[n].utility > tempUtil: 
                                            tempUtil = tempTree[n].utility
                                        elif player != "1" and tempTree[n].utility < tempUtil:
                                            tempUtil = tempTree[n].utility
                        else:
                            if len(tempTree) == 1:
                                if player == "1" and tempTree[0].utility > tempUtil: 
                                    tempUtil = tempTree[0].utility / 4
                                elif player != "1" and tempTree[0].utility < tempUtil:
                                    tempUtil = tempTree[0].utility / 4
                            else:
                                for n in range(len(tempTree)):
                                    if n != 0:
                                        if player == "1" and tempTree[n][0].utility > tempUtil:
                                            tempUtil = tempTree[n][0].utility
                                        elif player != "1" and tempTree[n][0].utility < tempUtil:
                                            tempUtil = tempTree[n][0].utility

                        # Assign this node(the parent) a utility value based on its children
                        if player == "1":
                            thisList[0].utility = tempUtil - 1
                        else:
                            thisList[0].utility = tempUtil + 1

        
        
        # Base case (Depth == 1)
        else:

            if player == "1":
                tempUtil = -1024
            else:
                tempUtil = 1024

            # If there are no open spaces, we're at a terminal node
            if self.remainingMoves() == 0:
                tempUtil = self.heuristic(player)

            else:
                # For every open space
                for i in range(self.rows):
                    for j in range(self.cols):
                        if self.board[i][j] == "-":
                            
                            # Make that move and calculate it's utility value
                            temp = copy.deepcopy(self).makeMove(i, j, player)
                            temp.utility = temp.heuristic(player)

                            # If this is the best move yet, store the best utility value
                            if player == "1" and temp.utility > tempUtil:
                                tempUtil = temp.utility
                            elif player != "1" and temp.utility < tempUtil:
                                tempUtil = temp.utility

                            # Add it to the list as a child state/node
                            thisList.append(temp)

                            solver.nodesExpanded = solver.nodesExpanded + 1

            # Once all leaf nodes have been calculated, update this(the parent) node's utility, but +/- 1 because it is not the move itself
            # Based on whether the play is Max(1) or Min(2)
            # If the length of the list is 1, then it's a terminal state
            if len(thisList) == 1:
                if player == "1":
                    thisList[0].utility = tempUtil
                else:
                    thisList[0].utility = tempUtil
            else:
                if player == "1":
                    thisList[0].utility = tempUtil - 1
                else:
                    thisList[0].utility = tempUtil + 1

        return thisList



    def ABTree(self, player, depth, alpha, beta, solver):

        thisList = []

        thisList.append(copy.deepcopy(self))

        # Make every possible move and append them to thisList
        # Recursive Cases
        if depth > 1:

            # For every open space
            for i in range(self.rows):
                if beta <= alpha: # Pruning
                    break
                for j in range(self.cols):
                    if self.board[i][j] == "-":

                        # Make that move and calculate it's utility value from it's children
                        temp = copy.deepcopy(self).makeMove(i, j, player)
                        tempTree = temp.ABTree(Board.swapPlayer(player), depth - 1, alpha, beta, solver)

                        # Add this tree to the list as a child node/state
                        thisList.append(tempTree)

                        solver.nodesExpanded = solver.nodesExpanded + 1

                        # Calculate the utility value of this(the parent) node from its children
                        if player == "1":
                            tempUtil = -1024
                        else:
                            tempUtil = 1024

                        # When depth == 2 the accessing is different because it's a list of nodes/boards and not a list of lists yet
                        if depth == 2:
                            if len(tempTree) == 1:
                                if player == "1" and tempTree[0].utility > tempUtil:
                                    tempUtil = tempTree[0].utility / 2
                                elif player != "1" and tempTree[0].utility < tempUtil:
                                    tempUtil = tempTree[0].utility / 2
                            else:
                                for n in range(len(tempTree)):
                                    if n != 0:
                                        if player == "1" and tempTree[n].utility > tempUtil:
                                            tempUtil = tempTree[n].utility
                                        elif player != "1" and tempTree[n].utility < tempUtil:
                                            tempUtil = tempTree[n].utility
                        else:
                            if len(tempTree) == 1:
                                if player == "1" and tempTree[0].utility > tempUtil:
                                    tempUtil = tempTree[0].utility / 4
                                elif player != "1" and tempTree[0].utility < tempUtil:
                                    tempUtil = tempTree[0].utility / 4
                            else:
                                for n in range(len(tempTree)):
                                    if n != 0:
                                        if player == "1" and tempTree[n][0].utility > tempUtil:
                                            tempUtil = tempTree[n][0].utility
                                        elif player != "1" and tempTree[n][0].utility < tempUtil:
                                            tempUtil = tempTree[n][0].utility

                        # Assign this node(the parent) a utility value based on its children
                        if player == "1":
                            thisList[0].utility = tempUtil - 1
                        else:
                            thisList[0].utility = tempUtil + 1

                        # # Pruning
                        if player == "1":
                            if tempTree[0].utility > alpha:
                                alpha = tempTree[0].utility
                        else:
                            if tempTree[0].utility < beta:
                                beta = tempTree[0].utility

                        if beta <= alpha:
                            break

        
        
        # Base case (Depth == 1)
        else:

            if player == "1":
                tempUtil = -1024
            else:
                tempUtil = 1024

            # If there are no open spaces, we're at a terminal node
            if self.remainingMoves() == 0:
                tempUtil = self.heuristic(player)

            else:
                # For every open space
                for i in range(self.rows):
                    for j in range(self.cols):
                        if self.board[i][j] == "-":
                            
                            # Make that move and calculate it's utility value
                            temp = copy.deepcopy(self).makeMove(i, j, player)
                            temp.utility = temp.heuristic(player)

                            # If this is the best move yet, store the best utility value
                            if player == "1" and temp.utility > tempUtil:
                                tempUtil = temp.utility
                            elif player != "1" and temp.utility < tempUtil:
                                tempUtil = temp.utility

                            # Add it to the list as a child state/node
                            thisList.append(temp)

                            solver.nodesExpanded = solver.nodesExpanded + 1

            # Once all leaf nodes have been calculated, update this(the parent) node's utility, but +/- 1 because it is not the move itself
            # Based on whether the play is Max(1) or Min(2)
            # If the length of the list is 1, then it's a terminal state
            if len(thisList) == 1:
                if player == "1":
                    thisList[0].utility = tempUtil
                else:
                    thisList[0].utility = tempUtil
            else:
                if player == "1":
                    thisList[0].utility = tempUtil - 1
                else:
                    thisList[0].utility = tempUtil + 1

        return thisList