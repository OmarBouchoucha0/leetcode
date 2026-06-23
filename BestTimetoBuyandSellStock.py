class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 0:
            return 0
        buy = prices[0]
        for i in range(1, len(prices)):
            sell = prices[i]
            profit = sell - buy
            if profit > max_profit:
                max_profit = profit
            if sell < buy:
                buy = sell
        return max_profit
