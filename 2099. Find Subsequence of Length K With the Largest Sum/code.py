class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        cur = [(val, i) for i, val in enumerate(nums)]

        heapq.heapify(cur)

        while len(cur) > k:
            heapq.heappop(cur)

        cur.sort(key =lambda x: x[1])

        return [val for val, idx in cur]
                
        return cur
