'''
870. Advantage Shuffle
Medium

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]

Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]

 

Note:

    1 <= A.length = B.length <= 10000
    0 <= A[i] <= 10^9
    0 <= B[i] <= 10^9


Solution:
Apply the Greedy method, first sort both array, use a dict to memorize the pair
that which member in A should be pair with member in B.

Use two indexes or one index + one loop.
If current member of A(sorted) is smaller than current member of B(sorted), move the 
index to next one, and add this element to a list for future purpose. If bigger, then
this is a match, put it into dictionary for final result.

After go through every element in Sorted A, every node with a pair is stored in the 
dictionary. At the end we go through B, if the element is in dictionary, great, fill 
the list's position with the value; If not, fill the current position with the first
element in remaining list, which means there's no pair for current element.

Greedy solution.
'''
class Solution(object):
    def advantageCount(self, A, B):
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # Reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop()
                for b in B]