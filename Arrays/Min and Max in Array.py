# Program to find minimum and maximum elements in an array

arr=input("Enter elements of array separated by space: ").split()
min=arr[0]
max=arr[0]
for i in arr:
    if i<min:
        min=i
    if i>max:
        max=i
print("Minimum element is:",min)
print("Maximum element is:",max)