'''

Actually a boring problem.
Use recursive relationship to compute the whole count that the knight may come to specific
Once the knight come to a digit, plus the current value to the next step.

'''
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 10
        stack = [1,2,3,4,6,7,8,9,0]
        grid = [[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[4,2],[4,6]]
        
        cnt = 1
        cnt_list = [1 for i in grid]
        while cnt < N:
            tmp_list = [0 for i in grid]
            for i in range(len(tmp_list)):
                for k in range(len(grid[i])):
                    tmp_list[grid[i][k]-1] += cnt_list[i]
            cnt_list = tmp_list
            cnt += 1
            
        return sum(cnt_list) % (pow(10,9)+7)


if __name__ == '__main__':
    s = Solution()
    for i in range(1,19):
        print s.knightDialer(i)