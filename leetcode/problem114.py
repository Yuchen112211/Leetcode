# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def flatten(self, root):
		if root is None:
			return None
		if root.left is None and root.right is None:
			return root
		head = root
		l = [root]
		while l:
			current_node = l.pop()
			if current_node.right is not None:
				l.append(current_node.right)
			if current_node.left is not None:
				l.append(current_node.left)
			if l:
				current_node.right = l[-1]
			current_node.left = None

def Traversal(root):
	if not root:
		return
	print root.val
	Traversal(root.right)

def construct():
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(5)
	root.left.left = TreeNode(3)
	root.right.right = TreeNode(6)
	root.left.right = TreeNode(4)
	return root


if __name__ == '__main__':
	root = construct()

	s = Solution()
	s.flatten(root)
	Traversal(root)
