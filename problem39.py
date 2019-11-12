'''

39. Combination Sum
Medium

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

Solution:
Maintain a global list, and use a dfs to add the valid answer to the global list.

Why this works? The numbers can be used multiple times, so we do not have to modify the 
candidates list, means that we do not have to maintain another list to record the changes.

Why no duplicate? Cause "if path not in res". Not clever but useful.

DFS is a good approach, should read the code carefully.

'''
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