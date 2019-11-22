'''

894. All Possible Full Binary Trees
Medium

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

 

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

Solution:
Classic dp, use the trees that are formated before, store them into a dp list, use them to form the next possible tree.
Easy if using dp. Recursion is bullshit, it takes too much time.

'''

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def allPossibleFBT(self, N):
		"""
		:type N: int
		:rtype: List[TreeNode]
		"""
		if N == 1:
			return [TreeNode(0)]
		if not N % 2:
			return []

		dp = [[] for i in range(N+1)]
		dp[1] = [TreeNode(0)]

		for index in range(3, N + 1, 2):
			left = [i for i in range(1,index - 1, 2)]
			for leftTreeIndex in left:
				rightTreeIndex = index - 1 - leftTreeIndex
				for leftTree in dp[leftTreeIndex]:
					for rightTree in dp[rightTreeIndex]:
						currentNode = TreeNode(0)
						currentNode.left = leftTree
						currentNode.right = rightTree
						dp[index].append(currentNode)
		return dp[N]

s = Solution()
print s.allPossibleFBT(7)