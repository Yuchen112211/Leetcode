'''

174. Dungeon Game
Hard

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
-2 (K) 	-3 	3
-5 	-10 	1
10 	30 	-5 (P)

Solution:
DP problem.
The limit is not only cost, because any path from top left to the bottom right has the same path
length, which is width + height - 1. Not only we should memo the cost of current pos, we also need to
memo the min_value appeared before in this road.

Iterate the matrix from the bottom right of the board. Maintain a same size 2-D matrix called cost,
represents that how many health points the knight needs to get such place.

At the destination, if the point there is positive, we only need 1 point to get here; If negative, reverse
it and plus 1 to it.

Then for the following cells, we determine which direction to go by selecting the min cost. We simply add the
current cell's health point to the min value of two directions, which would give us at least how many
health points we need start from current cell to get to the destination.

This problem is a little different from standard procedure of 2-D DP problem.
We need to use the Top-down strategy rather than Bottom-up.

Worth re-think and re-write.

'''




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