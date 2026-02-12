class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        numsmax = [-s for s in nums]
        heapq.heapify(numsmax)

        val1 = (heapq.heappop(numsmax) +1) * (heapq.heappop(numsmax) +1)
        return val1
