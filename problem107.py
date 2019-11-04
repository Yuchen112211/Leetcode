'''

107. Binary Tree Level Order Traversal II
Easy

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

Solution:

The same as 102, the only change is add the level list into the first index of the 
rst.

'''

# Definition for a binary tree node.
import os
class TreeNode(object):
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        if root is None:
            return []
        rst = []
        stack = [root]
        
        while stack:
            rst.insert(0,[])
            length_now = len(stack)
            for i in range(length_now):
                if stack[i].left is not None:
                    stack.append(stack[i].left)
                if stack[i].right is not None:
                    stack.append(stack[i].right)
                rst[0].append(stack[i].val)
            stack = stack[length_now:]
        return rst

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print s.levelOrderBottom(root)