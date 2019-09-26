# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def max_value(self,root):
		if root is None:
			return 0,0
		rob = root.val
		left_max,left_max_not = self.max_value(root.left)
		right_max,right_max_not = self.max_value(root.right)
		rob_all = rob + left_max_not + right_max_not
        
		not_rob = 0
		not_rob_all = not_rob + max(left_max,left_max_not) + max(right_max,right_max_not)
		return rob_all,not_rob_all

	def rob(self, root):
		return max(self.max_value(root))
		return max(self.max_value(root))
		
if __name__ == '__main__':
	solution = Solution()
	root = TreeNode(3)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.right = TreeNode(3)
	root.right.right = TreeNode(1)
	print solution.rob(root)

        