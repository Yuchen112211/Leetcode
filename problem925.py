'''

925. Long Pressed Name
Easy

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Solution:
Go over the name and typed, jump the characters at leat the times that appears in name.
Actually ez, maintain two pointers.

'''
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


