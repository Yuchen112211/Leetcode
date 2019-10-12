def searchRange(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        elif len(nums) == 1:
            if target == nums[0]:
                return [0,0]
            else:
                return [-1,-1]
        
        left = 0
        right = len(nums) - 1
        signal = 0
        while nums[(left+right)/2] != target:
            if right - left <= 1:
                if nums[right] == target:
                    left = right
                    break
                else:
                    signal = 1
                    break
            if nums[(left+right)/2] > target:
                right = (left+right)/2
            else:
                left = (left+right)/2
        if signal == 1:
            return [-1,-1]
        mid_index = (left+right) / 2
        left,right = mid_index,mid_index
        while nums[left] == target and left > 0:
            left -= 1
        while nums[right] == target and right < len(nums) - 1:
            right += 1
        left += 1
        right -= 1
        if nums[0] == target:
            left = 0
        if nums[-1] == target:
            right = len(nums) - 1
        return [left,right]

print searchRange([5,7,7,8,8,10],8)
