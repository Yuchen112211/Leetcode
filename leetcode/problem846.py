class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) < W*3:
        	return False
       	hand = sorted(hand)
       	while hand:
       		tmp = hand[0]
       		for k in range(W):
       			if tmp+k not in hand:
       				return False
       			else:
       				hand.remove(tmp+k)
       	return True

if __name__ == '__main__':
	s = Solution()
	hand = [1,2,3,6,2,3,4,7,8]
	w = 3
	print s.isNStraightHand(hand,w)