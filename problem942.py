'''

942. DI String Match
Easy

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

    If S[i] == "I", then A[i] < A[i+1]
    If S[i] == "D", then A[i] > A[i+1]

 

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]

Example 2:

Input: "III"
Output: [0,1,2,3]

Example 3:

Input: "DDI"
Output: [3,2,0,1]

Solution:
Use two pointers, left and right. Fill in each D with left, I with right.
Right starts at the tail of the array, left starts at head.

'''
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