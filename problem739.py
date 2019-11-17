'''

739. Daily Temperatures
Medium

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100]. 

Solution:
Can use min heap and dictionary. Use min heap to find out the next greater number, use dictionary to get
the position of the next greater number.

Another solution is stack, which might be more flexible and optimized.

'''

class Solution(object):
    def dailyTemperatures(self, T):
        import heapq, collections
        pos = {T[-1]:len(T)-1}
        minheap = [T[-1]]
        rst = collections.deque([T[-1]])
        cnt = collections.deque([])
        for i in range(len(T)-1, -1, -1):
            pos[T[i]] = i
            while minheap:
                if minheap[0] <= T[i]:
                    heapq.heappop(minheap)
                else:
                    break
            if not minheap:
                rst.appendleft(0)
                cnt.appendleft(0)
                minheap.append(T[i])
            else:
                rst.appendleft(minheap[0])
                cnt.appendleft(pos[minheap[0]] - i)
                heapq.heappush(minheap, T[i])
                heapq.heapify(minheap)
        return cnt

'''
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
	T = [73, 74, 75, 71, 69, 72, 76, 73]
	print s.dailyTemperatures(T)