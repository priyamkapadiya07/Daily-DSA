# Best time to buy and Sell stock

arr =  [4, 2]

ans=0 
for i in range(1,len(arr)):
    if arr[i]>arr[i-1]:
        ans+=arr[i]-arr[i-1]
print(ans)