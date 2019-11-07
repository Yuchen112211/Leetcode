'''

19. Remove Nth Node From End of List
Medium

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Solution:
Use two pointers with one pass.
The second pointer goes N steps ahead of the first pointer. When the second is None, we encounter
the node that we need to remove.
Notice, I use second.next to determine whether we have encountered the designated node. Because we have
to assign the remove node's next to be the next node of the previous node.

'''
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		
		first = head
		second = head
		num = n
		while num > 0:
			second = second.next
			num -= 1
		if not second:
			return head.next
		
		while second.next:
			second = second.next
			first = first.next
		first.next = first.next.next
		return head

if __name__ == '__main__':
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	head.next.next.next.next = ListNode(5)

	x = removeNthFromEnd(head,1)
	while x is not None:
		print x.val
		x = x.next