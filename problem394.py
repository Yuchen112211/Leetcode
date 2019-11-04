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