class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = []
        index = 0
        for i in range(len(s)):
            if s[i] == s[index]:
                continue
            else:
                groups.append(i - index)
                index = i
        if index < len(s):
            groups.append(len(s) - index)
        cnt = 0
        for i in range(len(groups) - 1):
            cnt += min(groups[i], groups[i+1])

        return cnt

sol = Solution()
s = "10101"
print sol.countBinarySubstrings(s)
