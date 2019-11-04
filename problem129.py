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