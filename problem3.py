'''
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


Solution:
My original solution is brute force with set usage. Not efficient but solved the problem.

The efficient algorithm use list's function find. When there's no target in the list, the find
function would return -1.
We first initialize the curlen to be 0, in the iteration, the s[i-curlen:i] is the length of 
string with distinct characters with the before element.

So, s[i-curlen:i] is the max length of the string with non-repeated characters
Then we call the find function, s[i-curlen:i].find(num), which means that find the same character
in the previous string. If not found, the function would return -1, if not, it will return the
relative position(The first element is 0, second is 1, ignore the original index). 

So the curlen[i] - s[i-curlen:i].find(num) which means the current string length with non-repeated characters,
because it is the previous length minus the position where the same character appeared.

Then make the maxlen to be the bigger one in the two lenth.

'''

def lengthOfLongestSubstring_efficient(s):
	curlen = maxlen = 0
	for i,num in enumerate(s):
		print curlen,i,num
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

if __name__ == '__main__':
	s = "abcabcbb"
	print lengthOfLongestSubstring_efficient(s)