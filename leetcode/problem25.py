
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