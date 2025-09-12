from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])
        
        for val, freq in d.items():
            buckets[freq].append(val)

        cur = []
        for i in range(len(nums), -1, -1):
            for val in buckets[i]:
                cur.append(val)
                if len(cur) == k:
                    return cur
         
