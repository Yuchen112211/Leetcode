def lengthOfLongestSubstring_efficient(s):
	curlen = maxlen = 0
	for i,num in enumerate(s):
		curlen -= s[i-curlen:i].find(num)
		maxlen = max(maxlen,curlen)
	return maxlen

def lengthOfLongestSubstring_window(s):
	window = 0
	first,second = 0,0
	while second <= len(s):
		if len(s[first:second]) == len(set(s[first:second])):
			window = max(second-first,window)
			second += 1
		else:
			second -= 1
			window = max(second-first,window)
			first += 1
	return window

	