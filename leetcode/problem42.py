class Solution(object):	
	def boarder(self,height,index):
		middle = height[index]
		left = right = index
		while height[left] <= height[left-1] and left > 0:
			left -= 1
		while right < len(height)-1:
			if height[right] <= height[right+1]:
				right += 1
			else:
				break
		return left,right,height[left:right+1]

	def compute(self,l):
		length = len(l)
		highest = min(l[0],l[-1])
		rst = 0
		for i in l[1:len(l)-1]:
			if highest-i>0:
				rst += highest-i
		return rst

	def trap(self,height):
		right = index = 1
		rst = 0
		while right < len(height):
			left_tmp,right_tmp,to_do = self.boarder(height,index)
			if right_tmp-left_tmp < 2:
				index += 1
				right = index+1
			else:
				print to_do
				rst += self.compute(to_do)
				index = right_tmp+1
				right = index+1
		return rst

if __name__ == '__main__':
	height = [5,2,1,2,1,5]
	#[0,1,0,2,1,0,1,3,2,1,2,1]
	index = 2
	s = Solution()

	print s.trap(height)