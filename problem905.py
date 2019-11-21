'''

905. Sort Array By Parity
Easy

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Solution:
Use two pointers and while loop.
Remember to add the even < odd restriction inside the %2 loop, otherwise it would go off to the 
wrong positions.

'''
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = 0
        odd = len(A)-1
        while even < odd:
            while even < odd and A[even] % 2 == 0:
                even += 1
            while even < odd and A[odd] % 2:
                odd -= 1
            A[even], A[odd] = A[odd], A[even]
        return A

s = Solution()
A = [1,2,3,4,5,6]
print s.sortArrayByParity(A)