# Program to sort an array consisting of only 0s, 1s and 2s

# Time Complexity: O(n log n) | Space Complexity: O(n)
# Reason: Dictionary creation is O(n). Sorting dictionary items is O(n log n). Result list stores all elements.

arr = list(map(int, input("Enter elements of array (0s, 1s and 2s) separated by space: ").split()))
d={}
for i in arr:
    d[i]=d.get(i,0)+1
    
result = []
for i,j in d.items():
    result.extend([i]*j)
print("Sorted array of 0s, 1s and 2s is:", sorted(result))