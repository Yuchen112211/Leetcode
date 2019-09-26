class Solution(object):
    def dailyTemperatures(self, T):
        wait_days = [0]
        stack = [(len(T)-1,T[-1])]

        index = len(T) - 2
        while index >= 0:
        	index_tmp = 0
        	while index_tmp < len(stack):
        		if stack[index_tmp][1] <= T[index]:
        			index_tmp += 1
        		else:
        			break
        	if index_tmp == len(stack):
        		wait_days.insert(0,0)
        		stack = [(index,T[index])]
        	else:
        		wait_days.insert(0,stack[index_tmp][0] - index)
	        	stack = stack[index_tmp:]
	        	stack.insert(0,(index,T[index]))
        	index -= 1
        return wait_days

'''
class Solution:
    def dailyTemperatures(self, T):
        stack = []
        warmerMap = [0] * len(T)

        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                    popped = stack.pop()
                    warmerMap[popped] = i - popped
            stack.append(i)
        return warmerMap
'''
if __name__ == '__main__':
	s = Solution()
	T = [89,62,70,58,47,47,46,76,100,70]
	print s.dailyTemperatures(T)