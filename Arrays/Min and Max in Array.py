# Program to find minimum and maximum elements in an array

# Time Complexity: O(n) | Space Complexity: O(1)
# Reason: Single pass through array comparing with min and max. Only constant space variables used.

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