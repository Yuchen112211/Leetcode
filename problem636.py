'''

636. Exclusive Time of Functions
Medium

On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

We store logs in timestamp order that describe when a function is entered or exited.

Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the function with id 1 ended at the end of timestamp 2.

A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any recursive calls to child functions.

The CPU is single threaded which means that only one function is being executed at a given time unit.

Return the exclusive time of each function, sorted by their function id.
Input:

n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3, 4]

Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 1 starts at the beginning of time 2, executes 4 units of time and ends at time 5.
Function 0 is running again at the beginning of time 6, and also ends at the end of time 6, thus executing for 1 unit of time. 
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.

Solution:
Use stack to solve the problem. Every time we encounter a log that is start of a thread, push it into the stack.
Since the CPU is single-threaded in this problem, everytime we encounter a end log, it should be paired up with the last element in
the stack.

Here's the trick part, for every pair of the logs, after we compute the time, if the stack is not empty, which means there's a task
has been waiting for the current task to finish, so we need to substract the last log by the current time.

Why this works? For every substract, after we updated the rst, the time in the stack is not modified. After several substraction, the result
of some logs may be negative, but in the pair up the time length would make up the time that was taken by other tasks.

'''
class Solution(object):
    def exclusiveTime(self, n, logs):
        stack = []
        result = [0] * n
        
        for log in logs:
            idx,tag,time = log.split(":")
            
            if tag == "start":
                stack.append([idx, time])
            elif tag == "end" and idx == stack[-1][0]:
                _, startTime = stack.pop()
                timeTaken = int(time) - int(startTime) + 1
                result[int(idx)] += timeTaken
                if stack:
                    result[int(stack[-1][0])] -= timeTaken
                    
        return result

s = Solution()
n = 8
logs = ["0:start:0","1:start:5","2:start:6","3:start:9","4:start:11","5:start:12","6:start:14","7:start:15","1:start:24","1:end:29","7:end:34","6:end:37","5:end:39","4:end:40","3:end:45","0:start:49","0:end:54","5:start:55","5:end:59","4:start:63","4:end:66","2:start:69","2:end:70","2:start:74","6:start:78","0:start:79","0:end:80","6:end:85","1:start:89","1:end:93","2:end:96","2:end:100","1:end:102","2:start:105","2:end:109","0:end:114"]



print s.exclusiveTime(n, logs)