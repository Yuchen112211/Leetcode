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
            next_l = []
            tmp = []
            while stack:
                current_node = stack.popleft()
                if current_node.left:
                    next_l.append(current_node.left)
                if current_node.right:
                    next_l.append(current_node.right)
                tmp.append(current_node.val)
            rst.append(tmp)
            stack = deque(next_l)
        return rst

if __name__ == '__main__':
    root = TreeNode(3)
    root.right = TreeNode(20)

    s = Solution()
    print s.levelOrder(root)