'''

775. Global and Local Inversions
Medium

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.

Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.

Solution:
First I used max(left) > min(right), which clearly is TLE.
Actually through the iteration, we can find out the biggest value before i-2, and
compare the value to i, which saves the min(right) time, but still accomplish the job.

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return True
        leftMax = float('-inf')
        for i in range(2, len(A)):
            leftMax = max(leftMax, A[i-2])
            if leftMax > A[i]:
                return False
        return True

However there's a detail about the problem, the A is of [0,1,....,N-1], we can use this detail
to come up with fine solution as below.

Once there's a number that has shifted away more than 1, there must be an associated number that
can form aother gloabal inversion. Very clever.  
'''

class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        distance = [abs(i-x) for i, x in enumerate(A)]
        return all(x == 1 or x==0 for x in distance)

