def MaximumProfit(prices):
    buy, sell = 0, 1
    maxprofit = 0

    while sell < len(prices):
        if prices[sell] > prices[buy]:
            profit = prices[sell] - prices[buy]
            maxprofit = max(maxprofit, profit)
        else:
            buy = sell
        sell += 1
    
    print(maxprofit)

MaximumProfit([7,1,5,3,6,4])

# [7, 1, 5, 3, 6, 4]
#     b           s