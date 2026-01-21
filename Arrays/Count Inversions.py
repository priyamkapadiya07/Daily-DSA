# Count Inversions

arr = list(map(int, input("Enter elements of array separated by space: ").split()))

c = 0

for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        if arr[i] > arr[j]:
            c += 1
print(c)