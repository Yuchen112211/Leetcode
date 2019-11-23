'''

838. Push Dominoes
Medium

There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Solution:
Brute force would TLE, that makes sense.
My solution is record the appearance of R's index.

If current Character is L:
1. There's no R before this L that can be pair up.
We simply add the length of index i - len(rst) of character 'L' into rst.
There's no R before this L to pair up, so everything between the last index and current
index are character L.
2. There is a R before this L that can be pair up.
This is essential, since we need to determine the ending point of the fall. Read the code,
you'll get it.
Then we need to set the pointer R to be not exist, so that the followed pair would not
be confused. This indicates that this R has been used to be paired up.

If current Character is R:
1. There's no R before.
Great, all domino would not be pushed, since the dominoes on the right of an R would never 
be pushed. Add the length of i - len(rst) number of character R to the rst.
2. There is a R before.
Since this R has never been paired up with a L, everything between the before R and current R
would be pushed by the before R. We add the length number of R to the rst.
We do not set the pointer to be -1, because we might use this R later.

At the end, we check if there is a R that has not been paired up. If so, set all the rest characters
to be 'R', if not, set them to '.'.

'''
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        if len(dominoes) <= 1:
            return dominoes
        right = -1
        rst = ''
        for i in range(len(dominoes)):
            if dominoes[i] == 'L':
                if right == -1:
                    rst += (i - len(rst) + 1) * 'L'
                else:
                    length = i - right - 1
                    rst += (length / 2) * 'R'
                    rst += (length % 2) * '.'
                    rst += (length / 2 + 1) * 'L'
                    right = -1
            if dominoes[i] == 'R':
                if right != -1:
                    rst += (i - len(rst)) * 'R'
                else:
                    rst += (i - len(rst)) * '.'
                rst += 'R'
                right = i
        if right == -1:
            rst += (len(dominoes) - len(rst)) * '.'
        else:
            rst += (len(dominoes) - len(rst)) * 'R'
        return rst

s = Solution()
dominoes = "R....R..L..R"
print s.pushDominoes(dominoes)
