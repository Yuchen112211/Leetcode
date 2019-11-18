'''
795. Number of Subarrays with Bounded Maximum
Medium

We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

Example :
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Solution:
DP Solution below is TLE. Funny.

解题思路：
以 A = [73,55,36,5,55,14,9,7,72,52]，L = 32，R = 69 为例：
1、因为是连续子数组，所以可以根据 A[i] > R 进行分段。以上述为例，可以分为 3 段，即 [73]、[55,36,5,55,14,9,7]、[72,52]；
2、以中间一段为例，共有 21 个符合题意的子数组。那么这个 21 是怎么计算得到的呢？首先，总共有 (1+7) * 7 // 2 = 28 个子数组，然后我们排除连续的 A[i] < L 的子数组个数，即 [5] 和 [14,9,7]，共有 1 + (1+3) * 3 // 2 = 7 个子数组，因此就得到了该段子数组的个数为 21；
3、每一段都进行这样的操作，就可以得到最终结果 ans = 0 + 21 + 1 = 22。

代码实现：
1、使用两个变量 cntLessR 和 cntLessL 分别记录小于等于 R 的连续子数组长度和小于 L 的连续子数组长度，对结果 ans 进行累加 cntLessR，同时累减 cntLessL；
2、如果 A[i] >= L，说明小于 L 的子数组不连续，则置 cntLessL 为 0； 如果 A[i] > R，说明小于等于 R 的子数组不连续，则置 cntLessR 为 0；
3、这种做法的时间复杂度为 O(N)，空间复杂度为 O(1)。

'''

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        ans = 0
        cntLessR = 0  # 记录小于R的连续子数组长度
        cntLessL = 0  # 记录小于L的连续子数组长度
        for i in range(len(A)):
            if A[i] <= R:  # 小于R的连续子数组个数累加
                cntLessR += 1
                ans += cntLessR
            if A[i] < L:  # 小于L的连续子数组个数累减
                cntLessL += 1
                ans -= cntLessL
            if A[i] >= L:  # 不连续，将cntLessL置0
                cntLessL = 0
            if A[i] > R:  # 不连续，将cntLessR置0
                cntLessR = 0
        return ans
        
if __name__ == '__main__':
	s = Solution()
	L = 2
	R = 3
	A = [2, 1, 4, 3]

	print s.numSubarrayBoundedMax(A,L,R)