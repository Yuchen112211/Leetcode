'''

86. Partition List
Medium

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

Solution:
First approach is to store each node's value and partition them according to K.
Second apprach is one-way pass iteration, maintain two node, at the end link two nodes.

'''

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

'''
class Solution(object):
	def partition(self, head, x):
		"""
		:type head: ListNode
		:type x: int
		:rtype: ListNode
		"""
		big = []
		small = []
		if head is None:
			return None
		while head is not None:
			if head.val < x:
				small.append(head.val)
			else:
				big.append(head.val)
			head = head.next
		rst = []
		rst = small+big
		rst1 = ListNode(rst[0])
		rst_return = rst1
		for i in range(1,len(rst)):
			rst1.next = ListNode(rst[i])
			rst1 = rst1.next
		return rst_return
'''
def printListNode(root):
	while root:
		print root.val,
		root = root.next
class Solution(object):
	def partition(self, head, x):
		if not head:
			return None

		big = ListNode(-1)
		bigHead = big
		small = ListNode(-1)
		smallHead = small

		while head:
			if head.val < x:
				smallHead.next = ListNode(head.val)
				smallHead = smallHead.next
			else:
				bigHead.next = ListNode(head.val)
				bigHead = bigHead.next
			head = head.next
		smallHead.next = big.next
		return small.next


if __name__ == '__main__':
	s = Solution()
	head = ListNode(1)
	x = head
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(3)
	head.next.next.next.next = ListNode(4)
	head.next.next.next.next.next = ListNode(4)
	head.next.next.next.next.next.next = ListNode(5)

	printListNode(s.partition(head,4))