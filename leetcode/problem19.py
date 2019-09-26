class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
	tmp_list = []
	while head is not None:
		tmp_list.append(head)
		head = head.next
	tmp_list = tmp_list[:len(tmp_list)-n]+tmp_list[len(tmp_list)-n+1:]
	if tmp_list == []:
		return None
	if len(tmp_list) == 1:
		tmp_list[0].next = None
		return tmp_list[0]
	head = tmp_list[0]
	for i in range(len(tmp_list)-1):
		tmp_list[i].next = tmp_list[i+1]
		tmp_list[i+1].next = None
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