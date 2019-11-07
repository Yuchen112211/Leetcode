'''

199. Binary Tree Right Side View
Medium

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


Solution:
First use level traversal, then everytime we get the most right node.

'''


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