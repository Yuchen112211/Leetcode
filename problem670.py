class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 10:
            return num
        str_num = str(num)
        length = len(str_num)
        index = length-1
        biggest = '0'
        start = 0
        while start < length:
            if max(str_num[start:]) == str_num[start]:
                start += 1
            else:
                break
        if start == length:
            return num
        for i in range(1,length-start):
            if str_num[length-i] > biggest:
                biggest = str_num[length-i]
                index = length-i
            if biggest == '9':
                break
        if index == length-1 and str_num[index] < str_num[start]:
            return num
        rst = str_num[:start]+str_num[index]+str_num[start+1:index]+str_num[start]+str_num[index+1:]
        return int(rst)

if __name__ == '__main__':
    s = Solution()
    num = 193
    print s.maximumSwap(num)