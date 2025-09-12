from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        
        d = list(dict(sorted(d.items(), key =lambda x: x[1], reverse=True)).keys())
        cur = []
        for i in range(k):
            cur.append(d[i])
        return cur
         
