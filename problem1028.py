'''

1028. Recover a Tree From Preorder Traversal
Hard

We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.

 

Example 1:

		1
	   / \
	  2   5
	 / \ / \
	3  4 6  7

Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:

		1
	   / \
	  2   5
	 /	 /
	3	6
   /   /
  4   7

Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

 

Example 3:

		1
	   /
	  401
	 /   \
   349   88
   /
  90

Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]

Solution:
The given string is in infix form, which means that the first number that appears
is the root.
Then we simply find the next paramter, which represents the level of the nodes.
Means we have to divide the string into to parts, split by the '---'

For instance, if string is 1-2--3--4-5, we find the root 1, left is 2--3--4 and left 
is 5. After we recorded the dashes, find the next same form dashed and divide the 
string into two parts.

Call the function recursively.


'''
class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def recoverFromPreorder(self,S):
		S = S.strip('-')
		S = S.strip(' ')
		if S == '':
			return None
		if '-' not in S:
			return TreeNode(int(S))
		i = 0
		while S[i].isdigit():
			i += 1
		root = TreeNode(int(S[:i]))
		S = S[i:]
		parameter = ''
		i = 0
		while not S[i].isdigit():
			parameter += S[i]
			i += 1
		S = S.strip('-')
		j = 1

		while j+len(parameter) < len(S):
			if S[j:j+len(parameter)] == parameter and S[j-1].isdigit() and S[j+len(parameter)].isdigit():
				break
			j += 1
		if j == len(S)-len(parameter):
			left_tree = S
			root.left = self.recoverFromPreorder(left_tree)
		else:
			left_tree = S[:j+len(parameter)-1]
			right_tree = S[j+len(parameter):]
			#print left_tree,right_tree
			root.left = self.recoverFromPreorder(left_tree)
			root.right = self.recoverFromPreorder(right_tree)
		return root

if __name__ == '__main__':
	s = Solution()
	S = "1-2--3--4-5--6--7"

	def printT(root):
		if root is not None:
			printT(root.left)
			print root.val
			printT(root.right)

	root = s.recoverFromPreorder(S)
	printT(root)