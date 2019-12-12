class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        if not matrix[0]:
            return 0

        M = len(matrix)
        N = len(matrix[0])
        x = [0,0,1,-1]
        y = [1,-1,0,0]
        memo = {}
        self.currentPath = 0

        def backtrack(node, path):
            hasBigger = False
            if node in memo:
                self.currentPath = max(self.currentPath, memo[node] + path)
                return
            for i in range(4):
                nx = x[i] + node[0]
                ny = y[i] + node[1]
                if 0 <= nx < M and 0 <= ny < N:
                    if matrix[nx][ny] > matrix[node[0]][node[1]]:
                        hasBigger = True
                        backtrack((nx,ny), path + 1)
            if not hasBigger:
                memo[node] = 1
                self.currentPath = max(path, self.currentPath)
            else:
                #print node,matrix[node[0]][node[1]],self.currentPath,path
                memo[node] = self.currentPath - path

                # if path == 0:
                #     memo[node] -= 1
        for i in range(M):
            for k in range(N):
                self.currentPath = 0
                backtrack((i,k), 0)

        # for i in memo:
        #     print i,matrix[i[0]][i[1]],memo[i]
        return max(memo.values()) + 1





s = Solution()
matrix = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
print s.longestIncreasingPath(matrix) 