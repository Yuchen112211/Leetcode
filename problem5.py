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