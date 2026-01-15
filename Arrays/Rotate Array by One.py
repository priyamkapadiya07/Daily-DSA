# Write a program to cyclically rotate an array by one.

arr = [1, 2, 3, 4, 5]
n=int(input("Enter no. of rotation you want: "))
while n>0:
    arr.insert(0,arr.pop())
    n-=1
print(arr)