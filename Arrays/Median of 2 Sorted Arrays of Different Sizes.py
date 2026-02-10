# Median of 2 Sorted Arrays of Different Sizes

def median(arr):
    '''
    Time Complexity: O((m + n) log(m + n))
    Reason:
    - Concatenating the two input lists (`a + b`) creates a new list of length
    k = m + n, which takes O(m + n) time.
    - Sorting that combined list dominates the runtime: Timsort sorts k items
    in O(k log k) = O((m + n) log(m + n)). Indexing to find the median is O(1).

    Space Complexity: O(m + n)
    Reason:
    - The concatenation `a + b` allocates a new list of size k = m + n, so the
    extra space used is O(m + n).
    - In-place sorting (Timsort) uses O(log k) auxiliary space, but this is
    asymptotically dominated by the concatenation allocation.
    '''
    arr.sort()
    n = len(arr)

    if n % 2 == 0:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return (arr[mid1] + arr[mid2]) / 2
    else:
        mid = n // 2
        return arr[mid]

a = list(map(int, input("Enter the first sorted array (space-separated): ").split()))
b = list(map(int, input("Enter the second sorted array (space-separated): ").split()))
print(median(a+b))