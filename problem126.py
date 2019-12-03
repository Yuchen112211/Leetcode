class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not endWord in wordList:
            return []
        if not wordList:
            return []
        
        from collections import defaultdict
        neightbors = defaultdict(list)
        wordLength = len(wordList[0])
        for word in wordList:
            for index in range(wordLength):
                formats = word[:index] + '_' + word[index+1:]
                neightbors[formats].append(word)
        self.visited = set([])

        stack = [[beginWord],[endWord]]
        ans = []
        while stack:
            nextStack = []
            while stack:
                beforePath = stack.pop()
                previousWord = beforePath[-1]
                for index in range(wordLength):
                    formats = previousWord[:index] + '_' + previousWord[index+1:]
                    for nextWord in neightbors[formats]:
                        if nextWord in beforePath:
                            continue
                        if nextWord == endWord:
                            tmpRst = beforePath + [nextWord]
                            if tmpRst not in ans:
                                ans.append(tmpRst)
                        elif nextWord == beginWord:
                            tmpRst = (beforePath + [nextWord])[::-1]
                            if tmpRst not in ans:
                                ans.append(tmpRst)
                        else:
                            nextStack.append(beforePath + [nextWord])
            if ans == []:
                stack = nextStack
            else:
                break

        return ans
s = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print s.findLadders(beginWord, endWord, wordList)