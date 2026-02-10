# Median of 2 Sorted Arrays of Different Sizes


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

a = [3, 5, 6, 12, 15]
b = [3, 4, 6, 10, 10, 12]
print(median(a+b))