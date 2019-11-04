'''

105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


Solution:
Preorder's first element is the organized root, divide the inorder list by the root,
the left part is the left subtree, right part is the right subtree.
Every time just pop the first element of the preorder list, and then start building the
left subtree, then right subtree.
Since the procedure is recursive, every node on the left subtree would be popped out
from the preorder list and formed a subtree, then it comes to right tree.

Which means we do not have to worry about whether the current root is in the inorder
sequence, cause we go over all the nodes and popped the nodes that do not belongs to
current inorder list.

Build the two children seperately.

'''
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	
	def buildTree(self, preorder, inorder):
		if not preorder:
			return None
		if not inorder:
			return None
		ele = preorder.pop(0)
		inOrderIndex = inorder.index(ele)
		left = inorder[:inOrderIndex]
		right = inorder[inOrderIndex+1:]
		currentNode = TreeNode(ele)
		currentNode.left = self.buildTree(preorder,left)
		currentNode.right = self.buildTree(preorder,right)
		return currentNode

	"""
	def buildTree(self, preorder, inorder):
		if not preorder:
			return None
		if not inorder:
			return None
		ele = preorder.pop(0)
		root = TreeNode(ele)
		idx = inorder.index(ele)
		root.left = self.buildTree(preorder, inorder[:idx])
		root.right = self.buildTree(preorder, inorder[idx+1:])
		return root
	"""

if __name__ == '__main__':
	s = Solution()
	preorder = [1,2,4,5,6,7,3]
	inorder = [4,2,6,5,7,1,3]
	root = s.buildTree(preorder,inorder)
	def traverse(root):
		if root is None:
			return
		traverse(root.left)	
		print root.val,
		traverse(root.right)
	traverse(root)