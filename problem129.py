'''

129. Sum Root to Leaf Numbers
Medium

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

Solution:
With a helper method, do a traverse, Record the current char and string.
If encountered a leaf, append it to list that passed by function.
Last we add all these numbers together and return it.

'''

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        str_root = root
        total = []
        def getVal(root,val,total):
            if not root:
                return
            if not root.left and not root.right:
                total.append(int(val+str(root.val)))
                return
            getVal(root.left,val+str(root.val),total)
            getVal(root.right,val+str(root.val),total)
            root.val = val + str(root.val)
            
        getVal(str_root,'',total)
        return sum(total)
            
s = Solution()
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

print s.sumNumbers(root)