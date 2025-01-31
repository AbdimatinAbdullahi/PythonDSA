def MaximumProfit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += (prices[i] - prices[i - 1])
    
    print(profit)

MaximumProfit([7,1,5,3,6,4])

