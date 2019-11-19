'''

99. Recover Binary Search Tree
Hard

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Solution:
First use in-order to traverse the tree, put all nodes into an array. Since the tree was
supposed to be a BST, the original sequence should be sorted.

The second step is to find out which two nodes are in wrong positions. While the recorded 
list is empty, once we encounter a node with value bigger than the next, we push it into the
list.

If there's a node existed in the recorded list, next we only have to find the node which is 
bigger than the node in recorded list, since the node is swapped, the previous node should
be the other swapped node.

Convenient but not space-optimized.

'''
class Solution(object):
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        
        #1 in-order traversal and store in list 0(n)
        #2 get two out of order elements in list 0(n)
        #3 swap nodes 0(1)
        
        arr =[]
        self.inorder(root,arr)
        switchNodes = self.retreiveTwoNodes(arr)
        switchNodes[0].val,switchNodes[1].val = switchNodes[1].val,switchNodes[0].val
        return root
              
        
    def inorder(self,root,array):
        if not root:
            return []
        self.inorder(root.left,array)
        array += [root]
        self.inorder(root.right,array)
    
    def retreiveTwoNodes(self,arr):
        res = []
        for i in range(len(arr)):
            if not len(res):
                if arr[i].val > arr[i+1].val:
                    res.append(arr[i])
            else:
                if res[0].val < arr[i].val:
                    res.append(arr[i-1])
                    break
        if len(res) == 1:
            res.append(arr[-1])
        return res 