'''

743. Network Delay Time
Medium

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Solution:
This is actually a dijkstra's algorithm problem.

Since we are given a single source graph and all weights are non-negative, we have to find the max value of the shortest path from
the source to each nodes.

So this can be actually solved in dijkstra algorithm, with some help of the sorting or min value finding.

Shouldn't be hard to think through.

'''
class Solution(object):
	def networkDelayTime(self, times, N, K):
		"""
		:type times: List[List[int]]
		:type N: int
		:type K: int
		:rtype: int
		"""
		#First let's construct the graph/edges
		from collections import defaultdict
		edges = defaultdict(list)
		for start,end,weight in times:
			edges[start].append((end,weight))
		#Then let's write the dijkstra's algorithm
		vertexValue = {i+1:float('inf') for i in range(N)}
		vertexValue[K] = 0
		currentNode = K
		waitToBeAdded = []
		while True:
			for target, weight in edges[currentNode]:
				if vertexValue[target] > vertexValue[currentNode] + weight:
					waitToBeAdded.append(target)
					vertexValue[target] = vertexValue[currentNode] + weight
			minNode = -1
			weightNode = float('inf')
			for node in waitToBeAdded:
				if vertexValue[node] < weightNode:
					weightNode = vertexValue[node]
					minNode = node
			if minNode == -1:
				break
			currentNode = minNode
			waitToBeAdded.remove(minNode)
		rst = max(vertexValue.values())
		return rst if rst < float('inf') else -1 

		
s = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
print s.networkDelayTime(times, N, K)