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
		
if __name__ == '__main__':
	s = Solution()
	airlines = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
	s.findItinerary(airlines)