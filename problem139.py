class Solution:
    def wordBreak(self, s, wordDict):
        import collections
        _end = '__end__'
        trie = {}
        for word in wordDict:
            root = trie
            for character in word:
                root = root.setdefault(character, {})
            root['end'] = _end
        self.visited = set([])
        def backtrack(s, trie):
            if s in self.visited:
                return False
            root = trie
            for i in range(len(s)):
                if s[i] not in root:
                    return False
                root = root[s[i]]
                if 'end' in root:
                    if i == len(s) - 1:
                        return True
                    else:
                        if backtrack(s[i+1:], trie):
                            return True
                        self.visited.add(s[i+1:])
            return False

        return backtrack(s,trie)

S = Solution()
s = "leetcode"
wordDict = ["leet", "code"]
print S.wordBreak(s, wordDict)

