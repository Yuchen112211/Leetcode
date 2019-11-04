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