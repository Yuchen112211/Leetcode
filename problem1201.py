class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        cnt = {a:1,b:1,c:1}
        rst = set([])
        res = 0
        while n > 0:
            currentA = a * cnt[a]
            currentB = b * cnt[b]
            currentC = c * cnt[c]
            tmp = 0
            if currentA <= currentB and currentA <= currentC:
                tmp = currentA
                cnt[a] += 1
            elif currentB < currentA and currentB <= currentC:
                tmp = currentB
                cnt[b] += 1
            elif currentC < currentA and currentC < currentB:
                tmp = currentC
                cnt[c] += 1
            if tmp in rst:
                n += 1
            else:
                res = tmp
            rst.add(tmp)
            n -= 1
        return res

s = Solution()
n = 3

a = 2

b = 3

c = 5
print s.nthUglyNumber(n,a,b,c)