'''

1017. Convert to Base -2
Medium

Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

The returned string must have no leading zeroes, unless the string is "0".

 

Example 1:

Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2

Example 2:

Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3

Example 3:

Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4

 

Note:

    0 <= N <= 10^9


Solution:
Actually I do not get this completely.
Mark this as unsolved.

'''


class Solution:
    def baseNeg2(self, N):
        if not N:
            return "0"
        ret = []
        while N:
            r = N % (-2)
            N //= (-2)
            if r < 0:
                r = 2 + r
                N += 1
            ret.append(str(r))
        ret.reverse()
        return "".join(ret)

if __name__ == '__main__':
	s = Solution()
	N = 14
	print s.baseNeg2(N)
