'''

32. Longest Valid Parentheses
Hard

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

Solution:
Use deque to perform as stack
Description are as below in code.
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import deque
        if len(s) < 2:
            return 0
        stack = deque([-1])
        max_length = 0
        for i in range(len(s)):
            print stack
            if s[i] == '(':
                #Record the last ('s position appears.
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    #Current character is )
                    #If the stack is empty, which means -1 is popped out
                    #that is invalid.
                    #So append the new beginning.
                    stack.append(i)
                else:
                    #If not empty, which is the last ( position.
                    max_length = max(max_length, i - stack[-1])

        return max_length

s = Solution()
print s.longestValidParentheses(")))))")