'''

1029. Two City Scheduling
Easy

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Solution:
Sort the original array by x[0] - x[1], which indicates that the bigger the substract value of x[1] - x[0], the element would be 
more behind in this array, and in the meantime, the bigger the x[0], it would be more ahead of the array.

Somehow a greedy approach.

'''
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        newCost = sorted(costs, key=lambda x:x[0] - x[1])
        rst = 0
        length = len(costs) / 2
        for i in range(length):
            rst += newCost[i][0]
        for i in range(length, len(costs)):
            rst += newCost[i][1]
        return rst