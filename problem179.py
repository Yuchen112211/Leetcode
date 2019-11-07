'''
179. Largest Number
Medium

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

Solution:
Transform every data into String format, then sort it, which would make the list form the biggest number.

Write a lambda function to perform such sort.
if x+y < y+x we determine that x would become less than x would become the previous one.

Would need functools.cmp_to_key
Just memorize this.
'''

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def tupleSort(t):
            return t[1]
        if len(nums) == 1:
            return str(nums[0])
        if set(nums) == set([0]):
            return '0'
        strs = [str(i) for i in nums]
        strs = sorted(strs)
        to_do = []
        rst = ''
        while strs:
            to_do = []
            first_chr = strs[-1][0]
            while strs and strs[-1][0] == first_chr:
                to_do.append(strs.pop())
            if len(to_do) == 1:
                rst += to_do[0]
            else:
                longest = max([len(i) for i in to_do])
                to_do1 = [(i,to_do[i]+(longest-len(to_do[i]))*first_chr) for i in range(len(to_do))]
                to_do1 = sorted(to_do1,key=tupleSort)
                while to_do1:
                    rst += to_do[to_do1.pop()[0]]
        return rst
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        def func(x, y):
            if x+y < y+x:return 1
            if x+y > y+x:return -1
            return 0
        nums = sorted([str(x) for x in nums], key=cmp_to_key(func))
        return "".join(nums).lstrip('0') or '0'
'''

if __name__ == '__main__':
    s = Solution()
    case = [9051,5526,2264,5041,1630,5906,6787,8382,4662,4532,6804,4710,4542,2116,7219,8701,8308,957,8775,4822,396,8995,8597,2304,8902,830,8591,5828,9642,7100,3976,5565,5490,1613,5731,8052,8985,2623,6325,3723,5224,8274,4787,6310,3393,78,3288,7584,7440,5752,351,4555,7265,9959,3866,9854,2709,5817,7272,43,1014,7527,3946,4289,1272,5213,710,1603,2436,8823,5228,2581,771,3700,2109,5638,3402,3910,871,5441,6861,9556,1089,4088,2788,9632,6822,6145,5137,236,683,2869,9525,8161,8374,2439,6028,7813,6406,7519]
    #case = [830,8308]
    print s.largestNumber(case)
'''
"995998549642963295795569525905189958985890288238775871870185978591838283748308308827481618052787813771758475277519744072727265721971071006861683682268046787640663256310614560285906582858175752573156385565552654905441522852245213513750414822478747104662455545424532434289408839763963946391038663723370035134023393328828692788270926232581243924362362304226421162109163016131603127210891014"
"995998549642963295795569525905189958985890288238775871870185978591838283748308830827481618052787813771758475277519744072727265721971071006861683682268046787640663256310614560285906582858175752573156385565552654905441522852245213513750414822478747104662455545424532434289408839763963946391038663723370035134023393328828692788270926232581243924362362304226421162109163016131603127210891014"
'''