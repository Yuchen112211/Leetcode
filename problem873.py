class Solution(object):
    def lenLongestFibSubseq(self, A):
        import collections

        map = collections.defaultdict(int)
        for i, v in enumerate(A):
            map[v]=i
        n = len(A)
        dp = [[2 for _ in range(n+1)] for _ in range(n+1)]
        for j in range(n):
            for i in range(j):
                diff = A[j]-A[i]
                if diff in map and map[diff] < i:
                    k = map[diff]
                    dp[i][j] = max(dp[i][j], 1+dp[k][i])
        ans = max([max(n) for n in dp])
        return 0 if ans <= 2 else ans

s = Solution()
A = [2,4,5,6,7,8,11,13,14,15,21,22,34]
print s.lenLongestFibSubseq(A)