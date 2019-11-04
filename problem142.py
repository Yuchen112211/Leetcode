class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        visited = {}
        p = head
        while(p):
            if visited.get(p) != None:
                return p
            else:
                visited[p] = True
            p = p.next
        return None

if __name__ == '__main__':
    s = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print s.detectCycle(head)