'''

38. Count and Say
Easy

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"

Solution:
Simple recusion can solve this problem, can be optimized to use dynamic programming.
Not so difficult, get the current string by previous one.

'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            tmp_str = self.countAndSay(n-1)
            cnt = 0
            current_char = ''
            rst = ''
            for i in tmp_str:
                if current_char != i:
                    if cnt != 0:
                        rst += str(cnt)
                        rst += current_char
                    current_char = i
                    cnt = 1
                else:
                    cnt += 1
            rst += str(cnt)
            rst += current_char
            return rst

if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(5)