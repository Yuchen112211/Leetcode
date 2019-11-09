'''

947. Most Stones Removed with Same Row or Column
Medium

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Example 3:

Input: stones = [[0,0]]
Output: 0

Solution:
The description of the problem is confusing, but I figured it out finally with discuss page.
A move means on the same row of column, if the number of stones are more than 1, we can take 1
stone away.

This means that nodes who are "Connected" can be removed recursively until there's only one
stone is left, this would give the move count (number of nodes in one union) - 1(the union number);

Thus, the total number of move = the number of stones - the number of unions.

Now, how can we form unions in this question?
As defined, the union of this case is formed by the nodes with same rows and cols, and this is not 
"So strict". Any node has either same column of row as any node in a union, this node belongs to such
union as well.

After a traversal of the nodes, another loop to find the number of unions, we can calculate
the answer (number of nodes) - (number of unions);

'''
     
class Solution(object):
    def removeStones(self, stones):
        import collections
        if not stones:
            return 0

        numOfIslands = 0
        visited = set()

        points = {(i, j) for i, j in stones}
        row = collections.defaultdict(list)
        col = collections.defaultdict(list)
        for i, j in stones:
            row[i].append(j)
            col[j].append(i)

        for i, j in stones:
            if (i, j) in points:
                self.dfs(i, j, points, row, col)
                numOfIslands += 1

        return len(stones) - numOfIslands

    def dfs(self, x, y, points, row, col):

        points.discard((x, y))
        row[x].remove(y)
        col[y].remove(x)

        for j in row[x]:
            if (x, j) in points:
                self.dfs(x, j, points, row, col)

        for i in col[y]:
            if(i, y) in points:
                self.dfs(i, y, points, row, col)
