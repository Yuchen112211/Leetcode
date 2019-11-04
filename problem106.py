'''

106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


Solution:

The same as 105, the difference is pop from the tail.

'''


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