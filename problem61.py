
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        import collections
        arr = []
        if head is None:
            return None
        while head is not None:
            arr.append(head.val)
            head = head.next
        turns = k%len(arr)
        arr_d = collections.deque(arr)
        arr_d.rotate(turns)
        rst = ListNode(arr_d[0])
        rst_return = rst
        for i in range(1,len(arr)):
            rst.next = ListNode(arr_d[i])
            rst = rst.next
        return rst_return

if __name__ == '__main__':
    s = Solution()
    head = ListNode(0)
    x = head
    for i in range(1,3):
        head.next = ListNode(i)
        head = head.next
    print s.reverseKGroup(x,4)