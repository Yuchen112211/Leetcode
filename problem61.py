'''

61. Rotate List
Medium

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

Solution:
Any kind of solution would involve find out the length of the linked list, after found out
the length of the linked list, the remaining is very simple.

'''
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