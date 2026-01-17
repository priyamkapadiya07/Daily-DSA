# Find duplicate in an array of N+1 Integers

# Method - 1 (Using Dictionary)
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
d={}
for i in arr:
    d[i]=d.get(i,0)+1
duplicate=list(k for k,v in d.items() if v>1)
print(duplicate)


# Method - 2 (Using Set)
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
arr = list(map(int, input("Enter elements: ").split()))
duplicates = []

for i in range(len(arr)):
    index = abs(arr[i]) - 1
    
    if arr[index] < 0:
        duplicates.append(abs(arr[i]))
    else:
        arr[index] = -arr[index]

print("Duplicates:", list(set(duplicates)))