class TreeNode(object):
	def __init__(self,val):
		self.val = val
		self.left=  None
		self.right = None

class Solution(object):
	def diameterOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1

s = Solution()
root = TreeNode(3)
