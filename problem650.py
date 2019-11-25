'''

650. 2 Keys Keyboard
Medium

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

    Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
    Paste: You can paste the characters which are copied last time.

 

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Solution:
So this is actually a math problem.
In order to find out the minimum steps, we need to paste as longest as we can. 400 As can be reduced to 200 As by paste 200 As, and this is the biggest times that can be reduced
by paste operation. Then the problem is simply looking for the biggest factor of the current n.

To find the biggest factor of n, a way to do so is to find the smallest prime factor of n, why prime is pretty obvious. After we find the smallest factor, we at the smallest factor
into the result, and replace the current n by the biggest factor, the biggest factor can simply computed by the smallest factor we got before.

When the smallest factor is the number itself, we stop the iteration since it is a prime number, we add this number to the result and return it.

Actually a math problem.

'''
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        def findSmallestPrimFactor(number):
            if number % 2 == 0:
                return 2
            i = 3
            while i * i <= number:
                if number % i == 0:
                    return i
                i += 2
            return number

        rst = 0
        factor = -1
        while True:
            factor = findSmallestPrimFactor(n)
            if factor == n:
                break
            else:
                times = n / factor
                rst += factor
                n = times
        rst += n
        return rst
 
s = Solution()
print s.minSteps(824)