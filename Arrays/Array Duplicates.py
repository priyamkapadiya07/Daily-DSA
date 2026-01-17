# Find duplicate in an array

# Time Complexity: O(n log n) to O(n) | Space Complexity: O(n)
# Reason: Depends on the method used

# Method - 1 (Using Dictionary)
# Time Complexity: O(n) | Space Complexity: O(n)
# Reason: Single pass through array and dictionary lookup is O(1). Dictionary stores all unique elements.
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
d={}
for i in arr:
    d[i]=d.get(i,0)+1
duplicate=list(k for k,v in d.items() if v>1)
print(duplicate)


# Method - 2 (Using Set)
# Time Complexity: O(n) | Space Complexity: O(n)
# Reason: Single pass through array and set lookup/insertion is O(1). Set stores unique elements.
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
s=set()
duplicate=[]
for i in arr:
    if i in s:
        duplicate.append(i)
    else:
        s.add(i)
print(duplicate)


# Method - 3 (Using Negation Technique)
# Time Complexity: O(n) | Space Complexity: O(k) where k is number of duplicates
# Reason: Single pass through array with constant time operations. Space only for duplicates list.
arr = list(map(int, input("Enter elements: ").split()))
duplicates = []

for i in range(len(arr)):
    index = abs(arr[i]) - 1
    
    if arr[index] < 0:
        duplicates.append(abs(arr[i]))
    else:
        arr[index] = -arr[index]

print("Duplicates:", list(set(duplicates)))