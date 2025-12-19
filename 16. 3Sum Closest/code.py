class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_val = 2**31-1
        val = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                sov = nums[i] + nums[left] + nums[right]

                if sov == target:
                    return target

                elif sov < target:
                    
                    left += 1
                else:
                    right -= 1
                
                if abs(sov-target) < min_val:
                    min_val = abs(sov-target)
                    val = sov
        return val

