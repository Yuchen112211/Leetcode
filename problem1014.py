class Solution:
    def maxScoreSightseeingPair(self, A):
        pre = A[0]
        ans = float('-inf')
        for i in range(1, len(A)):
            ans = max(ans, pre+A[i]-i)
            pre = max(pre, A[i]+i)
        return ans
        
if __name__ == '__main__':
	s = Solution()
	A = [8,1,5,2,6]
	print s.maxScoreSightseeingPair(A)