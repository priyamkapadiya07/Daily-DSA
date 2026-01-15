# Find Largest sum contiguous Subarray [V. IMP]

arr = [2, 3, -8, 7, -1, 2, 3]
d={}

for i in range(len(arr)-1):
    n=i+1
    while n<=len(arr):
        subarr=arr[i:n]
        d[sum(subarr)]=subarr
        n+=1

for k,v in d.items():
    if k==max(d.keys()):
        print("Largest sum contiguous Subarray is:",v,"with sum =",k)