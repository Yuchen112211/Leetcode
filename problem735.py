'''

735. Asteroid Collision
Medium

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example 2:

Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.

Example 3:

Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.

Example 4:

Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.

Solution:
Every stone is going left or right, and the position in the list indicates the original places of the stones.
Use stack to solve this problem.

Start from the beginning, if ever encounter a stone that has positive value, push it into the stack to be paired up in the future.
If encounter a negative stone, pop out the tail of the stack, we have several situations:
1. Popped out stone has bigger absolute value.
We push the stone back into the stack and continue/
2. Popped out stone has smaller absolute value.
This means that the stone will be crashed, until we find a stone that is heading right and with a bigger absolute value, we keep popping 
out the stack.
3. Popped out stone has the same absolute value.
Go to the next stone, don't do anything, because the two stones are crashed together.

'''
class Solution(object):
	def asteroidCollision(self, asteroids):
		"""
		:type asteroids: List[int]
		:rtype: List[int]
		"""
		if len(asteroids) <= 1:
			return asteroids
		from collections import deque
		stack = deque([])

		rst = []
		for i in range(len(asteroids)):
			if asteroids[i] >= 0:
				stack.append(asteroids[i])
			if asteroids[i] < 0:
				while True:
					if not stack:
						rst.append(asteroids[i])
						break
					else:
						before = stack.pop()
						if before > abs(asteroids[i]):
							stack.append(before)
							break
						elif before < abs(asteroids[i]):
							continue
						elif before == abs(asteroids[i]):
							break
		rst += stack
		return rst

asteroids = []
s = Solution()
print s.asteroidCollision(asteroids)