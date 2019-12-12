class Solution(object):
	def scheduleCourse(self, courses):
		courses = sorted(courses, key = lambda x:(x[0],x[1]))
		currentTime = 0
		cnt = 0
		for duration, endTime in courses:
			if currentTime + duration <= endTime:
				cnt += 1
				currentTime += duration
			else:
				continue
		return cnt


S = Solution()
courses = [[100,200],[200,2400],[1000,1250],[2000,3200]]

print S.scheduleCourse(courses)