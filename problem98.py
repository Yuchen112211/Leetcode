# Definition for a binary tree node.
# class TreeNode(object):
#   def __init__(self, x):
#      self.val = x
#      self.left = None
#      self.right = None

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        if root is None:
            return True
        """
        # Approach 1

        tmp_val = root.val
        def traverse(root,l):
            if root is None:
                return
            traverse(root.left,l)
            l.append(root.val)
            traverse(root.right,l)
        def isValid(val,l):
            index = l.index(val)
            for i in l[:index]:
                if i >= val:
                    return False
            for i in l[index+1:]:
                if i <= val:
                    return False
            return True
        tmp_l = []
        traverse(root,tmp_l)
        if isValid(tmp_val,tmp_l):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False

        # Approach 2
        import sys
        boundary = [-sys.maxint-1,sys.maxint]
        def valid(root,boundary):
            if root is None:
                return True
            if root.val <= boundary[0] or root.val >= boundary[1]:
                return False
            valid_left = valid_right = False
            return valid(root.left,[boundary[0],root.val]) and valid(root.right,[root.val,boundary[1]])
        return valid(root,boundary)


        # Approach 3
        def traverse(root,l):
            if root is None:
                return
            traverse(root.left,l)
            l.append(root.val)
            traverse(root.right,l)
        import copy
        tmp_l = []
        traverse(root,tmp_l)
        rst = copy.deepcopy(tmp_l)
        tmp_l = sorted(tmp_l)
        if rst != tmp_l or len(set(rst)) != len(rst):
            return False
        return True

        """ 
        #Approach 4
        def traverse(root,l):
            if root is None:
                return
            traverse(root.left,l)
            if len(l) != 0:
                if root.val <= l[-1]:
                    return False
            l.append(root.val)
            traverse(root.right,l)
        tmp_l = []
        rst = traverse(root,tmp_l)
        if rst is not None:
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print s.isValidBST(root)