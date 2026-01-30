# Given an array of size n and a number k, fin all elements that appear more than " n/k " times.

arr = [3, 1, 2, 2, 1, 2, 3, 3]
k = 4

d={}
for i in arr:
    d[i]=d.get(i,0)+1
    
res=0
for key in d:
    if d[key] > len(arr)//k:
        res+=1
print(res)