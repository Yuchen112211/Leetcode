'''
23. Merge k Sorted Lists
Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

Solution:
The trick here is divide and conqure.
Since we can not increase the merge of two linked list, we can observe the task and divide them
into subtask.
The deduction here is T(n) = 2T(n/2) + O(n)

T(n/2) means we first merge half of the lists with the same function, we do them twice, then we'll
have 2 linked lists, we merge them together, problem solved.

'''

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def mergeNodes(self, Node1, Node2):
        rst = None
        
        if not Node1 and not Node2:
            return None
        elif not Node1:
            return Node2
        elif not Node2:
            return Node1

        if Node1.val < Node2.val:
            rst = ListNode(Node1.val)
            Node1 = Node1.next
        else:
            rst = ListNode(Node2.val)
            Node2 = Node2.next
        curr = None
        prev = rst
        while Node1 and Node2:
            if Node1.val < Node2.val:
                curr = ListNode(Node1.val)
                Node1 = Node1.next
            else:
                curr = ListNode(Node2.val)
                Node2 = Node2.next
            prev.next = curr
            prev = prev.next
            curr = curr.next
        if Node1:
            prev.next = Node1
        elif Node2:
            prev.next = Node2
        return rst

    def mergeKLists(self, lists):  
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeNodes(lists[0],lists[1])

        else:
            left = self.mergeKLists(lists[:len(lists)/2])
            right = self.mergeKLists(lists[len(lists)/2:])
            return self.mergeNodes(left, right)


if __name__ == "__main__":
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(4)

    node2 = ListNode(2)
    node2.next = ListNode(5)

    node3 = ListNode(3)
    node3.next = ListNode(3)
    node3.next.next = ListNode(4)

    rst = Solution().mergeKLists([node1,node2,node3])

    while rst:
        print rst.val
        rst = rst.next