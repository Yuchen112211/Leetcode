'''

82. Remove Duplicates from Sorted List II
Medium

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:

Input: 1->1->1->2->3
Output: 2->3

Solution:
My own solution is very slow, I would put all the nodes into a list, remove all duplicate,
then reform the linked list.

The other is use the set, and go over the head node twice, which is not that smart either.

The trick of the second approach is maintain a set.
'''
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
'''
class Solution(object):
    def deleteDuplicates(self, head):
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
        arr_cnt = [arr.count(i) for i in arr]
        rst = []
        for i in range(len(arr)):
            if arr_cnt[i] > 1:
                continue
            else:
                rst.append(arr[i])
        rst.sort()
        rst1 = ListNode(rst[0])
        rst_return = rst1
        for i in range(1,len(rst)):
            rst1.next = ListNode(rst[i])
            rst1 = rst1.next
        return rst_return
'''
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode("inf")
        dummy.next = head
        dup_set = set()
        while head and head.next:
            if head.val == head.next.val:
                dup_set.add(head.val)
            head = head.next
        head = dummy
        while head and head.next:
            if head.next.val in dup_set:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next

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


    print s.deleteDuplicates(x)