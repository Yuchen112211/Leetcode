class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseBetween(self,head,m,n):
		def swap(l,i,k):
			tmp = l[i:k+1]
			tmp.reverse()
			l[i:k+1] = tmp
		rst = []
		if head is None:
			return None
		while head is not None:
			rst.append(head.val)
			head = head.next
		swap(rst,m-1,n-1)
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
	head.next.next.next = ListNode(4)
	head.next.next.next.next = ListNode(5)


	head = s.reverseBetween(head,2,4)
	while head is not None:
		print head.val
		head = head.next