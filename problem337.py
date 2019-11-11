'''
337. House Robber III
Medium

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

Solution:
Can be formed into dp, but here we use simple recursion.
For each nodes, we need to consider two different situations, which is rob or not rob current node.
When we rob the current node, we can not rob the children of current node, so
ROB_VALUE = NOTROB_LEFT + NOTROB_RIGHT + rob value. 

If we do not rob current node, we can rob both children, but remember, here is "we can", but not "We will", so
NOTROB_VALUE = max(NOTROB_LEFT, ROBL_EFT)  + max(NOTROB_RIGHT,ROB_RIght)

Hence we have the deductive relationship.
'''
class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def max_value(self,root):
		if root is None:
			return 0,0
		rob = root.val
		left_max,left_max_not = self.max_value(root.left)
		right_max,right_max_not = self.max_value(root.right)
		rob_all = rob + left_max_not + right_max_not
        
		not_rob = 0
		not_rob_all = not_rob + max(left_max,left_max_not) + max(right_max,right_max_not)
		return rob_all,not_rob_all

	def rob(self, root):
		return max(self.max_value(root))
		
if __name__ == '__main__':
	solution = Solution()
	root = TreeNode(3)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.right = TreeNode(3)
	root.right.right = TreeNode(1)
	print solution.rob(root)

        