class Solution(object):
    def numTrees(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        arr = [0] * (n+1)
        arr[0] = 0
        arr[1] = 1
        arr[2] = 2
        for i in range(3,n+1):
            for k in range(i-1):
                left = k
                right = i-1-k
                arr[i] += arr[left] * arr[right]
        return arr[-1]
