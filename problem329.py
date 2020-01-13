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
            #If the node has already been traversed, we can simply extract the value inside the memo.
            if node in memo:
                self.currentPath = max(self.currentPath, path - 1 + memo[node])
                return
            hasBigger = False
            for i in range(4):
                nx = node[0] + x[i]
                ny = node[1] + y[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if matrix[node[0]][node[1]] < matrix[nx][ny]:
                        #We have the next move
                        backtrack((nx,ny), path + 1)
                        hasBigger = True
            #If no bigger value
            #Current path is the longest path that we can go from this current point
            #The memo of the current node should be 1. 
            #The path has gone to the end of this path.
            if not hasBigger:
                memo[node] = 1
                self.currentPath = max(self.currentPath, path)
            else:
                #The node has the next move
                #But the longest path starting from the point has been recorded.
                #Thus, the longest path that the current node have equals to self.currentPath - path of this node.
                memo[node] = self.currentPath - path + 1
        for i in range(M):
            for k in range(N):
                self.currentPath = 0
                backtrack((i,k), 0)

        # for i in memo:
        #     print i,matrix[i[0]][i[1]],memo[i]
        return max(memo.values())





s = Solution()
matrix = [[7,7,11,19,17,13,15,7,1,6,15,6,19,10,13,3,5,16,10,6,0,9,14],[17,6,9,19,7,7,8,17,13,0,8,2,10,9,9,14,13,15,14,3,10,15,12],[12,14,18,1,12,16,19,17,14,0,14,9,0,4,7,14,8,6,15,14,15,16,6],[18,9,7,15,3,6,15,16,15,5,6,19,12,18,12,19,5,5,14,19,1,17,6],[14,16,15,6,15,8,6,7,15,9,5,6,5,10,4,1,6,16,7,3,4,3,19],[17,1,11,7,10,12,0,12,0,12,1,1,5,1,7,15,17,16,8,17,0,19,7],[16,8,2,19,18,17,0,11,17,9,14,5,19,12,15,11,0,13,9,7,15,8,0],[19,10,2,6,17,6,11,15,5,12,19,18,9,3,9,4,10,6,10,5,9,5,9],[13,17,0,0,10,5,0,18,13,6,7,16,7,18,11,15,17,1,2,11,8,16,17],[18,11,16,15,9,6,9,2,4,9,3,17,2,18,15,0,11,16,11,2,17,17,5],[0,2,7,14,12,12,18,2,17,0,2,12,17,2,17,19,9,9,17,13,0,11,17],[9,8,11,12,4,10,6,2,4,10,18,18,4,8,2,14,13,18,12,9,19,14,4],[11,1,10,13,14,10,7,10,11,19,4,3,14,17,13,11,0,9,8,14,9,9,11],[12,15,6,16,5,11,12,15,0,10,9,2,19,11,6,19,5,0,17,6,18,6,3],[5,0,18,18,11,11,10,10,17,11,14,10,0,15,9,12,4,10,0,17,12,19,1],[18,12,6,12,15,12,16,19,2,8,8,9,1,18,19,14,14,6,16,17,15,1,10],[3,14,0,6,7,8,5,9,8,2,18,10,19,17,10,18,14,17,8,1,7,1,1],[12,13,15,2,12,14,3,4,15,16,11,17,0,1,1,16,14,3,5,17,4,14,7]]
print s.longestIncreasingPath(matrix) 