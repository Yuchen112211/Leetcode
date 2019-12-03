'''

971. Flip Binary Tree To Match Preorder Traversal
Medium

Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

If we cannot do so, then return the list [-1].

 

Example 1:

Input: root = [1,2], voyage = [2,1]
Output: [-1]

Example 2:

Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]

Example 3:

Input: root = [1,2,3], voyage = [1,2,3]
Output: []


'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        preorder = []
        def traverse(root):
            if not root:
                return
            preorder.append(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        
        def determineSwap(root, preorderList, givenOrder):
            if len(preorderList) != len(givenOrder) or not preorderList or not givenOrder:
                return -1
            
            if preorderList[0] != givenOrder[0]:
                return -1
            if not root.left and not root.right:
                return []
            elif not root.left:
                return determineSwap(root.right, preorderList[1:], givenOrder[1:])
            elif not root.right:
                return determineSwap(root.left, preorderList[1:], givenOrder[1:])
            
            rightIndex = preorderList.index(root.right.val)
            if preorderList[1] == givenOrder[1]:
                if preorderList[rightIndex] == givenOrder[rightIndex]:
                    swapLeftNodes = determineSwap(root.left, preorderList[1:rightIndex], givenOrder[1:rightIndex])
                    swapRightNodes = determineSwap(root.right, preorderList[rightIndex:], givenOrder[rightIndex:])
                    if swapLeftNodes == -1 or swapRightNodes == -1:
                        return -1
                    return swapLeftNodes + swapRightNodes
                else:
                    return -1
            elif preorderList[1] == givenOrder[len(givenOrder) - rightIndex + 1]:
                if preorderList[rightIndex] == givenOrder[1]:
                    swapLeftNodes = determineSwap(root.left, preorderList[1:rightIndex], givenOrder[len(givenOrder) - rightIndex + 1:])
                    swapRightNodes = determineSwap(root.right, preorderList[rightIndex:], givenOrder[1:len(givenOrder) - rightIndex + 1])
                    if swapLeftNodes == -1 or swapRightNodes == -1:
                        return -1
                    return [root.val] + swapLeftNodes + swapRightNodes
                else:
                    return -1
            else:
                return -1
        
        rst = determineSwap(root, preorder, voyage)
        if rst == -1:
            return [-1]
        else:
            return rst

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

s = Solution()
#Acutall = [1,2,4,5,3,6,8]
voyage = [1,3,8,6,2,5,4]
print s.flipMatchVoyage(root, voyage)