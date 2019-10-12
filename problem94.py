#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal_recursion(root,rst):
	if root == None:
		return
	inorderTraversal_recursion(root.left,rst)
	rst.append(root.val)
	inorderTraversal_recursion(root.right,rst)

def inorderTraversal_iterate(root):
	if root == None:
		return []
	stack = [root]
	result = []

	while len(stack) != 0:
		while root.left is not None:
			stack.append(root.left)
			root = root.left 
		tmp = stack.pop()
		result.append(tmp.val)
		if tmp.right is not None:
			root = tmp.right
			stack.append(root)
	return result


if __name__ == "__main__":
	root = TreeNode(10)
	root.left = TreeNode(5)
	root.right = TreeNode(-3)
	root.left.left = TreeNode(3)
	root.left.left.left = TreeNode(3)
	root.left.left.right = TreeNode(-2)
	root.left.right = TreeNode(2)
	root.left.right.right = TreeNode(1)
	root.right.right = TreeNode(11)
	rst = []
	#inorderTraversal_recursion(root,rst)
	print inorderTraversal_iterate(root)