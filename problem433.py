class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        from collections import defaultdict
        startPoint = 0
        matrix = []
        if start in bank:
            startPoint = bank.index(start)
            matrix = [[0 for k in range(len(bank))] for i in range(len(bank))]
        else:
            bank = [start] + bank
            matrix = [[0 for k in range(len(bank))] for i in range(len(bank))]

        for i in range(len(bank)):
            for k in range(i+1,len(bank)):
                cnt = 0
                for index in range(8):
                    if bank[i][index] != bank[k][index]:
                        cnt += 1
                if cnt <= 1:
                    matrix[i][k] = cnt
                    matrix[k][i] = cnt
        visited = set([startPoint])
        distance = {startPoint:0}
        stack = [startPoint]
        
        while stack:
            nextStack = []
            while stack:
                node = stack.pop()
                for i in range(len(matrix)):
                    if matrix[node][i] == 1:
                        if not i in visited:
                            visited.add(i)
                            distance[i] = distance[node] + 1
                            nextStack.append(i)
            
            stack = nextStack
        for i in distance:
            if bank[i] == end:
                return distance[i]
        minDistance = float('inf')
        index = bank.index(end)
        if index not in distance:
            return -1
        else:
            return distance[index]

s = Solution()
start = "AAAAAAAA"
end = "CCCCCCCC"
bank = ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]
print s.minMutation(start, end, bank)