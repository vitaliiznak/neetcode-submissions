class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0

        days = len(prices)
        profit_max = 0

        while right < days:
            profit = prices[right] - prices[left]
            profit_max = max(profit_max, profit)
            if prices[left] < prices[right]:
                right += 1
            else:
                left = right
                right += 1
        return profit_max



















