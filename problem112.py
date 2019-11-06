'''

112. Path Sum
Easy

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Solution:
Simple traversal. Add the number into the list passed through function when encoutner
Leaf node.	

Use set rather than list would provide less time complexity.

'''

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None

class Solution(object):
	def hasPathSum(self, root, sum):
		sum_l = set()
		def getPossibleSum(root,current_sum,sum_l):
			if root is None:
				sum_l.add(current_sum)
				return
			if root.left is None and root.right is None:
				sum_l.add(current_sum+root.val)
				return
			if root.left is not None:
				getPossibleSum(root.left,current_sum+root.val,sum_l)
			if root.right is not None:
				getPossibleSum(root.right,current_sum+root.val,sum_l)
		getPossibleSum(root,0,sum_l)
		if sum in sum_l:
			return True
		return False


if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(2)
	sum = 1
	s = Solution()
	print s.hasPathSum(root,sum)