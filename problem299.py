class Solution(object):
	def getHint(self, secret, guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""
		import collections
		cnt_secret = collections.Counter(secret)
		cnt_guess = collections.Counter(guess)
		Bulls,Cows = 0,0
		for i in range(len(secret)):
			if secret[i] == guess[i]:
				Bulls += 1
				cnt_secret[secret[i]] -= 1
				cnt_guess[guess[i]] -= 1
		for i in range(len(secret)):
			if guess[i] in secret and cnt_guess[guess[i]] != 0 and cnt_secret[guess[i]] != 0:
				Cows += 1
				cnt_secret[guess[i]] -= 1
				cnt_guess[guess[i]] -= 1
		return str(Bulls)+'A'+str(Cows)+'B'

if __name__ == '__main__':
	s = Solution()
	secret = '1122'
	guess = '1222'
	print s.getHint(secret,guess)