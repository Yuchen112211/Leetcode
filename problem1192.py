class Solution(object):
	def criticalConnections(self, n, connections):
		"""
		:type n: int
		:type connections: List[List[int]]
		:rtype: List[List[int]]
		"""
		import collections
		self.cur = 0
		low = [None for i in range(n)]
		dfn = [None for i in range(n)]
		graph = collections.defaultdict(list)
		for i,k in connections:
			graph[i].append(k)
			graph[k].append(i)

		def dfs(node, parent):
			if dfn[node] == None:
				dfn[node] = self.cur
				low[node] = self.cur
				self.cur += 1

				for nextNode in graph[node]:
					if dfn[nextNode] == None:
						dfs(nextNode, node)
				if parent != None:
					lowValue = min([low[i] for i in graph[node] if i != parent] + [low[node]])
				else:
					lowValue = min([low[i] for i in graph[node]] + [low[node]])
				low[node] = lowValue
		dfs(0, None)
		res = []
		for v in connections:
			if low[v[0]]>dfn[v[1]] or low[v[1]]>dfn[v[0]]:
				res.append(v)
		return res

		

s = Solution()

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

print s.criticalConnections(n, connections)