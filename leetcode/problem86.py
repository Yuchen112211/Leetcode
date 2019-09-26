class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

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

	print s.partition(head,4)