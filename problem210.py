class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		import copy
		sequence = []
		pre_request = {}
		for i in prerequisites:
			if i[0] in pre_request:
				pre_request[i[0]].append(i[1])
			else:
				pre_request[i[0]] = [i[1]]
		for i in range(numCourses):
			if i not in pre_request.keys():
				sequence.append(i)
		cnt = 0
		ori = copy.deepcopy(sequence)
		while cnt < numCourses:
			go = []
			for i in pre_request:
				if i in sequence:
					continue
				tmp = pre_request[i]
				if False in [(k in sequence) for k in tmp]:
					continue
				else:
					if i not in sequence:
						sequence.append(i)
						go.append(i)
			for i in go:
				pre_request.pop(i)
			if sequence == ori:
				break
			else:
				ori = copy.deepcopy(sequence)
			cnt += 1
		if len(sequence) < numCourses:
			return []
		return sequence
		
if __name__ == '__main__':
	s = Solution()
	numCourses = 3
	prerequisites =[[0,1],[0,2],[1,2]]
	print s.findOrder(numCourses,prerequisites)