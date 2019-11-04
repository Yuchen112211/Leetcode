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