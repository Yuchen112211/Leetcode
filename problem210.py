'''

210. Course Schedule II
Medium

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

Solution:
Simple DFS.
Only have to remember that a class may have more than one prerequisites.
'''

class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		d = {}
		d = {i:0 for i in range(numCourses)}
		noPrerequisites = set((i[0],i[1]) for i in prerequisites)
		for i in prerequisites:
			d[i[0]] += 1
		rst = []
		while True:
			has_no = False
			tmp = -1
			for i in d:
				if d[i] == 0:
					d.pop(i)
					tmp = i
					rst.append(i)
					has_no = True
					break
			if not has_no:
				break
			for i in d:
				if (i,tmp) in noPrerequisites:
					d[i] -= 1
		if len(rst) == numCourses:
			return rst
		else:
			return []

		
if __name__ == '__main__':
	s = Solution()
	numCourses = 3
	prerequisites = [[1,0],[2,0]]
	print s.findOrder(numCourses,prerequisites)