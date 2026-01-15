# Write a program to cyclically rotate an array by one.

arr = list(map(int, input("Enter elements of array separated by space: ").split()))
n=int(input("Enter no. of rotation you want: "))
no=n
while n>0:
    arr.insert(0,arr.pop())
    n-=1
print(f"After rotating array {no} times:",arr)