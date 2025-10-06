def maxProfit(prices: List[int]) -> int:
    profits = 0
    if len(prices) == 1:
        return profits
    buy = prices[0]
    for i in range(1,len(prices)):
        sell = prices[i]
        if sell - buy > profits:
            profits = sell - buy
        if sell < buy:
            buy = sell
    return profits



