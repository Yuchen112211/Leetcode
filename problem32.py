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