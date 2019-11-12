'''

394. Decode String
Medium

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

Solution:
This is a good practice of stack manipulation.
Any character that is not ], push it back into the stack.

When encounter a ] character, until we encounter the [, we pop out everything and record them as the
string that we need to use. After we popped out the [, we find out the previous number that should be
used to multiply the string. Simply use isdigit() method to determine the number.

Very interesting question, can be studied several times.
'''
class Solution:
    def decodeString(self, s):
        stack = []
        ans = ''       
        for i in s:
            if i != ']':
                stack.append(i)
                # print(i, stack)
            else:
                tmp = ''
                while stack and stack[-1] != '[':
                    tmp = stack.pop() + tmp
                if stack and stack[-1] == '[':
                    stack.pop()
                c = ''
                while stack and stack[-1].isdigit():
                    c = stack.pop() + c
                if c:
                    tmp = int(c) * tmp 
                else:
                    tmp = ''
                stack += list(tmp)
        return ''.join(stack)





if __name__ == '__main__':
    x = Solution()
    s = "3[a]2[bc]"
    print x.decodeString(s)