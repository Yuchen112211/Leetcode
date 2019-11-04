class TreeNode(object):
	def __init__(self,val):
		self.val = val
		self.left=  None
		self.right = None

class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		import collections
		if not root:
			return None
		right_view = collections.deque()
		stack = collections.deque([root])
		
		while stack:
			current_arr = []
			while stack:
				current_node = stack.popleft()
				current_arr.append(current_node)
			right_view.append(current_arr[-1].val)
			for i in current_arr:
				if i.left:
					stack.append(i.left)
				if i.right:
					stack.append(i.right)

		return right_view

if __name__ == '__main__':
	s = Solution()
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.right = TreeNode(5)
	root.right.right = TreeNode(4)

	print s.rightSideView(root)