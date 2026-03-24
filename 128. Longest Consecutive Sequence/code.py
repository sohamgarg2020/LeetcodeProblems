class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        start = []
        for i in nums:
            if i-1 in nums:
                continue
            else:
                start.append(i)
        maxc = 1
        for i in start:
            count = 1
            j = i+1
            while j in nums:
                count += 1
                j+=1
            if maxc < count:
                maxc = count
        return maxc
