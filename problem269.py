class Solution(object):
    def alienOrder(self, words):
        import collections
        sentences = [words]
        relationship = collections.defaultdict(list)
        distinctCharacters = set([])
        for word in words:
            distinctCharacters = distinctCharacters.union(set(word))
        while sentences:
            stack = []
            for sentence in sentences:
                if len(sentence) == 1:
                    string = sentence[0]
                    for charac in string:
                        relationship[charac] = relationship[charac]

                samePrefixWord = collections.defaultdict(list)
                prefix = []
                for word in sentence:
                    prefix.append(word[0])
                    if word[1:] != '':
                        samePrefixWord[word[0]].append(word[1:])
                for i in range(len(prefix)-1):
                    for k in range(i+1,len(prefix)):
                        if prefix[i] == prefix[k]:
                            continue
                        if prefix[i] in relationship[prefix[k]]:
                            return ''
                        relationship[prefix[i]].append(prefix[k])

                for value in samePrefixWord.values():
                    stack.append(value)
            sentences = stack
        inDegree = collections.defaultdict(int)

        for key in relationship:
            value = relationship[key]
            for charac in value:
                inDegree[charac] += 1
            inDegree[key] += 0
        for charac in distinctCharacters:
            if charac not in inDegree:
                inDegree[charac] = 0

        zeroDegree = []
        for key in inDegree:
            if inDegree[key] == 0:
                zeroDegree.append(key)
        rst = ''

        while zeroDegree:
            currentNode = zeroDegree.pop(0)
            rst += currentNode
            for charac in relationship[currentNode]:
                inDegree[charac] -= 1
                if inDegree[charac] == 0:
                    zeroDegree.append(charac)
        return rst if len(rst) == len(distinctCharacters) else ''


s = Solution()
words = ['z','z']

print s.alienOrder(words)