'''

863. All Nodes Distance K in Binary Tree
Medium

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

         3
       /   \
      5     1
     / \   / \
    6  2  0   8
      / \
     7   4


Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Solution:
I did this like huffman code.
After assign each node a string value to represents the path, we findout the distance
of two nodes by comparing two nodes' string.

In order to do compare, iterate through the shorter string, increase index when encounter
the same character, which means the two nodes has the same path and the character should
be ignored when computing distances.
After stop, the index indicates the common substring. The distance should be the sum of 
length of two string and subtract 2*index.

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        d = {}
        def findDistance(str1,str2):
            if not str1:
                return len(str2)
            elif not str2:
                return len(str1)
            index = 0
            for i in range(min(len(str1),len(str2))):
                if str1[i] == str2[i]:
                    index += 1
                else:
                    break
            return len(str1) + len(str2) - index * 2
                    
        def traverse(node, cnt):
            if not node:
                return
            d[node.val] = cnt
            traverse(node.right, cnt + '1')
            traverse(node.left, cnt + '2')
            
        traverse(root, '')
        rst = []

        
        target_path = d[target.val]
        for i in d:
            if findDistance(d[i], target_path) == K:
                rst.append(i)
        return rst

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    print s.distanceK(root,TreeNode(5),2)