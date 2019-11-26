class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        listA = list(A)
        listB = list(B)
        exist = {}
        rst = 0
        for i in range(len(listA)):
            if (listB[i], listA[i]) in exist:
                index = exist[(listB[i], listA[i])]
                exist.pop((listB[i], listA[i]))
                listA[i],listA[index] = listA[index], listA[i]
                rst += 1
            else:
                exist[(listA[i], listB[i])] = i
                continue
        index = 0
        while index < len(A):
            if listA[index] == listB[index]:
                index += 1
            else:
                anotherIndex = index
                for i in range(index, len(listA)):
                    if listA[i] == listB[index]:
                        anotherIndex = i
                        break
                listA[index], listA[anotherIndex] = listA[anotherIndex], listA[index]
                index += 1
                rst += 1
        return rst
s = Solution()
A = "abccaacceecdeea"
B = "bcaacceeccdeaae"
print s.kSimilarity(A,B)