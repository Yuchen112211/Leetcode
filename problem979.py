'''

979. Distribute Coins in Binary Tree
Medium

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

 

Example 1:
		3
	   / \
	  0   0

Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:
		0
	   / \
	  3   0

Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.

Example 3:
		1
	   / \
	  0   2

Input: [1,0,2]
Output: 2

Example 4:
		1
	   / \
	  0   0
	   \
	    3

Input: [1,0,0,null,3]
Output: 4

Solution:
Very interesting problem.
Use recursive function to solve this problem.

Let's first explain how to come up with the solution. At the leaf node, we have to determine how many
coins are to moved to or moved from this leaf node. If the node is 0, we need 1 more coin to be shipped
into the node. If the node is 2, we need to ship 1 coin outside the node. So that is why we have to add
abs(count) to the global self.ans, because whether to be shipped outside or inside, it would take moves.

We can compute the left subtree as L, right subtree as R, and the current value of the root should be L+R-1.
L+R means how many coins should be shipped in or out to or from the root, minus 1 is because the root
should keep one coin.

Remember, count the moves should add abs, but the node value to be returned should be l + r - 1, since we 
have to count how many coins should be shipped on the root node(internal node).

'''

class Solution(object):
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans