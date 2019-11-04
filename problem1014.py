'''
1014. Best Sightseeing Pair
Medium

Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

 

Note:

    2 <= A.length <= 50000
    1 <= A[i] <= 1000

Solution:
Using DP, but do not need a one-dimensional array for memorization.

Simply use two variables to perform dp.

pre variable as the maximum previous score that can achieved before i, and ans variable
represents the max scores that can be achieved at current i.

Score is computed as A[i] + A[k] + i - k where i < k, in such case, bigger the i+A[i] would
give us the bigger score, and we simply compute the current score by add the prev and current
A[k], then minus the k.
'''

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