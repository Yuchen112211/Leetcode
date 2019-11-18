'''

236. Lowest Common Ancestor of a Binary Tree
Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Solution:
So my thought is to record each node's position, like the level traversal, get the both indexes of the 
given p and q, then simply compute these two indexes' ancestor.

If index is odd, the previous is index-1/2, if even, previous is index-2/2.

Should be a more efficient way.

'''
class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		from collections import deque
		stack = deque([(root, 0)])
		arr = {}
		while stack:
			tmp = deque([])
			while stack:
				node, index = stack.popleft()
				arr[node] = index
				if node:
					tmp.append((node.left, 2 * index + 1))
					tmp.append((node.right, 2 * index + 2))
			stack = tmp

		def getAncestor(num1, num2):
			numbers = set([])
			while num1 >= 0:
				numbers.add(num1)
				if num1 % 2 == 1:
					num1 = (num1 - 1) / 2
				else:
					num1 = (num1 - 2) / 2
			while num2 >= 0:
				if num2 in numbers:
					return num2
				else:
					if num2 % 2 == 1:
						num2 = (num2 - 1) / 2
					else:
						num2 = (num2 - 2) / 2

		index1 = arr[p]
		index2 = arr[q]
		designated = getAncestor(index1,index2)
		for i in arr:
			if arr[i] == designated:
				return i

if __name__ == '__main__':
	root = TreeNode(3)
	root.left = TreeNode(5)
	root.left.left = TreeNode(6)
	root.left.right = TreeNode(2)
	root.left.right.left = TreeNode(7)
	root.left.right.right = TreeNode(4)
	root.right = TreeNode(1)
	root.right.left = TreeNode(0)
	root.right.right = TreeNode(8)
	s = Solution()
	print s.lowestCommonAncestor(root, root.left, root.left.right.right).val
