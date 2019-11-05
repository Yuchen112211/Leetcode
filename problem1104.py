'''

https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

1104. Path In Zigzag Labelled Binary Tree
Medium

In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

reverse the order

Example 1:

Input: label = 14
Output: [1,3,4,14]

Example 2:

Input: label = 26
Output: [1,2,6,10,26]

Solution:
Actually it's pretty easy, we first find out which level is the current value is on.
If the level is odd number, the current position is the original pos, if even, it's
on the opposite site of the original place.
So for each index, we find out the N for 2^N <= index < 2^(N+1), if check the even-odd
of the N. If even, index = 2^(N+1) - 1 - index + 2^N, and repeat the process until index
is 1 or 0.
Thus we can find out the path.

Divide by two is find out the index of previous parent.

'''
class Solution(object):
	def pathInZigZagTree(self, label):
		"""
		:type label: int
		:rtype: List[int]
		"""
		if label == 1:
			return [1]
		rows = 0
		while True:
			if pow(2,rows) > label:
				break
			rows += 1
		rows -= 1
		offset = pow(-1,rows % 2)
		rst = [label]
		index_now = 0
		if rows % 2 == 0:
			index_now = label
		else:
			index_now = pow(2,rows+1)-label + pow(2,rows) - 1
		offset = -1 * offset
		rows -= 1
		while index_now != 1:
			if index_now % 2 == 1:
				next_index = (index_now - 1) / 2
			else:
				next_index = (index_now) / 2
			if rows % 2 == 0:
				val = next_index
			else:
				val = pow(2,rows) + pow(2,rows+1) - next_index-1
			rows -= 1
			index_now = next_index
			rst.append(val)
		rst.reverse()
		return rst

if __name__ == '__main__':
	s = Solution()
	s.pathInZigZagTree(31)