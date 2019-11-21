'''

839. Similar String Groups
Hard

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

Example 1:

Input: ["tars","rats","arts","star"]
Output: 2

Solution:
I think union find is super neat, however solution below reaches TLE after half the test cases.
The actuall solution on leetcode is also union find, however it would not affect the time.

class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def isSimilar(word1, word2):
            cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    cnt += 1
            if cnt == 2:
                return True
            return False
        
        graph = [set([]) for i in A]
        for i in range(len(A) - 1):
            for k in range(i, len(A)):
                if isSimilar(A[i], A[k]):
                    graph[i].add(k)
                    graph[k].add(i)
        unions = {}
        cnt = 0
        for i in range(len(graph)):
            if i not in unions:
                unions[i] = cnt
                cnt += 1
            for k in graph[i]:
                if k not in unions:
                    unions[k] = unions[i]
                elif unions[k] == unions[i]:
                    continue
                elif unions[k] != unions[i]:
                    tmp = unions[k]
                    for j in unions:
                        if unions[j] == tmp:
                            unions[j] = unions[i]

        return len(set((unions.values())))

DFS, TLE
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def isSimilar(word1, word2):
            cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    cnt += 1
            if cnt == 2:
                return True
            return False
        
        graph = [set([]) for i in A]
        for i in range(len(A) - 1):
            for k in range(i, len(A)):
                if isSimilar(A[i], A[k]):
                    graph[i].add(k)
                    graph[k].add(i)
        visited = set([])
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in graph[node]:
                dfs(i)
        groups = 0
        for i in range(len(graph)):
            if i not in visited:
                groups += 1
                dfs(i)
        return groups

The below DFS passed? why?
I should not form the graph ahead? That's a new angle.
'''
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        group = 0 
        visited = set()
        for string_ in A:
            if(string_ in visited): continue
            visited.add(string_)
            self.dfs(string_,A,visited)
            group += 1
        return group
            
    def dfs(self,string_,A,visited):
        for i in range(len(A)):
            if(A[i] in visited): continue
            if(self.similar(A[i],string_)):
                visited.add(A[i])
                self.dfs(A[i],A,visited)
                
    def similar(self,A,B):
        diff = 0 
        for i in range(len(B)):
            if(A[i] != B[i]):
                diff+= 1
            if (diff > 2): return False
        return True

s = Solution()
A = ["zkhnmefhyr","ykznfhehmr","mkhnyefrzh","zkhnyefrmh","zkmnhefhyr","ykznhfehmr","zkynhfehmr","mkhnhefrzy","zkhnmefryh","zkmnhfehyr"]


print s.numSimilarGroups(A)