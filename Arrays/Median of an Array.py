# Median of an Array


def median(arr):
    arr.sort()
    n = len(arr)
    
    if n % 2 == 0:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return (arr[mid1] + arr[mid2]) / 2
    else:
        mid = n // 2
        return arr[mid]

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
print(median(arr))