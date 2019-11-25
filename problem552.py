'''

552. Student Attendance Record II
Hard

Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

	'A' : Absent.
	'L' : Late.
	'P' : Present.

A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:

Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 

Solution:

Recurrence formula:
Let Q(n) be the solution of the the question, namely the number of all rewardable records.
Let R(n) be the number of all rewardable records without A.

Thinking the problem as replacing Ps and As on an array of Ls instead. Since the constraint is no more than 3 continuous Ls is allowed. For a n-size array, let's just look into the first 3 places, since there must be at least on replacement been taken place there:

First, let's consider the case we replacing with P. There're 3 cases:

	P??: meaning we replace the first L with P. Doing so will shrink the problem size by one, so the number of this case is Q(n-1);
	LP?: meaning we replace the second L with P. The first place got to be L since the case where P in the first place is being considered above. So the number of this case is Q(n-2);
	LLP: meaning we replace the third L with P. Leaving us the number of Q(n-3);

Now let's consider the case we replacing with A:

	A??: This we narrow down the problem size by one, and for the rest places there must be no As. So the number is R(n-1);
	LA?: this will be R(n-2);
	LLA: this will be R(n-3);

It's easy to see that the recurrence formula of R is just similar to the first 3 cases combined, namely:
R(n) = R(n-1) + R(n-2) + R(n-3)

So the recurrence formula of Q is:

Q(n) = Q(n-1) + Q(n-2) + Q(n-3) + R(n-1) + R(n-2) + R(n-3)
	 = Q(n-1) + Q(n-2) + Q(n-3) + R(n)

'''
from collections import deque

class Solution(object):
	def checkRecord(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		MOD = 1000000007
		withA = deque([1, 3, 8])
		withoutA = deque([1, 2, 4])
		if n < 3:
			return withA[n]
		for i in range(3, n+1):
			withoutA.append(sum(withoutA) % MOD)
			withA.append((sum(withA) + withoutA[-1]) % MOD)
			withoutA.popleft()
			withA.popleft()
		return withA[-1]

s = Solution()
s.checkRecord(10)