class Solution:
    def isLongPressedName(self, name, typed ):
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                while j < len(typed) and name[i] != typed[j]:
                    j += 1
        return i == len(name)
        
if __name__ == '__main__':
    name = "leelee"
    typed = "lleeelee"
    s = Solution()
    print s.isLongPressedName(name,typed)


