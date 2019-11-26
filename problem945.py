'''

945. Minimum Increment to Make Array Unique
Medium

Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].

Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

Solution:
Since we can only increment the element by 1, not substract of other, so this would simplify the question a lot.

First sort the array, now we maintain a variable `current`, this variable records the numbers that we are to fill in the array.
For instance, after we go through [1,1,1] the current would change like [1,2,3,4], current indicates the next element to be filled.
After go through [1,3,3,4,8], current would go like [1,3,4,5,8,9].

At iteration, if the current variable is bigger or equal to the iterated element, this means that we need to modify the iterated element
in order to meet the the "Supposed to fill" element, we add the difference to rst.

If the current variable is smaller than the iterated element, means that the iterated element is a distinct number, we update the current 
to be 1 + iterated element, means that the next element to be filled should be the `current` number. This would not take any steps of operations.

'''

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        current = 1
        A = sorted(A)
        rst = 0
        for i in A:
            if current >= i:
                rst += (current - i)
                current += 1
            else:
                current = i+1
        return rst

s = Solution()
A = [6, 2, 6, 7, 1, 7, 5, 5, 5, 10, 9, 10, 10, 10, 3, 5, 10, 10, 9, 6]

print s.minIncrementForUnique(A)