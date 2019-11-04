class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(target,path,res):
            if target < 0:
                return
            if target == 0:
                path.sort()
                if path not in res:
                    res.append(path)
            else:
                for i in candidates:
                    dfs(target - i, path + [i], res)
        
        dfs(target,[],res)
        return res

if __name__ == '__main__':
    s = Solution()
    candidates = [2,3,6,7]
    target = 7
    print s.combinationSum(candidates, target)