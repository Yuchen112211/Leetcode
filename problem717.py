class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        index = 0
        while index < len(bits)-1:
            if bits[index] == 1:
                index += 2
            else:
                index += 1

        return index < len(bits)


if __name__ == '__main__':
    s = Solution()
    print s.isOneBitCharacter([1,1,0])