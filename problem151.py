'''

151. Reverse Words in a String
Medium

Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Solution:
Very simple, split then reverse. Mind the spaces.

'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        s.reverse()
        rst = ''
        for i in s:
        	if i == '':
        		continue
        	else:
        		rst += i
        		rst += ' '
        rst = rst.strip(' ')
        return rst

if __name__ == '__main__':
	s = Solution()
	print s.reverseWords(" a good   example")