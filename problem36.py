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