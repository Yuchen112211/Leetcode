'''

25. Reverse Nodes in k-Group
Hard

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.

Solution:
Put every node into a list, reverse them in groups with k length.
Or when we put the value into the list, we do the reverse ahead.

Another solution is Recursion, very efficient.
Reverse the first K node, and then call the reverseKGroup function on the current node's next
node. Point the current node to the function's return node.
Very intuitive method.

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
        arr = []
        if head is None:
            return None
        while head is not None:
            arr.append(head.val)
            head = head.next
        rst = []
        for i in range(len(arr)/k+1):
            tmp_arr = arr[i*k:(i+1)*k]
            if tmp_arr != [] and len(tmp_arr) == k:
                tmp_arr.reverse()
            rst += tmp_arr
        rst_node = ListNode(rst[0])
        result = rst_node
        for i in range(1,len(rst)):
            rst_node.next = ListNode(rst[i])
            rst_node = rst_node.next
        return result

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    x = head
    for i in range(2,10):
        head.next = ListNode(i)
        head = head.next
    print s.reverseKGroup(x,4)