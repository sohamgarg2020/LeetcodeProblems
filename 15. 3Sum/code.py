class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while right > left:
                if nums[right] + nums[left] == -nums[i]:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left+= 1
                    right -= 1
                    continue
                elif (nums[right] + nums[left]) > -nums[i]:
                    right -= 1
                    continue
                else:
                    left += 1
                    continue
        return ans
            
