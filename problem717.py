'''

717. 1-bit and 2-bit Characters
Easy

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:

Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:

Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Solution:
Use simple greedy approach. If encounter 1, we skip two digit, if encounter 0, skip one.
A substring starts at 1 would indicates that this string has length of 2, if starts at 0, means that this string has length of 1.

Maybe not so greedy.

'''

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