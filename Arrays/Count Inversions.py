# Count Inversions

def count_inversions(arr):
    c = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                c += 1
    return c

arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(count_inversions(arr))