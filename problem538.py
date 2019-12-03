'''

538. Convert BST to Greater Tree
Easy

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

Solution:
Simple traverse. Recursive is very slow, maybe iteration can do better job.

'''

class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution(object):

	def convertBST(self, root):
		self.currentVal = 0
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		def traverseAdd(root):
			if not root:
				return
			traverseAdd(root.right)
			self.currentVal += root.val
			root.val = self.currentVal
			traverseAdd(root.left)
		traverseAdd(root)
		return root

		
def traverse(root):
	if not root:
		return
	traverse(root.left)
	print root.val,
	traverse(root.right)


s = Solution()
root = TreeNode(7)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(4)

root.right = TreeNode(11)
root.right.left = TreeNode(9)
root.right.left.left = TreeNode(8)
root.right.left.right = TreeNode(10)
root.right.right = TreeNode(13)
root.right.right.left = TreeNode(12)
root.right.right.right = TreeNode(14)

traverse(s.convertBST(root))