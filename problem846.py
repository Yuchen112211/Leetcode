'''

846. Hand of Straights
Medium

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.

Solution:
Since we have to make every card to be part of one group with size w, we have to form each of the element
into a group.

Simple approach is sort the list first, then start iteration.

For each iteration, we extract the first element `tmp` of the remaining cards, them find all elements that
are in the same grouop as tmp, so we find tmp+1, tmp+2....tmp+w, and we remove them.

If any of the above element is not in the remaining cards, retrun False.

Then start a new iteration, repeat the operations until the cards are empty. Return True at the end.

'''
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) < W:
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