'''

102. Binary Tree Level Order Traversal
Medium

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]


Solution:

This should be easy.
Apply a stack in order to store everything in the same level.
Use the deque in order to append and pop from the head of the list/queue.

In each level's travsesal, pop out everything in stack, and process them all at once.
Add each node's left node and right node into the next_l list in order to put them into next round
of traversal.

This will implement the level traversal.

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        from collections import deque
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        stack = deque([root])
        rst= []
        while stack:
            next_l = [] #Record the next level.
            tmp = []#Record the current level.
            while stack:
                current_node = stack.popleft()
                if current_node.left:
                    next_l.append(current_node.left)
                if current_node.right:
                    next_l.append(current_node.right)
                tmp.append(current_node.val)
            rst.append(tmp)
            #Set the stack to be next level.
            stack = deque(next_l)
        return rst

if __name__ == '__main__':
    root = TreeNode(3)
    root.right = TreeNode(20)

    s = Solution()
    print s.levelOrder(root)