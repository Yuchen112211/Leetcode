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