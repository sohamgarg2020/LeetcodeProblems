class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) != 0:
            min_val = prices[0]
            max_prof = 0
            for i in prices:
                if i < min_val:
                    min_val = i
                if i - min_val > max_prof:
                    max_prof = i-min_val
            return max_prof
        return 0
