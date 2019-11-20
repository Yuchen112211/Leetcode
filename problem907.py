'''

907. Sum of Subarray Minimums
Medium

Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

Solution:
This problem due to the amount of data, DP solution would TLE.

The other solution is super clever, maintain two lists, left and right, record the smaller element that on
the left or right. Use stack to implement such function. At each index, the length that right[i] - left[i]
can be computed as the number of subarray that has the minimum element as arr[i].

(i - left[i]) * (right[i] - i) means that the current element must be contained in the subarray, and left 
elements of the current one has i - left[i] kinds of subarrays.

Super intelligent approach.
'''

class Solution(object):
	def sumSubarrayMins(self, A):
		stack = []
		left = [-1]*len(A)
		right = [len(A)]*len(A)
		for i in range(len(A)):
			while stack and A[i] <= A[stack[-1]]:
				tmp = stack.pop()
				right[tmp] = i
			left[i] = stack[-1] if stack else -1
			stack.append(i)

		res = 0
		for cur, (a,b) in enumerate(zip(left,right)):
			res += A[cur]*(b-cur)*(cur-a)
		return res%(10**9+7)


if __name__ == '__main__':
	s = Solution()
	A = [3,1,2,4]
	print s.sumSubarrayMins(A)