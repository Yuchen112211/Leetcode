'''
399. Evaluate Division
Medium

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 


Solution:
Basic idea is same as other solutions have ponted out, i.e. model the numerator and denominator as vertices in graph and their ratio as weight of the edge, thus result would be product of the edges which makes up the path between numerator and denominator of the query

for e.g. x1/x2 = 2.0, x2/x3 = 3.0,x3/x4 = 4.0
becomes x1--2.0-->x2--3.0-->x3--4.0--x4
and thus x1/x4 becomes 24.0

This solution uses simple dfs to traverse the graph and calculate the product(if any)

Maintain a global variable self.flag to indicates that current query has result or not.
'''

class Solution(object):
	def calcEquation(self, equations, values, queries):
		import collections
		graph = collections.defaultdict(list)
		for i in range(len(equations)):
			n,m = equations[i]
			val = values[i]
			graph[n].append((m,val))
			graph[m].append((n,1/val))

		def dfs(node,target,product):
			if(node == target):
				res.append(product)
				self.flag=True
				return			
			seen.add(node)
			for nei in graph[node]:
				if(nei[0] not in seen):
					dfs(nei[0],target,product*nei[1])
						
		res=[]

		self.flag = False
		for n,m in queries:
			seen=set()
			if(n not in graph or m not in graph):
				res.append(-1.0)
			elif(n==m):
				res.append(1.0)
			else:
				dfs(n,m,1.0)
				if(not self.flag):
					res.append(-1.0)
			self.flag = False
					
		return res
s = Solution()
equations = [["a","b"],["e","f"],["b","e"],['h','z']]
values = [3.4,1.4,2.3, 2.2]
queries = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]



print s.calcEquation(equations, values, queries)