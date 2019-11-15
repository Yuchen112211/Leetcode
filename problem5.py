'''

5. Longest Palindromic Substring
Medium

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

Solution:
Use a helper method expandCenter, which takes two pointers, left and right, check if the 
elements under left and right are eqaul, if so, move left to further left, move right to
further right, stop when there's bound or no longer equals.

Use a for loop, start the healper method on each index, make sure that start both kinds of 
situations, like the parlindrome has an odd length or even length.

'''
class Solution(object):
    def longestPalindrome(self, s):
        def expandCenter(s,left,right):
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                	break
            return s[left+1:right]
        
        rst = ''
        length = 0
        if len(s) < 2:
            return s
        for i in range(len(s)-1):
            current_sub_1 = expandCenter(s, i, i)
            current_sub_2 = expandCenter(s, i, i+1)
            if len(current_sub_1) > length:
                rst = current_sub_1
                length = len(current_sub_1)
            if len(current_sub_2) > length:
                rst = current_sub_2
                length = len(current_sub_2)
        return rst

if __name__ == '__main__':
	string = "a"
	s = Solution()
	print s.longestPalindrome(string)