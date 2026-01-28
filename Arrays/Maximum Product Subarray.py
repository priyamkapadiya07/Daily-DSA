# Find maximum product subarray

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

for i in range(len(arr)):
    pro=1
    for j in range(i, len(arr)):
        pro *= arr[j]
        arr[i]=max(arr[i], pro)
print("The maximum product subarray is:", max(arr))