'''

24. Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

Solution:
Relatively ez.

'''
class Solution:
    def swapPairs_others(self, head):
        tmp = prev = curr = ListNode(None)
        prev.next = head
        prev = prev.next
        head = curr
        
        while prev and prev.next != None:
            curr = prev.next                # Update the current node for the new pair to be swapped
            prev.next, curr.next, tmp.next = prev.next.next, prev, curr # Swap nodes and connect the current swapeed pair with last(tmp) node 
            tmp, prev = prev, prev.next     # Update the 1st and 3rd node in line
            
        head = head.next                    # Move head to the 1st node of the swapped linked list
        return head

    def swapPairs(self,head):
        if head is None:
            return None
        l = []
        while head is not None:
            l.append(head)
            head = head.next
        if len(l) == 1:
            return l[0]

        for i in range(len(l)/2):
            tmp = l[2*i]
            l[2*i] = l[2*i+1]
            l[2*i+1] = tmp
        for i in range(len(l)-1):
            l[i].next = l[i+1]
            l[i+1].next = None
        return l[0]

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s = Solution()
    print s.swapPairs(head).val