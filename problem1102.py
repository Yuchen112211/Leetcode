class Solution(object):
    def maximumMinimumPath(self, A):
        dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(A), len(A[0])
        
        unique = set()
        ceiling = min(A[0][0], A[-1][-1])

        for r in range(R):
            for c in range(C):
                if A[r][c] <= ceiling:
                    unique.add(A[r][c])
               
        def check(val):
            memo = [[0 for _ in range(C)] for _ in range(R)]
            
            def dfs(x,y):
                if x == R - 1 and y == C - 1:
                    return True
                memo[x][y] = 1
                for d in dire:
                    nx = x + d[0]
                    ny = y + d[1]
                    if 0 <= nx < R and 0 <= ny < C and not memo[nx][ny] and A[nx][ny] >= val and dfs(nx,ny):
                        return True
                return False
            
            return dfs(0,0)   
            
        arr = sorted(unique)
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l+r) / 2
            # if check(m):
            if check(arr[m]):
                # cause we're trying to find the MAXIMUM of 'minimum'
                l = m + 1
            else:
                r = m - 1
        return arr[r]


s = Solution()
A = [[5,4,5],[1,2,6],[7,4,6]]
print s.maximumMinimumPath(A)