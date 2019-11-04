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