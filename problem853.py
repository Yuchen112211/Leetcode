'''

853. Car Fleet
Medium

N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Solution:
Sort the zip of position and speed, compute each car's reaching time.
For each iteration, pop out the last element, compare it to the remaining tail of the time,
if the popped element is bigger, set the current tail to be the popped out element.

How this works? The sort of the zip is actually sort of position, since the latter car
can never pass ahead of the previous car, this sort would actually works as the sequence of
the car arrives.

So every time we pop out the last element in the time, we can determine whether the latter car
would come to join the fleet.

Smart.

'''

class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        print cars
        print times
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]: ans += 1  # if lead arrives sooner, it can't be caught
            else: times[-1] = lead # else, fleet arrives at later time 'lead'

        return ans + bool(times) # remaining car is fleet (if it exists)

if __name__ == '__main__':
	target = 12
	position = [10,8,0,5,3]
	speed = [2,4,1,1,3]
	s = Solution()
	s.carFleet(target, position, speed)