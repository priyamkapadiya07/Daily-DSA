# Best time to buy and Sell stock

"""
Time Complexity: O(n)
Reason: We iterate through the array once from index 1 to n-1

Space Complexity: O(1)
Reason: We only use constant extra space for the ans variable, 
        regardless of input size
"""

def stockBuySell(arr):
    ans = 0
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            ans += arr[i] - arr[i - 1]
    
    return ans

arr = list(map(int, input("Enter stock prices separated by space: ").split()))
print(stockBuySell(arr))