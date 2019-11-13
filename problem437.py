'''

437. Path Sum III
Easy

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

Solution:
Simple traversal, only difference is modify the global variable, add each path's value into the
list.

'''
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
	rst = countAll(root, [], 0)
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