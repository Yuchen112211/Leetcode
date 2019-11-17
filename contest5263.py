class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        arr = []
        if not grid:
            return grid
        
        for i in grid:
            for j in i:
                arr.append(j)

        length = len(arr)
        k = k % length
        if k == len(arr):
            return grid

        rst = [[0 for j in grid[0]] for i in grid]
        index = length - k
        
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                rst[i][k] = arr[index % length]
                index += 1
        return rst

x = Solution()
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print x.shiftGrid(grid, k)