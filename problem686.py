'''

686. Repeated String Match
Easy

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.

Solution:
Easy problem, use two pointers to see if there's rotation. Once the first pointer becomes 0, plus one to the count.

'''
class Solution(object):
	def repeatedStringMatch(self, A, B):
		"""
		:type A: str
		:type B: str
		:rtype: int
		"""
		if B in A:
			return 1
		if set(A) != set(B):
			return -1
		pointer2 = 0
		startPoints = []
		for i in range(len(A)):
			if A[i] == B[pointer2]:
				startPoints.append(i)

		minTimes = float('inf')

		for pointer1 in startPoints:
			pointer2 = 0
			times = 1
			matched = True
			while pointer2 < len(B):
				if B[pointer2] != A[pointer1]:
					matched = False
					break
				else:
					pointer2 += 1
					pointer1 += 1
					if pointer1 == len(A):
						pointer1 = 0
						times += 1
			if matched:
				if pointer1 == 0:
					times -= 1
				minTimes = min(minTimes, times)
		return minTimes if minTimes != float('inf') else -1

		
s = Solution()
A = "a" 
B = "aa"
print s.repeatedStringMatch(A,B)