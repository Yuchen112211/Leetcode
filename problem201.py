class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        index = m
        i = m
        next_num = int('1'+bin(m)[2:],2)
        if n > next_num:
        	return 0
        while i <= n:
        	if len(bin(i)) > len(bin(m)) or index == 0:
        		index = index & i
        		break
        	index = index & i
        	i += 1

        return index
        
if __name__ == '__main__':
	s = Solution()
	print s.rangeBitwiseAnd(600000000,2147483645)