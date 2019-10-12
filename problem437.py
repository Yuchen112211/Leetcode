class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def countAll(root,rst,tmp):
	rst.append(root.val + tmp)
	if root.left != None:
		countAll(root.left,rst,root.val+tmp)
	if root.right != None:
		countAll(root.right,rst,root.val+tmp)
	return rst

def pathSum(root, sum):
	final_num = 0
	if root == None:
		return 0
	rst = countAll(root,[],0)
	return rst.count(sum) + pathSum(root.left,sum) + pathSum(root.right,sum)


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
	print pathSum(root,8)