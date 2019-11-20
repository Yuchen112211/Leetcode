'''

96. Unique Binary Search Trees
Medium

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


Solution:
Actually this is a problem using DP solution.
The BST with one node can only form one tree, two nodes form two. 
With n node, we only have to compute leftTreeNum * rightTreeNum, let's say the current root
is i, then the nodes in left tree is [:i], right is [i+1:], then just recursively compute the 
DP array.

For instance, we now dp[0] = 1, dp[1] = 1, dp[2] = 2, then let's compute dp[3]:
dp[3] = dp[0] * dp[2] + dp[1] * dp[1] + dp[2] * dp[0].

However I wonder why in the below code arr[0] equals 0.

But, you get the idea.

'''
class Solution(object):
    def numTrees(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        arr = [0] * (n+1)
        arr[0] = 0
        arr[1] = 1
        arr[2] = 2
        for i in range(3,n+1):
            for k in range(i-1):
                left = k
                right = i-1-k
                arr[i] += arr[left] * arr[right]
        return arr[-1]
