class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        prev_sell, sell, buy = 0, 0, -prices[0]

        for i in range(1, n):
            prev_sell, sell, buy = sell, max(buy+prices[i], sell), max(prev_sell-prices[i], buy)
        return max(sell, buy)