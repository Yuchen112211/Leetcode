class Solution(object):
	def knightProbability(self, N, K, r, c):
		memo={}
		def dfs(x,y,k):
			if not (0<=x<N and 0<=y<N): return 0
			if k==0: return 1
			if (x,y,k) not in memo:
				memo[x,y,k]=0.125*sum(dfs(x+i,y+j,k-1)+dfs(x+j,y+i,k-1) for i in (1,-1) for j in (2,-2))
			return memo[(x,y,k)]
		return dfs(r,c,K)


if __name__ == '__main__':
	s = Solution()
	N = 8
	K = 30
	r = 0
	c = 0
	print s.knightProbability(N,K,r,c)