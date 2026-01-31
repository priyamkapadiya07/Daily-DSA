'''
Maximum profit by buying and selling a share at most twice

Time Complexity: O(n * k)
Reason: The algorithm uses two nested loops: the outer loop iterates
over transactions `t` from 1..k and the inner loop iterates over days `d`
from 1..n. Each inner iteration performs O(1) work (a couple of assignments
and max comparisons), so the total work is proportional to n * k.

Space Complexity: O(n * (k + 1))
Reason: The DP table `dp` has dimensions n x (k+1), so it requires
O(n*(k+1)) space. Other variables use O(1) additional space.

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

