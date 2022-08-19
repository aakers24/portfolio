Evaluation Function:

	For leaf nodes my evaluation function uses the number of spaces on the board which are taken after that move for its ulitity value. In more specific terms, boardSize - remainingSpaces. For nodes that aren't leaf nodes, 
		the leaf node utlity value is passed to the "parent" but changed by an arethmetic operation(+, -, or /).

	The function itself is:

		def heuristic(self, player):

        		boardSize = self.rows*self.cols

        		util = boardSize - self.remainingMoves()

        		if player != "1":
            		util = util * -1

        		return util



Minmax Algorithm:

	Board Size - (6x6)
	Nodes Expanded - 26,607
	Depth - 3

	Board Size - (6x6)
	Nodes Expanded - 439,431
	Depth - 4

	Board Size - (7x6)
	Nodes Expanded - 48,952
	Depth - 3

	Board Size - (7x6)
	Nodes Expanded - 1,021,912
	Depth - 4

	Board Size - (8x7)
	Nodes Expanded - 151,253
	Depth - 3

	Board Size - (8x7)
	Nodes Expanded - 4,743,175
	Depth - 4

	Board Size - (8x8)
	Nodes Expanded - 6,309
	Depth - 2

	Board Size - (8x8)
	Nodes Expanded - 254,265
	Depth - 3

AB Pruning Algorithm:

	Board Size - (6x6)
	Nodes Expanded - 15,787
	Depth - 3

	Board Size - (6x6)
	Nodes Expanded - 44,383
	Depth - 4

	Board Size - (7x6)
	Nodes Expanded - 29,140
	Depth - 3

	Board Size - (7x6)
	Nodes Expanded - 74,682
	Depth - 4

	Board Size - (8x7)
	Nodes Expanded - 100,924
	Depth - 3

	Board Size - (8x7)
	Nodes Expanded - 249,992
	Depth - 4

	Board Size - (8x8)
	Nodes Expanded - 165,080
	Depth - 3

	Board Size - (8x8)
	Nodes Expanded - 447,316
	Depth - 4