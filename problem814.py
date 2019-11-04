# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def contain_one(self,root):
		if root is None:
			return False
		if root.val == 1:
			return True
		else:
			if root.left is None:
				if root.right is None:
					return False
				return self.contain_one(root.right)
			else:
				if root.right is None:
					return self.contain_one(root.left)
				return self.contain_one(root.right) or self.contain_one(root.left)
	def pruneTree(self, root):
		if not self.contain_one(root):
			root = None
		else:
			root.left = self.pruneTree(root.left)
			root.right = self.pruneTree(root.right)
		return root

if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(0)
	root.left.left = TreeNode(0)
	root.left.left = TreeNode(0)
	root.right = TreeNode(1)
	root.right.left = TreeNode(0)
	root.right.right = TreeNode(1)
	s = Solution()
	root1 = s.pruneTree(root)
	def printT(root):
		if root is not None:
			printT(root.left)
			print root.val
			printT(root.right)
	printT(root1)

	printT(root)
		