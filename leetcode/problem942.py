class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        wait_for = [i for i in range(len(S)+1)]
        rst = []
        left = 0
        right = len(S)
        for i in S:
        	if i == 'D':
        		rst.append(wait_for[right])
        		right -= 1
        	else:
        		rst.append(wait_for[left])
        		left += 1
        rst.append(wait_for[right])
        return rst

if __name__ == '__main__':
	s = Solution()
	print s.diStringMatch('IDID')