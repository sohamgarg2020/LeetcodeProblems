class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        for idx, val in enumerate(score):
            heapq.heappush(heap, (-val, idx))

        cur = [0]*len(score)
        place = 1
        while heap:
            val = heapq.heappop(heap)[1]
            if place == 1:
                cur[val] = "Gold Medal"
            elif place == 2:
                cur[val] = "Silver Medal"
            elif place == 3:
                cur[val] = "Bronze Medal"
            else:
                cur[val] = str(place)
            place += 1
        return cur


