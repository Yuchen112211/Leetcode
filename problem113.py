# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

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
class Solution(object):
	"""
	def pathSum(self, root, sum):
		if not root:
			return []
		paths = {root:[root.val]}
		rst = []
		self.findSum(root,paths,rst,sum)
		return rst

	def findSum(self, root, paths,rst,sum1):
		import copy
		if root.left is not None:
			paths[root.left] = copy.deepcopy(paths[root])
			paths[root.left].append(root.left.val)
			self.findSum(root.left, paths,rst,sum1)
		if root.right is not None:
			paths[root.right] = copy.deepcopy(paths[root])
			paths[root.right].append(root.right.val)
			self.findSum(root.right, paths,rst,sum1)

		if not root.left and not root.right:
			if sum(paths[root]) == sum1:
				rst.append(paths[root])
	"""
	
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