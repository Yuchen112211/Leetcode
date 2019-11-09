'''
201. Bitwise AND of Numbers Range
Medium

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

Example 2:

Input: [0,1]
Output: 0

Solution:
In the solution,  first we have to determine whether the bigger number is bigger than
the smaller number * 2, which means the AND recursive operation would be 0

For example, 8 is 1000, 4 is 100, 8 & 4 == 0. For N, 2 * N would some how pass the number
of form pow(2,x), whose binary form is 1000....00, that's why when the n is bigger than
2 * m, the result should 0.

After we easily determined the relationship, we use iterate to go over the number between 
m and n.
However, once the iterative number's binary form has longer length than m, which means it
reached the pow(2,x), we should break the loop, because however we perform the AND operation,
the result would still be 0.

If there's a 0 has been generated in the middle of the iteration, we should also break due to
the same reason.

'''



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