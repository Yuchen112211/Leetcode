class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        base = 10 
        index = len(A) - 1
        UpNumber = 0
        while index >= 0:
            numToAdd = K % base
            realNumber = numToAdd + A[index] + UpNumber
            UpNumber = 0
            if realNumber >= 10:
                UpNumber = 1
                realNumber -= 10
            A[index] = realNumber
            K /= 10
            index -= 1

        while K != 0:
            numToAdd = K % base
            realNumber = numToAdd + UpNumber
            UpNumber = 0
            if realNumber >= 10:
                UpNumber = 1
                realNumber -= 10
            #A[index] = realNumber
            A.insert(0,realNumber)
            K /= 10
        if UpNumber > 0:
            A.insert(0, UpNumber)

        return A

s = Solution()
A = [0]
K = 1
print s.addToArrayForm(A, K)