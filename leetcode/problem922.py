class Solution(object):
    def swap(self,A,index1,index2):
        tmp = A[index1]
        A[index1] = A[index2]
        A[index2] = tmp

    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        index1 = 0
        index2 = 1
        while index2 < len(A):
            if index1 % 2 == A[index1] % 2:
                index1 += 1
                index2 = index1+1
            else:
                if index2 % 2 ==  A[index2] % 2:
                    index2 += 1
                elif A[index2] % 2 != A[index1] % 2:
                    self.swap(A,index1,index2)
                    index1 = index2 + 1
                    index2 = index1 + 1
                else:
                    index1 += 1
                    index2 = index1 + 1
        return A
if __name__ == '__main__':
    s = Solution()
    A = [648,831,560,986,192,424,997,829,897,843]

    print s.sortArrayByParityII(A)