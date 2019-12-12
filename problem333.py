'''

333. Largest BST Subtree
Medium

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.

Solution:


'''
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution(object):
	def largestBSTSubtree(self, root):
		self.size = -1

		def isBST(root):
			if not root:
				return (-1,-1,0)
			if not root.left and not root.right:
				self.size = max(1, self.size)
				return (root.val, root.val, 1)

			ll,lr,lsize = isBST(root.left)
			rl,rr,rsize = isBST(root.right)
			cl, cr, csize = root.val, root.val, 1

			if lsize == -1 or rsize == -1:
				return (-1, -1, -1)

			if lsize != 0:
				if lr >= root.val:
					return (-1,-1,-1)
				else:
					cl = ll
					csize += lsize
			if rsize != 0:
				if rl <= root.val:
					return (-1,-1,-1)
				else:
					cr = rr
					csize += rsize
			self.size = max(self.size, csize)
			return (cl, cr, csize)

		if not root:
			return 0

		isBST(root)
		return self.size

root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(5)

S = Solution()
print S.largestBSTSubtree(root)