# по времени: O(k * n) 
# по памяти: O(n)
def solver(prices, k):
    if not prices:
        return 0
    if k > len(prices) / 2:
        return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))
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
          
            
