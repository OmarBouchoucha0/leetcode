class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        i = 0
        j = len(prices) - 1
        while i < j:
            if prices[j] - prices[i] > output:
                output = prices[j] - prices[i]
            if prices[j] < prices[i]:
                i += 1
            else:
                j -= 1
        return output
