class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        strings = str.split(' ')
        if len(strings) == 0:
            return 0
        nums = []
        i = ''
        index = 0
        if len(strings) == 1 and strings == ['']:
            return 0
        while strings[index] == '':
            index += 1
        if index >= len(strings):
            return 0
        i = strings[index]
        if i[0] == '-':
            if i[1:].isdigit():
                return max(-pow(2,31),int(i))
        else:
            if i.isdigit():
                return min(pow(2,31)+1,int(i))
        return 0

if __name__ == '__main__':
    s = Solution()
    string = ''
    print s.myAtoi(string)