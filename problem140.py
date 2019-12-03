class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        trie = {}
        _end = '__end__'
        for word in wordDict:
            root = trie
            for character in word:
                root = root.setdefault(character, {})
            root[_end]  = 'end'
            
        self.ans = []

        def backtrack(string, trie, path):
            if string in wordDict:
                self.ans.append(path + ' ' + string.strip())
            if string == '':
                self.ans.append(path.strip())
            root = trie
            for index in range(len(string)):
                character = string[index]
                if character not in root:
                    return 
                root = root[character]
                if _end in root:
                    backtrack(string[index+1:], trie, path + ' ' + string[:index+1])
                    
        backtrack(s, trie, '')

        self.ans = [i.strip() for i in self.ans]
        return set(self.ans)

S = Solution()
s = "aaaaaaa"
wordDict = ["aaaa","aa", "a"]
print S.wordBreak(s,wordDict)

