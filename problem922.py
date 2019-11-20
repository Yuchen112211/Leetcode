'''

922. Sort Array By Parity II
Easy

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Solution:
Maintain another index for odd numbers, then use a for loop to go over the even numebrs.
If ever encounter an odd number on an even index, start to increase the odd index, if 
found an even number on the odd index, swap two numbers.

'''

class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in xrange(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
if __name__ == '__main__':
    s = Solution()
    A = [648,831,560,986,192,424,997,829,897,843]

    print s.sortArrayByParityII(A)