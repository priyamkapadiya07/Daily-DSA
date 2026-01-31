'''
Maximum profit by buying and selling a share at most twice
'''

def maxProfit(prices, k):
    n = len(prices)
    if n == 0:
        return 0

    dp = [[0] * (k + 1) for _ in range(n)]

    for t in range(1, k + 1):
        maxDiff = -prices[0]
        for d in range(1, n):
            dp[d][t] = max(dp[d - 1][t], prices[d] + maxDiff)
            maxDiff = max(maxDiff, dp[d][t - 1] - prices[d])

    return dp[n - 1][k]

prices = list(map(int, input("Enter the stock prices separated by spaces: ").split()))
k = int(input("Enter the maximum number of transactions allowed (k): "))
result = maxProfit(prices, k)
print("Maximum profit with at most two transactions:", result)