# Program to move all negative elements to the end of the array

arr = [1, -1, 3, 2, -7, -5, 11, 6 ]
p=[]
n=[]
for i in arr:
    if i>0:
        p.append(i)
    else:
        n.append(i)
result=p+n
print("Array after moving all negative elements to the end:",result)