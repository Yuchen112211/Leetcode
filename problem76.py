'''

76. Minimum Window Substring
Hard

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

Solution:
Use two pointers.
One left pointer and one right pointer, combine the two pointers can give us a substring starts 
at left, and ends in right.

Maintain the counter of t, modify the dictionary or counter while go through each combinartion of 
left and right.

If the right pointer has come to the tail of the s string, stop and return the minString.

Not fast but solvable.

'''

class Solution(object):

    def minWindow(self, s, t):
        from collections import Counter
        length_t = len(t)
        left = right = 0
        t_dict = Counter(t)
        s_dict = Counter(s)
        string_min = s
        for i in t_dict:
            if t_dict[i] > s_dict[i]:
                return ''

        while left <= len(s) - len(t):
            signal = 0
            while max(t_dict.values()) > 0:
                if right >= len(s):
                    signal = 1
                    break
                if s[right] in t:
                    t_dict[s[right]] -= 1
                right += 1
            if signal:
                return string_min
            if len(string_min) > right - left:
                string_min = s[left:right]
            if s[left] in t:
                t_dict[s[left]] += 1
            left += 1
        return string_min



if __name__ == '__main__':
    S = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print S.minWindow(s,t)