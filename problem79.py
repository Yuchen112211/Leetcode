'''

79. Word Search
Medium

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Solution:
Another classic backtrack problem. The trick here is to set the character that has 
passed before to invalid or illegal character.

Should write this easily.

'''

class Solution(object):
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		from collections import deque
		
		def isValid(row, col):
			if 0 <= row < len(board) and 0 <= col < len(board[0]):
				return True
			return False

		def backtrack(row, col, index):
			if index == len(word):
				return True
			diff_x = [0,0,1,-1]
			diff_y = [1,-1,0,0]
			res = False
			for i in range(4):
				current_row = diff_x[i] + row
				current_col = diff_y[i] + col
				
				if isValid(current_row, current_col):
					
					if board[current_row][current_col] == word[index]:
						tmp = board[row][col]
						board[row][col] = '#'
						if backtrack(current_row, current_col, index + 1):
							res = True
							break
						board[row][col] = tmp

			return res
		for i in range(len(board)):
			for k in range(len(board[0])):
				if board[i][k] == word[0]:
					tmp = board[i][k]
					board[i][k] = '#'
					if backtrack(i,k,1):
						return True
					board[i][k] = tmp
		return False

if __name__ == '__main__':
	board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
	word = 'ABCCED'
	s = Solution()
	print s.exist(board, word)
