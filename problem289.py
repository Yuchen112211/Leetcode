'''

289. Game of Life
Medium

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Solution:
Write two helper functions, with additional space, which means another matrix should be initialize.
Simple iteration should solve this problem.

The in-place solution is rather interesting, instead of changing the 0 and 1 to 1 and 0,
we change them to 2 and -1.

For e.g. 
If the value of the cell was 1 originally but it has now become 0 after applying the rule, 
then we can change the value to -1.
The negative sign signifies the cell is now dead(0) but the magnitude signifies the cell was a live(1) cell originally.

Also, if the value of the cell was 0 originally but it has now become 1 after applying the rule,
then we can change the value to 2. 
The positive sign signifies the cell is now live(1) but the magnitude of 2 signifies the cell was a dead(0) cell originally.

Very simple solution, if the cell is not modified, maintain them as original value. 

'''
class Solution(object):
	def gameOfLife(self, board):
		"""
		:type board: List[List[int]]
		:rtype: None Do not return anything, modify board in-place instead.
		"""
		import copy 

		def getSurrondings(board,pos):
			rst = []
			if pos[0] > 0:
				rst.append([pos[0]-1,pos[1]])
				if pos[1] > 0:
					rst.append([pos[0]-1,pos[1]-1])
				if pos[1] < len(board[0]) - 1:
					rst.append([pos[0]-1,pos[1]+1])

			if pos[0] < len(board)-1:
				rst.append([pos[0]+1,pos[1]])
				if pos[1] > 0:
					rst.append([pos[0]+1,pos[1]-1])
				if pos[1] < len(board[0]) - 1:
					rst.append([pos[0]+1,pos[1]+1])

			if pos[1] > 0:
				rst.append([pos[0],pos[1]-1])
			if pos[1] < len(board[0])-1:
				rst.append([pos[0],pos[1]+1])
			return rst

		def live_cell(board,pos):
			surrondings = getSurrondings(board,pos)
			res = []
			for i in surrondings:
				res.append(board[i[0]][i[1]])
			live_cells = res.count(1)
			dead_cells = len(res) - live_cells

			if live_cells < 2:
				return 0
			elif live_cells <= 3:
				return 1
			else:
				return 0
			return 0

		def dead_cell(board,pos):
			surrondings = getSurrondings(board,pos)
			res = []
			for i in surrondings:
				res.append(board[i[0]][i[1]])
			live_cells = res.count(1)
			dead_cells = len(res) - live_cells

			if live_cells == 3:
				return 1
			return 0
		board_next = copy.deepcopy(board)

		for i in range(len(board)):
			for k in range(len(board[0])):
				if board_next[i][k] == 1:
					board[i][k] = live_cell(board_next,[i,k])
				elif board_next[i][k] == 0:
					board[i][k] = dead_cell(board_next,[i,k])


		
if __name__ == '__main__':
	s = Solution()
	board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
	s.gameOfLife(board)
	print board