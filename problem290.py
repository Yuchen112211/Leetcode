'''

290. Word Pattern
Easy

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Solution:
First determine the length of the substrings, if not equals to the pattern's length, return false;
Then simply use the built-in zip function and the set manipulation, with several comparison, return them
together(all equal)

'''

class Solution(object):
    def wordPattern(self, pattern, string):
        str_list = string.split(' ')
        if len(pattern) != len(str_list):
            return False
        return len(set(zip(pattern,str_list))) == len(set(pattern)) == len(set(str_list))

if __name__ == '__main__':
    s = Solution()
    pattern = 'abba'
    string = 'dog cat cat dog'
    print s.wordPattern(pattern,string)