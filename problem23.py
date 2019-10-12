class ListNode(object):
    """docstring for ClassName"""
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def mergeNodes(self, Node1, Node2):
        rst = None
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
        lists_now = []
        for i in range(len(lists)/2):
            tmp = self.mergeNodes(lists[2*i],lists[2*i+1])
            lists_now.append(tmp)
        if len(lists) % 2 == 1:
            lists_now.append(lists[-1])

        if len(lists_now) == 1:
            return lists_now
        else:
            return self.mergeKLists(lists_now)
        

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

    rst = Solution().mergeKLists([node1,node2,node3])[0]

    while rst:
        print rst.val
        rst = rst.next