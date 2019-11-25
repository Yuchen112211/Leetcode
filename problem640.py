'''

640. Solve the Equation
Medium

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:

Input: "x+5-3+x=6+x-2"
Output: "x=2"

Example 2:

Input: "x=x"
Output: "Infinite solutions"

Example 3:

Input: "2x=x"
Output: "x=0"

Example 4:

Input: "2x+3x-6x=x+2"
Output: "x=-1"

Example 5:

Input: "x=x+2"
Output: "No solution"

Solution:
The only fun part of this problem is to replace '-' to '+-', then we can parse the string by simply split it by '+'.
Determine 1 and -1 is tricky and bothering.

'''
class Solution(object):
    def solveEquation(self, equation):
        equation = equation.replace('-', '+-')
        leftPoly, rightPoly = equation.split('=')
        
        leftPolyParams = leftPoly.split('+')
        currentX = 0
        currentConst = 0
        for i in leftPolyParams:
            if i == '':
                continue
            if i[-1] == 'x':
                if i[:len(i)-1] == '':
                    currentX += 1
                elif i[:len(i)-1] == '-':
                    currentX -= 1
                else:
                    currentX += int(i[:len(i)-1])
            else:
                currentConst += int(i)
        rightPolyParams = rightPoly.split('+')

        for i in rightPolyParams:
            if i == '':
                continue
            if i[-1] =='x':
                if i[:len(i)-1] == '':
                    currentX -= 1
                elif i[:len(i)-1] == '-':
                    currentX += 1
                else:
                    currentX -= int(i[:len(i)-1])
            else:
                currentConst -= int(i)
        if currentX == 0 and currentConst == 0:
            return "Infinite solutions"
        elif currentX == 0:
            return "No solution"
        value = (-1) * (currentConst / currentX)
        return "x=" + str(value)
                
s = Solution()
equation = "-x=x+2"
print s.solveEquation(equation)