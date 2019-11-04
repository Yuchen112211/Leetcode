class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	
	def buildTree(self, inorder, postorder):
		if not postorder:
			return None
		if not inorder:
			return None
		ele = postorder.pop()
		inOrderIndex = inorder.index(ele)
		left = inorder[:inOrderIndex]
		right = inorder[inOrderIndex+1:]
		currentNode = TreeNode(ele)
		currentNode.right = self.buildTree(right,postorder)
		currentNode.left = self.buildTree(left,postorder)
		return currentNode


if __name__ == '__main__':
	s = Solution()
	postorder = [9,3,15,20,7]
	inorder = [9,15,7,20,3]
	root = s.buildTree(postorder,inorder)
	def traverse(root):
		if root is None:
			return
		traverse(root.left)	
		print root.val,
		traverse(root.right)
	traverse(root)

	#Open this folder and please post a brief bio of yourself. 
	#Feel free to include your background, interests, hobbies, 
	#and what you hope to gain from this course.
	#Think of this as your first day of class and get to know each other!