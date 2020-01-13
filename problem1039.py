'''

1039. Minimum Score Triangulation of Polygon
Medium

Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.

Suppose you triangulate the polygon into N-2 triangles.  For each triangle, the value of that triangle is the product of the labels of the vertices, and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

 

Example 1:

Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

Example 2:

Input: [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.

Example 3:

Input: [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.

Solution:
DP solution. I find this relatively hard.
For every triangle in the polygon, the middle point of the triangle can not be used again, which means
there must be no edge that comes out of the middle point and connect to the outer nodes of left and right 
nodes edge.

So for every start point and the end point, its score would be the minimum score that can be achieved by
selecting middle point. The score equals to dp[i][k] + dp[k][j] + product of i,k,j.
dp[i][k] means that after connect i and k, there are still some points that might exist between i and k, and
the score of i and k is the minimum score that can be achieved by selecting triangles between i and k.
Same for dp[k][j].

The result is dp[0][-1], which is the minimum score that can be achieved with first point and the last point.

It's seems simple and straightforward, but I am sure that I can not come up with the solution during interview.
'''

class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [[0]*n for i in xrange(n)]
        for l in xrange(2, n):
            for left in xrange(0, n - l):
                right = left + l
                dp[left][right] = float("inf")
                for k in xrange(left + 1, right):
                    dp[left][right] = min(dp[left][right], dp[left][k] + dp[k][right] + A[left]*A[right]*A[k])
        return dp[0][-1]
