class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.right = None
		self.left = None

class Solution(object):
	def hasPathSum(self, root, sum):
		"""
		
		if root is None:
			return 0
		if root.left is None and root.right is None:
			if sum == root.val:
				return True
			return False
		def getPossibleSum(root):
			if root is None:
				return []
			if root.left is None and root.right is None:
				return [root.val]
			left_sum = []
			right_sum = []
			current_sum = []
			if root.left is not None:
				left_sum = getPossibleSum(root.left)
				if left_sum is not []:
					current_sum += [i+root.val for i in left_sum]
				else:
					current_sum += [root.val]
			if right_sum is not None:
				right_sum = getPossibleSum(root.right)
				if right_sum is not []:
					current_sum += [i+root.val for i in right_sum]
				else:
					current_sum += [root.val]
			return list(set(current_sum))
		sums = getPossibleSum(root)
		if sum in sums:
			return True
		return False
		"""
		sum_l = []
		def getPossibleSum(root,current_sum,sum_l):
			if root is None:
				sum_l.append(current_sum)
				return
			if root.left is None and root.right is None:
				sum_l.append(current_sum+root.val)
				return
			if root.left is not None:
				getPossibleSum(root.left,current_sum+root.val,sum_l)
			if root.right is not None:
				getPossibleSum(root.right,current_sum+root.val,sum_l)
		getPossibleSum(root,0,sum_l)
		if sum in sum_l:
			return True
		return False


if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(2)
	sum = 1
	s = Solution()
	print s.hasPathSum(root,sum)