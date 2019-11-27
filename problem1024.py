'''

1024. Video Stitching
Medium

You are given a series of video clips from a sporting event that lasted T seconds.  These video clips can be overlapping with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].  We can cut these clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event ([0, T]).  If the task is impossible, return -1.

 

Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation: 
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].

Example 2:

Input: clips = [[0,1],[1,2]], T = 5
Output: -1
Explanation: 
We can't cover [0,5] with only [0,1] and [0,2].

Example 3:

Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
Output: 3
Explanation: 
We can take clips [0,4], [4,7], and [6,9].

Example 4:

Input: clips = [[0,4],[2,8]], T = 5
Output: 2
Explanation: 
Notice you can have extra video after the event ends.


Solution:
Maintain a value temp, which records the previous position that we have cut out.
The initial valud of temp is 0, since there is no video has been cut/copied before. For each iteration, check whether the current element has 
a smaller left boarder than the temp value, if so, record the right boarder.
Once we find that the left boarder is bigger than tmp, that means we have gone through the clips that we should cut to make longer video, so 
we now update the temp to be the recorded right boarders' biggest value, and add one to the count of clips.

Actually a greedy method, each time we go as far as we can and not exceeding the temp value, which should record the biggest left boarder possible.

'''
class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        result = 0
        temp = 0
        while temp < T:
            candidates = []
            for item in clips:
                if item[0] <= temp and item[1] > temp: #This line is why the function works.
                #We have to determine the left boarder is smaller than temp, which would cover the left boarder.
                #And next we select the max value of right boarder, which would extend our right boarder.
                    candidates.append(item[1])
            if not len(candidates) and temp < T:
                return -1
            else:
                temp = max(candidates)
            result += 1

        return result

s = Solution()
print s.videoStitching(clips, T)