class Solution(object):
	def calculateMinimumHP(self, dungeon):
		last_move = [[0 for i in dungeon[0]] for k in dungeon]
		cost = [[0 for i in dungeon[0]] for k in dungeon]
		for i_1 in range(1,len(dungeon)+1):
			i = len(dungeon)-i_1
			for k_1 in range(1,len(dungeon[0])+1):
				k = len(dungeon[0])-k_1
				if k == len(dungeon[0])-1:
					if i == len(dungeon)-1:
						if dungeon[i][k] < 0:
							cost[i][k] = 1 - dungeon[i][k]
						else:
							cost[i][k] = 1
					else:
						current_num = cost[i+1][k] - dungeon[i][k]
						if current_num <= 0:
							current_num = 1
						cost[i][k] = current_num
				elif i == len(dungeon) - 1:
					current_num = cost[i][k+1] - dungeon[i][k]
					if current_num <= 0:
						current_num = 1
					cost[i][k] = current_num
				else:
					pre_determine = min(cost[i][k+1],cost[i+1][k])
					current_num = pre_determine - dungeon[i][k]
					if current_num <= 0:
						current_num = 1
					cost[i][k] = current_num
		return cost[0][0]

		
if __name__ == '__main__':
	s = Solution()
	dungeon = [[0,0,0],[1,1,-1]]

	print s.calculateMinimumHP(dungeon)