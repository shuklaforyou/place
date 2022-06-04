def max_profit(prices: list, days: int) -> int:
 
    profit = 0
 
    for i in range(1, days):
 
        # checks if elements are adjacent and in increasing order
        if prices[i] > prices[i-1]:
 
            # difference added to 'profit'
            profit += prices[i] - prices[i-1]
            print(profit)
 
    return profit
 
# Driver Code
if __name__ == '__main__':
 
    # stock prices on consecutive days
    prices = [100, 180, 260, 310, 40, 535, 695]
 
    # function call
    profit = max_profit(prices, len(prices))
    print(profit)