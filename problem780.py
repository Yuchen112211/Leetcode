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