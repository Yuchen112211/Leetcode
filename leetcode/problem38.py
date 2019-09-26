class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            tmp_str = self.countAndSay(n-1)
            cnt = 0
            current_char = ''
            rst = ''
            for i in tmp_str:
                if current_char != i:
                    if cnt != 0:
                        rst += str(cnt)
                        rst += current_char
                    current_char = i
                    cnt = 1
                else:
                    cnt += 1
            rst += str(cnt)
            rst += current_char
            return rst

if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(5)