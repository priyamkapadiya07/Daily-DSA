# Find Largest sum contiguous Subarray [V. IMP]

arr = list(map(int, input("Enter elements of array separated by space: ").split()))
d={}

for i in range(len(arr)-1):
    n=i+1
    while n<=len(arr):
        subarr=arr[i:n]
        d[sum(subarr)]=subarr
        n+=1

print("Largest sum contiguous Subarray is:",d[max(d.keys())],"with sum =",max(d.keys()))