# Given an array of size n and a number k, fin all elements that appear more than " n/k " times.

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
k = int(input("Enter the value of k: "))

d={}
for i in arr:
    d[i]=d.get(i,0)+1
    
res=0
for key in d:
    if d[key] > len(arr)//k:
        res+=1
print(res)