class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i] - prices[i-1], 0) for i in range(1, len(prices)))
