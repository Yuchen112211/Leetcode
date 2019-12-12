# Definition for a binary tree node.
# class TreeNode(object):x
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None
class TreeNode(object):
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

class Solution(object):
	def boundaryOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []
		self.leaf = []
		self.leftBoader = [root]
		self.rightBoader = [root]
		cur = root.left
		while cur:
			self.leftBoader.append(cur)
			cur = cur.left or cur.right
		cur = root.right
		while cur:
			self.rightBoader.append(cur)
			cur = cur.right or cur.left

		def findLeaf(root):
			if not root:
				return
			if not root.left and not root.right:
				self.leaf.append(root)
				return
			findLeaf(root.left)
			findLeaf(root.right)

		rst = self.leftBoader
		findLeaf(root)
		for i in self.leaf:
			if i in rst:
				continue
			else:
				rst.append(i)
		for i in self.rightBoader[::-1]:
			if i in rst:
				continue
			else:
				rst.append(i)

		return [i.val for i in rst]

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left = TreeNode(7)

print s.boundaryOfBinaryTree(root)