'''
Three way partitioning of an array around a given value

Time Complexity: O(n)
Reason: We traverse the array once with a single pass using the mid pointer.
        Each element is visited at most once, and we perform constant time 
        operations (comparisons and swaps) for each element.

Space Complexity: O(1)
Reason: We use only a constant amount of extra space for three pointers (low, mid, high).
        The sorting is done in-place, and no additional data structures are used.
'''

def three_way_partition(arr, a, b):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > b:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1
arr = list(map(int, input("Enter the array elements: ").split()))
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
three_way_partition(arr, a, b)
print(arr)