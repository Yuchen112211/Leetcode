'''

36. Valid Sudoku
Medium

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.


A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Solution:
Classic Backtrack, read the code carefully.
Check_valid is not neccesary, but it will make the code more readable.

'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def check_valid(matrix,num,pos):
            for i in range(len(matrix)):
                if (matrix[i][pos[1]] == num or matrix[pos[0]][i] == num) and ([i,pos[1]] != pos and [pos[0],i] != pos):
                    return False
            index_x = pos[0]/3
            index_y = pos[1]/3
            for i in range(index_x*3,(index_x+1)*3):
                for k in range(index_y*3,(index_y+1)*3):
                    if matrix[i][k] == num and [i,k] != pos:
                        return False
            return True
        
        matrix = [[0 for i in range(len(board))] for k in range(len(board))]
        for i in range(len(board)):
            for k in range(len(board)):
                if board[i][k] != '.':
                    matrix[i][k] = int(board[i][k])
        for i in range(len(matrix)):
            for k in range(len(matrix)):
                if matrix[i][k] != 0:
                    if not check_valid(matrix,matrix[i][k],[i,k]):
                        return False
        return True

if __name__ == '__main__':
    sudoku = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    print s.isValidSudoku(sudoku)