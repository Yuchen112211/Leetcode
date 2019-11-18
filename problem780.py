'''

780. Reaching Points
Hard

A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Solution:
Reverse thinking. Instead of computing sx and sy, we can compute the tx and ty but 
subtract to each other.

Simply different angles of observing the question can bring us the easier solution.

There are only two kinds of operations, x,y -> x+y,y or x,y -> x,x+y, so at the end 
result, we can transform them into x,y -> x-y,y or x,y -> x,y-x, in this case, we do not 
have too many cases to verify, since all of them should follow the procedure.

'''

'''
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        def solve(tx,ty):    
            if tx<sx or ty<sy: return False
            if tx==sx: return True if  (ty-sy)%sx==0 else False
            if ty==sy: return True if (tx-sx)%sy ==0 else False
            return solve(tx-ty,ty)|solve(tx,ty-tx)
        return solve(tx,ty)
'''
class Solution(object):
	def reachingPoints(self, sx, sy, tx, ty):
		if sx == tx and sy == ty:
			return True
		if tx == 0 or ty == 0:
			return False
		if tx == sx:
			if (ty-sy) % sx == 0 or ty % sx == 0:
				return True
		if ty == sy:
			if (tx-sx) % sy == 0 or tx % sy == 0:
				return True
		if tx > ty:
			return self.reachingPoints(sx,sy,tx-ty,ty)
		else:
			return self.reachingPoints(sx,sy,tx,ty-tx)
		return True

if __name__ == '__main__':
	s = Solution()
	print s.reachingPoints(1,2,1000000000000,2)