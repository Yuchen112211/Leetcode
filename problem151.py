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