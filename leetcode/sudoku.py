def find_next(sudoku, i, j):
	for i in range(i,9):
		for k in range(j,9):
			if sudoku[i][k] == 0:
				return i,k
	return -1,-1

def isValid(sudoku, i, j):
	nums = all([e != grid[i][x] for x in range(9)])
	print nums


if __name__ == '__main__':
	sudoku = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
	