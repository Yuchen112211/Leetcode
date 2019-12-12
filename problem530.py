'''

530. Minimum Absolute Difference in BST
Easy

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
	\
	 3
	/
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Solution:
Use boaders to record the min value and the max value of the current tree, compare them to define if the current tree is a BST.
'''
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution(object):
	def getMinimumDifference(self, root):
		#Do inorder traverse
		#Since this is a BST, then the order of the values are strictly increasing if we do the inorder traverse. Then the difference are strictly
		#defined by the order.
		#We can not avoid traversing the whole BST, but we can do this faster with a little help of memo.
		self.order = []
		self.ans = float('inf')
		def inorder(root):
			if not root:
				return
			inorder(root.left)
			if self.order:
				self.ans = min(self.ans, root.val - self.order[-1])
			self.order.append(root.val)
			inorder(root.right)
		inorder(root)
		return self.ans

S = Solution()
root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)

print S.getMinimumDifference(root)