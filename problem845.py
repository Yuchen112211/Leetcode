'''

845. Longest Mountain in Array
Medium

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:

    0 <= A.length <= 10000
    0 <= A[i] <= 10000

Solution:
When I tried to use expand center, TLE, sad.

The solution below is one-pass solution, very smart and intuitive.
Start from the beginning, go over the array to find longest potential mountain. 
If the current number is smaller than the next one, increase the current index by 1, for 
this is a potential left part of a mountain. Use a while loop to find the whole left part
of the mountain.

Then we have the peak, continue the index increasing, once an element is bigger than the next
one, plus 1, again use a while loop to find the right most point that is potential part of the
mountain.

Then update the base and answer. Base means the first index of a mountain.

Two while loop is very efficient and smart. Can solve the proble in one-pass iteration.
Also the procedure can be regarded greedy however not so greedy, since one mountain can not overlap
with another mountain, so the longest mountain we have found, stays seperated.

'''
class Solution(object):
    def longestMountain(self, A):
        N = len(A)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]: #if base is a left-boundary
                #set end to the peak of this potential mountain
                while end+1 < N and A[end] < A[end+1]:
                    end += 1

                if end + 1 < N and A[end] > A[end + 1]: #if end is really a peak..
                    #set 'end' to right-boundary of mountain
                    while end+1 < N and A[end] > A[end+1]:
                        end += 1
                    #record candidate answer
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans


if __name__ == '__main__':
	s = Solution()
	A = [2,1,4,7,3,2,5]
	print s.longestMountain(A)
	