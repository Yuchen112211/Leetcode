'''

814. Binary Tree Pruning
Medium

We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
 
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]



Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Solution:
Just use recursive, check for each subtree, if not containing any one, set the current node
to None.

Very simple recusive problems.

'''
class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def contain_one(self,root):
		if root is None:
			return False
		if root.val == 1:
			return True
		else:
			if root.left is None:
				if root.right is None:
					return False
				return self.contain_one(root.right)
			else:
				if root.right is None:
					return self.contain_one(root.left)
				return self.contain_one(root.right) or self.contain_one(root.left)
	def pruneTree(self, root):
		if not self.contain_one(root):
			root = None
		else:
			root.left = self.pruneTree(root.left)
			root.right = self.pruneTree(root.right)
		return root

if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(0)
	root.left.left = TreeNode(0)
	root.left.left = TreeNode(0)
	root.right = TreeNode(1)
	root.right.left = TreeNode(0)
	root.right.right = TreeNode(1)
	s = Solution()
	root1 = s.pruneTree(root)
	def printT(root):
		if root is not None:
			printT(root.left)
			print root.val
			printT(root.right)
	printT(root1)

	printT(root)
		