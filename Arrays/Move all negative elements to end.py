# Program to move all negative elements to the end of the array

# Time Complexity: O(n) | Space Complexity: O(n)
# Reason: Single pass through array to separate elements. Two lists store positive and negative elements.

arr = list(map(int, input("Enter elements of array separated by space: ").split()))
p=[]
n=[]
for i in arr:
    if i>0:
        p.append(i)
    else:
        n.append(i)
result=p+n
print("Array after moving all negative elements to the end:",result)