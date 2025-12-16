class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            stone1 = abs(heapq.heappop(maxheap))
            stone2 = abs(heapq.heappop(maxheap))
            if stone1 == stone2:
                continue
            else:
                heapq.heappush(maxheap, stone2-stone1)
        if len(maxheap) == 0:
            return 0
        return -maxheap[0]
