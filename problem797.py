'''

797. All Paths From Source to Target
Medium

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


Solution:
Classic backtrack problem.
Since the graph is asyclic, this saves a lot of trouble.

The graph is directed, for every node we add the nodes that are connected to the node into the path, then call the helper method recursively.
If the last element of the path is the target, add the path into the result that we are going to return in the end.

For each node, we do not alter the path, we simply pass the path + [node] to the next recursion.

Or at least I think this is a backtrack problem.
'''
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        rst = []
        paths = [0]
        target = len(graph) - 1
        def walk(path):
            if path[-1] == target:
                rst.append(path)
            else:
                nextNode = path[-1]
                for i in graph[nextNode]:
                    walk(path + [i])
        walk(paths)
        return rst