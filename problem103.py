'''

103. Binary Tree Zigzag Level Order Traversal
Medium

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

Solution:
Remember, how the node is popped out of the stack is the same, the only different is 
which direction that every iteration by finding out how many members are in rst.

In order to change direction, only use [::-1] as the method to reverse the list.

'''
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def zigzagLevelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []

		from collections import deque
		stack = deque([root])
		rst = []
		while stack:
			tmp = []
			nextStack = deque([])
			while stack:
				node = stack.popleft()
				tmp.append(node.val)
				if node.left:
					nextStack.append(node.left)
				if node.right:
					nextStack.append(node.right)

			if len(rst) % 2 == 0:
				rst.append(tmp)
			else:
				rst.append(tmp[::-1])
			stack = nextStack
		return rst


if __name__ == '__main__':
	s = Solution()
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.right.right = TreeNode(5)
	print s.zigzagLevelOrder(root)