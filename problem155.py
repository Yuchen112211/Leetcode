'''

55. Min Stack
Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

Solution:
Use two stack, one for normal stack to perform top operation, one for min stack to perform min operation.

For each push, we define if the current value is bigger than the last member of min stack. Since it is stack, before pop out the 
smaller value it will definitely pop out the bigger value, so we only need to store the min value in the min stack.

In pop operation, determine if the current last member of the normal stack is the same as the last member of min stack, if so, pop the 
min stack as well.

'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack= []
        self.min_stack=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min_stack or self.min_stack[-1]>=x:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: None
        """

        deleteValue=self.stack.pop()
        if deleteValue == self.min_stack[-1]:
            self.min_stack.pop()
        return deleteValue
        

    def top(self):
        """
        :rtype: int
        """
        # if self.stack:
        #     return self.stack[-1]
        # else:
        # return None
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
    