# Best time to buy and Sell stock



def stockBuySell(arr):
    ans=0
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            ans+=arr[i]-arr[i-1]
    return ans

arr =  [4, 2]
print(stockBuySell(arr))