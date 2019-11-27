'''

828. Unique Letter String
Hard

A character is unique in string S if it occurs exactly once in it.

For example, in string S = "LETTER", the only unique characters are "L" and "R".

Let's define UNIQ(S) as the number of unique characters in string S.

For example, UNIQ("LETTER") =  2.

Given a string S with only uppercases, calculate the sum of UNIQ(substring) over all non-empty substrings of S.

If there are two or more equal substrings at different positions in S, we consider them different.

Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.

 

Example 1:

Input: "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:

Input: "ABA"
Output: 8
Explanation: The same as example 1, except uni("ABA") = 1.

Solution:

Intuition:

Let's think about how a character can be found as a unique character.

Think about string "XAXAXXAX" and focus on making the second "A" a unique character.
We can take "XA(XAXX)AX" and between "()" is our substring.
We can see here, to make the second "A" counted as a uniq character, we need to:

	insert "(" somewhere between the first and second A
	insert ")" somewhere between the second and third A

For step 1 we have "A(XA" and "AX(A", 2 possibility.
For step 2 we have "A)XXA", "AX)XA" and "AXX)A", 3 possibilities.

So there are in total 2 * 3 = 6 ways to make the second A a unique character in a substring.
In other words, there are only 6 substring, in which this A contribute 1 point as unique string.

Instead of counting all unique characters and struggling with all possible substrings,
we can count for every char in S, how many ways to be found as a unique char.
We count and sum, and it will be out answer.

Explanation:

	index[26][2] record last two occurrence index for every upper characters.
	Initialise all values in index to -1.
	Loop on string S, for every character c, update its last two occurrence index to index[c].
	Count when loop. For example, if "A" appears twice at index 3, 6, 9 seperately, we need to count:
		For the first "A": (6-3) * (3-(-1))"
		For the second "A": (9-6) * (6-3)"
		For the third "A": (N-9) * (9-6)"

Complexity:
One pass, time complexity O(N).
Space complexity O(1).

Since the problem is asking for each character's distinct subarray, the solution works.
I think this is a math problem.

Below is my dp solution, TLE but I think it is working, just not this case.
'''
class Solution(object):
	def uniqueLetterString(self, S):
		import string
		index = {}
		res = 0
		for i, c in enumerate(S):
			k, j = index.setdefault(c, [-1,-1])

			res += (i - j) * (j - k)
			index[c] = [j, i]
		for c in index:
			k, j = index[c]
			res += (len(S) - j) * (j - k)
		return res % (10**9 + 7)

'''
class Solution(object):
	def uniqueLetterString(self, S):
		"""
		:type S: str
		:rtype: int
		"""
		if not S:
			return 0

		import copy
		from collections import Counter
		initial = Counter()
		initial[S[0]] = 1
		previousCounters = [initial]
		arr = [[0 for i in S] for k in S]
		arr[0][0] = 1
		for i in range(1,len(S)):
			counterNow = copy.deepcopy(previousCounters[-1])
			counterNow[S[i]] += 1
			if counterNow[S[i]] == 1:
				arr[0][i] = arr[0][i-1] + 1
			elif counterNow[S[i]] == 2:
				arr[0][i] = arr[0][i-1] - 1
			else:
				arr[0][i] = arr[0][i-1]
			previousCounters.append(counterNow)

		for i in range(1,len(S)):
			char = S[i-1]
			for counterIndex in range(i, len(S)):
				counter = previousCounters[counterIndex]
				counter[char] -= 1
				if counter[char] == 1:
					arr[i][counterIndex] = arr[i-1][counterIndex] + 1
				elif counter[char] == 0:
					arr[i][counterIndex] = arr[i-1][counterIndex] - 1
				else:
					arr[i][counterIndex] = arr[i-1][counterIndex]
		rst = 0

		for i in arr:
			rst += sum(i)
		return rst % (pow(10,9) + 7)
'''

s = Solution()
S = "ABA"
print s.uniqueLetterString(S)