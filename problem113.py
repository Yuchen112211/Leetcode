class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class TreePath(TreeNode):
	def __init__(self,l,val,root):
		self.path = l
		self.sum = val
		self.node = root

'''

113. Path Sum II
Medium

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

Solution:
This is actually a backtrack solution.
When traversal, we append the current value to the list which records the path that go all way from root to leaf.
After we finished recursion of current node, and then we simply pop out the tail element of the recorded list in
order to conduct next tree's traversal.

Since we append the current val, then we call recursive of the same function, after we go through all the children
we then pop out the tail element.

That's it, backtrack.

'''

class Solution(object):

    def pathSum(self, root, summ):
        a = []
        b = []
        if root is None:
            return []
        def path(root, summ, current_sum):
            if root.left is None and root.right is None:
                current_sum += root.val
                if current_sum == summ:
                    b.append(root.val)
                    a.append(b[:])
                    b.pop()
                return 
            if root.left is not None:
                b.append(root.val)
                path(root.left, summ, current_sum + root.val)
                b.pop()
            if root.right is not None:
                b.append(root.val)
                path(root.right, summ , current_sum + root.val)
                b.pop()
        path(root, summ, 0)
        return a


def Traversal(root):
	if not root:
		return
	Traversal(root.left)
	print root.val
	Traversal(root.right)

def construct():
	root = TreeNode(5)
	root.left = TreeNode(4)
	root.right = TreeNode(8)
	root.left.left = TreeNode(11)
	root.right.left = TreeNode(13)
	root.right.right = TreeNode(4)
	root.left.left.left = TreeNode(7)
	root.left.left.right = TreeNode(2)
	root.right.right.left = TreeNode(5)
	root.right.right.right = TreeNode(1)
	return root

if __name__ == '__main__':
	root = construct()

	s = Solution()
	print s.pathSum(root,22)