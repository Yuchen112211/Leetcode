'''

40. Combination Sum II
Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

Solution:
Classic Backtrack. Maybe now it's too late. This is 1:12 AM on 11.17.
I will rewrite this tomorrow.
Should have done this by myself.

'''

class Solution(object):
	def combinationSum2(self, candidates, target):
		def comb(A, target,r, res,start):
			if target == 0:
				if sorted(r) not in res:
					res.append(sorted(r))
			else:
				for i in range(start,len(candidates)):
					if i > start and candidates[i] == candidates[i-1]:
						continue
					if candidates[i] <= target:
						r.append(candidates[i])
						comb(candidates[i+1:],target-candidates[i],r,res,i+1)
						r.pop()
		res = []
		comb(candidates,target,[],res,0)
		return res