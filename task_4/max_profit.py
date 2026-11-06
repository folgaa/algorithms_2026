# по времени: O(k * n) 
# по памяти: O(n)
def solver(prices, k):
    arr = [0] * len(prices)
    for t in range(k):
        pos = -prices[0]
        profit = 0
        for i in range(1, len(prices)):
            pos = max(pos, arr[i] - prices[i])
            profit = max(profit, pos + prices[i])
            arr[i] = profit
    return arr[-1]

def max_profit():
    prices = list(map(int, input().split()))
    k = int(input())
    return solver(prices, k)
          
            
