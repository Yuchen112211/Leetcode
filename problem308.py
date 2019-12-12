class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if not matrix:
            return
        self.sums = [[0 for i in matrix[0]] for k in matrix]
        self.sums[0][0] = matrix[0][0]

        for i in range(1, len(matrix)):
            self.sums[i][0] = self.sums[i-1][0] + matrix[i][0]

        for i in range(1, len(matrix[0])):
            self.sums[0][i] = self.sums[0][i-1] + matrix[0][i]

        for i in range(1, len(matrix)):
            for k in range(1, len(matrix[0])):
                self.sums[i][k] = self.sums[i-1][k] + self.sums[i][k-1] - self.sums[i-1][k-1] + matrix[i][k]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        if not self.matrix:
            return
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        for i in range(row, len(self.sums)):
            for k in range(col, len(self.sums[0])):
                self.sums[i][k] += diff


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix:
            return 0
        result = self.sums[row2][col2]
        if row1 > 0:
            result -= self.sums[row1-1][col2]
        if col1 > 0:
            result -= self.sums[row2][col1-1]
        if row1 > 0 and col1 > 0:
            result += self.sums[row1-1][col1-1]
        return result
        

matrix = [[2,4],[-3,5]]
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(0,0,1,1)
numMatrix.update(0,1,3)
print numMatrix.sumRegion(0,0,1,1)
numMatrix.update(1,1,-3)
print numMatrix.sumRegion(0,0,1,1)
numMatrix.update(0,1,1)
print numMatrix.sumRegion(0,0,1,1)
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)