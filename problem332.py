'''

332. Reconstruct Itinerary
Medium

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

	If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
	All airports are represented by three capital letters (IATA code).
	You may assume all tickets form at least one valid itinerary.

Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
			 But it is larger in lexical order.

Solution:
This has a tricky requirement, that the traveller has to start at JFK.
Use topological sort in this, along with dfs. Or we can say that topological sort is implemented
by dfs.

Read the code again and carefully, we should get this.

'''
'''
class Solution(object):
	def findItinerary(self, tickets):
		locations = []
		for i in tickets:
			locations.append(i[0])
			locations.append(i[1])
		locations = list(set(locations))
		locations_dict = {}
		for i,location in enumerate(locations):
			locations_dict[location] = i
		for i in tickets:
			i[0] = locations_dict[i[0]]
			i[1] = locations_dict[i[1]]
		grid = [[0 for i in range(len(locations))] for i in range(len(locations))]
		for i in tickets:
			grid[i[0]][i[1]] = 1
		print tickets
		start = locations_dict['JFK']
		def rec_dfs(graph, start, visited = None):
			if visited == None:
				visited = []
			visited.append(start)
			
			for next in graph[start] - visited:
				rec_dfs(graph, next, visited)
			
			return visited 
		rec_dfs(grid,0)
'''

from collections import defaultdict,deque

class Solution(object):
	
	def _DFS(self, graph, node):
		neighbors = graph[node]
		while neighbors:
			nei = neighbors.popleft()
			self._DFS(graph, nei)
		self.itinerary.append(node)
	
	def _makeGraph(self, edges):
		graph = defaultdict(deque)
		for e in edges:
			graph[e[0]].append(e[1])
		return graph

	def findItinerary(self, tickets):
		tickets.sort(key= lambda x: x[1])
		graph = self._makeGraph(tickets)
		self.itinerary = []
		self._DFS(graph, "JFK")
		return self.itinerary[::-1]




if __name__ == '__main__':
	s = Solution()
	airlines = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
	print s.findItinerary(airlines)