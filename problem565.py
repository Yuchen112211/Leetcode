'''

565. Array Nesting
Medium

A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

 

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

Solution:
Originally I thought the question can maintain a visited set, start at every index, go over
the whole list. 
Like backtrack solution, set the nums[index] to be -1, if encounter an element with the value
of -1, stop and move on to the next element.

Clever, "in" function of set can be optimized even more.

'''
class Solution:
    def arrayNesting(self, nums):
        result = 0
        n = len(nums)
        
        for i in range(n):
            curr = i
            size = 0
            
            while not nums[curr] == -1:
                size += 1
                temp = nums[curr]
                nums[curr] = -1
                curr = temp
            
            result = max(result, size)
        
        return result
