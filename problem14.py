
'''
Pretty ez, gonna skip.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        prefix = strs[0]
        for i in strs[1:]:
            index = 0
            lens = min(len(prefix),len(i))
            while index < lens:
                if prefix[index] == i[index]:
                    index += 1
                else:
                    break
            if index == 0:
                return ""
            else:
                prefix = prefix[:index]
        return prefix

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    s = Solution()
    print s.longestCommonPrefix(strs)