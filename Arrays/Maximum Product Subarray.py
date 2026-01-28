# Find maximum product subarray

arr = [-2, 6, -3, -10, 0, 2]

for i in range(len(arr)):
    pro=1
    for j in range(i, len(arr)):
        pro *= arr[j]
        arr[i]=max(arr[i], pro)
print("The maximum product subarray is:", max(arr))