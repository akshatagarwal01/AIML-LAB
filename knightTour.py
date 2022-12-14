n = 8
def check_pos(x, y, board):
	if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
		return True
	return False


def printSolution(n, board):

	for i in range(n):
		for j in range(n):
			print(board[i][j], end=' | ')
		print()


def KnightTour(n):

	board = [[-1 for i in range(n)]for i in range(n)]


	move_x = [2, 1, -1, -2, -2, -1, 1, 2]
	move_y = [1, 2, 2, 1, -1, -2, -2, -1]


	board[0][0] = 0

	pos = 1

	if(not Recurse_Knight_Tour(n, board, 0, 0, move_x, move_y, pos)):
		print("Solution does not exist")
	else:
		printSolution(n, board)


def Recurse_Knight_Tour(n, board, curr_x, curr_y, move_x, move_y, pos):
	if(pos == n**2):
		return True


	for i in range(8):
		new_x = curr_x + move_x[i]
		new_y = curr_y + move_y[i]
		if(check_pos(new_x, new_y, board)):
			board[new_x][new_y] = pos
			if(Recurse_Knight_Tour(n, board, new_x, new_y, move_x, move_y, pos+1)):
				return True

			
			board[new_x][new_y] = -1
	return False



KnightTour(n)

